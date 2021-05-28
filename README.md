# ``moodle`` LaTeX class

This uses the [Moodle package in CTAN](https://ctan.org/pkg/moodle) to easily edit and generate Moodle quizzes and essays.

## Purpose (target outputs)

Output formats:

* ``PDF``

* ``XML``

## While editing

While editing you may want to activate the option to ``draft`` in

``\usepackage[draft]{moodle}``

## Finished product

When you have your final product recompile with

``\usepackage{moodle}``

set in your ``.tex`` file's preamble.

## Custom compilation recipe

The custom latex compilation recipe is by default set for ``XeLaTeX`` compilation with option for shell escape.

These are the first two magic lines in the ``examples.tex`` file. Don't remove them, or else you have errors compiling to your targets.
