from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from recipes.models import Recipe


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 12
    ordering = ["-created_at"]

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = "recipes/recipe_form.html"
    fields = ["title", "description", "instructions", "preparation_time", "servings", "image", "category"]
    success_url = reverse_lazy("recipe-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = "recipes/recipe_form.html"
    fields = ["title", "description", "instructions", "preparation_time", "servings", "image", "category"]
    success_url = reverse_lazy("recipe-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipes/recipe_confirm_delete.html"
    success_url = "/recipes/"