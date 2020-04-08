#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name: fabfile
# Version: 0.1a1
# Owner: Ruslan Korniichuk
# E-mail: ruslan.korniichuk(at)gmail.com

from fabric.api import local


def git():
    """Configure Git"""

    local('git remote rm origin')
    local('git remote add '
          'origin https://korniichuk@github.com/korniichuk/phd.git')
