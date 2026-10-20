from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from cooks.models import Cook


# Create your views here.
class CookListView(ListView):
    model = Cook
    template_name = "cooks/cook_list.html"
    context_object_name = "cooks"
    paginate_by = 10
    ordering = ["-created_at"]


class CookDetailView(DetailView):
    model = Cook
    template_name = "cooks/cook_detail.html"
    context_object_name = "cook"


class CookCreateView(CreateView):
    model = Cook
    template_name = "cooks/cook_form.html"
    fields = ["name", "bio", "image"]
    success_url = "/cooks/"


class CookUpdateView(UpdateView):
    model = Cook
    template_name = "cooks/cook_form.html"
    fields = ["name", "bio", "image"]
    success_url = "/cooks/"


class CookDeleteView(DeleteView):
    model = Cook
    template_name = "cooks/cook_confirm_delete.html"
    success_url = "/cooks/"
