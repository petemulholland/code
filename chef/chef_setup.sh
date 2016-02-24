#!/bin/bash

echo "Installing Ruby Version Manager RVM"
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm

echo "Installing Ruby"
rvm install 2.0.0

echo "Creating gemset for chef"
rvm use 2.0.0@chef --create
