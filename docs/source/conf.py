# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
current_file_dir = os.path.dirname(os.path.abspath(__file__))  # source folder
docs_dir = os.path.dirname(current_file_dir)                   # docs folder
project_dir = os.path.dirname(docs_dir)                        # project folder

sys.path.insert(0, project_dir)

project = 'Менеджер Заметок'
copyright = '2025, Дмитрий Лютиков ВКБ-33'
author = 'Дмитрий Лютиков ВКБ-33'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
