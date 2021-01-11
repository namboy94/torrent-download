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
from typing import Optional
from puffotter.os import makedirs
from torrent_download.entities.TorrentInfo import TorrentInfo


class TorrentDownload:
    """
    Class used to store all information required for downloading a torrent
    """

    def __init__(
            self,
            torrent_info: TorrentInfo,
            destination_dir: str,
            destination_filename: Optional[str] = None
    ):
        """
        Initializes the TorrentDownload object
        :param torrent_info: The torrent information
        :param destination_dir: The destination directory
        :param destination_filename: Optional filename, if not provided will
                                     be automatically inferred
        """
        self.torrent_info = torrent_info
        self.destination_dir = destination_dir
        makedirs(destination_dir)
        if destination_filename is None:
            if torrent_info.filename is None:
                self.destination = destination_dir
            else:
                self.destination = os.path.join(
                    destination_dir, torrent_info.filename
                )
        else:
            self.destination = os.path.join(
                destination_dir, destination_filename
            )

    def add_extension(self, ext: str):
        """
        Adds an extension to the destination filename
        :param ext: The extension to add
        :return: None
        """
        if not self.destination.endswith(f".{ext}"):
            self.destination += f".{ext}"
