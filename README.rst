Opinionated
===========

``opinionated`` provides simple, clean stylesheets for plotting with
``matplotlib`` and ``seaborn``.

It’s modeled and named after hrbrthemes in R, by hrbrmstr, which are
“Opinionated, typographic-centric ggplot2 themes”. It’s not meant to be
an exact clone though, I have made a few different choices.

The main application I had in mind was to increase the quality of plots
in colab-environments, where there is a very small range of preinstalled
fonts. The package therefore automatically downloads fonts from
GoogleFonts. But I think everything should also work on your local
machine. Be aware though, that it’s not super well-tested, and might e.
g. fail with facets.

Installation
------------

::

   pip install opinionated

Usage
-----

The package is very simple to use, you just import it and set the style
you want:

::

   import opinionated
   plt.style.use("opinionated_rc")

Then you do your plotting:

::

   f, ax = plt.subplots(figsize=(10, 7))
   sns.scatterplot(x="bill_length_mm", y="flipper_length_mm", hue='species', data=penguins, s=100, alpha=0.9)

And finally, you can slap on some additional information, using some
convenience functions with reasonable defaults. Of course, the usual
ways of setting titles, legends, etc. still work.

::

   opinionated.add_legend(title='Species')
   opinionated.add_attribution('by Maximilian Noichl')
   opinionated.set_title_and_suptitle('Penguins!','They are an excellent type of bird!')

Here’s the result:

.. figure:: https://raw.githubusercontent.com/MNoichl/opinionated/master/img/opinionated_rc_example.png
   :alt: img



This certainly does look better than what the defaults would give you,
right? –

.. figure:: https://raw.githubusercontent.com/MNoichl/opinionated/master/img/outofthebox_penguins.png
   :alt: img

You can find more options, stylesheets, etc. in the github-repository!