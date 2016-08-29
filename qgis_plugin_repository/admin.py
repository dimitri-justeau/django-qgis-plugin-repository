# coding: utf-8

from django.contrib import admin

from qgis_plugin_repository.models import QgisPlugin


class QgisPluginAdmin(admin.ModelAdmin):
    list_display = ('name', 'version')


admin.site.register(QgisPlugin, QgisPluginAdmin)
