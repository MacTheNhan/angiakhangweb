# -*- coding: utf-8 -*-
import os
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from angiakhangproject import settings
from .models import *
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
import datetime

import hashlib
from angiakhangproject.common.login_require import user_login_required


# Create your views here.
# PORTFOLIO PROJECT
# Get all data about portfolio project
def showAllPortfolioProject(request):
    listPortfolioProject = PortfolioProject.objects.all()
    return render(request, 'portfolioproject/portfolioproject.html', {'listPortfolioProject': listPortfolioProject})


# Get 1 Portfolio Project to edit
def getPortfolioProject(request, idPortfolio):
    portfolioProject = PortfolioProject.objects.get(id=idPortfolio)
    return render(request, 'portfolioproject/editPortfolioProject.html', {'portfolioProject': portfolioProject})


# Get profile of Portfolio Project
def get_PortfolioProject(request, idPortfolio):
    portfolio_project = PortfolioProject.objects.get(id=idPortfolio)
    data_portfolioproject = []
    data_portfolioproject.append({
        'id': portfolio_project.id,
        'name_portfolio_project': portfolio_project.name_portfolio_project
    })
    return JsonResponse({'data': data_portfolioproject})


# Delete 1 Portfolio Project
def deletePortfolioProject(request):
    if request.method == 'POST':
        id_portfolio_delete = request.POST.get('id_portfolio_delete')
        portfolio_project = PortfolioProject.objects.get(id=id_portfolio_delete)
        if portfolio_project:
            try:
                portfolio_project.delete()
            except:
                messages.error(request, 'Deleting ' + portfolio_project.name_portfolio_project + ' failed')
        return redirect(showAllPortfolioProject)


# Create new Portfolio Project
def createPortfolioProject(request):
    if request.method == 'POST':
        name_portfolio_project = request.POST['txtNamePortfolio']
        avatar = request.FILES.get('txtImages')
        description_portfolio = request.POST['txtContent']
        portfolio_project = PortfolioProject(name_portfolio_project=name_portfolio_project, avatar=avatar, description_portfolio=description_portfolio)
        portfolio_project.save()
        messages.success(request, '' + name_portfolio_project + u' tạo thành công !')
        return redirect(showAllPortfolioProject)
    else:
        return render(request, 'portfolioproject/addPortfolioProject.html')


# Update Portfolio Project
def updatePortfolioProject(request, idPortfolio):
    portfolio_project = PortfolioProject.objects.get(id=idPortfolio)
    if portfolio_project is not None:
        portfolio_project.name_portfolio_project = request.POST['txtNamePortfolio']
        portfolio_project.description_portfolio = request.POST['txtContent']
        if request.FILES.get('txtImages'):
            portfolio_project.avatar = request.FILES.get('txtImages')
        portfolio_project.save()
        messages.success(request, '' + portfolio_project.name_portfolio_project + u' cập nhật thành công')
        return redirect(showAllPortfolioProject)
    return render(request, 'portfolioproject/editPortfolioProject.html', {'portfolio_project': portfolio_project})


# AREA MODEL
# Get all data about Area
def showAllArea(request):
    listArea = Area.objects.all()
    return render(request, 'area/area.html', {'listArea': listArea})


# Get 1 Area to edit
def getArea(request, idArea):
    area = Area.objects.get(id=idArea)
    return render(request, 'area/editArea.html', {'area': area})


# Get profile of Area
def get_Area(request, idArea):
    area = Area.objects.get(id=idArea)
    data_area = []
    data_area.append({
        'id': area.id,
        'name_area': area.name_area
    })
    return JsonResponse({'data': data_area})


# Delete 1 Area
def deleteArea(request):
    if request.method == 'POST':
        id_area = request.POST.get('id_area')
        area = Area.objects.get(id=id_area)
        if area:
            try:
                area.delete()
            except:
                messages.error(request, u'Xóa' + area.name_area + u' thất bại')
        return redirect(showAllArea)


# Create new Area
def createArea(request):
    if request.method == 'POST':
        name_area = request.POST['txtNameArea']
        area = Area(name_area=name_area)
        area.save()
        messages.success(request, '' + name_area + u' tạo thành công !')
        return redirect(showAllArea)
    else:
        return render(request, 'area/addArea.html')


# Update Area
def updateArea(request, idArea):
    area = Area.objects.get(id=idArea)
    if area is not None:
        area.name_area = request.POST['txtNameArea']
        area.save()
        messages.success(request, '' + area.name_area + u' cập nhật thành công !')
        return redirect(showAllArea)
    return render(request, 'area/editArea.html', {'area': area})


# MEMBER MODEL
def showAllMember(request):
    listMember = Member.objects.all()
    return render(request, 'member/member.html', {'listMember': listMember})


# Get 1 Member to edit
def getMember(request, idMember):
    member = Member.objects.get(id=idMember)
    return render(request, 'member/editMember.html', {'member': member})


# Get profile of Member
def get_Member(request, idMember):
    member = Member.objects.get(id=idMember)
    data_member = []
    data_member.append({
        'id': member.id,
        'name_company_member': member.name_company_member
    })
    return JsonResponse({'data': data_member})


# Delete 1 Member
def deleteMember(request):
    if request.method == 'POST':
        id_member = request.POST.get('id_member')
        member = Member.objects.get(id=id_member)
        if member:
            try:
                member.delete()
            except:
                messages.error(request, u'Xóa ' + member.name_company_member + u' thất bại')
        return redirect(showAllMember)


# Create new Member
def createMember(request):
    if request.method == 'POST':
        name_company_member = request.POST['txtNameMember']
        description = request.POST['txtDescription']
        type = request.POST['cbbType']
        avatar_member = request.FILES.get('txtImages')
        member = Member(name_company_member=name_company_member, avatar_member=avatar_member, description=description,
                        type=type)
        member.save()
        messages.success(request, '' + name_company_member + u' tạo thành công !')
        return redirect(showAllMember)
    else:
        return render(request, 'member/addMember.html')


# Update Member
def updateMember(request, idMember):
    member = Member.objects.get(id=idMember)
    if member is not None:
        member.name_company_member = request.POST['txtNameMember']
        member.description = request.POST['txtDescription']
        member.type = request.POST['cbbType']
        if request.FILES.get('txtImages'):
            member.avatar_member = request.FILES.get('txtImages')
        member.save()
        messages.success(request, '' + member.name_company_member + u' cập nhật thành công')
        return redirect(showAllMember)
    return render(request, 'member/editMember.html', {'member': member})


# SLIDE MODEL
def showAllSlide(request):
    listSlide = Slide.objects.all()
    return render(request, 'slide/slide.html', {'listSlide': listSlide})


# Get 1 slide to edit
def getSlide(request, idSlide):
    slide = Slide.objects.get(id=idSlide)
    return render(request, 'slide/editSlide.html', {'slide': slide})


# Get profile of Slide
def get_Slide(request, idSlide):
    slide = Slide.objects.get(id=idSlide)
    data_slide = []
    data_slide.append({
        'id': slide.id,
        'title': slide.title
    })
    return JsonResponse({'data': data_slide})


# Delete 1 Slide
def deleteSlide(request):
    if request.method == 'POST':
        id_slide = request.POST.get('id_slide')
        slide = Slide.objects.get(id=id_slide)
        if slide:
            try:
                slide.delete()
            except:
                messages.error(request, u'Xóa ' + slide.title + u' thất bại')
        return redirect(showAllSlide)


# Create new Slide
def createSlide(request):
    if request.method == 'POST':
        title = request.POST['txtNameSlide']
        image = request.FILES.get('txtImages')
        url = request.POST['txtURL']
        position = request.POST['slPosition']
        slide = Slide(title=title, image=image, url=url, position=position)
        slide.save()
        messages.success(request, '' + title + u' tạo thành công !')
        return redirect(showAllSlide)
    else:
        return render(request, 'slide/addSlide.html')


# Update Slide
def updateSlide(request, idSlide):
    slide = Slide.objects.get(id=idSlide)
    if slide is not None:
        slide.title = request.POST['txtNameSlide']
        slide.url = request.POST['txtURL']
        slide.position = request.POST['slPosition']
        if request.FILES.get('txtImages'):
            slide.image = request.FILES.get('txtImages')
        slide.save()
        messages.success(request, '' + slide.title + u' cập nhật thành công')
        return redirect(showAllSlide)
    return render(request, 'slide/editSlide.html', {'slide': slide})


# VIDEO MODEL
def showAllVideo(request):
    listVideo = Video.objects.all()
    return render(request, 'video/video.html', {'listVideo': listVideo})


# Get 1 video to edit
def getVideo(request, idVideo):
    video = Video.objects.get(id=idVideo)
    return render(request, 'video/editVideo.html', {'video': video})


# Get profile of Slide
def get_Video(request, idVideo):
    video = Video.objects.get(id=idVideo)
    data = []
    data.append({
        'id': video.id,
        'title': video.title
    })
    return JsonResponse({'data': data})


# Delete 1 Video
def deleteVideo(request):
    if request.method == 'POST':
        id_video = request.POST.get('id_video')
        video = Video.objects.get(id=id_video)
        if video:
            try:
                video.delete()
            except:
                messages.error(request, u'Xóa' + video.title + u' thất bại')
        return redirect(showAllVideo)


# Create new Video
def createVideo(request):
    if request.method == 'POST':
        title = request.POST['txtTitle']
        url = request.POST['txtURL']
        avatar = request.FILES.get('txtImages')
        slide = Video(title=title, url=url, avatar=avatar)
        slide.save()
        messages.success(request, u'Video tạo thành công')
        return redirect(showAllVideo)
    else:
        return render(request, 'video/addVideo.html')


# Update Video
def updateVideo(request, idVideo):
    video = Video.objects.get(id=idVideo)
    if video is not None:
        video.title = request.POST['txtTitle']
        video.url = request.POST['txtURL']
        if request.FILES.get('txtImages'):
            video.avatar = request.FILES.get('txtImages')
        video.save()
        messages.success(request, u'Cập nhật thành công')
        return redirect(showAllVideo)
    return render(request, 'video/editVideo.html', {'video': video})


# PORTFOLIO POSTS
# Get all data about portfolio post
def showAllPortfolioPosts(request):
    listPortfolioPosts = PortfolioPosts.objects.all()
    return render(request, 'portfolioposts/portfolioposts.html', {'listPortfolioPosts': listPortfolioPosts})


# Get 1 Portfolio Posts to edit
def getPortfolioPosts(request, idPortfolio):
    portfolioPosts = PortfolioPosts.objects.get(id=idPortfolio)
    listPortfolioPosts = PortfolioPosts.objects.filter(id_parent=0)
    context = {'portfolio_posts': portfolioPosts, 'listPortfolioPosts': listPortfolioPosts}
    return render(request, 'portfolioposts/editPortfolioPosts.html', context)


# Get profile of Portfolio Posts
def get_PortfolioPosts(request, idPortfolio):
    portfolio_posts = PortfolioPosts.objects.get(id=idPortfolio)
    data = []
    data.append({
        'id': portfolio_posts.id,
        'name_portfolio_posts': portfolio_posts.name_portfolio_posts
    })
    return JsonResponse({'data': data})


# Delete 1 Portfolio Posts
def deletePortfolioPosts(request):
    if request.method == 'POST':
        id_portfolio_delete = request.POST.get('id_portfolio_delete')
        portfolio_posts = PortfolioPosts.objects.get(id=id_portfolio_delete)
        if portfolio_posts:
            try:
                portfolio_posts.delete()
            except:
                messages.error(request, u'Xóa  ' + portfolio_posts.name_portfolio_posts + u' thất bại')
        return redirect(showAllPortfolioPosts)


# Create new Portfolio Posts
def createPortfolioPosts(request):
    if request.method == 'POST':
        name_portfolio_posts = request.POST['txtNamePortfolio']
        id_parent = request.POST['slPortfolioParent']
        portfolio_posts = PortfolioPosts(name_portfolio_posts=name_portfolio_posts, id_parent=id_parent)
        portfolio_posts.save()
        messages.success(request, '' + name_portfolio_posts + u' tạo thành công !')
        return redirect(showAllPortfolioPosts)
    else:
        listPortfolioPosts = PortfolioPosts.objects.filter(id_parent=0)
        return render(request, 'portfolioposts/addPortfolioPosts.html', {'listPortfolioPosts': listPortfolioPosts})


# Update Portfolio Posts
def updatePortfolioPosts(request, idPortfolio):
    portfolio_posts = PortfolioPosts.objects.get(id=idPortfolio)
    listPortfolioPosts = PortfolioPosts.objects.filter(id_parent=0)
    if portfolio_posts is not None:
        portfolio_posts.name_portfolio_posts = request.POST['txtNamePortfolio']
        if request.POST['slPortfolioParent'] != idPortfolio:
            portfolio_posts.id_parent = request.POST['slPortfolioParent']
        portfolio_posts.save()
        messages.success(request, '' + portfolio_posts.name_portfolio_posts + u' cập nhật thành công')
        return redirect(showAllPortfolioPosts)
    context = {'portfolio_posts': portfolio_posts, 'listPortfolioPosts': listPortfolioPosts}
    return render(request, 'portfolioposts/editPortfolioPosts.html', context)


# POSTS MODEL
# Get all data about Posts
def showAllPosts(request):
    query = request.GET.get('search')
    if query:
        listPosts = Posts.objects.filter(Q(title__icontains=query))
    else:
        listPosts = Posts.objects.all()
    return render(request, 'posts/posts.html', {'listPosts': listPosts})


# Get 1 Posts to edit
def getPosts(request, idPosts):
    posts = Posts.objects.get(id=idPosts)
    listPortfolioPosts = PortfolioPosts.objects.all()
    return render(request, 'posts/editPosts.html', {'posts': posts, 'listPortfolioPosts': listPortfolioPosts})


# Get profile of Posts
def get_Posts(request, idPosts):
    posts = Posts.objects.get(id=idPosts)
    data = []
    data.append({
        'id': posts.id,
        'title': posts.title
    })
    return JsonResponse({'data': data})


# Delete 1 Post
def deletePosts(request):
    if request.method == 'POST':
        id_posts = request.POST.get('id_posts')
        posts = Posts.objects.get(id=id_posts)
        if posts:
            try:
                posts.delete()
            except:
                messages.error(request, u'Xóa ' + posts.title + u' thất bại')
        return redirect(showAllPosts)


# Create new Posts
def createPosts(request):
    if request.method == 'POST':
        title = request.POST['txtTitle']
        portfolio_posts = PortfolioPosts.objects.get(id=request.POST['slPortfolioParent'])
        avatar_posts = request.FILES.get('txtImages')
        content = request.POST['txtContent']
        posts = Posts(title=title, portfolio_posts=portfolio_posts, avatar_posts=avatar_posts, content=content)
        posts.save()
        messages.success(request, '' + title + u' tạo thành công !')
        return redirect(showAllPosts)
    else:
        listPortfolioPosts = PortfolioPosts.objects.all()
        return render(request, 'posts/addPosts.html', {'listPortfolioPosts': listPortfolioPosts})


# Update Posts
def updatePosts(request, idPosts):
    posts = Posts.objects.get(id=idPosts)
    if posts is not None:
        posts.title = request.POST['txtTitle']
        posts.portfolio_posts = PortfolioPosts.objects.get(id=request.POST['slPortfolioParent'])
        if request.FILES.get('txtImages'):
            posts.avatar_posts = request.FILES.get('txtImages')
        posts.content = request.POST['txtContent']
        posts.save()
        messages.success(request, '' + posts.title + u' cập nhật thành công')
        return redirect(showAllPosts)
    return render(request, 'posts/editPosts.html', {'posts': posts})


# For user table
def login(request):
    return render(request, 'users/login.html')


def logout(request):
    if 'user_login' in request.session:
        del request.session['user_login']
    return redirect(login)


@user_login_required
def home_page(request):
    user_login = User.objects.get(username=request.session['user_login']['username'])
    return render(request, 'home_page.html', {'user_login': user_login})


def remove_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)


@user_login_required
def get_user(request, id_user):
    get_user_id = User.objects.get(id_user=id_user)
    data_user = []
    data_user.append({
        'id_user': get_user_id.id_user,
        'username': get_user_id.username,
        'name_user': get_user_id.name_user,
        'password': get_user_id.password,
        'email': get_user_id.email,
        'avatar': str(get_user_id.avatar.url) if str(get_user_id.avatar) != '' and str(
            get_user_id.avatar) is not None else None,
        'status': get_user_id.status
    })
    return JsonResponse({'data': data_user})


@user_login_required
def check_user_exist(request, query):
    get_user_exist = User.objects.filter(Q(username=query) | Q(email=query)).all()
    data_user = {}
    for user_item in get_user_exist:
        data_user = {
            'id_user': user_item.id_user,
            'username': user_item.username,
            'email': user_item.email,
        }
    return JsonResponse(data=data_user, safe=False)


def handle_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        check_exist = User.objects.filter(username=username,
                                          password=hashlib.md5(bytes(password, 'ascii')).hexdigest()).first()
        if check_exist:
            user_login_session = User.objects.get(username=username)
            request.session['user_login'] = {
                'username': user_login_session.username,
                'avatar': str(user_login_session.avatar.url) if str(user_login_session.avatar) != '' and str(
                    user_login_session.avatar) is not None else None,
            }
            return HttpResponseRedirect(reverse('user_page'))
        else:
            messages.add_message(request, messages.WARNING, 'Username/Password is incorrect...')
            return redirect(login)
    return redirect(login)


@user_login_required
def user_page(request):
    query = request.GET.get('search')
    list_user = []
    user_login = User.objects.get(username=request.session['user_login']['username'])
    if user_login:
        list_user = User.objects.all()
    if query:
        list_user = User.objects.filter(Q(name_user__icontains=query) | Q(
            username__icontains=query) | Q(email__icontains=query)).all()

    context = {
        'list_user': list_user,
        'user_login': user_login,
    }
    return render(request, 'users/user_page.html', context)


@user_login_required
def update_user(request):
    list_check_err = []
    if request.method == 'POST':
        id_user = request.POST.get('id_user')
        username = request.POST.get('username')
        name_user = request.POST.get('name_user')
        password = request.POST['password']
        email = request.POST['email']
        avatar = request.FILES.get('avatar_img')
        status = bool(request.POST.get('status'))
        if id_user:
            remove_avatar = ''
            user_edit = User.objects.get(id_user=id_user)
            user_edit.username = username
            user_edit.name_user = name_user
            if password != user_edit.password:
                user_edit.password = hashlib.md5(bytes(password, 'ascii')).hexdigest()
            if avatar is None or avatar == '':
                avatar = user_edit.avatar
            else:
                check_null_avatar = str(user_edit.avatar.path) if str(user_edit.avatar) is not None and str(
                    user_edit.avatar) != '' else None
                if check_null_avatar:
                    remove_avatar = user_edit.avatar.path
            user_edit.email = email
            user_edit.avatar = avatar
            user_edit.status = status
            try:
                # update session user_login
                if username == request.session['user_login']['username']:
                    request.session['user_login']['username'] = user_edit.username
                    session_avatar = str(user_edit.avatar.name) if str(user_edit.avatar.name) != '' and str(
                        user_edit.avatar.name) is not None else None
                    if session_avatar is not None:
                        request.session['user_login']['avatar'] = settings.MEDIA_URL + 'images/' + session_avatar
                    request.session.modified = True
                user_edit.save()
                remove_file(remove_avatar)
                messages.success(request, user_edit.username + ' is updated successfully')
            except Exception as e:
                messages.error(request, user_edit.username + ' is updated failed' + ' ' + e)
        else:
            try:
                password_encode = hashlib.md5(bytes(password, 'ascii')).hexdigest()
                user_add = User(username=username, name_user=name_user, password=password_encode, email=email,
                                avatar=avatar, status=status)
                user_add.save()
                messages.success(request, username + ' is added successfully')
            except Exception as e:
                messages.error(request, username + ' is added failed' + ' ' + e)
        for message in list_check_err:
            messages.error(request, message)
        return redirect(user_page)


@user_login_required
def delete_user(request):
    if request.method == 'POST':
        id_user = request.POST.get('id_user_delete')
        user_perm = User.objects.get(id_user=int(id_user))
        if user_perm:
            try:
                user_perm.delete()
                remove_file(user_perm.avatar.path)
                messages.success(request, user_perm.username + ' is deleted successfully')
            except Exception as e:
                messages.error(request, user_perm.username + ' is deleted failed' + e)
        return redirect(user_page)


def send_mail_user(subject_content, message_content, mail_user, project):
    list_receiver = []
    list_check_error = []
    try:
        get_mail_manager = User.objects.filter(Q(id_project__id_project=project) | Q(user_role__lte=1))
        for user in get_mail_manager:
            list_receiver.append(user.email)
        if mail_user is not None:
            list_receiver.append(mail_user)
        if list_receiver:
            try:
                send_mail(subject=subject_content, message=message_content, from_email=settings.MAIL_HOST,
                          recipient_list=list_receiver, fail_silently=False)
            except:
                list_check_error.append('Cannot send mail to email ')
    except:
        return list_check_error

    return list_check_error


def forget_password(request):
    return render(request, 'users/forget_password.html')


def handle_forget_password(request):
    if request.method == 'POST':
        username = request.POST.get('username_forgetpass')
        email = request.POST.get('email_forgetpass')
        try:
            check_username_exist = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.warning(request, 'username:' + username + " doesn't exist")
            return redirect(forget_password)
        if check_username_exist:
            mail_project = check_username_exist.id_project.id_project
            list_check_send = send_mail_user("Reset Password",
                                             "User " + username + " with email: " + email + ".Please check and help to reset password",
                                             None, mail_project)
            if list_check_send:
                for message in list_check_send:
                    messages.error(request, message)
            else:
                messages.success(request, "Your mail sent to admin for reseting password")
    return redirect(forget_password)


# PROJECT MODEL
# Get all data about project
def showAllProject(request):
    query = request.GET.get('search')
    if query:
        listProject = Project.objects.filter(Q(name_project__icontains=query))
    else:
        listProject = Project.objects.all()
    return render(request, 'project/project.html', {'listProject': listProject})


# Get 1 Project to edit
def getProject(request, idProject):
    project = Project.objects.get(id=idProject)
    listPortfolioProject = PortfolioProject.objects.all()
    listAlbum = Album.objects.filter(id_project=idProject)
    listArea = Area.objects.all()
    return render(request, 'project/editProject.html',
                  {'project': project, 'listPortfolioProject': listPortfolioProject, 'listArea': listArea, 'listAlbum':listAlbum})


# Get profile of Project
def get_Project(request, idProject):
    project = Project.objects.get(id=idProject)
    data = []
    data.append({
        'id': project.id,
        'name_project': project.name_project
    })
    return JsonResponse({'data': data})


# Delete 1 Project
def deleteProject(request):
    if request.method == 'POST':
        id_project = request.POST.get('id_project')
        project = Project.objects.get(id=id_project)
        if project:
            try:
                project.delete()
            except:
                messages.error(request, u'Xóa ' + project.name_project + u' thất bại')
        return redirect(showAllProject)


# Create new Project
def createProject(request):
    if request.method == 'POST':
        name_project = request.POST['txtNameProject']
        area = Area.objects.get(id=request.POST['slArea'])
        portfolio_project = PortfolioProject.objects.get(id=request.POST['slPortfolioProject'])
        status_progress = request.POST['slStatus']
        status_interior = request.POST['slStatusInterior']
        avatar_image = request.FILES.get('txtImages')
        date = datetime.datetime.strptime(request.POST['txtYear'], '%d/%m/%Y')
        year = date.year
        description_project = request.POST['txtContent']
        project = Project(name_project=name_project, area=area, portfolio_project=portfolio_project,
                          status_progress=status_progress, avatar_image=avatar_image,
                          description_project=description_project, year=year, date=date, status_interior=status_interior)
        project.save()
        photo_album = request.FILES.getlist('txtAlbums')
        for image in photo_album:
            photo = image
            id_project = project.id
            album = Album(photo=photo, id_project=id_project)
            album.save()

        messages.success(request, '' + name_project + u' tạo thành công !')
        return redirect(showAllProject)
    else:
        listPortfolioProject = PortfolioProject.objects.all()
        listArea = Area.objects.all()
        return render(request, 'project/addProject.html',
                      {'listPortfolioProject': listPortfolioProject, 'listArea': listArea})


# Update Project
def updateProject(request, idProject):
    project = Project.objects.get(id=idProject)
    if project is not None:
        project.name_project = request.POST['txtNameProject']
        project.area = Area.objects.get(id=request.POST['slArea'])
        project.portfolio_project = PortfolioProject.objects.get(id=request.POST['slPortfolioProject'])
        project.status_progress = request.POST['slStatus']
        project.status_interior = request.POST['slStatusInterior']
        # if request.FILES.get('txtAlbums'):
        #     project.photo_album = request.FILES.get('txtAlbums')
        if request.FILES.get('txtImages'):
            project.avatar_image = request.FILES.get('txtImages')
        project.description_project = request.POST['txtContent']
        date = datetime.datetime.strptime(request.POST['txtYear'], '%d/%m/%Y')
        project.date = date
        project.year = date.year
        project.save()
        messages.success(request, '' + project.name_project + u' cập nhật thành công')
        return redirect(showAllProject)
    return render(request, 'project/editProject.html', {'project': project})


# Implement for Index page
def showIndex(request):
    listPortfolioPosts = PortfolioPosts.objects.all()
    listPortfolioProject = PortfolioProject.objects.all()
    listArea = Area.objects.all()
    listVideo = Video.objects.all()
    listProject = Project.objects.filter(status_interior=False)[0:10]
    listProject_Interior = Project.objects.filter(status_interior=True)[0:10]
    listMember = Member.objects.all()[0:10]
    listSlide = Slide.objects.all()
    listPost = Posts.objects.all()[0:5]
    isIndex = True

    postCompany = PortfolioPosts.objects.get(id=6)
    postMarket = PortfolioPosts.objects.get(id=5)
    listPostCompany = []
    listMarket = []
    listSubMenu = []
    if postCompany:
        listPostCompany = Posts.objects.filter(portfolio_posts=postCompany)[0:3]

    if postMarket:
        listMarket = Posts.objects.filter(portfolio_posts=postMarket)[0:3]

    for item in listPortfolioPosts:
        if listPortfolioPosts.filter(id_parent=item.id).count() > 0:
            listSubMenu.append(item.id)

    data = {'listPortfolioPosts': listPortfolioPosts,
            'listSubMenu': listSubMenu,
            'listPortfolioProject': listPortfolioProject,
            'listArea': listArea,
            'listVideo': listVideo,
            'listProject': listProject,
            'listProject_Interior':listProject_Interior,
            'listMember': listMember,
            'listPostCompany': listPostCompany,
            'listMarket': listMarket,
            'listSlide': listSlide,
            'listPost': listPost,
            'isIndex': isIndex}
    return render(request, 'frontend/index.html', data)


def showListPostByIdPortfolio(request, idPortfolio):
    # List block
    listPortfolioPosts = PortfolioPosts.objects.all()
    listPortfolioProject = PortfolioProject.objects.all()
    listArea = Area.objects.all()
    listSubMenu = []
    for item in listPortfolioPosts:
        if listPortfolioPosts.filter(id_parent=item.id).count() > 0:
            listSubMenu.append(item.id)
    listMember = Member.objects.all()[0:10]

    # Add more
    name_parent = ''
    listPortfolioPostsParent = []
    portfolioPosts = PortfolioPosts.objects.get(id=idPortfolio)
    listProject = Project.objects.all()[0:10]
    listPost = []
    if portfolioPosts:
        listPost = Posts.objects.filter(portfolio_posts=portfolioPosts)
        if listPost.count() == 1:
            idPost = listPost[0].id
            post = Posts.objects.get(id=idPost)
            listPost = Posts.objects.filter(portfolio_posts=post.portfolio_posts)[0:3]

            if post.portfolio_posts.id_parent != 0:
                listPortfolioPostsParent = PortfolioPosts.objects.filter(id_parent=post.portfolio_posts.id_parent)
                name_parent = PortfolioPosts.objects.get(id=post.portfolio_posts.id_parent).name_portfolio_posts

            data = {'listPortfolioPosts': listPortfolioPosts,
                    'listPortfolioProject': listPortfolioProject,
                    'listSubMenu': listSubMenu,
                    'listMember': listMember,
                    'listProject': listProject,
                    'listArea': listArea,
                    'post': post,
                    'name_parent': name_parent,
                    'listPortfolioPostsParent': listPortfolioPostsParent,
                    'listPost': listPost}
            return render(request, 'frontend/post_detail.html', data)
        paginator = Paginator(listPost, 5)  # Show 5 product per page
        page = request.GET.get('page')
        try:
            listPost = paginator.page(page)
        except PageNotAnInteger:
            listPost = paginator.page(1)
        except EmptyPage:
            listPost = paginator.page(paginator.num_pages)

    if portfolioPosts.id_parent != 0:
        listPortfolioPostsParent = PortfolioPosts.objects.filter(id_parent=portfolioPosts.id_parent)
        name_parent = PortfolioPosts.objects.get(id=portfolioPosts.id_parent).name_portfolio_posts

    data = {'listPortfolioPosts': listPortfolioPosts,
            'listPortfolioProject': listPortfolioProject,
            'listSubMenu': listSubMenu,
            'listMember': listMember,
            'listProject': listProject,
            'listArea': listArea,
            'listPost': listPost,
            'portfolioPosts': portfolioPosts,
            'listPortfolioPostsParent': listPortfolioPostsParent,
            'name_parent': name_parent}
    return render(request, 'frontend/news.html', data)


def showListPostByIdProject(request, idProject):
    # List block
    listPortfolioPosts = PortfolioPosts.objects.all()
    listPortfolioProject = PortfolioProject.objects.all()
    listArea = Area.objects.all()
    listSubMenu = []
    for item in listPortfolioPosts:
        if listPortfolioPosts.filter(id_parent=item.id).count() > 0:
            listSubMenu.append(item.id)
    listMember = Member.objects.all()[0:10]

    # Add more
    portfolioProject = PortfolioProject.objects.get(id=idProject)
    name = ''
    listProject = []
    if portfolioProject:
        name = portfolioProject.name_portfolio_project
        listProject = Project.objects.filter(portfolio_project=portfolioProject)
        paginator = Paginator(listProject, 9)  # Show 5 product per page
        page = request.GET.get('page')
        try:
            listProject = paginator.page(page)
        except PageNotAnInteger:
            listProject = paginator.page(1)
        except EmptyPage:
            listProject = paginator.page(paginator.num_pages)

    data = {'listPortfolioPosts': listPortfolioPosts,
            'listPortfolioProject': listPortfolioProject,
            'listSubMenu': listSubMenu,
            'listMember': listMember,
            'listArea': listArea,
            'listProject': listProject,
            'name': name}
    return render(request, 'frontend/project_by_id_portfolio_project.html', data)


def showListProjectByYear(request, year):
    # List block
    listPortfolioPosts = PortfolioPosts.objects.all()
    listPortfolioProject = PortfolioProject.objects.all()
    listArea = Area.objects.all()
    listSubMenu = []
    for item in listPortfolioPosts:
        if listPortfolioPosts.filter(id_parent=item.id).count() > 0:
            listSubMenu.append(item.id)
    listMember = Member.objects.all()[0:10]

    # Add more
    listProject = Project.objects.order_by('-date').filter(year=year)
    data = {'listPortfolioPosts': listPortfolioPosts,
            'listPortfolioProject': listPortfolioProject,
            'listSubMenu': listSubMenu,
            'listMember': listMember,
            'listArea': listArea,
            'listProject': listProject,
            'year': year}
    return render(request, 'frontend/project_by_year.html', data)


def showListProjectByStatus(request, status):
    # List block
    listPortfolioPosts = PortfolioPosts.objects.all()
    listPortfolioProject = PortfolioProject.objects.all()
    listArea = Area.objects.all()
    listSubMenu = []
    for item in listPortfolioPosts:
        if listPortfolioPosts.filter(id_parent=item.id).count() > 0:
            listSubMenu.append(item.id)
    listMember = Member.objects.all()[0:10]

    # Add more
    if status == '1':
        listProject = Project.objects.order_by('-date').filter(status_progress=1)
        name = u'Hoàn thành'
    else:
        listProject = Project.objects.order_by('-date').filter(status_progress=0)
        name = u'Đang thi công'
    paginator = Paginator(listProject, 9)  # Show 5 product per page
    page = request.GET.get('page')
    try:
        listProject = paginator.page(page)
    except PageNotAnInteger:
        listProject = paginator.page(1)
    except EmptyPage:
        listProject = paginator.page(paginator.num_pages)

    data = {'listPortfolioPosts': listPortfolioPosts,
            'listPortfolioProject': listPortfolioProject,
            'listSubMenu': listSubMenu,
            'listMember': listMember,
            'listArea': listArea,
            'listProject': listProject,
            'name': name}
    return render(request, 'frontend/project_by_id_portfolio_project.html', data)


def showListProjectByArea(request, idArea):
    # List block
    listPortfolioPosts = PortfolioPosts.objects.all()
    listPortfolioProject = PortfolioProject.objects.all()
    listArea = Area.objects.all()
    listSubMenu = []
    for item in listPortfolioPosts:
        if listPortfolioPosts.filter(id_parent=item.id).count() > 0:
            listSubMenu.append(item.id)
    listMember = Member.objects.all()[0:10]

    # Add more
    area = listArea.get(id=idArea)
    listProject = Project.objects.order_by('-date').filter(area=area)
    paginator = Paginator(listProject, 9)  # Show 5 product per page
    page = request.GET.get('page')
    try:
        listProject = paginator.page(page)
    except PageNotAnInteger:
        listProject = paginator.page(1)
    except EmptyPage:
        listProject = paginator.page(paginator.num_pages)

    data = {'listPortfolioPosts': listPortfolioPosts,
            'listPortfolioProject': listPortfolioProject,
            'listSubMenu': listSubMenu,
            'listMember': listMember,
            'listArea': listArea,
            'listProject': listProject,
            'name': area.name_area}
    return render(request, 'frontend/project_by_id_portfolio_project.html', data)



def showDetailPost(request, idPost):
    # List block
    listPortfolioPosts = PortfolioPosts.objects.all()
    listPortfolioProject = PortfolioProject.objects.all()
    listArea = Area.objects.all()
    listSubMenu = []
    for item in listPortfolioPosts:
        if listPortfolioPosts.filter(id_parent=item.id).count() > 0:
            listSubMenu.append(item.id)
    listMember = Member.objects.all()[0:10]

    # Add more
    name_parent = ''
    listProject = Project.objects.all()[0:10]
    post = Posts.objects.get(id=idPost)
    listPost = Posts.objects.filter(portfolio_posts=post.portfolio_posts)[0:3]

    listPortfolioPostsParent = []
    if post.portfolio_posts.id_parent != 0:
        listPortfolioPostsParent = PortfolioPosts.objects.filter(id_parent=post.portfolio_posts.id_parent)
        name_parent = PortfolioPosts.objects.get(id=post.portfolio_posts.id_parent).name_portfolio_posts

    data = {'listPortfolioPosts': listPortfolioPosts,
            'listPortfolioProject': listPortfolioProject,
            'listSubMenu': listSubMenu,
            'listMember': listMember,
            'listProject': listProject,
            'listArea': listArea,
            'post': post,
            'name_parent': name_parent,
            'listPortfolioPostsParent': listPortfolioPostsParent,
            'listPost': listPost}
    return render(request, 'frontend/post_detail.html', data)


def showDetailProject(request, idProject):
    # List block
    listPortfolioPosts = PortfolioPosts.objects.all()
    listPortfolioProject = PortfolioProject.objects.all()
    listArea = Area.objects.all()
    listAlbums =Album.objects.filter(id_project=idProject)
    listSubMenu = []
    for item in listPortfolioPosts:
        if listPortfolioPosts.filter(id_parent=item.id).count() > 0:
            listSubMenu.append(item.id)
    listMember = Member.objects.all()[0:10]

    # Add more
    project = Project.objects.get(id=idProject)
    listProject = Project.objects.filter(portfolio_project=project.portfolio_project)[0:3]
    data = {'listPortfolioPosts': listPortfolioPosts,
            'listPortfolioProject': listPortfolioProject,
            'listSubMenu': listSubMenu,
            'listMember': listMember,
            'listArea': listArea,
            'listProject': listProject,
            'project': project,
            'listAlbums': listAlbums,
            'isProjectDetail': True}
    return render(request, 'frontend/project_detail.html', data)


def showDetailContentPortfolioProject(request, idPortfolioProject):
    # List block
    listPortfolioPosts = PortfolioPosts.objects.all()
    listPortfolioProject = PortfolioProject.objects.all()
    listArea = Area.objects.all()
    listSubMenu = []
    for item in listPortfolioPosts:
        if listPortfolioPosts.filter(id_parent=item.id).count() > 0:
            listSubMenu.append(item.id)
    listMember = Member.objects.all()[0:10]

    # Add more
    name_parent = ''
    listProject = Project.objects.all()[0:10]
    portfolioProject = PortfolioProject.objects.get(id=idPortfolioProject)

    data = {'listPortfolioPosts': listPortfolioPosts,
            'listPortfolioProject': listPortfolioProject,
            'listSubMenu': listSubMenu,
            'listMember': listMember,
            'listProject': listProject,
            'listArea': listArea,
            'portfolioProject': portfolioProject,
            'name_parent': name_parent}
    return render(request, 'frontend/content_portfolio_project_detail.html', data)