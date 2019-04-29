from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>Hello this is class based view</h1>')

class TemplatesCBV(TemplateView):
    template_name = 'home.html'

class TemplatesCBVContext(TemplateView):
    template_name = 'info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name']='durga'
        context['subject']='python'
        context['fee']=2000
        return context