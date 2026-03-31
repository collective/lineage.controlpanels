from plone import api
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer


class BrowserLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.lineage

        self.loadZCML(package=collective.lineage)
        import lineage.registry

        self.loadZCML(package=lineage.registry)
        import lineage.controlpanels

        self.loadZCML(package=lineage.controlpanels)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "lineage.controlpanels:default")

        wf_tool = api.portal.get_tool("portal_workflow")
        wf_tool.setDefaultChain("simple_publication_workflow")


LINEAGE_CONTROLPANELS_FIXTURE = BrowserLayer()


LINEAGE_CONTROLPANELS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LINEAGE_CONTROLPANELS_FIXTURE,), name="BrowserLayer:IntegrationTesting"
)


LINEAGE_CONTROLPANELS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LINEAGE_CONTROLPANELS_FIXTURE,), name="BrowserLayer:FunctionalTesting"
)
