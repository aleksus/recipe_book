from django.urls import path

from cooks import views

urlpatterns = [
    path("", views.CookListView.as_view(), name="cook-list"),
    path("create/", views.CookCreateView.as_view(), name="cook-create"),
    path("<int:pk>/", views.CookDetailView.as_view(), name="cook-detail"),
    path("<int:pk>/update/", views.CookUpdateView.as_view(), name="cook-update"),
    path("<int:pk>/delete/", views.CookDeleteView.as_view(), name="cook-delete"),
]