# Contributing

## Joining the team

So you want to help out with PurdueStat? That's awesome! We're always looking for new contributors, and we're glad you're interested in helping out. PurdueStat's code is designed to be accessible to everyone, so don't worry if you are new to programming! This document will explain how to get started with development, and how to submit a pull request. If you have any questions, don't hesitate to reach out on Discord at park#0001.

## Setup

If you are already familiar with installing packages via pip, you can skip this section after creating a virtual environment and/or installing packages from `requirements.txt`. If not, continue reading.

There are two methods of setting up a development environment for PurdueStat. The first is to install the packages within a virtual environment, and the second is to install the packages globally. We recommend using a virtual environment, because it will allow you to contain the packages locally. This means that you can install the packages without affecting your global python installation, which could be useful if you are working on other projects that use different versions of the same packages.

### Prerequisites

- python 3.x and pip3 (python 3.11 was used for development)

### Method 1: Using a virtual environment (recommended)

**You may use a command line tool such as `direnv` to automatically activate/deactivate the virtual environment for you, but it is not required.**

- Verify that you are in the root directory of the repo and run `make virtualenv` in your command line.
  - This creates a virtual environment in your directory called `.venv`, and installs the packages from `requirements.txt` into it.
- Activate the virtual environment by running `source .venv/bin/activate` in your command line.
  - If using an unmodified shell, you should see `(venv)` appear at the beginning of your command line. This means that you are now in the virtual environment.
  - If you are using a modified shell or you do not see the name of the environment, you can run `echo $VIRTUAL_ENV` to verify that you are in the virtual environment.

### Method 2: Installing packages globally

  **This is not the recommended method of installation, as it will install the packages globally and may affect other projects you are working on.**

- Step 1: Install python3 and pip3
- Step 2: Run `python3 install -r requirements.txt` to install package dependencies
  - Depending on your system, you may need to run `pip3 install -r requirements.txt` instead

That's it! If you opted to use a virtual environment, you can deactivate it by running `deactivate` in your command line. If you are using a modified shell, you may need to run `exit` to exit the virtual environment.

## Development

### Code style

PurdueStat uses the [black](https://www.github.com/psf/black) code formatter. This means that all code is formatted using black before being committed. This is done automatically by the [pre-commit](https://github.com/pre-commit) hook whenever you commit changes, but you can manually run black by entering `black .` into your command line. This can be useful if you want to see how the formatted code looks before you commit.

### Documentation

All functions and classes should be documented using PEP 257 style docstrings. This means that the first line of the docstring should be a short description of the function or class, and the rest of the docstring should be a detailed explanation of the function or class. For example:

  ```python
  def test_function():
      """This is a short description of the function.

      This is a detailed explanation of the function. It should explain what the function does, and how it does it.
      """
      pass
  ```
