
from django.urls import path,include
from . import views
from rest_framework import routers
#import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

# router = routers.DefaultRouter()
# router.register(r'users', views.UserView)

urlpatterns = [

    # path('', include(router.urls)),
    path('users/', views.UserView.as_view()),
    path('users/<int:pk>', views.UserView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('api-token-auth/', obtain_auth_token)

    # path('booking/', views.BookingViewSet.as_view()),
    # path('booking/<int:pk>', views.BookingViewSet.as_view()),
    # path('restaurantapp/menu/',include('restaurantapp.urls')),
]

