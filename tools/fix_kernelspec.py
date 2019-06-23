import os

import jupytext

from generate_contents import iter_notebooks, NOTEBOOK_DIR

def fix_kernelspec():
    for nb_name in iter_notebooks():
        nb_file = os.path.join(NOTEBOOK_DIR, nb_name)
        nb = jupytext.readf(nb_file, as_version=4)

        print("- Updating kernelspec for {0}".format(nb_name))
        nb['metadata']['kernelspec']['display_name'] = 'Python 3'

        jupytext.writef(nb, nb_file)


if __name__ == '__main__':
    fix_kernelspec()
