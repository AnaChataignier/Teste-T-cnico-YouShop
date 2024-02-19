from django.urls import path
from . import views

urlpatterns = [
    path('planted_tree_list', views.PlantedTreeListAPIView.as_view(), name='planted_tree_list'),
    # Outras URLs da API podem ser adicionadas aqui conforme necessário
]