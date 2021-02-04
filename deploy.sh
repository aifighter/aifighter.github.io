#!/bin/zsh
python3 resize_images.py
git add .
git commit -m 'update static files'
git push origin hexo
nvm use 13
hexo clean
hexo generate
hexo deploy
