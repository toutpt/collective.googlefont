from zope import interface
from zope import schema
from collective.googlefont.i18n import messageFactory as _

class IGoogleFont(interface.Interface):
    """Configuration to use the service
    """
    
    webfontconfig = schema.ASCII(title=_(u"label_webfontconfig",
                                         default=u'Webfontconfig'),
                              description=_(u"help_webfontconfig",
                                            default=u'Write a web font configuartion (javascript). Will be used with Webfontconfig = your stuff'),
                              required=False)
    
    cssfonturl = schema.ASCIILine(title=_(u"label_cssfonturl",
                                          default=u'Add here a css url'),
                              description=_(u"help_extracss", default=u''),
                              required=False)
    
    activated = schema.Boolean(title=_(u"label_activated"))
    
    def javascript():
        """Return the javascript code to include in pages"""
    
    def css():
        """Return the css code to include in pages"""
        