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


# imports
import os
from setuptools import setup, find_packages


if __name__ == "__main__":

    setup(
        name="torrent-dl",
        version=open("version", "r").read(),
        description="An torrent file downloader",
        long_description=open("README.md", "r").read(),
        long_description_content_type="text/markdown",
        author="Hermann Krumrey",
        author_email="hermann@krumreyh.com",
        classifiers=[
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
        ],
        url="https://gitlab.namibsun.net/namibsun/python/torrent-dl",
        license="GNU GPL3",
        packages=find_packages(),
        scripts=list(map(lambda x: os.path.join("bin", x), os.listdir("bin"))),
        install_requires=[
            "bs4",
            "requests",
            "cfscrape",
            "typing",
            "colorama",
            "qbittorrent",
            "puffotter",
            "sentry-sdk"
        ],
        include_package_data=True,
        zip_safe=False
    )
