from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.
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