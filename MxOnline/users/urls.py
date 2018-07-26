from django.urls import path
from .views import UserInfoView, UploadImageView, UpdatePwdView


urlpatterns = [
    path('info/', UserInfoView.as_view(), name='user_info'),
    path('image/upload', UploadImageView.as_view(), name='image_upload'),
    path('update/pwd/', UpdatePwdView.as_view(), name='update_pwd'),
]