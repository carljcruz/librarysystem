from django.urls import path

from catalogs.views import create_book, view_book, update_book, delete_book, create_acquisition, update_acquisition, delete_acquisition, view_acquisition

app_name = 'catalogs'
urlpatterns = [
    path('book/create-book', create_book, name='create-book'),
    path('book/update_book/<str:title_proper>',
         update_book, name='update_book'),
    path('book/view_book/<str:title_proper>', view_book, name='view_book'),
    path('book/delete_book/<str:title_proper>', delete_book, name='delete_book'),

    # acquisition
    path('acquisition/create-acquisition', create_acquisition, name='create_acquisition'),
    path('acquisition/update-acquisition/<str:title>', update_acquisition, name='update_acquisition'),
    path('acquisition/view-acquisition/<str:title>', view_acquisition, name='view_acquisition'),
    path('acquisition/delete-acquisition/<str:title>', delete_acquisition, name='delete_acquisition'),


]
