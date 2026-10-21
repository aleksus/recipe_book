from django.db.models import Count, Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from cooks.models import Cook


class CookListView(ListView):
    model = Cook
    template_name = "cooks/cook_list.html"
    context_object_name = "cooks"
    paginate_by = 10
    ordering = ["display_name"]

    def get_queryset(self):
        queryset = super().get_queryset().annotate(review_count=Count("reviews"))
        query = self.request.GET.get("q", "").strip()
        if query:
            queryset = queryset.filter(
                Q(display_name__icontains=query)
                | Q(bio__icontains=query)
                | Q(specialty__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("q", "").strip()
        return context


class CookDetailView(DetailView):
    model = Cook
    template_name = "cooks/cook_detail.html"
    context_object_name = "cook"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("reviews__recipe")


class CookCreateView(CreateView):
    model = Cook
    template_name = "cooks/cook_form.html"
    fields = ["display_name", "bio", "specialty"]
    success_url = reverse_lazy("cook-list")


class CookUpdateView(UpdateView):
    model = Cook
    template_name = "cooks/cook_form.html"
    fields = ["display_name", "bio", "specialty"]
    success_url = reverse_lazy("cook-list")


class CookDeleteView(DeleteView):
    model = Cook
    template_name = "cooks/cook_confirm_delete.html"
    success_url = reverse_lazy("cook-list")
