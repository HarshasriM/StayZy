
from django.urls import path
from accounts import views
urlpatterns = [
    path("login/",views.login_user,name="login_user"),
    path("register/",views.register_user,name="register_user"),
    path("verify-account/<token>/", views.verify_email_token, name="verify_email_token"),
    path("send_otp/<email>/", views.send_otp, name="send_otp"),
    path("verify-otp/<email>/", views.verify_otp, name="verify_otp"),
    path('login-vendor/' , views.login_vendor, name='login_vendor'),
    path('register-vendor/' , views.register_vendor, name='register_vendor'),
    path('dashboard/' , views.dashboard, name='dashboard'),
    path('add-hotel/' , views.add_hotel, name='add_hotel'),
    path('<slug>/upload-images/',views.upload_images,name="upload_images"),
    path('<slug>/edit-hotel/',views.edit_hotel,name='edit_hotel'),
    path('delete-image/<id>/',views.delete_image,name="delete_image"),
    path("logout/",views.logout_user, name="logout_user")
]