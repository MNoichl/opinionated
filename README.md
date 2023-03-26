# Opinionated

`opinionated` provides simple, clean stylesheets for plotting with `matplotlib`. 
It's modelled and named after hrbrthemes in R, by hrbrmstr, which are "Opinionated, typographic-centric ggplot2 themes", although I have made some different choices. 

The main application I had in mind was to increase the quality of plots in colab-environments, where there is a very small range of preinstalled fonts. The package therefore automatically downloads fonts from GoogleFonts. But I think everything should also work on your local machine. Be aware though, that it does monkeypatch the defaults of the legend-function, which might lead to unexpected results.



## Installation

    pip install git+https://github.com/MNoichl/opinionated.git#egg=opinionated


## Usage
The usage is really simple, you just import the package and set the style you want to use:

    import opinionated
    plt.style.use("opinions_rc")

Then you do your plotting:

    f, ax = plt.subplots(figsize=(10, 7))
    sns.scatterplot(x="bill_length_mm", y="flipper_length_mm", hue='species', data=penguins, s=100, alpha=0.9)

And finally you can slap on some additional information:

    ax.legend(title='Species')
    opinionated.add_attribution('by Maximilian Noichl')
    opinionated.set_title_and_suptitle('Penguins!','They are a very good type of bird!')

Here's the result:
<img src="img/opinions_rc_example.png" width="672" />

This certainly does look better than what the defaults would give you, right? –
<img src="img/outofthebox_penguins.png" width="672" />


The style `opinions_rc` 
<!-- ![A sample plot of the opinions_rc theme.](img/opinions_rc_example.png) -->

## Inspiration 

https://github.com/dhaitz/mplcyberpunk

https://github.com/hrbrmstr/hrbrthemes
