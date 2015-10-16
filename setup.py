# -*- coding: utf-8 -*-
import os
import sys
from subprocess import call, check_output
from setuptools import find_packages, setup
from setuptools.command.install import install

NODE_URL = "https://nodejs.org/dist/v4.2.1/node-v4.2.1-linux-x64.tar.gz"

# install prerequisites
def install_node():
	print "Installing node..."

	# clean up old install
	call("rm -r ~/node", shell=True)
	call("rm ~/.heroku/python/bin/npm", shell=True)
	call("rm ~/.heroku/python/bin/node", shell=True)
	call("rm ~/.heroku/python/bin/tsc", shell=True)

	# create temp directory
	call("mkdir -p ~/node", shell=True)
	
	# download and extract node
	call("wget –quiet -O ~/node/node.tar.gz {}".format(NODE_URL), shell=True)
	call("tar -xzf ~/node/node.tar.gz -C ~/node", shell=True)
	call("mv ~/node/node-* ~/node/temp", shell=True)
	call("mv ~/node/temp/* ~/node/", shell=True)
	call("rmdir ~/node/temp", shell=True)
	call("ln -s ~/node/bin/node ~/.heroku/python/bin/node", shell=True)
	call("ln -s ~/node/bin/npm ~/.heroku/python/bin/npm", shell=True)
	call("ln -s ~/node/bin/node /usr/bin/node", shell=True)
	call("ln -s ~/node/bin/npm /usr/bin/npm", shell=True)

def install_typescript():
	call("npm install --prefix ~/node/ typescript", shell=True)
	call("ln -s ~/node/node_modules/typescript/bin/tsc ~/.heroku/python/bin/tsc", shell=True)
	call("ln -s ~/node/node_modules/typescript/bin/tsc /usr/bin/tsc", shell=True)

def pre_install():
	install_node()
	install_typescript()

class custom_install(install):  
	def run(self):
		self.execute(pre_install, [], msg="Installing dependencies...")
		install.run(self)


# package settings
setup(
	# info
	name='tsfilter',
	version='0.0.1',
	author=u'Stephen Quebe',
	author_email='squebe@gmail.com',
	url='https://github.com/squebe/tsfilter',
	description="TSFilter is a typescript filter for Django Compressor.",
	long_description=open('README.md').read(),
	license='MIT',

	# include
	packages=find_packages(),
	include_package_data=True,
	install_requires=['django-compressor>=1.3'],

	# custom pre-install script to install requirements
	cmdclass={'install': custom_install}
)