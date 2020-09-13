from django.urls import path
from . import views
from training.views import CourseHome

app_name = 'pekuric_mgt'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    # path('bot/', views.ChatterBotApiView.as_view(), name='bot'),
    # path('bot-main/', views.BotApi.as_view(), name='main'),
    path('it-courses/', CourseHome.as_view(), name="course-home"),
    path('admin/', views.UserSignin.as_view(), name='user-signin'),
    path('make-payment/', views.PaymentForm.as_view(), name='payment-info'),
    path('admin/portfolio/', views.Portfolio.as_view(), name='portfolio'),
    path('admin/portfolio-slides/', views.PortfolioView.as_view(), name='portfolio-slides'),
    path('<int:pk>/admin/portfolio-delete/', views.PortfolioDeleteView.as_view(), name='portfolio-delete'),
    path('services/', views.ServiceView.as_view(), name='services'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('<int:pk>/product-detail/', views.ProductDetailView.as_view(), name='detail-product'),
    path('<int:pk>/service-detail/', views.ServiceDetails.as_view(), name='detail-service'),
    path('admin/service-create/', views.CreateService.as_view(), name='create-services'),
    path('<int:pk>/service-edit/', views.UpdateService.as_view(), name='update-service'),
    path('admin/logout/', views.UserLogout.as_view(), name='user-signout'),
    path('admin/daily-task/', views.TaskManagement.as_view(), name='daily-task'),
    path('admin/add-task/', views.TaskCreate.as_view(), name='add-task'),
    path('<int:pk>/admin/update-task/', views.TaskUpdate.as_view(), name='update-task'),
    path('<int:pk>/admin/task-delete/', views.TaskDelete.as_view(), name='delete-task'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('admin/sign-up/', views.UserRegistration.as_view(), name="user-signup"),
    path('<int:pk>/admin/update/', views.unicornUpdate.as_view(), name='edit'),
    path('<int:pk>/admin/del/', views.unicornDelete.as_view(), name='delete'),
    path('admin/index/', views.Dashboard.as_view(), name='panel'),
    path('admin/add/', views.UnicornInsert.as_view(), name='add'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('preview/', views.Preview.as_view(), name='preview'),
    path('admin/users-request/', views.MakeRequestView.as_view(), name='make-request'),
    path('admin/create-about/', views.Menu.as_view(), name='create-about'),
    path('<int:pk>/admin/update-about/', views.UpdateAbout.as_view(), name='update-about'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('admin/product-rating/', views.ProductRatings.as_view(), name='ratings'),
    path('admin/search-product/', views.product_search, name='search')
]
