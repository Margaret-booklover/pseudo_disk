import os

from django.core.validators import MinValueValidator
from django.db import models


class Folder(models.Model):
    folder_name = models.CharField(max_length=20)
    owner = models.ForeignKey('auth.User', related_name='folders', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='parents')


class File(models.Model):
    filename = models.CharField(max_length=20)
    mime_type = models.CharField(max_length=40)
    size = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(max_length=20, auto_now_add=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=True, null=True, related_name='file_parent')
    upload = models.FileField(upload_to='uploads/')
    owner = models.ForeignKey('auth.User', related_name='files', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.filename = os.path.basename(self.upload.name)
        self.mime_type = self.upload.file.content_type
        self.size = self.upload.file.size
        super().save(*args, **kwargs)
