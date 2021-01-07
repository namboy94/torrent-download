"""LICENSE
Copyright 2021 Hermann Krumrey <hermann@krumreyh.com>

This file is part of torrent-dl.

torrent-dl is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

torrent-dl is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with torrent-dl.  If not, see <http://www.gnu.org/licenses/>.
LICENSE"""

from puffotter.units import human_readable_bytes


class TorrentInfo:
    """
    Class that stores information for a torrent
    """

    def __init__(
            self,
            filename: str,
            torrent_file: str,
            magnet_link: str,
            size: int
    ):
        """
        Initializes the torrent info object
        :param filename: The name of the file for the torrent
        :param torrent_file: The link to the torrent file
        :param magnet_link: A magnet link to the torrent
        :param size: The size of the file in bytes
        """
        self.filename = filename
        self.torrent_file = torrent_file
        self.magnet_link = magnet_link
        self.size = size

    def __str__(self) -> str:
        """
        :return: A string representation of the torrent
        """
        return f"{self.filename} [{human_readable_bytes(self.size)}]"
