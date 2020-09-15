#!/bin/zsh
python3 resize_images.py
git add .
git commit -m 'update static files'
git push origin hexo
hexo clean
hexo generate
hexo deploy
