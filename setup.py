from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='cldfbench_walker2011bayesian',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_walker2011bayesian'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'walker2011bayesian=cldfbench_walker2011bayesian:Dataset',
        ]
    },
    install_requires=[
        'pyglottography',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
