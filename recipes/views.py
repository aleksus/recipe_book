from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.core.paginator import Paginator
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from recipes.models import Category, Ingredient, Recipe, RecipeIngredient


RecipeIngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    fields=("ingredient", "quantity", "unit"),
    extra=1,
    can_delete=True,
)


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

    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            "ingredients__ingredient",
        )


class RecipeIngredientsMixin:
    def get_ingredient_formset(self):
        return RecipeIngredientFormSet(
            self.request.POST or None,
            instance=getattr(self, "object", None),
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredient_formset"] = kwargs.get(
            "ingredient_formset",
            self.get_ingredient_formset(),
        )
        return context

    def form_valid(self, form):
        ingredient_formset = self.get_ingredient_formset()
        if not ingredient_formset.is_valid():
            return self.render_to_response(
                self.get_context_data(
                    form=form,
                    ingredient_formset=ingredient_formset,
                )
            )

        with transaction.atomic():
            response = super().form_valid(form)
            ingredient_formset.instance = self.object
            ingredient_formset.save()
        return response


class RecipeCreateView(RecipeIngredientsMixin, CreateView):
    model = Recipe
    template_name = "recipes/recipe_form.html"
    fields = ["title", "description", "instructions", "preparation_time", "servings", "image", "category"]
    success_url = reverse_lazy("recipe-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(RecipeIngredientsMixin, UpdateView):
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


class IngredientListView(ListView):
    model = Ingredient
    template_name = "recipes/ingredient_list.html"
    context_object_name = "ingredients"
    paginate_by = 20
    ordering = ["name"]


class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = "recipes/ingredient_detail.html"
    context_object_name = "ingredient"


class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = "recipes/ingredient_form.html"
    fields = ["name", "unit"]
    success_url = reverse_lazy("ingredient-list")


class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "recipes/ingredient_form.html"
    fields = ["name", "unit"]
    success_url = reverse_lazy("ingredient-list")


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "recipes/ingredient_confirm_delete.html"
    context_object_name = "ingredient"
    success_url = reverse_lazy("ingredient-list")


class CategoryListView(ListView):
    model = Category
    template_name = "recipes/category_list.html"
    context_object_name = "categories"
    paginate_by = 20
    ordering = ["name"]


class CategoryDetailView(DetailView):
    model = Category
    template_name = "recipes/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipes = self.object.recipes.order_by("-created_at")
        paginator = Paginator(recipes, 12)
        context["page_obj"] = paginator.get_page(self.request.GET.get("page"))
        return context


class CategoryCreateView(CreateView):
    model = Category
    template_name = "recipes/category_form.html"
    fields = ["name"]
    success_url = reverse_lazy("category-list")


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "recipes/category_form.html"
    fields = ["name"]
    success_url = reverse_lazy("category-list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "recipes/category_confirm_delete.html"
    context_object_name = "category"
    success_url = reverse_lazy("category-list")