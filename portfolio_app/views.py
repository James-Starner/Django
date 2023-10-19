from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic
from portfolio_app.forms import *
from portfolio_app.models import *

# Create your views here.
def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})



class StudentListView(generic.ListView):
    model = Student
class StudentDetailView(generic.DetailView):
    model = Student

class ProjectListView(generic.ListView):
    model = Project
class ProjectDetailView(generic.DetailView):
    model = Project

class PortfolioListView(generic.ListView):
    model = Portfolio
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    def get_context_data(self, **kwargs): #change this later
        context = super().get_context_data(**kwargs)
        context['project_list'] = Project.objects.all()
        return context
    

def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        
        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)





def updateProject(request, portfolio_id, project_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    project = Project.objects.get(pk=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)  # Pass the instance to pre-fill the form
        if form.is_valid():
            form.save()
            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)
    else:
        form = ProjectForm(instance=project)  # Initialize the form with the instance

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)

def deleteProject(request, portfolio_id, project_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    project = Project.objects.get(pk=project_id)
    
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio-detail', portfolio_id)
    context = {
        'project': project,  # Pass the project object to the template context
    }

    return render(request, 'portfolio_app/project_delete.html', context)

def updatePortfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)

    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)  # Pass the instance to pre-fill the form
        if form.is_valid():
            form.save()
            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)
    else:
        form = PortfolioForm(instance=portfolio)  # Initialize the form with the instance

    context = {'form': form}
    return render(request, 'portfolio_app/portfolio_form.html', context)



"""   
from portfolio_app.models import Portfolio, Project
project = Project.objects.all()
portfolio = Portfolio.objects.all()
Projects = Project.objects.filter(project.portfolio == portfolio)
for project in Projects
print (project\n)
"""