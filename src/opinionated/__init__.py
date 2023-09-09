"""
src/opinionated/__init__.py
"""
from __future__ import absolute_import, annotations, division, print_function
import os
import time

from pathlib import Path
import sys

import matplotlib as mpl

# from matplotlib import font_manager as fm
import pkg_resources
# from typing import Optional
# import os
# import time 
import shutil
# import glob
# import colormaps as cmaps



from opinionated.core import (
    FONTS_DIR,
    STYLES_DIR,
    download_googlefont,
    update_matplotlib_fonts,
)

from opinionated.utils import (
    add_legend,
    # add_attribution,
    set_title_and_suptitle
)

__all__ = [
    'FONTS_DIR',
    'STYLES_DIR',
    'download_googlefont',
    'update_matplotlib_fonts',
    'add_legend',
    # 'add_attribution',
    'set_title_and_suptitle'
]


PYTHON_VERSION = [int(i) for i in sys.version.split(' ')[0].split('.')]
# HERE = Path(os.path.abspath(__file__)).parent
# PROJECT_DIR = HERE.parent.parent
# FONTS_DIR = PROJECT_DIR.joinpath('fonts')
# FONTS_DIR.mkdir(parents=True, exist_ok=True)
# if PYTHON_VERSION[0] >=3 and PYTHON_VERSION[1] >= 8:
#     from importlib.metadata import PackageNotFoundError, version
# else:
#     from importlib.metadata import PackageNotFoundError,
# if sys.version_info[:2] >= (3, 8):
#     # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
#     from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
# else:
#     from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

# try:
#     # Change here if project is renamed and does not equal the package name
#     dist_name = __name__
#     __version__ = version(dist_name)
# except PackageNotFoundError:  # pragma: no cover
#     __version__ = "unknown"
# finally:
#     del version, PackageNotFoundError


def reload_styles():
    # register the included stylesheet in the mpl style library
    # data_path = pkg_resources.resource_filename("opinionated", "data/")
    # print(data_path)
    opinionated_stylesheets = mpl.style.core.read_style_directory(STYLES_DIR)
    mpl.style.core.update_nested_dict(mpl.style.library, opinionated_stylesheets)
    mpl.style.reload_library()
    stylefiles = Path(
        pkg_resources.resource_filename("opinionated", "data/")
    ).rglob('*.mplstyle')
    STYLE_FILES = [STYLES_DIR.rglob('*.mplstyle')]
    mpl_stylelib_dir = Path(mpl.get_configdir()).joinpath('stylelib')
    mpl_stylelib_dir.mkdir(parents=True, exist_ok=True)
    # mpl_stylelib_dir = os.path.join(mpl.get_configdir() ,"stylelib")
    for stylefile in stylefiles:
        shutil.copy(
            stylefile,
            mpl_stylelib_dir.joinpath(os.path.basename(stylefile))
            # os.path.join(mpl_stylelib_dir, os.path.basename(stylefile))
        )
        
    # # Update the list of available styles  
    mpl.pyplot.style.core.available[:] = sorted(mpl.pyplot.style.library.keys())
    mpl.style.reload_library()


# 
# check if the font is already installed (WE SHOULD DO THIS)....

FONT_NAMES = {
    'Fira Sans',
    'Fira Sans Condensed',
    'IBM Plex Sans',
    'Jost',
    'Montserrat',
    'Roboto',
    'Roboto Condensed',
    'Source Code Pro',
    # 'Source Sans Pro',
    'Space Grotesk',
    'Space Mono',
    'Titillium Web',
    # 'Titillium WebRoboto Condensed'
}

FONT_PATHS = [
    FONTS_DIR.joinpath(f) for f in FONT_NAMES
]

def check_if_font_already_present(font):
    return FONTS_DIR.joinpath(font).exists()

def download_font_with_retry(font, retries=3, delay=3):
    for i in range(retries):
        try:
            print(f"Now downloading: {font}")
            download_googlefont(font=font)
            return  # return if the download was successful
        except Exception as e:
            if i < retries - 1:  # i is zero indexed
                print(
                    f"Attempt {i+1} to download {font} failed with error:"
                    f"{str(e)}. Retrying in {delay} seconds."
                )
                time.sleep(delay)
            else:
                print(
                    f"All attempts to download {font} failed."
                    "Please check your connection and the font name."
                )
                raise


for font in FONT_NAMES:
    if FONTS_DIR.joinpath(f"{font}.zip").is_file():
        print(f"{font} already downloaded, continuing!")
        continue
    if not check_if_font_already_present(font):
        download_font_with_retry(font)

update_matplotlib_fonts()
reload_styles()
