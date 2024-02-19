from django.contrib import admin
from django.urls import path, include
from .views import user_login, home, my_profile, user_logout, add_planted_tree, my_planted_trees, planted_tree_detail, my_accounts


urlpatterns = [
    path("", user_login, name="user_login"),
    path("home/", home, name="home"),
    path("my_profile/", my_profile, name="my_profile"),
    path('user_logout/', user_logout, name='user_logout'),
    path('add_planted_tree/', add_planted_tree, name='add_planted_tree'),
    path('my_planted_trees/', my_planted_trees, name='my_planted_trees'),
    path('planted_tree/<int:pk>/', planted_tree_detail, name='planted_tree_detail'),
    path('my_accounts/', my_accounts, name='my_accounts'),
    path('planted_tree_list/', include('api.urls')),
]
