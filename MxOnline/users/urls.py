from django.urls import path
from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MyCourseView, MyFavOrgView, MyFavTeacherView, MyMessageView, LogoutView


urlpatterns = [
    path('info/', UserInfoView.as_view(), name='user_info'),
    path('image/upload', UploadImageView.as_view(), name='image_upload'),
    path('update/pwd/', UpdatePwdView.as_view(), name='update_pwd'),
    path('sendmail_code/', SendEmailCodeView.as_view(), name='sendmail_code'),
    path('update_email/', UpdateEmailView.as_view(), name='update_email'),
    path('mycourse/', MyCourseView.as_view(), name='mycourse'),
    path('myfav/org/', MyFavOrgView.as_view(), name='myfav_org'),
    path('myfav/teacher/', MyFavTeacherView.as_view(), name='myfav_teacher'),
    path('my_message/', MyMessageView.as_view(), name='my_message'),
    path('logout/', LogoutView.as_view(), name="logout"),
]