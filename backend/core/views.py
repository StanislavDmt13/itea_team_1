from django.shortcuts import render
from django.views.generic import ListView
from db.models import Train


def index(request):
    return render(request, 'core/index.html')


# class TrainView(ListView):
#     template_name = 'core/train.html'
#     model = Train


def train(request):
    trains_list = Train.objects.all()
    return render(request, 'core/train.html', {"trains_list": trains_list})

