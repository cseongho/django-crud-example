"""basic_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from func_crud import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="homePage"),
    path('createPage', views.createPage, name="createPage"),
    path('create', views.createFunction, name="createFunction"),
    path('detail/<int:detail_id>', views.detailPage, name="detailPage"),
    path('updatePage/<int:update_id>', views.updatePage, name="updatePage"),
    path('update/<int:update_id>', views.updateFunction, name="updateFunction"),
    path('delete/<int:delete_id>', views.deleteFunction, name="deleteFunction"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
