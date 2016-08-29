# coding: utf-8

import os

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name):
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
    version = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    about = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(
        upload_to=QGIS_PLUGIN_DOWNLOAD_PATH,
        storage=OverwriteStorage()
    )
    is_trusted = models.BooleanField(default=False)
    qgis_minimum_version = models.CharField(max_length=20)
    qgis_maximum_version = models.CharField(max_length=20)
    homepage = models.CharField(max_length=50, null=True, blank=True)
    uploaded_by = models.CharField(max_length=100)
    create_date = models.DateField()
    update_date = models.DateField(null=True, blank=True)
    is_experimental = models.BooleanField(default=False)
    is_deprecated = models.BooleanField(default=False)

    @property
    def filename(self):
        return self.file.name.split('/')[1]

    @property
    def download_url(self):
        return self.file.url
