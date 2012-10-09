#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import bootstrap_admin_templates

packages = [
    'bootstrap_admin_templates',
]

package_data = {
    'bootstrap_admin_templates': [
        'templates/admin/*.html',
        'templates/admin/auth/user/*.html',
        'templates/admin/edit_inline/*.html',
        'templates/admin/includes/*.html',
        'templates/admin/registration/*.html',
    ],
}

setup(name='django-bootstrap-admin-templates',
      version=bootstrap_admin_templates.__version__,
      description=bootstrap_admin_templates.__description__,
      author='Marcus R. Brown (Precision Mojo, LLC)',
      author_email='mrbrown@precision-mojo.com',
      url='https://github.com/Precision-Mojo/django-bootstrap-admin-templates',
      packages=packages,
      package_data=package_data,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Site Management',
      ]
      )
