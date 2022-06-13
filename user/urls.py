from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user import views


urlpatterns = [
    path('login', views.CustomTokenView.as_view()),
    # path('branch/login', views.CustomTokenViewBranch.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ################### urls for users ##############
    path('user',views.users, name='users'),
    # path('user/<int:id>', views.getUser, name='get-User'),
    path('user/create', views.createUser, name='create-User'),
    # path('user/update/<int:id>/', views.updateUser, name='update-User'),
    # path('soft-delete/<int:id>/', views.softDeleteUser, name='soft-delete-User'),

    ########################## resetPassword #########################
    # path('user/changePassword/<int:id>',views.resetPassword, name='resetPassword'),

]
