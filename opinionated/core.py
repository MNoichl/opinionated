
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


# download fonts from google fonts and save them in the fonts folder:
def download_googlefont(font='Roboto Condensed', add_to_cache=False):
    """download a font from google fonts and save it in the fonts folder

    Args:
        font (str, optional): The font to download. Must be the name used by googlefonts. Defaults to 'Roboto Condensed'.
    """
    # download the font
    url = f'https://fonts.google.com/download?family={font}'
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    # extract into the package folder
    font_folder = Path(opinionated.__file__).parent / 'fonts'
    z.extractall(font_folder)
    print(f'Font saved to: {font_folder}')
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

def add_legend(ax: Optional[plt.Axes] = None, title: str = 'Title goes here!') -> None:
    ax.legend(bbox_to_anchor=(1.1, .5),
                borderaxespad=0.0,
                title="$\\bf{" + title + "}$",
                fancybox=True) 

def add_attribution(ax: Optional[plt.Axes] = None, attrib: str = 'Attribution goes here') -> None:
    plt.figtext( .9, -0.01, attrib, ha="right", fontsize=14)#, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
