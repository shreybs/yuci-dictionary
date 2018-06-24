from setuptools import setup, find_packages
setup(
    name = 'nontype_dict',
    version = '0.1',
    package = find_packages(),
    description = 'A tiny CLI dictionary built by python, based on youdao-web dictionary and require an internet connection.',
    keywords = 'python youdao terminal',
    author = 'Yucklys',
    author_email = 'yucklys687@outlook.com',
    license = 'MIT',
    install_requires = [
        'requests',
        'beautifulsoup4',
        'argparse',
        're',
    ],
    entry_points = {
        'console-scripts':[
            'ntype = youdao_dict.nonetype_dict:main'
        ]
    },
)