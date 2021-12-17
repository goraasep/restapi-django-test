
from django.conf.urls import url
from myapp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^posts$',views.contentApi),
    url(r'^posts/([0-9]+)$',views.contentApi),
    ]