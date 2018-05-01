========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/nlpeasy/badge/?style=flat
    :target: https://readthedocs.org/projects/nlpeasy
    :alt: Documentation Status

.. |codecov| image:: https://codecov.io/github/georgerichardson/nlpeasy/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/georgerichardson/nlpeasy

.. |version| image:: https://img.shields.io/pypi/v/nlpeasy.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/nlpeasy

.. |commits-since| image:: https://img.shields.io/github/commits-since/georgerichardson/nlpeasy/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/georgerichardson/nlpeasy/compare/v0.0.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/nlpeasy.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/nlpeasy

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/nlpeasy.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/nlpeasy

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/nlpeasy.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/nlpeasy


.. end-badges

A package for building block style NLP pipelines using spaCy.

* Free software: MIT license

Installation
============

::

    pip install nlpeasy

Documentation
=============

https://nlpeasy.readthedocs.io/

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
