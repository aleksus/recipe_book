from django import forms

from cooks.models import Cook
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, recipe, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.recipe = recipe
        self.fields["cook"].queryset = Cook.objects.order_by("display_name")

    def clean(self):
        cleaned_data = super().clean()
        cook = cleaned_data.get("cook")
        if cook and Review.objects.filter(
            recipe=self.instance.recipe, cook=cook
        ).exclude(pk=self.instance.pk).exists():
            self.add_error("cook", "This cook has already reviewed this recipe.")
        return cleaned_data

    class Meta:
        model = Review
        fields = ("cook", "rating", "comment")
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
            "comment": forms.Textarea(attrs={"rows": 4}),
        }
