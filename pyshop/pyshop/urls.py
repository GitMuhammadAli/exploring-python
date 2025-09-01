from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('', lambda request: redirect('all-options')),
]
