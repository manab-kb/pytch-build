=================
Pytch Build Tools
=================

Tools to assemble website from content, IDE, and tutorials.


Development setup
-----------------

To set up a virtualenv for development and testing::

  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade pip
  pip install 'tox>=4.0.0'

Then one or both of::

  python setup.py develop
  pip install -r requirements_dev.txt
  pytest tests

and/or::

  tox

(Using ``tox`` will also build the docs and run ``flake8``.)

For live reload while editing docs::

  cd doc
  sphinx-autobuild --re-ignore '/\.#' source build/html

and then visit the URL mentioned in the output.  (The ``--re-ignore
'/\.#'`` avoids Emacs auto-save files; other editors might require
something analogous.)
