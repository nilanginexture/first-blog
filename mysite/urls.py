from django.conf.urls import url,include
from django.contrib import admin 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'personal', include('personal.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^index/', include('personal.urls')),
    url(r'^holo/', include('holo.urls')),
]

