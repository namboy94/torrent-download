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
import requests
from typing import List
from bs4 import BeautifulSoup
from puffotter.units import byte_string_to_byte_count
from torrent_download.search.SearchEngine import SearchEngine
from torrent_download.entities.TorrentInfo import TorrentInfo


class NyaaSearchEngine(SearchEngine):
    """
    Search engine for nyaa.si
    """

    @classmethod
    def name(cls) -> str:
        """
        :return: The name of the search engine
        """
        return "nyaa"

    def search(self, search_term) -> List[TorrentInfo]:
        """
        Performs the actual search
        :param search_term: The term to search for
        :return: The search results
        """
        url = f"https://nyaa.si/?q={search_term.replace(' ', '+')}" \
              f"&s=seeders&o=desc"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        rows = soup.select("tr")

        if len(rows) == 0:
            return []

        rows.pop(0)

        results = []
        for row in rows:
            columns = row.select("td")
            name = columns[1].select("a")[-1].text.strip()
            links = columns[2].select("a")
            torrent_file = \
                os.path.join("https://nyaa.si", links[0]["href"][1:])
            magnet_link = links[1]["href"]
            size_string = columns[3].text.replace("i", "").replace(" ", "")
            size = byte_string_to_byte_count(size_string)
            results.append(TorrentInfo(name, torrent_file, magnet_link, size))

        return results
