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
from django.conf.urls.static import static
from django.contrib import admin
from .views import *

urlpatterns = [
    # URL for User model
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login, name='login'),
    url(r'^handle_login/', handle_login, name='handle_login'),
    url(r'^user_page/$', user_page, name='user_page'),
    url(r'^get_user/(?P<id_user>\d+)/$', get_user, name='get_user'),
    url(r'^check_user_exist/(?P<query>[\w\-\@\.]+)/$', check_user_exist, name='check_user_exist'),
    url(r'^home_page/$', home_page, name='home_page'),
    url(r'^update_user/$', update_user, name='update_user'),
    url(r'^delete_user/$', delete_user, name='delete_user'),
    url(r'^forget_password/$', forget_password, name='forget_password'),
    url(r'^handle_forget_pass/$', handle_forget_password, name='handle_forget_pass'),

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

    # URL for Slide model
    url(r'^listSlide/$', showAllSlide, name='listSlide'),
    url(r'^getSlide/(?P<idSlide>\d+)/$', getSlide, name='getSlide'),
    url(r'^updateSlide/(?P<idSlide>\d+)/$', updateSlide, name='updateSlide'),
    url(r'^createSlide/$', createSlide, name='createSlide'),
    url(r'^deleteSlide/$', deleteSlide, name='deleteSlide'),
    url(r'^get_Slide/(?P<idSlide>\d+)/$', get_Slide, name='get_Slide'),

    # URL for Video model
    url(r'^listVideo/$', showAllVideo, name='listVideo'),
    url(r'^getVideo/(?P<idVideo>\d+)/$', getVideo, name='getVideo'),
    url(r'^updateVideo/(?P<idVideo>\d+)/$', updateVideo, name='updateVideo'),
    url(r'^createVideo/$', createVideo, name='createVideo'),
    url(r'^deleteVideo/$', deleteVideo, name='deleteVideo'),
    url(r'^get_Video/(?P<idVideo>\d+)/$', get_Video, name='get_Video'),

    # URL for Portfolio Posts model
    url(r'^listPortfolioPosts/$', showAllPortfolioPosts, name='listPortfolioPosts'),
    url(r'^getPortfolioPosts/(?P<idPortfolio>\d+)/$', getPortfolioPosts, name='getPortfolioPosts'),
    url(r'^updatePortfolioPosts/(?P<idPortfolio>\d+)/$', updatePortfolioPosts, name='updatePortfolioPosts'),
    url(r'^createPortfolioPosts/$', createPortfolioPosts, name='createPortfolioPosts'),
    url(r'^deletePortfolioPosts/$', deletePortfolioPosts, name='deletePortfolioPosts'),
    url(r'^get_PortfolioPosts/(?P<idPortfolio>\d+)/$', get_PortfolioPosts, name='get_PortfolioPosts'),

    # URL for Posts model
    url(r'^listPosts/$', showAllPosts, name='listPosts'),
    url(r'^getPosts/(?P<idPosts>\d+)/$', getPosts, name='getPosts'),
    url(r'^updatePosts/(?P<idPosts>\d+)/$', updatePosts, name='updatePosts'),
    url(r'^createPosts/$', createPosts, name='createPosts'),
    url(r'^deletePosts/$', deletePosts, name='deletePosts'),
    url(r'^get_Posts/(?P<idPosts>\d+)/$', get_Posts, name='get_Posts'),

    # URL for Project model
    url(r'^listProject/$', showAllProject, name='listProject'),
    url(r'^getProject/(?P<idProject>\d+)/$', getProject, name='getProject'),
    url(r'^updateProject/(?P<idProject>\d+)/$', updateProject, name='updateProject'),
    url(r'^createProject/$', createProject, name='createProject'),
    url(r'^deleteProject/$', deleteProject, name='deleteProject'),
    url(r'^get_Project/(?P<idProject>\d+)/$', get_Project, name='get_Project'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
