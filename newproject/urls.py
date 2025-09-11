from django.contrib import admin
from django.urls import path
from newproject import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('reservation/', views.reservation, name='reservation'),
  
    
    path('testimonial/', views.testimonial, name='testimonial'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),   # removed space
    path('service/', views.service, name='service'),   # removed space
    path('menu/', views.menu, name='menu'),            # removed space
    path('coffeeData/', views.coffeeData, name='coffeeData'),  
    path('subscribe/', views.subscribe, name='subscribe'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
