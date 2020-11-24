from django.urls import path
from . import views


from django.contrib import admin
from django.urls import path, include
from ipl import *
from django.conf.urls import include, url
from django.views.generic.base import TemplateView


urlpatterns = [
    path('index/', views.index,name='register'),	
	path('admin/', admin.site.urls),
	#url(r'home/', TemplateView.as_view(template_name='home.html'), name='home'),
]	



