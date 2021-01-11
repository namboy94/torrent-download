"""LICENSE
Copyright 2021 Hermann Krumrey <hermann@krumreyh.com>

This file is part of torrent-download.

torrent-download is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

torrent-download is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with torrent-download.  If not, see <http://www.gnu.org/licenses/>.
LICENSE"""

import os
import time
import shutil
import requests
from typing import List
from qbittorrent import Client
from torrent_download.Config import Config
from torrent_download.entities.TorrentDownload import TorrentDownload


class QBittorrentDownloader:
    """
    Class that uses the qBittorrent Server API to download torrents
    """

    def __init__(
            self,
            url: str,
            username: str,
            password: str,
            download_dir: str
    ):
        """

        :param url:
        :param username:
        :param password:
        :param download_dir:
        """
        self.client = Client(url)
        self.client.login(username, password)
        self.download_dir = download_dir

    @classmethod
    def from_config(cls) -> "QBittorrentDownloader":
        """
        :return: A QBittorrentDownloader object based on the stored
                 configuration files
        """
        config = Config.load()
        return cls(
            config.qbittorrent_address,
            config.qbittorrent_username,
            config.qbittorrent_password,
            config.qbittorrent_download_dir
        )

    def download(self, torrents: List[TorrentDownload]):
        """
        Downloads a list of torrent files
        :param torrents: The torrents to download
        :return: None
        """
        for torrent in torrents:
            torrent_info = torrent.torrent_info

            print(f"Downloading Torrent: {torrent_info.filename}")

            if torrent_info.magnet_link is not None:
                self.client.download_from_link(torrent_info.magnet_link)
            else:
                assert torrent_info.torrent_file is not None
                torrent_file = torrent_info.torrent_file
                if not os.path.isfile(torrent_file):
                    torrent_file = "/tmp/torrentdltemp.torrent"
                    content = requests.get(torrent_info.torrent_file).content
                    with open(torrent_file, "wb") as f:
                        f.write(content)
                with open(torrent_file, "rb") as f:
                    self.client.download_from_file(f)

            time.sleep(1)

            while len(self.client.torrents()) > 0:
                for active in self.client.torrents():
                    if active["state"] not in [
                        "downloading", "metaDL", "stalledDL"
                    ]:
                        print("Done.     ")
                        torrent_path = os.path.join(
                            self.download_dir, active["name"]
                        )

                        if os.path.isdir(torrent_path):
                            children = [
                                os.path.join(torrent_path, x)
                                for x in os.listdir(torrent_path)
                            ]
                            children.sort(
                                key=lambda x: os.path.getsize(x), reverse=True
                            )
                            torrent_path = children[0]
                            ext = torrent_path.rsplit(".", 1)[1]
                            torrent.add_extension(ext)

                        self.client.delete(active["hash"])

                        if os.path.isdir(torrent.destination):
                            shutil.move(
                                torrent_path,
                                os.path.join(
                                    torrent.destination,
                                    os.path.basename(torrent_path)
                                )
                            )
                        else:
                            shutil.move(torrent_path, torrent.destination)
                    else:
                        print(f"{(100 * active['progress']):.2f}%", end="\r")

                time.sleep(1)
