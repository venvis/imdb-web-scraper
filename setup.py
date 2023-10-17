from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'An imdb search API that retreives the title , rank and year of necessary keywords.'
LONG_DESCRIPTION = 'An imdb search API that retreives the title , rank and year of necessary keywords.'

setup(
    name="imdb-web-scraper",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Vishal",
    author_email="vishalvenkat2604@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ],
     install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'imdb_scraper = my_imdb_scraper.module:main',
        ],
    },
)
