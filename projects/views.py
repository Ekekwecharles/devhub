from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import searchProject, paginateProjects

# Create your views here.

def projects(request):
    projects, search_query = searchProject(request)
    custom_range, projects = paginateProjects(request, projects, 3)

    context = {
        'projects': projects,
        'search_query': search_query,
        'custom_range': custom_range
        }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    form =  ReviewForm()
    tags = projectobj.tags.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectobj
        review.owner = request.user.profile
        review.save()

        projectobj.getVoteCount

        messages.success(request, "Your review was successfully submitted!")
        return redirect('project', pk=projectobj.id)

    context = {
        'project': projectobj,
        'tags': tags,
        'form': form,
    }
    return render(request, 'projects/single_project.html', context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        # Create a new instance of that form
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    # Prefills all the form fields with the project data
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()


        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('account')
    context = {'form': form, 'project': project}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    # project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {'object': project}
    return render(request, 'delete_template.html', context) 