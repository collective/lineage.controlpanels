"""Installer for the lineage.controlpanels package."""

from setuptools import setup

version = "2.0.0a1.dev0"
short_description = "Plone controlpanels for Lineage sites"
long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="lineage.controlpanels",
    version=version,
    description=short_description,
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="Johannes Raggam",
    author_email="thetetet@gmail.com",
    url="https://pypi.python.org/pypi/lineage.controlpanels",
    license="GPL version 2",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "collective.lineage>=2.1",
        "lineage.registry>=1.3.3",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.api",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
