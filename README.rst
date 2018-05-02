========
Overview
========

.. .. start-badges
.. 
.. .. list-table::
..     :stub-columns: 1
.. 
..     * - docs
..       - |docs|
..     * - tests
..       - |
..         | |codecov|
..     * - package
..       - | |version| |wheel| |supported-versions| |supported-implementations|
..         | |commits-since|
.. 
.. .. |docs| image:: https://readthedocs.org/projects/nlpeasy/badge/?style=flat
..     :target: https://readthedocs.org/projects/nlpeasy
..     :alt: Documentation Status
.. 
.. .. |codecov| image:: https://codecov.io/github/georgerichardson/nlpeasy/coverage.svg?branch=master
..     :alt: Coverage Status
..     :target: https://codecov.io/github/georgerichardson/nlpeasy
.. 
.. .. |version| image:: https://img.shields.io/pypi/v/nlpeasy.svg
..     :alt: PyPI Package latest release
..     :target: https://pypi.python.org/pypi/nlpeasy
.. 
.. .. |commits-since| image:: https://img.shields.io/github/commits-since/georgerichardson/nlpeasy/v0.0.1.svg
..     :alt: Commits since latest release
..     :target: https://github.com/georgerichardson/nlpeasy/compare/v0.0.1...master
.. 
.. .. |wheel| image:: https://img.shields.io/pypi/wheel/nlpeasy.svg
..     :alt: PyPI Wheel
..     :target: https://pypi.python.org/pypi/nlpeasy
.. 
.. .. |supported-versions| image:: https://img.shields.io/pypi/pyversions/nlpeasy.svg
..     :alt: Supported versions
..     :target: https://pypi.python.org/pypi/nlpeasy
.. 
.. .. |supported-implementations| image:: https://img.shields.io/pypi/implementation/nlpeasy.svg
..     :alt: Supported implementations
..     :target: https://pypi.python.org/pypi/nlpeasy
.. 
.. 
.. .. end-badges

A package for building-block style NLP pipelines using spaCy.

Installation
============

Download or git clone this respository and install with.

::

    pip install -e .

.. ::
.. 
..     pip install nlpeasy

.. Documentation
.. =============
.. 
.. https://nlpeasy.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

Design Principles
=================

Sometimes you want to try different pre-processing techniques on a corpus, but normally you don't want to write individual functions or classes to perform each unique iteration, you don't need to keep the intermediate transformed corpus, and you often get lost having lots of different objects floating around to perform various corpus pre-processing floating around. nlprep tries to resolve this issue.

The library conists of 3 main components so far:

- Cleaners

    - Take raw text documents and cleans them up using string and regex rules.
    - Take care of encoding.

- Taggers

    - Find tokens in each document that match some user-specified criteria

- Pipeline

    - Takes Taggers and applies them to text using either 'remove' or 'replace'.
    - Returns the transformed text

Some other components are under consideration:

- Builder

    - Build features in the corpus such as n-grams
