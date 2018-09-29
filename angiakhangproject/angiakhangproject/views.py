from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib import messages


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
    data_portfolioproject= []
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
        portfolio_project = PortfolioProject(name_portfolio_project=name_portfolio_project)
        portfolio_project.save()
        return redirect(showAllPortfolioProject)
    else:
        return render(request, 'portfolioproject/addPortfolioProject.html')


# Update Portfolio Project
def updatePortfolioProject(request, idPortfolio):
    portfolio_project = PortfolioProject.objects.get(id=idPortfolio)
    if portfolio_project is not None:
        portfolio_project.name_portfolio_project = request.POST['txtNamePortfolio']
        portfolio_project.save()
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
    data_area= []
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
                messages.error(request, 'Delete' + area.name_area + ' failed')
        return redirect(showAllArea)


# Create new Area
def createArea(request):
    if request.method == 'POST':
        name_area = request.POST['txtNameArea']
        area = Area(name_area=name_area)
        area.save()
        return redirect(showAllArea)
    else:
        return render(request, 'area/addArea.html')


# Update Area
def updateArea(request, idArea):
    area = Area.objects.get(id=idArea)
    if area is not None:
        area.name_area = request.POST['txtNameArea']
        area.save()
        return redirect(showAllArea)
    return render(request, 'area/editArea.html', {'area': area})


#MEMBER MODEL
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
                messages.error(request, 'Delete' + member.name_company_member + ' failed')
        return redirect(showAllMember)


# Create new Member
def createMember(request):
    if request.method == 'POST':
        name_company_member = request.POST['txtNameMember']
        description = request.POST['txtDescription']
        type = request.POST['cbbType']
        avatar_member = request.FILES.get('txtImages')
        member = Member(name_company_member=name_company_member, avatar_member=avatar_member, description=description, type=type)
        member.save()
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
        member.avatar_member = request.FILES.get('txtImages')
        member.save()
        return redirect(showAllMember)
    return render(request, 'member/editMember.html', {'member': member})


#SLIDE MODEL
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
                messages.error(request, 'Delete' + slide.title + ' failed')
        return redirect(showAllSlide)


# Create new Slide
def createSlide(request):
    if request.method == 'POST':
        title = request.POST['txtNameSlide']
        image = request.FILES.get('txtImages')
        slide = Slide(title=title, image=image)
        slide.save()
        return redirect(showAllSlide)
    else:
        return render(request, 'slide/addSlide.html')


# Update Slide
def updateSlide(request, idSlide):
    slide = Slide.objects.get(id=idSlide)
    if slide is not None:
        slide.title = request.POST['txtNameSlide']
        slide.image = request.FILES.get('txtImages')
        slide.save()
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
                messages.error(request, 'Delete' + video.title + ' failed')
        return redirect(showAllVideo)


# Create new Video
def createVideo(request):
    if request.method == 'POST':
        title = request.POST['txtTitle']
        url = request.POST['txtURL']
        slide = Video(title=title, url=url)
        slide.save()
        return redirect(showAllVideo)
    else:
        return render(request, 'video/addVideo.html')


# Update Video
def updateVideo(request, idVideo):
    video = Video.objects.get(id=idVideo)
    if video is not None:
        video.title = request.POST['txtTitle']
        video.url = request.POST['txtURL']
        video.save()
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
                messages.error(request, 'Deleting ' + portfolio_posts.name_portfolio_posts + ' failed')
        return redirect(showAllPortfolioPosts)


# Create new Portfolio Posts
def createPortfolioPosts(request):
    if request.method == 'POST':
        name_portfolio_posts = request.POST['txtNamePortfolio']
        id_parent = request.POST['slPortfolioParent']
        portfolio_posts = PortfolioPosts(name_portfolio_posts=name_portfolio_posts, id_parent=id_parent)
        portfolio_posts.save()
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
    data= []
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
                messages.error(request, 'Delete' + posts.title + ' failed')
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
        posts.avatar_posts = request.FILES.get('txtImages')
        posts.content = request.POST['txtContent']
        posts.save()
        return redirect(showAllPosts)
    return render(request, 'posts/editPosts.html', {'posts': posts})


# PROJECT MODEL
# Get all data about project
def showAllProject(request):
    query = request.GET.get('search')
    if query:
        listProject= Project.objects.filter(Q(name_project__icontains=query))
    else:
        listProject = Project.objects.all()
    return render(request, 'project/project.html', {'listProject': listProject})


# Get 1 Project to edit
def getProject(request, idProject):
    project = Project.objects.get(id=idProject)
    listPortfolioProject = PortfolioProject.objects.all()
    listArea = Area.objects.all()
    return render(request, 'project/editProject.html', {'project': project, 'listPortfolioProject': listPortfolioProject, 'listArea':listArea})

# Get profile of Project
def get_Project(request, idProject):
    project = Project.objects.get(id=idProject)
    data= []
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
                messages.error(request, 'Delete' + project.name_project + ' failed')
        return redirect(showAllProject)


# Create new Project
def createProject(request):
    if request.method == 'POST':
        name_project = request.POST['txtNameProject']
        area = Area.objects.get(id=request.POST['slArea'])
        portfolio_project = PortfolioProject.objects.get(id=request.POST['slPortfolioProject'])
        status_progress = request.POST['slStatus']
        photo_album = request.FILES.get('txtAlbums')
        avatar_image = request.FILES.get('txtImages')
        year = request.POST['txtYear']
        description_project = request.POST['txtContent']
        project = Project(name_project=name_project, area=area, portfolio_project=portfolio_project,
                          status_progress=status_progress, photo_album=photo_album,
                          avatar_image=avatar_image, description_project=description_project, year=year)
        project.save()
        return redirect(showAllProject)
    else:
        listPortfolioProject = PortfolioProject.objects.all()
        listArea = Area.objects.all()
        return render(request, 'project/addProject.html', {'listPortfolioProject': listPortfolioProject, 'listArea': listArea})


# Update Posts
def updateProject(request, idProject):
    project = Project.objects.get(id=idProject)
    if project is not None:
        project.name_project = request.POST['txtNameProject']
        project.area = Area.objects.get(id=request.POST['slArea'])
        project.portfolio_project = PortfolioProject.objects.get(id=request.POST['slPortfolioProject'])
        project.status_progress = request.POST['slStatus']
        project.photo_album = request.FILES.get('txtAlbums')
        project.avatar_image = request.FILES.get('txtImages')
        project.description_project = request.POST['txtContent']
        project.year = request.POST['txtYear']
        project.save()
        return redirect(showAllProject)
    return render(request, 'project/editProject.html', {'project': project})
