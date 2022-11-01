from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='posts'),
    path('group/<slug>/', views.group_posts, name='group_posts'),
    # path('group_list/', views.groups_list, name='group_list')
]