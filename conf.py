# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'polars_go_undersea'
copyright = '2026, Kristian Rother, Shreyaasri Prakash'
author = 'Kristian Rother, Shreyaasri Prakash'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    "sphinx.ext.intersphinx",
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ls'

# -- intersphinx configuration -----------------------------------------------

intersphinx_mapping = {
    "jupyter-tutorial": ("https://jupyter-tutorial.readthedocs.io/de/latest/", None),
    "python": ("https://docs.python.org/3", None),
    "ipython": ("https://ipython.readthedocs.io/en/latest/", None),
    "jupyter-notebook": ("https://jupyter-notebook.readthedocs.io/en/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "polars": ("https://docs.pola.rs/", None),
    "pyviz": ("https://pyviz-tutorial.readthedocs.io/de/latest/", None),
    "python-basics": ("https://python-basics-tutorial.readthedocs.io/de/latest/", None),
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_path = ['themes']
html_static_path = ['_static']
html_logo = "_static/banner_wide_1.svg"
html_favicon = "_static/logo.svg"


html_theme_options = {
    "sidebar_hide_name": True,
    "source_repository": "https://github.com/shreyaa98/polars_go_undersea/",
    "source_branch": "main",
    "source_directory": "/",

    "light_css_variables": {
        # see https://github.com/pradyunsg/furo/tree/main/src/furo/assets/styles/variables
        "color-card-background": "#005f99",
        "color-card-foreground": "#000000",
    },

    "dark_css_variables": {
        "color-card-background": "#003f66",
        "color-card-foreground": "#ffffff",
    },
}

todo_include_todos = True
