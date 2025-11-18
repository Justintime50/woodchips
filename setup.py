import re

import setuptools


with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

# Inspiration: https://stackoverflow.com/a/7071358/6064135
with open('woodchips/_version.py', 'r') as version_file:
    version_groups = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_groups:
        version = version_groups.group(1)
    else:
        raise RuntimeError('Unable to find version string!')

DEV_REQUIREMENTS = [
    'bandit == 1.9.*',
    'black == 25.*',
    'build == 1.3.*',
    'flake8 == 7.*',
    'isort == 7.*',
    'mypy == 1.18.*',
    'pytest == 9.*',
    'pytest-cov == 7.*',
]

setuptools.setup(
    name='woodchips',
    version=version,
    description='The cutest little logger you\'ve ever seen.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/woodchips',
    author='justintime50',
    license='MIT',
    packages=setuptools.find_packages(
        exclude=[
            'examples',
            'test',
        ]
    ),
    package_data={
        'woodchips': [
            'py.typed',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    python_requires='>=3.10, <4',
)
