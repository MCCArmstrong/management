from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import serve
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # path('admin/', admin.site.urls),
    path('', include('pekuric_mgt.urls')),
    path('it-courses/', include('pekuric_mgt.urls')),
    path('make-payment/', include('pekuric_mgt.urls')),
    # path('bot/', include('peckuric_mgt.urls')),
    # path('bot-main/', include('pekuric_mgt.urls')),
    path('admin/', include('pekuric_mgt.urls')),
    path('product/', include('pekuric_mgt.urls')),
    path('<int:pk>/product-detail/', include('pekuric_mgt.urls')),
    path('<int:pk>/admin/portfolio/delete/', include('pekuric_mgt.urls')),
    path('admin/service-create/', include('pekuric_mgt.urls')),
    path('services/', include('pekuric_mgt.urls')),
    path('<int:pk>/service-edit/', include('pekuric_mgt.urls')),
    path('<int:pk>/service-detail/', include('pekuric_mgt.urls')),
    path('admin/portfolio/', include('pekuric_mgt.urls')),
    path('admin/portfolio-slides/', include('pekuric_mgt.urls')),
    path('admin/logout/', include('pekuric_mgt.urls')),
    path('<int:pk>/admin/update/', include('pekuric_mgt.urls')),
    path('<int:pk>/admin/delete/', include('pekuric_mgt.urls')),
    path('admin/daily-task/', include('pekuric_mgt.urls')),
    path('admin/add-task/', include('pekuric_mgt.urls')),
    path('<int:pk>/admin/update-task/', include('pekuric_mgt.urls')),
    path('<int:pk>/admin/task-delete/', include('pekuric_mgt.urls')),
    path('admin/add/', include('pekuric_mgt.urls')),
    path('admin/sign-up/', include('pekuric_mgt.urls')),
    path('about/', include('pekuric_mgt.urls')),
    path('admin/index/', include('pekuric_mgt.urls')),
    path('product-detail/<int:pk>', include('pekuric_mgt.urls')),
    path('gallery/', include('pekuric_mgt.urls')),
    path('admin/create-about/', include('pekuric_mgt.urls')),
    path('preview/', include('pekuric_mgt.urls')),
    path('admin/users-request/', include('pekuric_mgt.urls')),
    path('<int:pk>/admin/update-about/', include('pekuric_mgt.urls')),
    path('admin/product-rating/', include('pekuric_mgt.urls')),
    path('admin/search-product/', include('pekuric_mgt.urls'))

]
