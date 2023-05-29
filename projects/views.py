from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render

projectsList = [
    {
        'id': '1',
        'title': 'Eccomerce Website',
        'description': 'Fully functional ecommerce website',
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This was a project where I built out my portfolio',
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I am still working '
    }
]


def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projectsList': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    return render(request, 'projects/single-project.html')
