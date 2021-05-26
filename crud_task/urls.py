from django.urls import path
from .views import CrudListView, CrudDetailView, CrudCreateView, CrudUpdatedView, CrudDeleteView


urlpatterns =[
    path('post/<int:pk>/delete/', CrudDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', CrudUpdatedView.as_view(), name='post_edit'),
    path('post/new/', CrudCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', CrudDetailView.as_view(), name='post_detail'),
    path('', CrudListView.as_view(), name='home'),

]