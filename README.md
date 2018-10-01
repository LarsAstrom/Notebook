# `from __future__ import solution`

This repository includes our notebook.

## Requirements to build: `pdf-latex`, `make` and `python-pygments`.

### Installation Ubuntu:
- `sudo apt-get install make texlive-full python-pygments`

### Installation macos:
- install `brew` from [brew.sh](https://brew.sh)
- `brew cask install mactex`
- `sudo easy_install Pygments` used for latex package minted 

## Build
`make all`

if you get weird latex errors, try to do `make rebuild`
