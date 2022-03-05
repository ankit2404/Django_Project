from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Project , Tag
from .forms import ProjectForm , ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .utils import searchProjects , paginateProjects
from django.core.paginator import Paginator ,PageNotAnInteger , EmptyPage


def projects(request) :
    projects , query_search = searchProjects(request)

    custom_range, projects = paginateProjects(request , projects , 6)

    return render(request , 'projects/projects.html' , {'projects' : projects , 'query_search' : query_search ,  'custom_range' : custom_range} )

def project(request , pk) :
    projectobj = Project.objects.get(id = pk)
    tags = projectobj.tags.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit = False)
        review.project = projectobj
        review.owner = request.user.profile
        review.save()
        projectobj.getVoteCount
 
        messages.success(request , 'Your comment added successfully')
        return redirect('project' , pk=projectobj.id)

    

    return render(request ,'projects/single-project.html' , {'project' : projectobj ,'tags' : tags , 'form' : form} )


@login_required(login_url = 'login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',' , " ").split()
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile
            project.save()
            for tag in newtags : 
                tag , created = Tag.objects.get_or_create(name = tag)
                project.tags.add(tag)
            return redirect('account')

    content = {'form' : form}
    return render(request ,'projects/project_form.html' , content)



@login_required(login_url = 'login')
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)

    form = ProjectForm(instance = project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',' , " ").split()
        print("data" , newtags)
        form = ProjectForm(request.POST , request.FILES , instance = project)
        if form.is_valid():
            project = form.save()
            for tag in newtags : 
                tag , created = Tag.objects.get_or_create(name = tag)
                project.tags.add(tag)

            return redirect('account')

    content = {'form' : form , 'project' : project}
    return render(request ,'projects/project_form.html' , content)


@login_required(login_url = 'login')
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)

    if request.method == 'POST':
        project.delete()
        return redirect('account')

    content = {'object' : project}
    return render(request ,'delete_template.html' , content)


