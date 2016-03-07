# -*- coding: utf-8 -*-
from ..testing import LINEAGE_CONTROLPANELS_FUNCTIONAL_TESTING
from collective.lineage.utils import enable_childsite
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.registry.interfaces import IRegistry
from plone.testing.z2 import Browser
from Products.CMFPlone.interfaces import ISiteSchema
from StringIO import StringIO
from zope.component import getUtility
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

import plone.api.content
import transaction
import unittest2 as unittest

# Red pixel with filename pixel.png
LOGO_1_FILENAME = 'pixel.png'
LOGO_1_BASE64 = 'filenameb64:cGl4ZWwucG5n;datab64:iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVQI12P4z8AAAAMBAQAY3Y2wAAAAAElFTkSuQmCC'  # noqa
LOGO_1_HEX = "\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDAT\x08\xd7c\xf8\xcf\xc0\x00\x00\x03\x01\x01\x00\x18\xdd\x8d\xb0\x00\x00\x00\x00IEND\xaeB`\x82"  # noqa

# Green pixel with filename pixelgreen.png
LOGO_2_FILENAME = 'pixelgreen.png'
LOGO_2_BASE64 = 'filenameb64:cGl4ZWxncmVlbi5wbmc=;datab64:iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVQI12Ng+M8AAAICAQCqKp4nAAAAAElFTkSuQmCC'  # noqa
LOGO_2_HEX = "\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDAT\x08\xd7c`\xf8\xcf\x00\x00\x02\x02\x01\x00\xaa*\x9e'\x00\x00\x00\x00IEND\xaeB`\x82"  # noqa


class SiteControlPanelFunctionalTest(unittest.TestCase):
    """Test that changes in the site control panel are actually
    stored in the registry.
    """
    layer = LINEAGE_CONTROLPANELS_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.portal_url = self.portal.absolute_url()

        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        plone.api.content.create(
            container=self.portal,
            type='Folder',
            id='subsite',
            title='subsite'
        )
        self.subsite = self.portal['subsite']
        plone.api.content.transition(obj=self.subsite, transition='publish')
        enable_childsite(self.subsite)

        transaction.commit()

        self.browser = Browser(self.app)
        self.browser.handleErrors = False
        self.browser.addHeader(
            'Authorization',
            'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,)
        )

    def _edit_and_save(self, controlpanel_url, data):
        """Open controlpanel on site, edit data and save."""
        browser = self.browser
        browser.open(controlpanel_url)

        get_ctrl = browser.getControl
        for item in data:
            ctrl = None
            ctrl = get_ctrl(name='form.widgets.{0}'.format(item['name']))
            if 'file' in item:
                import ipdb
                ipdb.set_trace()
                file_ = item['file']
                ctrl.add_file(
                    StringIO(file_['data']),
                    file_['mime_type'],
                    file_['file_name']
                )
            else:
                ctrl.value = item['value']
        get_ctrl('Save').click()
        transaction.commit()

    def _registry_assert(self, context, schema, data):
        """Assert given data against the data of a registry schema on a given
        context.
        """
        # Within a request, getUtility doesn't need to be fed explicitly with
        # the site because the site is set.
        # But in this test we have to.
        registry = getUtility(IRegistry, context=context)
        settings = registry.forInterface(schema, prefix="plone")

        for item in data:
            self.assertEqual(getattr(settings, item['name']), item['value'])

    def test_lineage_controlpanel_site_roundtrip(self):
        """Test editing the main site controlpanel and the lineage controlpanel
        in a subsite and check, if settings don't overwrite each other.
        """
        data_portal = [
            {'name': 'site_title', 'value': 'Main portal'},
            {'name': 'site_logo', 'value': LOGO_1_BASE64, 'file': {
                'data': LOGO_1_HEX,
                'file_name': LOGO_1_FILENAME,
                'mime_type': 'image/png'
            }},
            # {'name': 'exposeDCMetaTags', 'value_type': 'list', 'value': True},
            # {'name': 'enable_sitemap', 'value_type': 'list', 'value': True},
            {'name': 'webstats_js', 'value': '// dummy js'},
            # {'name': 'display_publication_date_in_byline', 'value_type': 'list', 'value': True},
            # {'name': 'icon_visibility', 'value_type': 'list', 'value': 'enabled'},
            # {'name': 'thumb_visibility', 'value_type': 'list', 'value': 'enabled'},
            # {'name': 'toolbar_position', 'value_type': 'list', 'value': 'side'},
            {'name': 'toolbar_logo', 'value': 'some_logo, nonexistent'},
            {'name': 'robots_txt', 'value': 'please, no robots'},
            # {'name': 'default_page', 'value': 'start.html'},
            # {'name': 'roles_allowed_to_add_keywords', 'value_type': 'list', 'value': 'Manager'},
        ]

        data_subsite = [
            {'name': 'site_title', 'value': 'Sub portal'},
            {'name': 'site_logo', 'value': LOGO_2_BASE64, 'file': {
                'data': LOGO_2_HEX,
                'file_name': LOGO_2_FILENAME,
                'mime_type': 'image/png'
            }},
            # {'name': 'exposeDCMetaTags', 'value_type': 'list', 'value': True},
            # {'name': 'enable_sitemap', 'value_type': 'list', 'value': True},
            #{'name': 'webstats_js', 'value': ''},
            # {'name': 'display_publication_date_in_byline', 'value_type': 'list', 'value': True},
            # {'name': 'icon_visibility', 'value_type': 'list', 'value': 'enabled'},
            # {'name': 'thumb_visibility', 'value_type': 'list', 'value': 'enabled'},
            # {'name': 'toolbar_position', 'value_type': 'list', 'value': 'side'},
            {'name': 'toolbar_logo', 'value': 'another_logo, also nonexistent'},
            {'name': 'robots_txt', 'value': 'more robots!'},
            # {'name': 'default_page', 'value': 'start.html'},
            # {'name': 'roles_allowed_to_add_keywords', 'value_type': 'list', 'value': 'Manager'},
        ]

        # Populate main site
        self._edit_and_save(
            '{0}/@@site-controlpanel'.format(self.portal.absolute_url()),
            data_portal
        )

        # Populate child site
        self._edit_and_save(
            '{0}/@@site-controlpanel'.format(self.subsite.absolute_url()),
            data_subsite
        )

        # Assert main portal
        self._registry_assert(
            self.portal,
            ISiteSchema,
            data_portal
        )

        # Assert sub portal
        self._registry_assert(
            self.subsite,
            ISiteSchema,
            data_subsite
        )
