
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')) ## If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root
]
