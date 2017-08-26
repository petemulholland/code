#!/bin/bash
git config --global user.name "Peter Mulholland"
git config --global user.email peter.mulholland@yahoo.co.uk

git config --global alias.co checkout
git config --global alias.cof "checkout --" 
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.cim "commit -m"
git config --global alias.st status
git config --global alias.sh stash
git config --global alias.shp "stash pop"
git config --global alias.shl "stash list"
git config --global alias.df diff
git config --global alias.dfc "diff --cached"
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"
git config --global alias.hist "log --pretty=format:\"%h %ad | %s%d [%an]\" --graph --date=short"
git config --global alias.ls "log --pretty=format:\"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]\" --decorate"
git config --global alias.ll "log --pretty=format:\"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]\" --decorate --numstat"
git config --global alias.lds "log --pretty=format:\"%C(yellow)%h\\ %ad%Cred%d\\ %Creset%s%Cblue\\ [%cn]\" --decorate --date=short"
