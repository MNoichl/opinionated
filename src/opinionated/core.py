"""
core.py
"""
from __future__ import absolute_import, annotations, division, print_function

import requests
import zipfile
import os
import sys
from pathlib import Path
import io

import matplotlib as mpl

from typing import Optional, Sequence

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from IPython.core.display import HTML

PYTHON_VERSION = [int(i) for i in sys.version.split(' ')[0].split('.')]
HERE = Path(os.path.abspath(__file__)).parent
PROJECT_DIR = HERE.parent.parent

FONTS_DIR = PROJECT_DIR.joinpath('fonts')
STYLES_DIR = HERE.joinpath('stylefiles')

FONTS_DIR.mkdir(parents=True, exist_ok=True)
STYLES_DIR.mkdir(parents=True, exist_ok=True)

STYLE_FILES = list(STYLES_DIR.rglob('*.mplstyle'))
STYLES = {f.stem: f.as_posix() for f in STYLE_FILES}

FONT_NAMES = (
    # 'Fira Sans',
    # 'Fira Sans Condensed',
    'IBM Plex Sans',
    'IBM Plex Sans Condensed',
    'IBM Plex Serif',
    # 'Jost',
    # 'Montserrat',
    # 'Roboto',
    # 'Roboto Condensed',
    # 'Source Code Pro',
    # 'Source Sans Pro',
    # 'Space Grotesk',
    # 'Space Mono',
    # 'Titillium Web',
    # 'Titillium WebRoboto Condensed',
    # 'Shadows Into Light Two'
)

FONTS = {
    f: FONTS_DIR.joinpath(f) for f in FONT_NAMES
}


def set_color_cycle(colors: list[str | Sequence[str | int]]) -> None:
    plt.rcParams['axes.prop_cycle'] = plt.cycler(
        'color',
        list(colors)
    )


def _download_font(font: str) -> requests.Response:
    return requests.get(
        f'https://fonts.google.com/download?family={font}'
    )


def save_font(font: str) -> None:
    response = _download_font(font)
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(FONTS_DIR)
    zip_fp = FONTS_DIR.joinpath(f'{font}.zip')
    with open(zip_fp, 'wb') as f:
        f.write(response.content)
    print(f'Font saved to: {FONTS_DIR}/{font}')


def download_googlefont(
        font='IBM Plex Sans',
        add_to_cache=True
):
    """download a font from Google fonts

    Args:
        font (str, optional): The font to download.
        Must be the name used by googlefonts. Defaults to 'IBM Plex Sans'.
    """
    try:
        save_font(font)
    except Exception:
        print(f'Failed to download font: {font}, skipping!')
    if add_to_cache:
        update_matplotlib_fonts()


def make_html(fontname):
    """
    Make a HTML snippet to display a font in a notebook.
    Utility used by show_installed_fonts().
    """
    return (
        f"<p>{fontname}: <span style='font-family:{fontname};"
        f"font-size: 24px;'>{fontname}</p>"
    )


def show_installed_fonts():
    """
    Show all installed fonts in a columnized HTML table. Works in notebooks
    only.
    """
    code = (
        "\n".join(
            [
                make_html(font) for font in
                sorted(set([f.name for f in fm.fontManager.ttflist]))
            ]
        )
    )
    HTML("<div style='column-count: 2;'>{}</div>".format(code))


def update_matplotlib_fonts():
    """Update matplotlib's font cache.
    Useful if you downloaded googlefonts to the fonts folder
    (with download_googlefont) and want to use them in matplotlib.
    """
    for font_file in fm.findSystemFonts(fontpaths=str(FONTS_DIR)):
        if ('.ttf' in font_file) or ('.otf' in font_file):
            try:
                fm.fontManager.addfont(
                    os.path.join(
                        FONTS_DIR,
                        font_file
                    )
                )
            except Exception:
                print('This font could not be added: ', font_file)


def add_legend(*args, **kwargs):
    fig: plt.Figure = plt.gcf()  # type:ignore
    ax: plt.Axes = plt.gca()  # type:ignore
    handles, _ = fig.axes[0].get_legend_handles_labels()
    is_scatter = isinstance(handles[0], mpl.collections.PathCollection)
    # is_scatter = (type(handles[0]) == mpl.collections.PathCollection)
    # is_line_plot = (type(handles[0]) == mpl.lines.Line2D)
    # kwargs |= {"bbox_to_anchor": (1.05, .5)}
    if "bbox_to_anchor" not in kwargs:
        kwargs["bbox_to_anchor"] = (1.05, .5)
    if is_scatter:
        if "handltextpad" not in kwargs:
            kwargs["handletextpad"] = 0.
        if 'scatterpoints' not in kwargs:
            kwargs["scatterpoints"] = 1
        if 'scatteryoffsets' not in kwargs:
            kwargs["scatteryoffsets"] = [0]
    legend = ax.legend(*args, **kwargs)
    # legend.get_title().set_fontweight('bold')
    if is_scatter:
        [t.set_va('center_baseline') for t in legend.get_texts()]
    return legend


def add_attribution(
        attrib: str,
        position: Optional[tuple[int, int]] = None,
):
    # fig = plt.gcf()
    # bbox = {
    #     "facecolor":"orange",
    #     "alpha":0.5,
    #     "pad":5
    # }
    loc = (.9, -0.01) if position is None else position
    plt.figtext(
        loc[0],
        loc[1],
        attrib,
        ha="right",
        fontsize=14
    )


def set_title_and_suptitle(
        title_string,
        sub_title_string: Optional[str] = None,
        position_title: Optional[list] = None,
        position_sub_title: Optional[list] = None,
):
    """
    Set the title and subtitle of a plot.
    The subtitle is set a bit lower than the title.
    The adjust_y parameter can be used to
    adjust the vertical position of the two titles.
    Args:
        title_string (str): The title string
        sub_title_string (str): The subtitle string
        position_title (list, optional): The position of the title.
            Defaults to [.12, .97].
        position_sub_title (list, optional): The position of the subtitle.
            Defaults to [.12, .918].
    """
    position_title = [.12, .97] if position_title is None else position_title
    position_sub_title = (
        [.12, .918] if position_sub_title is None else position_sub_title
    )
    if sub_title_string is not None:
        plt.figtext(
            position_title[0],
            position_title[1],
            title_string,
        )
    else:
        sub_title_string = title_string
    plt.figtext(
        position_sub_title[0],
        position_sub_title[1],
        sub_title_string,
    )
