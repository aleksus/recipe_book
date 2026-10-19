from django.db import models

class Cook(models.Model):
    display_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    specialty = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.display_name