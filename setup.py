from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'Yuci Dictionary',
    version = '0.1.1',
    package = find_packages(),
    description = 'A tiny CLI dictionary built by python, based on youdao-web dictionary and require an internet connection.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = 'python youdao terminal',
    py_modules = ['dictionary.yuci_dictionary_youdao'],
    author = 'Yucklys',
    author_email = 'yucklys687@outlook.com',
    url = 'https://github.com/Yucklys/nontype-dictionary',
    license = 'MIT',
    include_package_data = True,
    install_requires = [
        'beautifulsoup4>=4.6.0',
        'lxml>=4.0.0'
    ],
    entry_points = {
        'console_scripts':[
            'dict = dictionary.yuci_dictionary_youdao:main'
        ]
    },
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)