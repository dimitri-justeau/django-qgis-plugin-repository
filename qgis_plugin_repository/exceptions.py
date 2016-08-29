# coding: utf-8

"""
django-qgis-plugin-repository specific exception classes.
"""


class InvalidQgisPluginArchiveError(Exception):
    """
    Error that must be raised when a plugin archive is found to be invalid
    during the upload/publishing process.
    """
    pass
