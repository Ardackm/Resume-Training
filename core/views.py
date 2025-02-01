from django.shortcuts import render
from core.models import GeneralSetting

# Create your views here.
def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_name  = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameter
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'contact_mail': contact_mail,
        'contact_phone': contact_phone,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
    }
    return render(request, 'index.html', context=context)
