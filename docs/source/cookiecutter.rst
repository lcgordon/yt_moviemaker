How This Package Was Built Using Cookiecutter
=============================================


The cookiecutter docs are not super easy to follow. Here's all the steps I did to put this package together.

I'm running on my Mac M4 running Sequoia 15.6. 

- Set up a development environment using conda
    - https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
    - ``conda create --name myEnv``
    - ``conda activate myEnv``

- Installing and setting up cookiecutter
    - ``conda install pip``
    - ``pip install -U cookiecutter``
    - ``cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage.git``
        - Fill out the question prompts
    - This will create a local directory containing their boilerplate code
    - References:
        - https://github.com/audreyfeldroy/cookiecutter-pypackage
        - https://cookiecutter.readthedocs.io/en/stable/README.html#installation

- Writing the package
    - Code:
        - ``mypackage/src/mypackage/mypackage.py`` is where all your main functions go
        - You can put other modules in ``mypackage/src/mypackage`` and call them from mypackage.py (ie, a utils.py file)
    - Tests: 
        - Yes, you do have to write tests for your code
        - ``mypackage/tests/test_mypackage.py`` is the main test file
            - you can write separate test_{name}.py test files in this same directory for other submodules
        - ``pip install pytest``
        - then from the top level directory you can run the tests as ``python -m pytest``

- Installing the package:
    - Install locally: ``pip install .`` from inside the directory
    - Install locally and editable: ``pip install -e .``
        - You don't have to re-install every time you change your code

- Using your shiny new package:
    - From a different directory
    :: 

        from mypackage import mypackage, utils
        utils.do_something_useful()
        x = mypackage.foo()

- Writing and building documentation: 
    - ``pip install sphinx``
    - cd into ``mypackage/docs/``
    - ``sphinx-quickstart`` sets everything up
        - follow prompts
        - I set it up with separate source and build directories - if you don't you'll have to change the sphinx-build command
    - cd back up to ``mypackage/``
    - run ``sphinx-apidoc -o docs/ src/mypackage``
        - This will auto-generate the API docs
    - cd back into ``mypackage/docs/``
    - run ``sphinx-build source build``
    - after this point can just run ``make html`` every time you want to update the pages
    - you can now open the .html files from build/ in your browser. 

    - write some documentation
        - you can link other files' content into .rst pages using ``.. include:: ../../README.rst`` 
            - this gave me a ton of grief...just keep messing with it until it does what you want. 

    - Docstrings and formatting
        - In conf.py you can add:
        :: 

            extensions = ['sphinx.ext.napoleon']
            napoleon_google_docstring = False
            napoleon_use_param = False
            napoleon_use_ivar = True

        Which just does a nicer job of handling the docstring formatting in more standard Google/NumPy formatting


    - tutorials of use:
        - https://www.sphinx-doc.org/en/master/tutorial/getting-started.html
        - https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/ 
    - misc
        - https://www.sphinx-doc.org/en/master/usage/theming.html
        - https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#inserting-code-and-literal-blocks

- Hooking into readthedocs
    - Get the repo onto GitHub
        - these directions were useful for me: https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-using-git
        - Do NOT put your public access token into your work or you will be bonked when you commit and push
    - Follow the readthedocs instructions: https://docs.readthedocs.com/platform/stable/tutorial/index.html
        - Main thing I ran into: the new .readthedocs.yaml file needs the path to the conf.py file, which for me was in docs/source/conf.py and not the default docs/conf.py

    - voila! 


- Other bits and pieces:
    - dependencies (like numpy or matplotlib or what have you) go into pyproject.toml file 