from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer


class BrowserLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.lineage

        self.loadZCML(package=collective.lineage)
        import lineage.registry

        self.loadZCML(package=lineage.registry)
        import lineage.controlpanels

        self.loadZCML(package=lineage.controlpanels)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "lineage.controlpanels:default")


LINEAGE_CONTROLPANELS_FIXTURE = BrowserLayer()


LINEAGE_CONTROLPANELS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LINEAGE_CONTROLPANELS_FIXTURE,), name="BrowserLayer:IntegrationTesting"
)


LINEAGE_CONTROLPANELS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LINEAGE_CONTROLPANELS_FIXTURE,), name="BrowserLayer:FunctionalTesting"
)
