# Resizer for Icon Set

This python script create your image's clones with 128x128, 64x64, ..., 8x8 size.

  - Basic interface
  - GNOME shortcut for context menu

### Installation

Requires: Python3.x | tkinter | PIL

*PIL can installed with following steps:*

```sh
$ sudo apt-get install python3-pip
$ sudo apt-get install python3-dev python3-setuptools
$ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev
$ sudo pip3 install Pillow
```

For running script:

```sh
$ python3 ResizerIconSet.py
$ python3 ResizerIconSet.py /path/example.jpg
```

### Create Shortcuts

For symlink,
```sh
$ chmod +x ResizerIconSet.py
$ sudo cp ResizerIconSet.py /usr/lib
$ sudo ln -s /usr/lib/ResizerIconSet.py /usr/bin/resizericon
$ resizericon
```
For GNOME context menu:
```sh
$ cp Resizer ~/.local/share/nautilus/scripts
$ chmod +x ~/.local/share/nautilus/scripts/*
```
Now, you can see "Scripts" on context menu of right click of files.
