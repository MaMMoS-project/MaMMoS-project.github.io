# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MaMMoS'
copyright = '2023, MaMMos collaboration'
author = 'MaMMos collaboration'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',  # creates .nojekyll file in HTML directory
    'sphinxcontrib.email', 
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = '_static/mammos-logo.png'
html_static_path = ['_static']
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/mammos-project",
            "icon": "fab fa-github-square",
        },
    ],
    "show_prev_next": False,
    "header_links_before_dropdown": 6,
    "secondary_sidebar_items": ["page-toc"],
}
html_sidebars = {
    "**": []  # no subpages that would require the left sidebar
}
