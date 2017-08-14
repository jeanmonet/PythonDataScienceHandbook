"""
This script copies all notebooks from the book into the website directory, and
creates pages which wrap them and link together.
"""
import os
import nbformat

PAGEFILE = """title: {title}
slug: {slug}
Template: page

{{% notebook notebooks/{notebook_file} cells[2:] %}}
"""


def abspath_from_here(*args):
    here = os.path.dirname(__file__)
    path = os.path.join(here, *args)
    return os.path.abspath(path)

NB_SOURCE_DIR = abspath_from_here('..', 'notebooks')
NB_DEST_DIR = abspath_from_here('content', 'notebooks')
PAGE_DEST_DIR = abspath_from_here('content', 'pages')


def copy_notebooks():
    nblist = sorted(os.listdir(NB_SOURCE_DIR))
    name_map = {nb: nb.rsplit('.', 1)[0] + '.html'
                for nb in nblist}

    for nb in nblist:
        base, ext = os.path.splitext(nb)
        if ext != '.ipynb':
            continue
        print('-', nb)

        content = nbformat.read(os.path.join(NB_SOURCE_DIR, nb),
                                as_version=4)
        title = content.cells[2].source
        if not title.startswith('#'):
            raise ValueError('title not found in third cell')
        title = title.lstrip('#').strip()

        # put nav below title
        content.cells[1], content.cells[2] = content.cells[2], content.cells[1]

        for cell in content.cells:
            if cell.cell_type == 'markdown':
                for nbname, htmlname in name_map.items():
                    if nbname in cell.source:
                        cell.source = cell.source.replace(nbname, htmlname)
        nbformat.write(content, os.path.join(NB_DEST_DIR, nb))

        pagefile = os.path.join(PAGE_DEST_DIR, base + '.md')
        with open(pagefile, 'w') as f:
            f.write(PAGEFILE.format(title=title,
                                    slug=base.lower(),
                                    notebook_file=nb))

if __name__ == '__main__':
    copy_notebooks()

    
