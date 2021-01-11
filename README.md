# torrent Downloader

|master|develop|
|:---:|:---:|
|[![build status](https://gitlab.namibsun.net/namibsun/python/torrent-dl/badges/master/build.svg)](https://gitlab.namibsun.net/namibsun/python/torrent-dl/commits/master)|[![build status](https://gitlab.namibsun.net/namibsun/python/torrent-dl/badges/develop/build.svg)](https://gitlab.namibsun.net/namibsun/python/torrent-dl/commits/develop)|

![Logo](resources/logo/logo-readme.png)

An torrent file downloader that uses a running qBittorrent server to download
using bittorrent.

## Installation

Either install the program using `pip install torrent-dl` or `python setup.py install`

Additionally, a running instance of qbittorent web must be accessible to the user.
A good way to do so is using
[this docker image](https://hub.docker.com/r/linuxserver/qbittorrent).

After installing torrent-dl, you will need to run ```torrent-dl-config-gen```
to complete the setup.

## Projects using torrent-dl

* [toktokkie](https://gitlab.namibsun.net/namibsun/python/toktokkie)
   
## Further Information

* [Changelog](CHANGELOG)
* [License (GPLv3)](LICENSE)
* [Gitlab](https://gitlab.namibsun.net/namibsun/python/torrent-dl)
* [Github](https://github.com/namboy94/torrent-dl)
* [Progstats](https://progstats.namibsun.net/projects/torrent-dl)
* [PyPi](https://pypi.org/project/torrent-dl)
