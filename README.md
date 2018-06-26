# Yuci Dictionary

version = 0.1.1

## Introduction

> A tiny CLI dictionary built by python, based on youdao-web dictionary and require an internet connection. 

​	Yuci Dictionary is a simple dictionary built in your command line. Without too many useless examples and ads, Yuci Dictionary can provide you clear interface and the amount of examples and definitions are just right for your daily life.

Features:

- :dash: Simple way to search on cmd.
- :smile: Aimed to your daily life.
- :hammer_and_wrench: ~~Relatively search, convert ＇wod＇ to ＇word＇ for example.~~(Will add in next update, hopefully)
- :hammer_and_wrench: ~~History Search~~(Will add in the future)

## Install

​	To install Yuci Dictionary, just type `pip install yuci-dictionary` in cmd, or you can download the resource file and type `python setup.py install` in the folder.

## Get Start

​	In cmd, just use`dict`to call the dictionary.

Search for a word:

```
$ dict -w hello
```

Search for a word with n examples:

```
$ dict -w hello -n 10
```

## To-do list

- [x]  youdao support
- [x]  cmd support
- [ ]  help file
- [ ]  expand search function
- [ ]  history search
- [ ]  offline library

## Project website

- PyPI: <https://pypi.org/project/Yuci-Dictionary/>
- Github: https://github.com/Yucklys/yuci-dictionary 