# INE5426

## Requirements

This project uses [Poetry](https://python-poetry.org/) to handle its dependencies. IF you don't have Poetry installed, you can do so following these [inscructions](https://python-poetry.org/docs/#installation)

Otherwise, if you have `pip3`, this project's Makefile provides a method (although a not recommended one) of installing Poetry through `pip`. To do that, run the command `make install-poetry`

## Usage
- Run `make install-poetry` if you'd like;
- Run `make install` to use Poetry to install the project's dependencies;
- Run `make run src=<path/to/source_code` to execute the lexical analyzer on the source code provided. If you don't specify a src, the file used will be `examples/tests/success.lua`

## Examples
The three programs written in CC-2021-1 are in the `examples` directory, alongside a few simpler examples, in the `tests` subdirectory.
