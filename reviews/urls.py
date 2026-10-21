from django.urls import path

from reviews import views

urlpatterns = [
    path(
        "recipes/<int:recipe_pk>/create/",
        views.ReviewCreateView.as_view(),
        name="review-create",
    ),
    path(
        "recipes/<int:recipe_pk>/<int:pk>/update/",
        views.ReviewUpdateView.as_view(),
        name="review-update",
    ),
    path(
        "recipes/<int:recipe_pk>/<int:pk>/delete/",
        views.ReviewDeleteView.as_view(),
        name="review-delete",
    ),
]