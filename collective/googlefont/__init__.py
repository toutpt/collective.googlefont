  # -*- extra stuff goes here -*- 
from zope import component
from zope import interface
from collective.googlefont import interfaces
from Products.CMFCore.interfaces import IURLTool

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

class GoogleFont(object):
    interface.implements(interfaces.IGoogleFont)
    def __init__(self, context):
        self.context = context
        portal = IURLTool(context).getPortalObject()
        self.configuration = interfaces.IGoogleFont(portal)

    @property
    def wefontconfig(self):
        return self.configuration.webfontconfig

    @property
    def cssfonturl(self):
        return self.configuration.cssfonturl
    
    def css(self):
        return self.configuration.css()
    
    def javascript(self):
        return self.configuration.javascript()
