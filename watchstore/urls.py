from django.contrib import admin
from django.urls import path
from blog.views import home, watch_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home Page URL
    path('blog/', watch_list, name='watch_list'),  # Blog Page URL
]
