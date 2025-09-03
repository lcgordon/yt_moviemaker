How This Package Was Built Using Cookiecutter
=============================================


The cookiecutter docs are, quite frankly, bad. Here's all the steps I did to put this package together on my Mac M4 running Sequoia 15.6. 

- Set up a development environment using conda
    - substeps + link

- Installed cookiecutter
    - https://cookiecutter.readthedocs.io/en/stable/README.html#installation
    - Follow their instructions to install on system

- Initializing the repo: 
    - pipx run cookiecutter cookiecutter-pypackage/ (?) 
    - I'm about to have to follow my own directions I fear
    - The main source code is here: https://github.com/audreyfeldroy/cookiecutter-pypackage. 

- Once you have your repo set up, to install locally run ``pip install .`` from that directory
    - You can also run ``pip install -e .`` which will run it in editable mode - you don't have to re-install after every change. 



- Where code goes: 
    - ``yt_moviemaker/src/yt_moviemaker/yt_moviemaker.py`` is where all your main functions go
    - ``yt_moviemaker/src/yt_moviemaker/utils.py`` is where any helpers go
        - and similar for any other modules you want

- Where tests go: 
    - ``yt_moviemaker/tests/test_yt_moviemaker.py`` is where the tests for yt_moviemaker.py can go
    - run tests from the top level directory as ``python -m pytest``
        - you will need to install pytest for this


- After the package is installed, from a separate file in a different directory::

    from yt_moviemaker import utils, yt_moviemaker
    utils.do_something_useful()
    x = yt_moviemaker.moviemaker()
    

- Writing and building documentation: 
    - install sphinx
    - sphinx-quickstart to set it up
        - i set it up with separate source and build directories
    - sphinx-apidoc -o docs/ src/yt_moviemaker
    - sphinx-build [??]
    - after this point can just run make html every time you want to update it
    - .. include:: ../../README.rst should work but also gave me so much grief...
    - tutorials of use:
        - https://www.sphinx-doc.org/en/master/tutorial/getting-started.html
        - https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/ 
    - misc
        - https://www.sphinx-doc.org/en/master/usage/theming.html
        - https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#inserting-code-and-literal-blocks