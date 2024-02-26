from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("urlpattern",  views.index, name="index"),
    path("login",  views.login, name="index"),
    path("",  views.home, name="home"),
    path("specification", views.specs , name = "specs"),
    path("form", views.djangoforms , name = "forms"),
    path("restaurant", views.MyRestaurant , name = "restaurant"),
    path("article", views.manytomanyview,name="article")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

