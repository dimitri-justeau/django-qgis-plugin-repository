django-qgis-plugin-repository
=============================

*Tested with django 1.9*

Django reusable application providing a simple way to self-host a QGIS
plugin repository within a django project.

I decided to start this app to have a simple and minimalist way to host and distribute QGIS plugins for a private usage in my company. Plugins are published using the django admin interface. Right now the features are very basic, but enough for self-hosting and distributing QGIS plugins out of the box.

The official QGIS plugin repository is also managed by a django app, that can be seen in the offical QGIS github repository: https://github.com/qgis/QGIS-Django/tree/master/qgis-app/plugins. It provides much more advanced features. However, It was too much for me, and most of all I was lazy to check the code and the compatibility with my project and my django's version.

Detailed documentation is in the "docs" directory.


Installation
------------
    
### From source:

Download the source code, and execute the following command inside the source code directory: `python setup.py develop`.


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

4. Upload your plugins using the django admin interface. Each plugin must be packed in a .zip archive, with a metadata.txt containing at least the mandatory parameters as described here: http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/plugins.html#plugin-metadata

5. Add `[your_host]/qgis_plugin_repository/` as a new plugin repository in your QGIS client(s).
