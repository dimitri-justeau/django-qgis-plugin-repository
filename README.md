django-qgis-plugin-repository
=============================

Django reusable application providing a simple way to self-host a QGIS
plugin repository within a django project.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "qgis_plugin_repository" to your INSTALLED_APPS setting like this::
    ```
    INSTALLED_APPS = [
        ...
        'qgis_plugin_repository',
    ]
    ```

2. Run `python manage.py migrate` to create the qgis_plugin_repository models.

3. Add `url(r'^qgis_plugin_repository/', include('qgis_plugin_repository.urls')),` to your project's urls.
