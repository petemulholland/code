# Chefdk'ing up dev boxes:

## install chefdk
### windows
1. run install_chefdk.bat

check that the chefdk/embedded/bin path is in PATH for access to bundle.

2. Install Vagrant: https://www.vagrantup.com/
3. Run: ```$ vagrant plugin install vagrant-berkshelf```
4. on windows 10 install vc++ 32-bit redist for curl to work from vagrant


## creating a dev VM:
1. ```$ berks cookbook YourProjectName``` - to create cookbook
2. in root directory of cookbook:  ```$ bundle install``` [TODO: not sure what this does]
3. Add cookbook dependencies to metadata.rb
  a. run: ```$ berks install``` after each update to metadata.rb

4. update config.vm.box in Vagrant file to pick vagrant box required
