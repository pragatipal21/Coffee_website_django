from django.contrib import admin

# Register your models

from service.models import Service
class OurServiceAdmin(admin.ModelAdmin):
    list_display=('service_title','service_desc','service_read_link','service_img')
admin.site.register(Service,OurServiceAdmin)

from service.models import Learn
class LearnAdmin(admin.ModelAdmin):
    list_display=('learn_heading','learn_title','learn_desc','learn_read_link')
admin.site.register(Learn,LearnAdmin)


from service.models import OurServices
class OurServiceAdmin(admin.ModelAdmin):
    list_display=('our_read_link','our_title','our_desc','our_img')
admin.site.register(OurServices,OurServiceAdmin)

from service.models import pricing
class PricingAdmin(admin.ModelAdmin):
    list_display = ('title',)  # A tuple with a trailing comma
admin.site.register(pricing, PricingAdmin)



from service.models import TableBook
class TableBookAdmin(admin.ModelAdmin):
    list_display=('name','email','date','time','person')
admin.site.register(TableBook,TableBookAdmin)



from service.models import ContactInfo
class ContactInfoAdmin(admin.ModelAdmin):
    list_display=('address','phone','email')
admin.site.register(ContactInfo,ContactInfoAdmin)

from service.models import SocialMedia
class SocialMediaAdmin(admin.ModelAdmin):
    list_display=('url','icon_img','icon_class')
admin.site.register(SocialMedia,SocialMediaAdmin)

from service.models import OpenHour
class OpenHourAdmin(admin.ModelAdmin):
    list_display=('day_range','time_range')
admin.site.register(OpenHour,OpenHourAdmin)


from .models import Subscriber

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')

from service.models import Offer
class OfferAdmin(admin.ModelAdmin):
    list_display=('title','subtitle','description')
admin.site.register(Offer,OfferAdmin)

from service.models import MenuItem
class MenuItemAdmin(admin.ModelAdmin):
    list_display=('name','price','description','image','rating','swiggy_link')
admin.site.register(MenuItem,MenuItemAdmin)


from service.models import Testimonial
class TestimonialAdmin(admin.ModelAdmin):
    list_display=('name','message','created_at')
admin.site.register(Testimonial,TestimonialAdmin)


