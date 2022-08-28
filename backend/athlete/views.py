from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from django.urls import reverse
from django.views.generic import UpdateView, DetailView, DeleteView

from db.models import User, Train

from .forms import AthleteEditAvatar, AthleteEditForm, NewTrainForm, TrainEditForm


class AthleteView(LoginRequiredMixin, DetailView):
    template_name = "athlete/cabinet.html"
    queryset = User.objects.all()

    def get_object(self, queryset=None):
        return self.queryset.annotate(count=Count('trains')).get(pk=self.request.user.pk)


class AthleteEditView(LoginRequiredMixin, UpdateView):
    model = User

    form_class = AthleteEditForm
    avatar_form_class = AthleteEditAvatar

    template_name = 'athlete/edit.html'
    success_url = '/athlete/'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        if 'form' not in kwargs:
            kwargs['form'] = self.form_class(instance=self.get_object())
        if 'avatar_form' not in kwargs:
            kwargs['avatar_form'] = self.avatar_form_class(instance=self.get_object())

        return super(AthleteEditView, self).get_context_data(**kwargs)


class TrainEditView(UpdateView):
    model = Train
    form_class = TrainEditForm
    success_url = '/trains-user/'
    template_name = 'athlete/edit_train.html'


class TrainDeleteView(DeleteView):
    model = Train
    success_url = '/trains-user/'
    template_name = 'athlete/delete_train.html'


@login_required
def change_avatar(request):
    if request.method == 'POST':
        data = AthleteEditAvatar(request.POST, request.FILES, instance=request.user)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect(reverse('athlete'))


def add_train(request):
    if request.method == 'POST':
        form = NewTrainForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('athlete')
    else:
        form = NewTrainForm()
    return render(request, 'athlete/add_train.html', {'form': form})


def get_trains_user(request):
    trains_user_list = Train.objects.filter(author__username=request.user.username)
    return render(request, 'athlete/trains.html', {"trains_user_list": trains_user_list})
