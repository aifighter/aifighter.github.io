#!/bin/zsh
nvm use 12
python3 resize_images.py
git add .
git commit -m 'update static files'
git push origin hexo
# nvm use 12
hexo clean
hexo generate
hexo deploy
nvm use 18
