from django.conf.urls import url
from .views import  *

urlpatterns = [
    url(r'^home$',home,name='home'),
    url(r'^market$',market,name='market'),
    url(r'^cart$',cart,name='cart'),
    url(r'^mine$',mine,name='mine'),
    url(r'^market_with_params/(\d+)/(\d+)/(\d+)',
        market_with_params,
        name='market_params'),
    url(r'^register$',Register_API.as_view(),name='register'),
    url(r'^login$',Login_API.as_view(),name='login'),
    url(r'^confirm/(.*)',verify_email,name='verify'),
    url(r'^logout$',Logout_API.as_view(),name='logout'),
    url(r'^check_uname$',check_uname),
    url(r'^cart_api$',Cart_API.as_view()),
    url(r'^cart_status$',Cart_Status_API.as_view()),
    url(r'^cart_all_status$',Cart_All_Status_API.as_view()),
    url(r'^change_user$',Change_User_API.as_view(),name='change_user'),
    url(r'^cart_item$',Cart_Item_API.as_view()),
    url(r'^order$',Order_API.as_view(),name='order')
]
