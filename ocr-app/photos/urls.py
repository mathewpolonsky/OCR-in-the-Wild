from django.urls import path
from .views import GalleryView, PhotoView, delete_images, addPhoto, make_prediction


urlpatterns = [
    path('', GalleryView.as_view(), name="gallery"),
    path('photo/<str:pk>/', PhotoView.as_view(), name="photo"),
    path('add/', addPhoto, name="add_photo"),
    path('delete/', delete_images, name="delete_all_images"),
    path('make_prediction/', make_prediction, name="make_prediction"),
]