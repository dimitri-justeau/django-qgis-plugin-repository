# coding: utf-8

import zipfile
import re
import configparser

from django.db.models.fields import NOT_PROVIDED

from qgis_plugin_repository.models import QgisPlugin
from qgis_plugin_repository.exceptions import InvalidQgisPluginArchiveError


def update_qgis_plugin_instance(object, metadata_dict):
    """
    Update a QgisPlugin instance
    :param metadata_dict: Metadata of the plugin in a dict
    """
    # 2nd boolean member indicated wether the parameter is required or not
    params = (
        ('name', True),
        ('qgisMinimumVersion', True),
        ('qgisMaximumVersion', False),
        ('description', True),
        ('about', True),
        ('version', True),
        ('author', True),
        ('email', True),
        ('changelog', False),
        ('experimental', False),
        ('deprecated', False),
        ('tags', False),
        ('homepage', False),
        ('repository', True),
        ('tracker', False),
        ('icon', False),
        ('category', False),
    )
    metadata = metadata_dict['general']
    for var_name, required in params:
        var = metadata.get(var_name.lower(), None)
        if required and var is None:
            raise InvalidQgisPluginArchiveError(
                """
                Metadata describing the plugin is invalid. '{}' is not set
                while required.
                """.format(var_name)
            )
        if var is not None:
            setattr(object, var_name, var)
        else:
            default_value = QgisPlugin._meta.get_field(var_name).default
            if default_value != NOT_PROVIDED:
                setattr(object, var_name, default_value)


def read_plugin_zipfile_metadata(plugin_zipfile):
    """
    Extract metadata about a plugin from a zip archive and return it as
    a dict object.
    :param plugin_zipfile: The archive file handler.
    :return: The plugin metadata as a dict object.
    """
    with zipfile.ZipFile(plugin_zipfile, 'r') as plugin_zip:
        metadata_file = _find_metadata_file(plugin_zip.namelist())
        with plugin_zip.open(metadata_file, 'r') as metadata:
            return _convert_ini_config_to_dict(metadata)


def _find_metadata_file(filename_list):
    """
    Give a filename list, finds the metadata.txt file which describe a QGIS
    plugin. If more than one metadata.txt file are found, raise an error.
    :param filename_list: The filename list to inspect.
    :return: The filename of the found metadata.txt, None if none is found.
    """
    regex = re.compile(r'^.*/metadata.txt$')
    metadata_file = None
    for filename in filename_list:
        if regex.match(filename):
            if metadata_file is not None:
                raise InvalidQgisPluginArchiveError(
                    """
                    More than one 'metadata.txt' files had been found in the
                    qgis plugin archive. Please ensure that your archive
                    only contains a single plugin.
                    """
                )
            metadata_file = filename
    return metadata_file


def _convert_ini_config_to_dict(ini_config_file):
    """
    Convert an ini configuration file to a dict object.
    :param ini_config_file: The ini config file handler.
    :return: A dict object corresponding to the ini configuration file.
    """
    config_str = str(ini_config_file.read(), 'utf-8')
    config = configparser.ConfigParser()
    config.read_string(config_str)
    conf_dict = {}
    for section in config.sections():
        sect = section.lower()
        conf_dict[sect] = {}
        for option in config.options(sect):
            opt = option.lower()
            conf_dict[sect][opt] = config.get(sect, opt)
    return conf_dict
