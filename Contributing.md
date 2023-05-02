# Contributing

## Introduction

Welcome to the team! This document will explain how to get started with development. If you have any questions, don't hesitate to contact me on Discord at park#0001.

___

## Setup

> **Prerequisites**: `python3`, `pip3`, `make`.

This section will walk you through how to install the dependencies with and without the use of a virtual environment.

### Method 1: Using a virtual environment (recommended)

1. Verify that you are in the root directory of the repo and run `make virtualenv` in your command line.
2. Activate the virtual environment by running `source .venv/bin/activate` in your command line.

When you want to disable to environment, run `deactivate` to turn it off.

> _CLI tools like_ `direnv` _can automatically activate and deactivate your virtual environment for you._

### Method 2: Installing packages globally

1. Run `pip3 install -r requirements.txt` to install package dependencies

Depending on your system, you may need to subsititute `pip3` with either `pip` or `python3`.

___

## Development

### Making changes

Before starting to make changes, please create your own branch from `develop`. Any attempts to push changes to `main` will automatically be rejected.

### Code style

PurdueStat adheres to [black](https://www.github.com/psf/black)'s uncompromising style conventions. This is done automatically by the [pre-commit](https://github.com/pre-commit) hook whenever you commit changes, but you can manually run black by entering `black .` into your command line.

### Documentation

PurdueStat is documented using modified [PEP 257](https://peps.python.org/pep-0257/) style docstrings. I will not provide an exact style guide, just do your best to follow any existing documentation! The most important part of any documentation is keeping it detailed and consistent.

### Committing

When you run `git commit`, a series of commit hooks specified in `.pre-commit-config.yaml` will run and multiple pass/skip/fail messages will show up in your console. Some errors can be corrected automatically, so you might just need to restage any modified files before trying to commit again.

___

To merge your changes, simply submit a pull request with a detailed explanation of what you've changed. For any major updates, please open an issue beforehand to explain what kind of changes you'd like to make!

Submitting a pull request does not guarantee it will be merged, and we reserve the right to deny a pull request for any reason.
