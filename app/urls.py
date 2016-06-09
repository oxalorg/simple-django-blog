"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import blog.views

urlpatterns = [
    url(r'^$', blog.views.front, name='front'),
    url(r'^about/', blog.views.about,
        name='about'),
    url(r'^support/', blog.views.support,
        name='support'),
    url(r'^contact/', blog.views.contact,
        name='contact'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]

# Don't know where else to put this.
# Should work here for now.
admin.site.site_header = 'Earthly Admins'
admin.site.site_title = 'Earthly Admins'
