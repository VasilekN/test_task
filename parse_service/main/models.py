from django.db import models


class ParsedPage(models.Model):
    url = models.URLField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    h1_count = models.PositiveIntegerField()
    h2_count = models.PositiveIntegerField()
    h3_count = models.PositiveIntegerField()
    links = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"ParsedPage {self.id} for '{self.url}'"