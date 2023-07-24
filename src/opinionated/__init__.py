import sys

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError


####################### IMPORTS  ##############################

import matplotlib as mpl

from matplotlib import font_manager as fm
import pkg_resources
from typing import Optional, Union, List, Tuple
import os
import time 
import shutil
import glob
import colormaps as cmaps



from .core import (
    download_googlefont,
    show_installed_fonts,
    update_matplotlib_fonts,
    add_attribution,
    set_title_and_suptitle,
    add_legend
)


# register the included stylesheet in the mpl style library
data_path = pkg_resources.resource_filename("opinionated", "data/")
# print(data_path)
opinionated_stylesheets = mpl.style.core.read_style_directory(data_path)
mpl.style.core.update_nested_dict(mpl.style.library, opinionated_stylesheets)
mpl.style.reload_library()
 

# 
stylefiles = glob.glob(pkg_resources.resource_filename("opinionated", "data/") + '/*.mplstyle', recursive=True)
mpl_stylelib_dir = os.path.join(mpl.get_configdir() ,"stylelib")
if not os.path.exists(mpl_stylelib_dir):
    os.makedirs(mpl_stylelib_dir)
for stylefile in stylefiles:
    shutil.copy(
        stylefile, 
        os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))
    
# # Update the list of available styles  
mpl.pyplot.style.core.available[:] = sorted(mpl.pyplot.style.library.keys())
mpl.style.reload_library()




# check if the font is already installed (WE SHOULD DO THIS)....

fonts = [
    "Roboto Condensed",
    "Montserrat",
    "Source Code Pro",
    "Source Sans Pro",
    "Fira Sans",
    "Fira Sans Condensed",
    "IBM Plex Sans",
    "Space Grotesk",
    "Space Mono",
    "Roboto",
    "Jost",
    "Titillium Web"
]



import os
import time

fonts = [
    "Roboto Condensed",
    "Montserrat",
    "Source Code Pro",
    # "Source Sans Pro",
    "Fira Sans",
    "Fira Sans Condensed",
    "IBM Plex Sans",
    "Space Grotesk",
    "Space Mono",
    "Roboto",
    "Jost",
    "Titillium Web"
]

def check_if_font_already_present(font):
    # check if a file that contains the font name is already in the fonts folder:
    try:
        for file in [x.lower() for x in os.listdir("fonts")]:
            if font.replace(" ", "").lower() in file:
                return True
        return False
    except:
        return False

def download_font_with_retry(font, retries=3, delay=3):
    for i in range(retries):
        try:
            print(f"Now downloading: {font}")
            download_googlefont(font=font)
            return  # return if the download was successful
        except Exception as e:
            if i < retries - 1:  # i is zero indexed
                print(f"Attempt {i+1} to download {font} failed with error: {str(e)}. Retrying in {delay} seconds.")
                time.sleep(delay)
            else:
                print(f"All attempts to download {font} failed. Please check your connection and the font name.")
                raise

for font in fonts:
    if not check_if_font_already_present(font):
        download_font_with_retry(font)

update_matplotlib_fonts()