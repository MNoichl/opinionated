# Opinionated

`opinionated` provides simple, clean stylesheets for plotting with `matplotlib`. 
It's modelled and named after hrbrthemes in R, by hrbrmstr, which are "Opinionated, typographic-centric ggplot2 themes", although I have made some different choices. 

The main application I had in mind was to increase the quality of plots in colab-environments, where there is a very small range of preinstalled fonts. The package therefore automatically downloads fonts from GoogleFonts. But I think everything should also work on your local machine. Be aware though, that it does monkeypatch the defaults of some matplotlib-functions, which might lead to unexpected results.



## Installation

    pip install git+https://github.com/MNoichl/opinionated.git#egg=opinionated


## Usage


<img src="img/opinions_rc_example.png" width="672" />

<!-- ![A sample plot of the opinions_rc theme.](img/opinions_rc_example.png) -->

## Inspiration 

https://github.com/dhaitz/mplcyberpunk

https://github.com/hrbrmstr/hrbrthemes
