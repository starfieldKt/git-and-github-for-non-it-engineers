# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "非ITエンジニアに向けたGit,GitHubのすすめ"
copyright = "2024, Keita Hoshino"
author = "Keita Hoshino"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # ... other extensions
    "sphinx_search.extension",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = ["build"]

numfig = False

# numfig_format = {
#     "figure": "Figure %s",
#     "table": "Table %s",
#     "code-block": "List %s",
# }

language = "ja"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "navigation_depth": 5,
}

html_scaled_image_link = True
