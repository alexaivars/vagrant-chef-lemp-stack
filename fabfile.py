from fabric.api import *
from fabric.context_managers import *
from fabric.utils import puts
from fabric.colors import red, green
from fabric.contrib.project import *

# import simplejson
import os

# from fabric.api import env, local, run
def vagrant():
  # change from the default user to 'vagrant'
  env.user = 'vagrant'
  
  # connect to the port-forwarded ssh
  env.hosts = ['127.0.0.1:2222']
 
  # use vagrant ssh key
  result = local('cd vagrant && vagrant ssh_config | grep IdentityFile', capture=True)
  env.key_filename = result.split()[1]
 
def uname():
  run('uname -a')
