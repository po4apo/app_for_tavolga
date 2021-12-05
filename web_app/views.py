from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from web_app.models import Event, Nomination, Document


class EventView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = '/events/'
    queryset = Event.objects.all()
    template_name = 'list.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Мероприятия'
        context['path'] = 'nomination'
        context['back'] = None
        return context


class NominationView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = '/events/'
    model = Nomination
    template_name = 'nominations_list.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Номинации'
        context['path'] = 'users'
        context['back'] = 'events'
        return context


    def get(self, request, *args, **kwargs):
        pk = kwargs.pop('pk', None)
        print(pk)
        if pk:
            self.object_list = Nomination.objects.filter(event_id=pk)
            context = self.get_context_data(object_list=self.object_list)
            return self.render_to_response(context)
        else:
            return self.render_to_response(None)

class UserView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = '/events/'
    model = Document
    template_name = 'rating.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Участники'
        context['path'] = 'nomination'
        context['back'] = 'nomination'
        return context

    def get(self, request, *args, **kwargs):
        pk = kwargs.pop('pk', None)
        print(pk)
        if pk:
            old = Document.objects.filter(nomination__id=pk, document_name='old')
            new = Document.objects.filter(nomination__id=pk, document_name='new')
            object_list = []
            for user in old.values_list('user_id'):
                object_list.append( {'old': old.get(user_id=user), 'new':new.get(user_id=user)})
            self.object_list = object_list
            context = self.get_context_data(object_list=self.object_list)
            return self.render_to_response(context)
        else:
            return self.render_to_response(None)

