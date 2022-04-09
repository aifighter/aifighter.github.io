#!/bin/zsh
python3 resize_images.py
git add .
git commit -m 'update static files'
git remote set-url origin https://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@github.com/aifighter/aifighter.github.io.git
git push origin hexo
# nvm use 12
hexo clean
hexo generate
git remote set-url origin https://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@github.com/aifighter/aifighter.github.io.git
hexo deploy
