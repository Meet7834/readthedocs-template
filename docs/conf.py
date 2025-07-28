# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import pathlib

project = 'nirfmx-python'
copyright = '2025, National Instruments'
author = 'National Instruments'
release = '2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
              'sphinx.ext.autosectionlabel',
              'myst_parser']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = []

root_path = pathlib.Path(__file__).parent.parent


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['']

# html_theme = 'sphinx_rtd_theme'
# html_static_path = []

# -- Options for HTMLHelp output ------------------------------------------

htmlhelp_basename = 'NI-RFmxPythonAPIdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

latex_documents = [
    (master_doc, 'NI-RFmxPythonAPI.tex', 'NI-RFmx Python API Documentation',
     'National Instruments', 'manual'),
]


# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'ni-rfmxpythonapi', 'NI-RFmx Python API Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (master_doc, 'NI-RFmxPythonAPI', 'NI-RFmx Python API Documentation',
     author, 'NI-RFmxPythonAPI', 'One line description of project.',
     'Miscellaneous'),
]