from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^item/$',views.get_html),
    url(r'^add_item$',views.create_item),
    url(r'^items/$',views.selete_data),
    # url(r'^items/(\d+)/$',views.selete_data),
    url(r'^cates/$',views.get_category),
    url(r'^my_cate_item/$',views.get_item_by_c_id),
    url(r'^students/$',views.students),
    url(r'^add_student/$',views.add_student),
    url(r'^select_student/$',views.select_student),

]