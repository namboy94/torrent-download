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

from typing import List, Type
from torrent_download.search.SearchEngine import SearchEngine
from torrent_download.search.NyaaSearchEngine import NyaaSearchEngine

search_engines: List[Type[SearchEngine]] = [NyaaSearchEngine]
"""
All available search engines
"""
