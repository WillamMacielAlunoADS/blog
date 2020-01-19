from django.urls import path
from . import views

urlpatterns = [
	path('area/', views.area_list, name='area_list'),
	path('area/<int:pk>/', views.area_detail, name='area_detail'),
	path('area/new', views.area_new, name='area_new'),
	path('area/<int:pk>/edit/', views.area_edit, name='area_edit'),
	path('area/<pk>/remove/', views.area_remove, name='area_remove'),

	path('not/', views.not_list, name='not_list'),
	path('not/<int:pk>/', views.not_detail, name='not_detail'),
	path('not/new', views.not_new, name='not_new'),
	path('not/<int:pk>/edit/', views.not_edit, name='not_edit'),
	path('not/<pk>/remove/', views.not_remove, name='not_remove'),
	path('publicar/<int:pk>', views.publicar, name='publicar'),
	path('visita', views.not_list_visita, name='not_list_visita'),
	path('ativar/<int:pk>', views.ativar, name='ativar'),
	path('desativar/<int:pk>', views.desativar, name='desativar'),
]