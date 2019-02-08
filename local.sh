#!/bin/zsh
python3 resize_images.py
hexo clean
hexo generate
hexo server
