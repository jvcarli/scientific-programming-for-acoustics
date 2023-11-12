Contributing
============

Developing the website
----------------------

Building the website locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For building the website locally, you'll need the following dependencies installed:

- Python >= 3.9
- git

Then follow the steps below:

Unix like systems (macOS, Linux)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the repository:

.. code-block:: sh

   $ git clone https://github.com/jvcarli/scientific-programming-for-acoustics

Go to the cloned repository directory:

.. code-block:: sh

   $ cd scientific-programming-for-acoustics

It is **strongly recommended** to create a virtual environment for installing the dependencies.

First, check your Python version and make sure that it is the correct one:

.. code-block:: sh

   $ python --version

It **must output at least Python 3.9.0**.

Then create the virtual environment using:

.. code-block:: sh

   $ python -m venv venv

Activate the virtual environment:

.. code-block:: sh

   $ source venv/bin/activate

Then install the website dependencies using:

.. code-block:: sh

   $ pip install -r dev_requirements.txt

Install the project `git hooks`_ using `pre-commit`_:

.. admonition:: Security Disclaimer
   :class: warning

   ``pre-commit`` tool was installed in the step above with ``pip install -r dev_requirements.txt``.

   Please note that when we run ``pre-commit install`` we are
   installing custom git hooks defined in `.pre-commit-config.yaml`_.

   These scripts are safe. You can read their execution entrypoint by checking the file. Example_.

   Local git hooks scripts are in `tools/bin/git_hooks`_ directory.

.. code-block:: sh

   $ pre-commit install

Finally, build the website locally using:

.. code-block:: sh

   $ make html

The website will be located in the ``build`` directory.

You can view it in your browser by serving it locally with:

.. code-block:: sh

   $ python -m http.server --directory build/html

Then open the link: http://localhost:8000

.. _git hooks: https://git-scm.com/docs/githooks
.. _pre-commit: https://pre-commit.com/
.. _`.pre-commit-config.yaml`: https://github.com/jvcarli/scientific-programming-for-acoustics/blob/main/.pre-commit-config.yaml
.. _Example: https://github.com/jvcarli/scientific-programming-for-acoustics/blob/main/.pre-commit-config.yaml#L6
.. _`tools/bin/git_hooks`: https://github.com/jvcarli/scientific-programming-for-acoustics/tree/main/tools/bin/git_hooks
