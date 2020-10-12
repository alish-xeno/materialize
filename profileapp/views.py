from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import *
from .models import *


# HANDLERS
# HANDLERS
# HANDLERS
# HANDLERS


def handle404(request, exception=None):
    return render(request, '404.html', {
        # 'orginfo': OrgnizationalInformation.objects.first(),
        # 'webreq': WebsiteRequirement.objects.first(),
        # 'allcategories': Category.objects.filter(is_active=True),
        # 'clientsubscriberform': ClientSubscriberForm
    })


def handle500(request, exception=None):
    return render(request, '500.html', {
        # 'orginfo': OrgnizationalInformation.objects.first(),
        # 'webreq': WebsiteRequirement.objects.first(),
        # 'allcategories': Category.objects.filter(is_active=True),
        # 'clientsubscriberform': ClientSubscriberForm
    })


# Client Page
class ClientHomeView(TemplateView):
    template_name = "clienthome.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allsliders'] = Gallery.objects.get(slug='slider')

        return context


class ClientProfileView(TemplateView):
    template_name = "clientprofile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = Admin.objects.first()

        return context

