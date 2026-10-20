from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/create/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredient-list'),
    path('ingredients/create/', views.IngredientCreateView.as_view(), name='ingredient-create'),
    path('ingredients/<int:pk>/', views.IngredientDetailView.as_view(), name='ingredient-detail'),
    path('ingredients/<int:pk>/update/', views.IngredientUpdateView.as_view(), name='ingredient-update'),
    path('ingredients/<int:pk>/delete/', views.IngredientDeleteView.as_view(), name='ingredient-delete'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]
