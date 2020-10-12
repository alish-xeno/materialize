from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', include('profileapp.urls')),
    # path('summernote/', include('django_summernote.urls')),
    # path('api/', include('rest_framework.urls'))

]


# handler404 = 'reesapp.views.handle404'
# handler500 = 'reesapp.views.handle500'


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
