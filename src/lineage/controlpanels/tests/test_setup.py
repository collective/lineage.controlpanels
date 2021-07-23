# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from lineage.controlpanels.testing import LINEAGE_CONTROLPANELS_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that lineage.controlpanels is properly installed."""

    layer = LINEAGE_CONTROLPANELS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if lineage.controlpanels is installed."""
        self.assertTrue(self.installer.isProductInstalled("lineage.controlpanels"))

    def test_browserlayer(self):
        """Test that IBrowserLayer is registered."""
        from lineage.controlpanels.interfaces import IBrowserLayer
        from plone.browserlayer import utils

        self.assertIn(IBrowserLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = LINEAGE_CONTROLPANELS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(["lineage.controlpanels"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if lineage.controlpanels is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled("lineage.controlpanels"))

    def test_browserlayer_removed(self):
        """Test that IBrowserLayer is removed."""
        from lineage.controlpanels.interfaces import IBrowserLayer
        from plone.browserlayer import utils

        self.assertNotIn(IBrowserLayer, utils.registered_layers())
