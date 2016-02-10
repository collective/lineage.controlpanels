# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import lineage.controlpanels


class BrowserLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=lineage.controlpanels)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'lineage.controlpanels:default')


LINEAGE_CONTROLPANELS_FIXTURE = BrowserLayer()


LINEAGE_CONTROLPANELS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LINEAGE_CONTROLPANELS_FIXTURE,),
    name='BrowserLayer:IntegrationTesting'
)


LINEAGE_CONTROLPANELS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LINEAGE_CONTROLPANELS_FIXTURE,),
    name='BrowserLayer:FunctionalTesting'
)


LINEAGE_CONTROLPANELS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        LINEAGE_CONTROLPANELS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='BrowserLayer:AcceptanceTesting'
)
