from django.db import models
from recipes.models import Recipe

class Review(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    cook = models.ForeignKey(
        "cooks.Cook",
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("recipe", "cook")

    def __str__(self):
        return f"{self.recipe.title}"