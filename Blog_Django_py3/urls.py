"""Blog_Django_py3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^aboutme/$', views.about_me, name = 'aboutMe'),
    url(r'^messages/$', views.message, name = 'messages'),
    url(r'^mylife/$', views.mylife, name = 'life'),
    url(r'^life_list/(?P<year>[0-9]{4})/$', views.life_list, name='life_list'),
    url(r'^p/', include('blog.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
