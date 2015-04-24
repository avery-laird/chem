from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

class HomePage(Page, RichText):
    """
    The homepage
    """
    header = models.CharField(max_length=140)
    subheader = models.CharField(max_length=140)
    splash = FileField(verbose_name=_("Splash Image"),
        upload_to=upload_to("theme.HomePage.splash", "splash"), 
        format="Image", max_length=255, null=True, blank=True)    

    class Meta:
        verbose_name = _("Home Page")
        verbose_name_plural = _("Home Pages")
    
class Slide(Orderable):
    '''
    Homepage slider images
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)

class ExtendedBlog(Page, RichText):
    """
    RichText page, but with an optional splash image
    """
    splash = FileField(verbose_name=_("Splash Image"),
        upload_to=upload_to("theme.ExtendedBlog.splash", "splash"),
        format="Image", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("Extended Blog")
        verbose_name_plural = _("Extended Blogs")
# Create your models here.
