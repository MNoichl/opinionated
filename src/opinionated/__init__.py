"""
src/opinionated/__init__.py
"""
# ruff: noqa: F401
from __future__ import (
    absolute_import,
    annotations,
    division,
    nested_scopes,
    print_function,
)

import logging
import os
import shutil
import time
from pathlib import Path
from typing import Optional

import matplotlib as mpl
import matplotlib.pyplot as plt

from opinionated.core import (
    FONT_NAMES,
    FONTS_DIR,
    PROJECT_DIR,
    STYLES,
    STYLES_DIR,
    download_googlefont,
    update_matplotlib_fonts,
)
# from opinionated.utils import (
#     # add_attribution,
#     # add_legend,
#     # set_title_and_suptitle
# )

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

os.environ['PROJECT_DIR'] = os.path.abspath(PROJECT_DIR)

# __all__ = [
#     'FONTS_DIR',
#     'STYLES_DIR',
#     'PROJECT_DIR',
#     'download_googlefont',
#     'update_matplotlib_fonts',
#     'add_legend',
#     # 'add_attribution',
#     'set_title_and_suptitle'
# ]


def reload_styles(
        outdir: Optional[os.PathLike] = None,
        verbose: Optional[bool] = False,
):
    outdir = (
        Path(mpl.get_configdir()).joinpath('stylelib')
        if outdir is None else Path(outdir)
    )
    outdir.mkdir(parents=True, exist_ok=True)
    for src in STYLES.values():
        dst = outdir.joinpath(Path(src).stem)
        if verbose:
            log.debug(f"Copying {src} to {dst}")
        shutil.copy2(src, dst)

    plt.style.reload_library()
    opinionated_stylesheets = plt.style.core.read_style_directory(STYLES_DIR)
    plt.style.core.update_nested_dict(
        plt.style.library,
        opinionated_stylesheets
    )
    plt.style.reload_library()
    mpl_stylelib_dir = Path(mpl.get_configdir()).joinpath('stylelib')
    mpl_stylelib_dir.mkdir(parents=True, exist_ok=True)
    # # Update the list of available styles
    plt.style.core.available[:] = sorted(plt.style.library.keys())
    # mpl.pyplot.style.core.available[:] = sorted(
    #     mpl.pyplot.style.library.keys()
    # )
    plt.style.reload_library()


def check_if_font_already_present(font):
    return FONTS_DIR.joinpath(font).exists()


def download_font_with_retry(
        font: str,
        retries: int = 3,
        delay: int = 3,
        verbose: Optional[bool] = False,
) -> None:
    for i in range(retries):
        try:
            if verbose:
                log.debug(f"Now downloading: {font}")
            download_googlefont(font=font)
            return  # return if the download was successful
        except Exception as e:
            if i < retries - 1:  # i is zero indexed
                if verbose:
                    log.debug(
                        f"Attempt {i+1} to download {font} failed with error:"
                        f"{str(e)}. Retrying in {delay} seconds."
                    )
                time.sleep(delay)
            else:
                if verbose:
                    log.debug(
                        f"All attempts to download {font} failed."
                        "Please check your connection and the font name."
                    )
                raise


def update_fonts(verbose: Optional[bool] = False):
    for font in FONT_NAMES:
        if FONTS_DIR.joinpath(f"{font}.zip").is_file():
            if verbose:
                log.debug(f"{font} already downloaded, continuing!")
            continue
        if not check_if_font_already_present(font):
            download_font_with_retry(font)
    update_matplotlib_fonts()


update_fonts()
reload_styles()
