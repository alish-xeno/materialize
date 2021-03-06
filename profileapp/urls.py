# from django.conf import settings
from django.urls import path
from .views import *

app_name = "profileapp"
urlpatterns = [

    # Client Panel
    # path('', DemoHomeView.as_view(), name="demohome"),
    path('', ClientHomeView.as_view(), name="clienthome"),
    path('profile/', ClientProfileView.as_view(), name="clientprofile"),
    path('contact/', ClientContactView.as_view(), name="clientcontact"),

    # Axios requests
    path('axios/specifications/list/', AxiosSpecificationListView.as_view(), 
    	name = "axiosspecificationlist"),

]
