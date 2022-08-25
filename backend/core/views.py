from django.shortcuts import render
from django.views.generic import ListView
from db.models import Train, TrainProgram


def index(request):
    return render(request, 'core/index.html')


# class TrainView(ListView):
#     template_name = 'core/train.html'
#     model = Train


def train(request):
    trains_list = Train.objects.all()
    return render(request, 'core/train.html', {"trains_list": trains_list})


def train_page(request, train_pk):
    train_data = Train.objects.get(pk=train_pk)
    return render(request, 'core/train_page.html', {"train_data": train_data, 'title': train_data.title})


def train_program(request):
    train_program_list = TrainProgram.objects.all()
    return render(request, 'core/trainprogram.html', {"train_program_list": train_program_list})

