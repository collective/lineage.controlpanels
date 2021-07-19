# -*- coding: utf-8 -*-

from pkg_resources import parse_version
from Products.CMFPlone.interfaces import INonInstallable
from Products.GenericSetup.interfaces import IProfileImportedEvent
from zope.component import adapter
from zope.interface import implementer

import plone.api


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "lineage.controlpanels:uninstall",
            "lineage.controlpanels:plone51",
            "lineage.controlpanels:plone52",
        ]


@adapter(IProfileImportedEvent)
def handle_profile_imported_event(event):
    # Actions control panel was added
    if event.profile_id == "profile-plone.app.upgrade.v51:to51alpha1":
        setup = plone.api.portal.get_tool(name="portal_setup")
        setup.runAllImportStepsFromProfile("profile-lineage.controlpanels:plone51")

    # RedirectionTool was added
    if event.profile_id == "profile-plone.app.upgrade.v52:to52beta1":
        setup = plone.api.portal.get_tool(name="portal_setup")
        setup.runAllImportStepsFromProfile("profile-lineage.controlpanels:plone52")


def post_install(context):
    """Post install script"""
    # Check which additional configlets need to be installed/updated.
    current_version = parse_version(plone.api.env.plone_version())
    setup = plone.api.portal.get_tool(name="portal_setup")
    if current_version >= parse_version("5.1a1"):
        setup.runAllImportStepsFromProfile("profile-lineage.controlpanels:plone51")
    if current_version >= parse_version("5.2b1"):
        setup.runAllImportStepsFromProfile("profile-lineage.controlpanels:plone52")


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
