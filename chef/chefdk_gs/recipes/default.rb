#
# Cookbook Name:: chefdk_gs
# Recipe:: default
#
# Copyright (c) 2016 The Authors, All Rights Reserved.

include_recipe 'yum'

include_recipe 'git'
include_recipe 'poise-python'
include_recipe 'poise-ruby'
include_recipe 'poise-javascript'
