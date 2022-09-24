# not-a-hat
A Python application for handling CFG grammars according to the Backus-Naur Form.

This project uses Poetry as its main dependency manager. For installing it, you may use

```shell
make install-poetry
```

After the installation, ask Poetry to install the project dependencies
by using

```shell
make install
```

A classic `make run` can be used for running the code. Right now,
this project handles only the lexical analysis part. Inside
its `main` module, you can find all the token patterns and their
regexes according to the `resources/grammar.txt`.

The symbol tables for the respective test codes will be put
inside `output/`, at last.