from django import forms
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView

from recipes.models import Recipe
from reviews.forms import ReviewForm
from reviews.models import Review


class RecipeReviewMixin:
    form_class = ReviewForm
    template_name = "reviews/review_form.html"

    def get_recipe(self):
        return get_object_or_404(Recipe, pk=self.kwargs["recipe_pk"])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["recipe"] = self.get_recipe()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = self.get_recipe()
        return context

    def get_success_url(self):
        return reverse("recipe-detail", kwargs={"pk": self.kwargs["recipe_pk"]})


class ReviewCreateView(RecipeReviewMixin, CreateView):
    model = Review


class ReviewUpdateView(RecipeReviewMixin, UpdateView):
    model = Review

    def get_queryset(self):
        return super().get_queryset().filter(recipe_id=self.kwargs["recipe_pk"])


class ReviewDeleteView(RecipeReviewMixin, DeleteView):
    model = Review
    template_name = "reviews/review_confirm_delete.html"
    form_class = forms.Form

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop("recipe")
        return kwargs

    def get_queryset(self):
        return super().get_queryset().filter(recipe_id=self.kwargs["recipe_pk"])
