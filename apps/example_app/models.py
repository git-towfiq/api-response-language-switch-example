# from django.db import models


# class Translation(models.Model):
#     key = models.CharField(max_length=255, unique=True)
#     language = models.CharField(max_length=10)
#     message = models.TextField()

#     class Meta:
#         unique_together = ('key', 'language')

#     def __str__(self):
#         return f"{self.key} ({self.language})"
