from django.shortcuts import render

from recipes.models import Category, Recipe


def home(request):
    context = {
        "recipe_count": Recipe.objects.count(),
        "category_count": Category.objects.count(),
        "recent_recipes": Recipe.objects.order_by("-created_at")[:5],
    }
    return render(request, "common/dashboard.html", context)
