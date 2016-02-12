.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

=====================
lineage.controlpanels
=====================

.. warning::
    THIS IS STILL EXPERIMENTAL CODE!
    ... and wasn't used in production yet.

Allows Lineage child site specific configurations for plone.registry based controlpanels.

Not available in Lineage Childsites
-----------------------------------

The following control panels change global settings. Therefore they are not available in subsites.

- content-controlpanel
- dexterity-types
- filter-controlpanel
- maintenance-controlpanel
- prefs_install_products_form
- resourceregistry-controlpanel
- security controlpanel
- usergroup-groupprefs
- usergroup-userprefs


This is also disabled, but should probably fixed to work with local registries too:
- portal_registry

This one stores it's configuration in the registry but has changes one setting in portal_actions, which would affect all sites.
Thus disabled.
- syndication-controlpanel


Installation
------------

Install lineage.controlpanels by adding it to your buildout::

    [buildout]

    ...

    eggs =
        lineage.controlpanels


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/lineage.controlpanels/issues
- Source Code: https://github.com/collective/lineage.controlpanels


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
