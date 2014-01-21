#!/usr/bin/env python

import os
import sys
import json
import urllib2
import shlex
import subprocess

class Plz(object):
  def __init__(self, arg):
    self.host = 'http://slackware.cs.utah.edu/pub'
    self.api  = 'http://slackware-packages.herokuapp.com/packages'
    self.target_dir = '/boot/extra'

    self.arg      = arg
    self.command  = arg[1]
    self.name     = arg[2]
    self.version  = arg[3]
    self.pkg      = ''

  def install(self):
    self._download()
    self._installpkg()


  # Private methods

  def _installpkg(self):
    if not self._installed():
      print "Installing {0}".format(self.pkg['package_name'])
      file = self._path([self.target_dir, self.pkg['file_name']])
      subprocess.call(['installpkg', file])

  def _download(self):
    api = self._path([self.api, self.name])
    pkg = self._get(api)

    versions = [v for v in pkg['versions'] if v['version'] == self.version]
    self.pkg = versions[-1]

    local_pkg  = self._path([self.target_dir, self.pkg['file_name']])

    if not os.path.isfile(local_pkg):
      print "Downloading {0}".format(self.pkg['package_name'])
      self._wget(self._path([self.host, self.pkg['path']]))

  def _installed(self):
    return self.pkg['package_name'] in self._raw_installed_packages()

  def _raw_installed_packages(self):
    return os.listdir('/var/log/packages/')

  def _wget(self, url):
    cmd = 'wget -qP {0} {1}'.format(self.target_dir, url)
    subprocess.call(shlex.split(cmd))

  def _get(self, url):
    response = urllib2.urlopen(url)
    return json.load(response)

  def _path(self, list):
    return ('/').join(list)

# CLI
args = sys.argv
if len(args) == 4:
  plz = Plz(args)
  plz.install()
else:
  exit("Usage: plz install NAME VERSION")