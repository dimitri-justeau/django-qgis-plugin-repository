# coding: utf-8

"""
django-qgis-plugin-repository URL Configuration
"""

from django.conf.urls import url

from qgis_plugin_repository.views import repository_index


urlpatterns = [
    url(r'^', repository_index, name="django-qgis-plugin-repository_index"),
]
