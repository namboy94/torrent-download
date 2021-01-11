# torrent-download

|master|develop|
|:---:|:---:|
|[![build status](https://gitlab.namibsun.net/namibsun/python/torrent-download/badges/master/build.svg)](https://gitlab.namibsun.net/namibsun/python/torrent-download/commits/master)|[![build status](https://gitlab.namibsun.net/namibsun/python/torrent-download/badges/develop/build.svg)](https://gitlab.namibsun.net/namibsun/python/torrent-download/commits/develop)|

![Logo](resources/logo/logo-readme.png)

An torrent file downloader that uses a running qBittorrent server to download
using bittorrent.

## Installation

Either install the program using `pip install torrent-download` or `python setup.py install`

Additionally, a running instance of qbittorent web must be accessible to the user.
A good way to do so is using
[this docker image](https://hub.docker.com/r/linuxserver/qbittorrent).

After installing torrent-download, you will need to run ```torrent-dl-config-gen```
to complete the setup.

## Projects using torrent-download

* [toktokkie](https://gitlab.namibsun.net/namibsun/python/toktokkie)
   
## Further Information

* [Changelog](CHANGELOG)
* [License (GPLv3)](LICENSE)
* [Gitlab](https://gitlab.namibsun.net/namibsun/python/torrent-download)
* [Github](https://github.com/namboy94/torrent-download)
* [Progstats](https://progstats.namibsun.net/projects/torrent-download)
* [PyPi](https://pypi.org/project/torrent-download)
