#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'pygit2>=1.2.1',
    'Markdown>=3.2.2',
    'beautifulsoup4>=4.9.1',
    'click>=7.1.0',
    'watchdog>=0.10.3',
    'websockets>=8.1',
    'janus>=0.5.0',
    'pyyaml>=5.3.1',
    'colorlog>=4.2.1',
]

setup(
    author="Ben North",
    author_email='ben@redfrontdoor.org',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Assemble Pytch website from content, IDE, and tutorials",
    entry_points={
        'console_scripts': [
            'pytchbuild=pytchbuild.cli:main',
            'pytchbuild-watch=pytchbuild.watch:main',
            'pytchbuild-gather-tutorials=pytchbuild.gather_tutorials:main',
            'pytchbuild-new-tutorial=pytchbuild.new_tutorial:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme,
    include_package_data=True,
    keywords='pytchbuild',
    name='pytchbuild',
    packages=find_packages(include=['pytchbuild', 'pytchbuild.*']),
    url='https://github.com/pytchlang/pytch-build/',
    version='0.1.0',
    zip_safe=False,
)
