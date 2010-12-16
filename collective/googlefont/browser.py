from zope import interface
from Products.Five import BrowserView
from collective.googlefont import interfaces

class GoogleFont(BrowserView):
    """GoogleFont browserview"""
    interface.implements(interfaces.IGoogleFont)
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.configuration = interfaces.IGooleFont(context)
    
    @property
    def wefontconfig(self):
        return self.configuration.webfontconfig

    @property
    def cssfonturl(self):
        return self.configuration.cssfonturl
    
    def css(self):
        return ""
    
    def javascript(self):
        return ""
    