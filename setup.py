# -*- coding: utf-8 -*-
"""Installer for the lineage.controlpanels package."""

from setuptools import find_packages
from setuptools import setup


version = '1.0a2.dev0'
short_description = u'Plone controlpanels for Lineage sites'
long_description = u'\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='lineage.controlpanels',
    version=version,
    description=short_description,
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: Addon',
        'Framework :: Plone :: 5.0',
        'Framework :: Plone :: 5.1',
        'Framework :: Plone :: 5.2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords='Python Plone',
    author='Johannes Raggam',
    author_email='thetetet@gmail.com',
    url='https://pypi.python.org/pypi/lineage.controlpanels',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['lineage'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7, >=3.6",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'collective.lineage>=2.1',
        'lineage.registry>=1.3.3',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'lineage.themeselection',
            'plone.api',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
            'plone.testing>=5.0.0',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
