from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import *
from .models import *
from .forms import *
from django.http import JsonResponse
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin


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
class ClientMixin(SuccessMessageMixin, object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = Admin.objects.first()
        context['settings_debug'] = settings.DEBUG

        return context


class ClientHomeView(ClientMixin, TemplateView):
    template_name = "clienttemplates/clienthome.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allsliders'] = Gallery.objects.get(slug='slider')

        return context


class ClientProfileView(ClientMixin, TemplateView):
    template_name = "clienttemplates/clientprofile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ClientContactView(ClientMixin, CreateView):
    template_name = "clienttemplates/clientcontact.html"
    form_class = CustomerMessageForm
    success_url = reverse_lazy('profileapp:clienthome')
    success_message = "Message Sent Successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallerylist'] = Gallery.objects.all().order_by('title') 

        context['formset'] = MessageSpecificationFormSet()

        return context

    def form_valid(self, form):
        data = form.cleaned_data
        # print(data)
        gallery = form.save()
        try:
            formset = MessageSpecificationFormSet(data=self.request.POST)
            # formset = MessageSpecificationFormSet(
                # self.request.POST, self.request.FILES)
            # print(formset)
            for index, specform in enumerate(formset):
                print(specform)
                if specform.is_valid():
                    # print('valid +++++++++++++++++')
                    # print(specform)
                    value = specform.cleaned_data['value']
                    specification = specform.cleaned_data['specification']
                    spec = Specification.objects.get(id = specification)
                    MessageSpecificationComment.objects.get_or_create(
                        message_obj = gallery,
                        comment = value,
                        specification=spec)
                    # print(value)


            # Check if submitted forms are valid
            # if formset.is_valid():
            #     for data in formset.cleaned_data:
            #             print(data['value'])
            #             print(data['specification'])
            # if formset.is_valid():
            #     print(formset)
            #     print('success formset........................................')
        except:
            pass
        return super().form_valid(form)

    def form_invalid(self, form):
        print('failed form')
        return super().form_invalid(form)




# Axios Request Views
class AxiosSpecificationListView(ClientMixin, View):
    def get(self, request, *args, **kwargs):
        from django.core import serializers
        cat_id = self.request.GET.get('keyword', None)
        if cat_id:
            gallery_obj = Gallery.objects.get(id = cat_id)
            gallery_specifications = Specification.objects.filter(gallery = gallery_obj)
            print(gallery_specifications)
            list_spec = []
            for spec in gallery_specifications:
                list_spec.append({'id': spec.id, 'title': spec.title})
            serialized_gallery = serializers.serialize("json", gallery_specifications)
            return JsonResponse({
                'message': 'success', 
                'cat_id': cat_id, 
                'gallery_obj': serialized_gallery,
                'list_spec': list_spec
                })
        else:
            return JsonResponse({"error": "No search keyword"})