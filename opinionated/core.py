
import requests
import zipfile
import io
import os
import shutil
from pathlib import Path
import opinionated # this works?


from matplotlib import font_manager as fm
from IPython.core.display import HTML


# download fonts from google fonts and save them in the fonts folder:
def download_googlefont(font='Roboto Condensed'):
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



def make_html(fontname):
    """Make a HTML snippet to display a font in a notebook. Utility used by show_installed_fonts()."""
    return "<p>{font}: <span style='font-family:{font}; font-size: 24px;'>{font}</p>".format(font=fontname)

def show_installed_fonts():
    """Show all installed fonts in a columnized HTML table. Works in notebooks only.
    """
    code = "\n".join([make_html(font) for font in sorted(set([f.name for f in matplotlib.font_manager.fontManager.ttflist]))])
    display(HTML("<div style='column-count: 2;'>{}</div>".format(code)))


def update_matplotlib_fonts():
    """Update matplotlib's font cache. Useful if you installed new fonts and want to use them in matplotlib.
    """
    font_files = fm.findSystemFonts('.')
    for font_file in font_files:
        try:
            fm.fontManager.addfont(font_file)
        except:
            print('This font could not be added: ', font_file)
            pass
