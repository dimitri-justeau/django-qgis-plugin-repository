# coding: utf-8

from django.contrib import admin

from qgis_plugin_repository import models
from qgis_plugin_repository.plugin_metadata import *


class QgisPluginAdmin(admin.ModelAdmin):
    """
    Admin class for QgisPlugin model.
    """

    # fields = ('file', )
    readonly_fields = (
        'name',
        'qgisMinimumVersion',
        'qgisMaximumVersion',
        'description',
        'about',
        'version',
        'author',
        'email',
        'changelog',
        'experimental',
        'deprecated',
        'tags',
        'homepage',
        'repository',
        'tracker',
        'icon',
        'category',
        'create_date',
        'update_date',
        'file_name',
        'download_url'
    )
    list_display = ('name', 'version')

    def save_model(self, request, obj, form, change):
        # Extract metadata
        files = request.FILES
        if len(files) > 0:
            plugin_zipfile = files['file']
            metadata = read_plugin_zipfile_metadata(plugin_zipfile)
        # Construct QgisPlugin object from the metadata
        update_qgis_plugin_instance(obj, metadata)
        # Save the object
        super(QgisPluginAdmin, self).save_model(request, obj, form, change)


admin.site.register(models.QgisPlugin, QgisPluginAdmin)
