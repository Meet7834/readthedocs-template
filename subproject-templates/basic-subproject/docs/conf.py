# Configuration file for the Sphinx documentation builder.
# This is a template for a Read the Docs subproject

# -- Project information -----------------------------------------------------

project = 'Your Subproject Name'
copyright = '2025, Your Organization'
author = 'Your Name'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosectionlabel',
    'myst_parser',
    'sphinx.ext.intersphinx',  # For linking to other documentation
]

# Source file parsers
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# -- Options for intersphinx extension ---------------------------------------

# Links to other documentation projects
intersphinx_mapping = {
    'main-docs': ('https://your-main-project.readthedocs.io/', None),
    'python': ('https://docs.python.org/3/', None),
}

# -- Options for autodoc extension -------------------------------------------

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# -- Custom configuration for subproject ------------------------------------

# Add any custom configuration specific to your subproject here

# Add the main project's context
html_context = {
    'display_github': True,
    'github_user': 'your-username',
    'github_repo': 'your-subproject-repo',
    'github_version': 'main',
    'conf_py_path': '/docs/',
}

# Custom CSS or JS files
html_css_files = [
    # 'custom.css',
]

html_js_files = [
    # 'custom.js',
]
