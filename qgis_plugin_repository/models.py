# coding: utf-8

import os
from datetime import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class QgisPlugin(models.Model):
    """
    Model representing a qgis plugin to be served by the plugin repository.
    """

    QGIS_PLUGIN_DEFAULT_DOWNLOAD_PATH = "qgis_plugins"
    QGIS_PLUGIN_DOWNLOAD_PATH = getattr(
        settings,
        "QGIS_PLUGIN_DOWNLOAD_PATH",
        QGIS_PLUGIN_DEFAULT_DOWNLOAD_PATH
    )

    name = models.CharField(max_length=50, unique=True)
    qgisMinimumVersion = models.CharField(max_length=20)
    qgisMaximumVersion = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    version = models.CharField(max_length=20)
    author = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    changelog = models.CharField(max_length=255, null=True, blank=True)
    experimental = models.BooleanField(default=False)
    deprecated = models.BooleanField(default=False)
    tags = models.CharField(max_length=255)
    homepage = models.CharField(max_length=100, null=True, blank=True)
    repository = models.CharField(max_length=100)
    tracker = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(
        upload_to=QGIS_PLUGIN_DOWNLOAD_PATH,
        storage=OverwriteStorage()
    )
    create_date = models.DateTimeField()
    update_date = models.DateTimeField(null=True, blank=True)

    @property
    def file_name(self):
        if len(self.file.name.split("/")) > 1:
            return self.file.name.split("/")[1]
        return self.file.name

    @property
    def download_url(self):
        return self.file.url

    def save(self, *args, **kwargs):
        """
        Overload of save method: fill the fields using metadata.txt from the
        plugin zip file.
        """
        if not self.id:
            self.create_date = datetime.now()
        self.update_date = datetime.now()
        super(QgisPlugin, self).save(*args, **kwargs)
