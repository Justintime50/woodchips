import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

DEV_REQUIREMENTS = [
    'black == 22.*',
    'build == 0.7.*',
    'coveralls == 3.*',
    'flake8 == 4.*',
    'isort == 5.*',
    'mypy == 0.942',
    'pytest == 7.*',
    'pytest-cov == 3.*',
    'twine == 4.*',
]

setuptools.setup(
    name='woodchips',
    version='0.2.4',
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
    python_requires='>=3.7, <4',
)
