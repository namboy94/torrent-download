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
import json
from puffotter.os import makedirs
from puffotter.prompt import prompt
from torrent_download.exceptions import MissingConfig


class Config:
    """
    Configuration for the QBittorrent client
    """

    config_file = os.path.join(
        os.path.expanduser("~"),
        ".config/torrent-download/config.json"
    )
    """
    Path to the configuration file
    """

    def __init__(
            self,
            qbittorrent_address: str,
            qbittorrent_username: str,
            qbittorrent_password: str,
            qbittorrent_download_dir: str
    ):
        """
        Initializes the Config object
        :param qbittorrent_address: The qbittorrent address/URL
        :param qbittorrent_username: The qbittorent username
        :param qbittorrent_password: The qbittorent password
        :param qbittorrent_download_dir: The qbittorent download directory path
        """
        if qbittorrent_address.endswith("/"):
            qbittorrent_address = qbittorrent_address[0:-1]
        self.qbittorrent_address = qbittorrent_address
        self.qbittorrent_username = qbittorrent_username
        self.qbittorrent_password = qbittorrent_password
        self.qbittorrent_download_dir = qbittorrent_download_dir

    def save(self):
        """
        Saves the configuration
        :return: None
        """
        makedirs(os.path.dirname(self.config_file))
        with open(self.config_file, "w") as f:
            json.dump({
                "qbittorrent_address": self.qbittorrent_address,
                "qbittorrent_username": self.qbittorrent_username,
                "qbittorrent_password": self.qbittorrent_password,
                "qbittorrent_download_dir": self.qbittorrent_download_dir
            }, f, indent=4)

    @classmethod
    def load(cls) -> "Config":
        """
        Loads an existing configuration from disk
        :return: None
        """
        if not os.path.isfile(cls.config_file):
            raise MissingConfig(cls.config_file)
        else:
            with open(cls.config_file, "r") as f:
                data = json.load(f)
            return cls(
                data["qbittorrent_address"],
                data["qbittorrent_username"],
                data["qbittorrent_password"],
                data["qbittorrent_download_dir"]
            )

    @classmethod
    def prompt(cls) -> "Config":
        """
        Prompts the user for configuration details
        :return: The generated configuration
        """
        return cls(
            prompt("QBittorrent Address/URL"),
            prompt("QBittorrent Username"),
            prompt("QBittorrent Password"),
            prompt("QBittorrent Download Directory")
        )
