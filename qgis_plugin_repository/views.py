# coding: utf-8

from django.shortcuts import render

from qgis_plugin_repository.models import QgisPlugin


def repository_index(request):
    qgis_plugins = QgisPlugin.objects.all()
    return render(request, "plugins.xml", {'qgis_plugins': qgis_plugins})
