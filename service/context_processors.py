from .models import ContactInfo, SocialMedia, OpenHour

def footer_data(request):
    return {
        'contactinfoData': ContactInfo.objects.first(),
        'socialmediaData': SocialMedia.objects.all(),
        'openhourData': OpenHour.objects.all(),
    }
