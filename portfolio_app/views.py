from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from portfolio_app.models import Student

# Create your views here.
def index(request):
# Render index.html
    return render( request, 'portfolio_app/index.html')




class StudentListView(generic.ListView):
    model = Student
class StudentDetailView(generic.DetailView):
    model = Student