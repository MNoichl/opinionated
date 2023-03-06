"""opinionated - A new Python package"""

import matplotlib as mpl
from matplotlib import font_manager as fm
import pkg_resources
from typing import Optional, Union, List, Tuple
import os

from .core import download_googlefont, show_installed_fonts, update_matplotlib_fonts, add_attribution, add_legend


# __version__ = pkg_resources.require("opinionated")[0].version
__author__ = 'Maximilian Noichl <noichlmax@hotmail.co.uk>'
__all__ = []

# register the included stylesheet in the mpl style library
data_path = pkg_resources.resource_filename('opinionated', 'data/')
opinionated_stylesheets = mpl.style.core.read_style_directory(data_path)
mpl.style.core.update_nested_dict(mpl.style.library, opinionated_stylesheets)

# check if the font is already installed WE SHOULD DO THIS....

fonts = ['Roboto Condensed', 'Montserrat', 
         'Source Code Pro', 'Source Sans Pro',
         'Fira Sans','Fira Sans Condensed', 'IBM Plex Sans',
         'Space Grotesk', 'Space Mono',
         'Roboto','Roboto Condensed', 'Jost']


def check_if_font_already_present(font):
  # check if a file that contains thefont name is already in the fonts folder:
  try: 
    for file in [x.lower() for x in os.listdir('fonts')]:
      if font.replace(' ','').lower() in file:
        return True
    return False
  except:
    return False
  

for font in fonts:
  if not check_if_font_already_present(font):
    print('Now downloading: ' + font)
    download_googlefont(font=font)

update_matplotlib_fonts()