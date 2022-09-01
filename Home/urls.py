from django.urls import path

from Home.views import Publications_list, Detail_Publication, Create_Publication, Delete_Publication, Update_Publication, about_us

urlpatterns =[
    path('', Publications_list.as_view(), name = 'Home'),
    path('home/about-us/', about_us, name = 'about-us'),
    path('home/detail-publication/<int:pk>/', Detail_Publication.as_view(), name = 'detail-publication'),
    path('home/delete-publication/<int:pk>/', Delete_Publication.as_view(), name = 'delete-publication'),
    path('home/update-publication/<int:pk>/', Update_Publication.as_view(), name = 'update-publication'),
    path('home/create-publication/', Create_Publication.as_view(), name = 'create-publication'),
]