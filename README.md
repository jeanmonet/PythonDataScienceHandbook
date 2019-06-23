# Python Data Science Handbook

> What would Jake Vanderplas' Python Data Science Handbook have looked like if it used [Jupytext](https://github.com/mwouts/jupytext) from inception?
> 
> This is an unusual idea, and a complete anachronism: Jupytext was introduced in the late 2018, while Jake had already contributed most of his notebooks in 2016. But... it works! And was just a matter of running:
> 
>     git filter-branch --tree-filter 'jupytext --to md */*.ipynb && rm -f */*.ipynb' HEAD
>
> - Open this fork on  [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/mwouts/PythonDataScienceHandbook/jupytext_no_ipynb?filepath=notebooks%2FIndex.md)
> - Explore the [commit history](https://github.com/mwouts/PythonDataScienceHandbook/commits/jupytext_no_ipynb?after=4213d731ac9ec09ac4a928cfae737c045bbd72b4+105) and see how the diffs look like when we use `.md` files rather than `.ipynb` files.
> - See the full details of how it was done on this [GitHub issue](https://github.com/mwouts/jupytext/issues/263).

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jakevdp/PythonDataScienceHandbook/master?filepath=notebooks%2FIndex.md)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.md)

This repository contains the entire [Python Data Science Handbook](http://shop.oreilly.com/product/0636920034919.do), in the form of (free!) Jupyter notebooks.

![cover image](notebooks/figures/PDSH-cover.png)

## How to Use this Book

- Read the book in its entirety online at https://jakevdp.github.io/PythonDataScienceHandbook/

- Run the code using the Jupyter notebooks available in this repository's [notebooks](notebooks) directory.

- Launch executable versions of these notebooks using [Google Colab](http://colab.research.google.com): [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.md)

- Launch a live notebook server with these notebooks using [binder](https://beta.mybinder.org/): [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jakevdp/PythonDataScienceHandbook/master?filepath=notebooks%2FIndex.md)

- Buy the printed book through [O'Reilly Media](http://shop.oreilly.com/product/0636920034919.do)

## About

The book was written and tested with Python 3.5, though other Python versions (including Python 2.7) should work in nearly all cases.

The book introduces the core libraries essential for working with data in Python: particularly [IPython](http://ipython.org), [NumPy](http://numpy.org), [Pandas](http://pandas.pydata.org), [Matplotlib](http://matplotlib.org), [Scikit-Learn](http://scikit-learn.org), and related packages.
Familiarity with Python as a language is assumed; if you need a quick introduction to the language itself, see the free companion project,
[A Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython): it's a fast-paced introduction to the Python language aimed at researchers and scientists.

See [Index.md](http://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.md) for an index of the notebooks available to accompany the text.

## Software

The code in the book was tested with Python 3.5, though most (but not all) will also work correctly with Python 2.7 and other older Python versions.

The packages I used to run the code in the book are listed in [requirements.txt](requirements.txt) (Note that some of these exact version numbers may not be available on your platform: you may have to tweak them for your own use).
To install the requirements using [conda](http://conda.pydata.org), run the following at the command-line:

```
$ conda install --file requirements.txt
```

To create a stand-alone environment named ``PDSH`` with Python 3.5 and all the required package versions, run the following:

```
$ conda create -n PDSH python=3.5 --file requirements.txt
```

You can read more about using conda environments in the [Managing Environments](http://conda.pydata.org/docs/using/envs.html) section of the conda documentation.


## License

### Code
The code in this repository, including all code samples in the notebooks listed above, is released under the [MIT license](LICENSE-CODE). Read more at the [Open Source Initiative](https://opensource.org/licenses/MIT).

### Text
The text content of the book is released under the [CC-BY-NC-ND license](LICENSE-TEXT). Read more at [Creative Commons](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode).
