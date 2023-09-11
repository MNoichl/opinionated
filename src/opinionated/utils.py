"""
opinionated/utils.py
"""
from __future__ import absolute_import, annotations, division, print_function
from typing import Optional
import matplotlib as mpl

import matplotlib.pyplot as plt

def add_legend(*args, **kwargs):
    fig = plt.gcf()
    handles, labels = fig.axes[0].get_legend_handles_labels()
    try:
        is_scatter = type(handles[0]) == mpl.collections.PathCollection
    except Exception:
        is_scatter = False
    
    try:
        is_line_plot = type(handles[0]) == mpl.lines.Line2D
    except Exception:
        is_line_plot = False
    if is_scatter:
        if "handltextpad" not in kwargs:
        # if not "handletextpad" in kwargs:
            kwargs["handletextpad"] = 0.
        # if not "scatterpoints" in kwargs:
        if 'scatterpoints' not in kwargs:
            kwargs["scatterpoints"] = 1
        # if not "scatteryoffsets" in kwargs:
        if 'scatteryoffsets' not in kwargs:
            kwargs["scatteryoffsets"] = [0]

    # if not "bbox_to_anchor" in kwargs:
    if "bbox_to_anchor" not in kwargs:
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


def add_attribution(
        attrib = 'Attribution goes here',
        position = [.9, -0.01]
):
    fig = plt.gcf()
    plt.figtext(
        position[0],
        position[1],
        attrib,
        ha="right",
        fontsize=14
    )#, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})


def set_title_and_suptitle(
        title_string,
        sub_title_string,
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
    # fig = plt.gcf()
    plt.figtext(
        position_title[0],
        position_title[1],
        title_string,
        fontsize=26,
        fontweight='bold',
        ha='left'
    )
    plt.figtext(
        position_sub_title[0],
        position_sub_title[1],
        sub_title_string,
        fontsize=14,
        fontweight='regular',
        ha='left'
    )

