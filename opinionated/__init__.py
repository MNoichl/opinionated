"""opinionated - A new Python package"""

import matplotlib as mpl
from matplotlib import font_manager as fm
import pkg_resources

from .core import download_googlefont, show_installed_fonts, update_matplotlib_fonts

# __version__ = pkg_resources.require("opinionated")[0].version
__author__ = 'Maximilian Noichl <noichlmax@hotmail.co.uk>'
__all__ = []

# register the included stylesheet in the mpl style library
data_path = pkg_resources.resource_filename('opinionated', 'data/')
opinionated_stylesheets = mpl.style.core.read_style_directory(data_path)
mpl.style.core.update_nested_dict(mpl.style.library, opinionated_stylesheets)

# check if the font is already installed WE SHOULD DO THIS....
# font_path = pkg_resources.resource_filename('opinionated', 'fonts/RobotoCondensed-Regular.ttf')

download_googlefont(font='Roboto Condensed')
download_googlefont(font='Montserrat')
download_googlefont(font='Source Code Pro')
download_googlefont(font='Source Sans Pro')
download_googlefont(font='Fira Sans')



update_matplotlib_fonts()