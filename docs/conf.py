# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import os


#####
# This is the documentation config for {{ project_name }}.
# Commented out values are Sphinx defaults.

# Add project source path
sys.path.insert(0, os.path.abspath('../{{ project_name }}'))

# -- General configuration -----------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
]
#source_suffix = '.rst'
#source_encoding = 'utf-8-sig'
master_doc = 'index'
#exclude_patterns = []

#rst_prolog = ''
#rst_epilog = ''
#primary_domain = 'py'
#default_role = None
# Keep warnings in built files
keep_warnings = True
needs_sphinx = '1.1'
# Warn about all broken references
nitpicky = True
#nitpick_ignore = []


# -- Project information -----------------------------------------------------

project = '{{ project_name }}'
copyright = '2013, John Doe'
# The short X.Y version.
version = 'dev'
# The full version, including alpha/beta/rc tags.
release = 'dev'

#today = ''
#today_fmt = '%B %d, %Y'

#highlight_language = 'python'
pygments_style = 'default'

#add_function_parentheses = True
#add_module_names = True
#modindex_common_prefix = []

#show_authors = False

#trim_footnote_reference_space = False
#trim_doctest_flags = True


# -- Internationalization -----------------------------------------------------

# Currently no translation
#language = None
#locale_dirs = []
#gettext_compact = False


# -- HTML output -----------------------------------------------------

exclude_patterns = []
#default_role = None


# -- Extension configuration ------------------------------------------------

todo_include_todos = True
intersphinx_mapping = {
    'python': ('http://docs.python.org/2.7', None),
    'django': ('http://django.readthedocs.org/en/latest/', None),
    'venvwrapper': ('http://virtualenvwrapper.readthedocs.org/en/latest/', None),
}


# -- Options for HTML output ---------------------------------------------------

html_theme = 'nature'
html_theme_path = ['_templates']
html_static_path = ['_static']
html_theme_options = {
    'sidebarwidth': '300',
}

# Defaults to "<project> v<release> documentation".
#html_title = None
#html_short_title = '{{ project_name }}'
#html_logo = None
#html_favicon = None

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

#html_additional_pages = {}
#html_domain_indices = True
#html_use_index = True
#html_split_index = False
html_show_sourcelink = False
html_show_sphinx = False
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = '{{ project_name }}doc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

latex_documents = [
    # (source start file, target name, title, author, documentclass [howto/manual])
    ('index', '{{ project_name }}.tex', '{{ project_name }} Documentation', 'John Doe', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True
