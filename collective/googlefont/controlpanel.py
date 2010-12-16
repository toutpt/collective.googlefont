from plone.app.controlpanel.form import ControlPanelForm
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from zope.component import adapts, getUtility
from zope.formlib.form import FormFields
from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from collective.googlefont import interfaces
from collective.googlefont import messageFactory as _

font_iface = interfaces.IGoogleFont

class GoogleFontAdapter(SchemaAdapterBase):
    adapts(IPloneSiteRoot)
    implements(font_iface)
    
    def __init__(self, context):
        super(GoogleFontAdapter, self).__init__(context)
        self.context = getUtility(IPropertiesTool).googlefont_properties

    webfontconfig = ProxyFieldProperty(font_iface['webfontconfig'])
    cssfonturl = ProxyFieldProperty(font_iface['cssfonturl'])

    def css(self):
        return ""
    
    def javascript(self):
        return ""

class GoogleFontControlPanel(ControlPanelForm):
    form_fields = FormFields(font_iface)
    label = _(u"Googlefonts setup")
    description = _(u'Googlefonts configuration.')
    form_name = _(u'Google Font')

    def _on_save(self, data=None):
        jsregistry = getToolByName(self.context,
                                   'portal_javascripts')
        cssregistry = getToolByName(self.context,
                                   'portal_css')
        jsregistry.cookResources()
        cssregistry.cookResources()
