
import requests
import zipfile
import io
import os
import shutil
from pathlib import Path
import opinionated # this works?
import matplotlib as mpl

from typing import Optional, Union, List, Tuple



import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from IPython.core.display import HTML



# for the font downloading from datamapplot
import matplotlib.font_manager
from tempfile import NamedTemporaryFile
from fontTools import ttLib
import re
import requests


# download fonts from google fonts and save them in the fonts folder:
# def download_googlefont(font='Roboto Condensed', add_to_cache=False):
#     """download a font from google fonts and save it in the fonts folder

#     Args:
#         font (str, optional): The font to download. Must be the name used by googlefonts. Defaults to 'Roboto Condensed'.
#     """
#     # download the font
#     url = f'https://fonts.google.com/download?family={font}'
#     r = requests.get(url)
#     z = zipfile.ZipFile(io.BytesIO(r.content))
#     # extract into the package folder
#     font_folder = Path(opinionated.__file__).parent / 'fonts'
#     z.extractall(font_folder)
#     print(f'Font saved to: {font_folder}')
#     if add_to_cache:
#         update_matplotlib_fonts()


def download_googlefont(font='Roboto Condensed', add_to_cache=False):
    """Code taken from Leland McInnes amazing datamapplot-library"""
    api_fontname = font.replace(' ', '+')
    api_response = resp = requests.get(f"https://fonts.googleapis.com/css?family={api_fontname}:black,bold,regular,light")
    font_urls = re.findall(r'(https?://[^\)]+)', str(api_response.content))
    for font_url in font_urls:
        font_data = requests.get(font_url)
        f = NamedTemporaryFile(delete=False, suffix='.ttf')
        f.write(font_data.content)
        f.close()
        font = ttLib.TTFont(f.name)
        font_family_name = font['name'].getDebugName(1)
        matplotlib.font_manager.fontManager.addfont(f.name)
        print(f"Added new font as {font_family_name}")

    if add_to_cache:
        update_matplotlib_fonts()


def make_html(fontname):
    """Make a HTML snippet to display a font in a notebook. Utility used by show_installed_fonts()."""
    return "<p>{font}: <span style='font-family:{font}; font-size: 24px;'>{font}</p>".format(font=fontname)

def show_installed_fonts():
    """Show all installed fonts in a columnized HTML table. Works in notebooks only.
    """
    code = "\n".join([make_html(font) for font in sorted(set([f.name for f in fm.fontManager.ttflist]))])
    display(HTML("<div style='column-count: 2;'>{}</div>".format(code)))


def update_matplotlib_fonts():
    """Update matplotlib's font cache. Useful if you downloaded googlefonts to the fonts folder (with download_googlefont) and want to use them in matplotlib.
    """
    #update the font cache: 


    font_folder = Path(opinionated.__file__).parent / 'fonts'
    for font_file in fm.findSystemFonts(fontpaths=str(font_folder)):

        if ('.ttf' in font_file) or ('.otf' in font_file):
            try:
                fm.fontManager.addfont(os.path.join(font_folder,font_file))
            except:
                print('This font could not be added: ', font_file)
                pass

    # shutil.rmtree(mpl.get_cachedir())









    # Plotting functions:

def add_legend(*args, **kwargs):
    fig = plt.gcf()
  

    handles, labels = fig.axes[0].get_legend_handles_labels()
    try:
        is_scatter = type(handles[0]) == mpl.collections.PathCollection
    except:
        is_scatter = False
    
    try:
        is_line_plot = type(handles[0]) == mpl.lines.Line2D
    except:
        is_line_plot = False

    
    if is_scatter:
        if not "handletextpad" in kwargs:
            kwargs["handletextpad"] = 0.
        if not "scatterpoints" in kwargs:
            kwargs["scatterpoints"] = 1
        if not "scatteryoffsets" in kwargs:
            kwargs["scatteryoffsets"] = [0]


    if not "bbox_to_anchor" in kwargs:
        kwargs["bbox_to_anchor"] = (1.24, .5)
    # if is_line_plot:

    legend = plt.legend(*args, **kwargs)
    legend.get_title().set_fontweight('bold')

    if is_scatter:
        [t.set_va('center_baseline') for t in legend.get_texts()]


    return legend

    # ax.legend(bbox_to_anchor=(1.2, .5),
    #             borderaxespad=0.0,
    #             title="$\\bf{" + title + "}$",
    #             fancybox=True) 
# Add args
def add_attribution(attrib = 'Attribution goes here', position = [.9, -0.01]):
    fig = plt.gcf()
    plt.figtext(position[0],position[1], attrib, ha="right", fontsize=14)#, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})

def set_title_and_suptitle(title_string,sub_title_string, position_title = [.12, .97],
                            position_sub_title = [.12, .918]):
    """
    Set the title and subtitle of a plot. The subtitle is set a bit lower than the title. 
    The adjust_y parameter can be used to adjust the vertical position of the two titles.
    Args:
        title_string (str): The title string
        sub_title_string (str): The subtitle string
        position_title (list, optional): The position of the title. Defaults to [.12, .97].
        position_sub_title (list, optional): The position of the subtitle. Defaults to [.12, .918].
    """
    fig = plt.gcf()
    plt.figtext( position_title[0], position_title[1], title_string, fontsize=26, fontweight='bold', ha='left')
    plt.figtext( position_sub_title[0], position_sub_title[1], sub_title_string,  fontsize=14, fontweight='regular', ha='left')
