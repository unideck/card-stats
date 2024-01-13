from setuptools import setup, find_packages
from os.path import join, dirname

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    install_requires = f.read().split("\n")

setup(
    name='card-stats',
    version='0.1.0',
    url='https://github.com/unideck/card-stats',
    license='GPLv3+',
    author='Keegan Woodburn',
    author_email='keegan.woodburn@gmail.com',
    description='a simple tool to get card stats from a user defined game state',
    long_description=open('README.md').read(),
    packages=find_packages(include=['card_stats']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    tests_require=[
        'pytest',
        'packaging'
    ],
    test_suite='tests',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    ]
)
