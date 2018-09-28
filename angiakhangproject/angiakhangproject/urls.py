"""angiakhangproject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # URL for Portfolio Project model
    url(r'^listPortfolioProject/$', showAllPortfolioProject, name='listPortfolioProject'),
    url(r'^getPortfolioProject/(?P<idPortfolio>\d+)/$', getPortfolioProject, name='getPortfolioProject'),
    url(r'^updatePortfolioProject/(?P<idPortfolio>\d+)/$', updatePortfolioProject, name='updatePortfolioProject'),
    url(r'^createPortfolioProject/$', createPortfolioProject, name='createPortfolioProject'),
    url(r'^deletePortfolioProject/$', deletePortfolioProject, name='deletePortfolioProject'),
    url(r'^get_PortfolioProject/(?P<idPortfolio>\d+)/$', get_PortfolioProject, name='get_PortfolioProject'),

    # URL for Area model
    url(r'^listArea/$', showAllArea, name='listArea'),
    url(r'^getArea/(?P<idArea>\d+)/$', getArea, name='getArea'),
    url(r'^updateArea/(?P<idArea>\d+)/$', updateArea, name='updateArea'),
    url(r'^createArea/$', createArea, name='createArea'),
    url(r'^deleteArea/$', deleteArea, name='deleteArea'),
    url(r'^get_Area/(?P<idArea>\d+)/$', get_Area, name='get_Area'),

    # URL for Member model
    url(r'^listMember/$', showAllMember, name='listMember'),
    url(r'^getMember/(?P<idMember>\d+)/$', getMember, name='getMember'),
    url(r'^updateMember/(?P<idMember>\d+)/$', updateMember, name='updateMember'),
    url(r'^createMember/$', createMember, name='createMember'),
    url(r'^deleteMember/$', deleteMember, name='deleteMember'),
    url(r'^get_Member/(?P<idMember>\d+)/$', get_Member, name='get_Member'),
]
