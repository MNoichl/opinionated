"""opinionated - A new Python package"""

import matplotlib as mpl

from matplotlib import font_manager as fm
import pkg_resources
from typing import Optional, Union, List, Tuple
import os
import time 
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



# def check_if_font_already_present(font):
#     # check if a file that contains thefont name is already in the fonts folder:
#     try:
#         for file in [x.lower() for x in os.listdir("fonts")]:
#             if font.replace(" ", "").lower() in file:
#                 return True
#         return False
#     except:
#         return False


# for font in fonts:
#     if not check_if_font_already_present(font):
#         print("Now downloading: " + font)
#         download_googlefont(font=font)

# update_matplotlib_fonts()





# Monkeypatching matplotlib to change the legend font-width:
# import matplotlib.axes
# import matplotlib.pyplot as plt

import os
import time

fonts = [
    "Roboto Condensed",
    "Montserrat",
    # "Source Code Pro",
    # "Source Sans Pro",
    # "Fira Sans",
    # "Fira Sans Condensed",
    # "IBM Plex Sans",
    # "Space Grotesk",
    # "Space Mono",
    # "Roboto",
    # "Jost",
    # "Titillium Web"
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



# def check_if_font_already_present(font):
#     # check if a file that contains thefont name is already in the fonts folder:
#     try:
#         for file in [x.lower() for x in os.listdir("fonts")]:
#             if font.replace(" ", "").lower() in file:
#                 return True
#         return False
#     except:
#         return False


# for font in fonts:
#     if not check_if_font_already_present(font):
#         print("Now downloading: " + font)
#         download_googlefont(font=font)

# update_matplotlib_fonts()



##############################################################################

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