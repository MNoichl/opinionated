"""opinionated - A new Python package"""

import matplotlib as mpl
from matplotlib import font_manager as fm
import pkg_resources

from .core import download_font   

# __version__ = pkg_resources.require("opinionated")[0].version
__author__ = 'Maximilian Noichl <noichlmax@hotmail.co.uk>'
__all__ = []

# register the included stylesheet in the mpl style library
data_path = pkg_resources.resource_filename('opinionated', 'data/')
opinionated_stylesheets = mpl.style.core.read_style_directory(data_path)
mpl.style.core.update_nested_dict(mpl.style.library, opinionated_stylesheets)