from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.urls import reverse
from django.views.generic import TemplateView, UpdateView

from db.models import User

from .forms import AthleteEditAvatar, AthleteEditForm


class AthleteView(LoginRequiredMixin, TemplateView):
    template_name = 'athlete/cabinet.html'


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


@login_required
def change_avatar(request):
    if request.method == 'POST':
        data = AthleteEditAvatar(request.POST, request.FILES, instance=request.user)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect(reverse('athlete'))
