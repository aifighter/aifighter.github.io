#!/bin/zsh
git add .
git commit -m 'update static files'
git push origin hexo
hexo generate
hexo deploy
