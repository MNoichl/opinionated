"""opinionated - A new Python package"""

import matplotlib as mpl
from matplotlib import font_manager as fm
import pkg_resources
from typing import Optional, Union, List, Tuple
import os
import shutil
import glob


from .core import (
    download_googlefont,
    show_installed_fonts,
    update_matplotlib_fonts,
    add_attribution,
    set_title_and_suptitle,
    add_legend
)


# __version__ = pkg_resources.require("opinionated")[0].version
__author__ = "Maximilian Noichl <noichlmax@hotmail.co.uk>"
__all__ = []

# register the included stylesheet in the mpl style library
# data_path = pkg_resources.resource_filename("opinionated", "data/")
# print(data_path)
# opinionated_stylesheets = mpl.style.core.read_style_directory(data_path)
# mpl.style.core.update_nested_dict(mpl.style.library, opinionated_stylesheets)
stylefiles = glob.glob(pkg_resources.resource_filename("opinionated", "data/") + '/*.mplstyle', recursive=True)
print(stylefiles)
# Find stylelib directory (where the *.mplstyle files go)
mpl_stylelib_dir = os.path.join(mpl.get_configdir() ,"stylelib")
if not os.path.exists(mpl_stylelib_dir):
    os.makedirs(mpl_stylelib_dir)

# Copy files over
print("Installing styles into", mpl_stylelib_dir)
for stylefile in stylefiles:
    print(os.path.basename(stylefile))
    shutil.copy(
        stylefile, 
        os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))

# check if the font is already installed WE SHOULD DO THIS....

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


def check_if_font_already_present(font):
    # check if a file that contains thefont name is already in the fonts folder:
    try:
        for file in [x.lower() for x in os.listdir("fonts")]:
            if font.replace(" ", "").lower() in file:
                return True
        return False
    except:
        return False


for font in fonts:
    if not check_if_font_already_present(font):
        print("Now downloading: " + font)
        download_googlefont(font=font)

update_matplotlib_fonts()





# Monkeypatching matplotlib to change the legend font-width:
# import matplotlib.axes
# import matplotlib.pyplot as plt
# def legend_wrapper(*args, **kwargs):
#     # Extract title from kwargs, if provided
#     # print(kwargs)
#     # title = kwargs.pop("title", None)

#     # If title exists, make it bold
#     # if title:
#     #     title = "$\\bf{" + title + "}$"
#     #     kwargs["title"] = title
#     kwargs["bbox_to_anchor"] = (1.2, .5)
#     legend = original_legend_func(*args, **kwargs)
#     legend.get_title().set_fontweight('bold')

#     # Call the original legend function with the modified title and kwargs
#     return legend#original_legend_func(*args, **kwargs)

# # Save the original legend function for internal use
# original_legend_func = matplotlib.axes.Axes.legend

# # Monkey patch the legend function
# matplotlib.axes.Axes.legend = legend_wrapper