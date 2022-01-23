# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyzetasql', 'pyzetasql.proto']

package_data = \
{'': ['*'], 'pyzetasql': ['server/.gitkeep']}

install_requires = \
['grpcio>=1.43.0,<2.0.0', 'protobuf>=3.19.3,<4.0.0']

setup_kwargs = {
    'name': 'pyzetasql',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Katsuya Shimabukuro',
    'author_email': 'katsu.generation.888@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
