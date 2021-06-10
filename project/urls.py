from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
from project.api.v1_0 import router as v1_0


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1.0/', include(v1_0.urls)),
]
