# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'scientific-programming-for-acoustics'
copyright = '2023, João Vítor Carli Pereira'
author = 'João Vítor Carli Pereira'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# Localization options

# NOTE: language = 'en' is the default for sphinx, but
#       since we are working with multiple languages is
#       better to explicit about it.
language = 'en'
locale_dirs = ['_locales/']
gettext_compact = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Scientific Programming for Acoustics"
html_theme = 'piccolo_theme'
html_static_path = ['_static']

# piccolo_theme options
html_theme_options = {
    "banner_text": '⚠️ This guide is incomplete and in its early stages!',
    "banner_hiding": "temporary",
    "source_url": 'https://github.com/jvcarli/scientific-programming-for-acoustics/'
}
