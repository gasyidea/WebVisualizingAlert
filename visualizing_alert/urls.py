from django.conf.urls import url
from django.contrib import admin
from chart import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^check$', views.get_url),
    url(r'^checkValidation', views.checkVulnerability)
]
