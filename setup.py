from setuptools import setup, find_packages

VERSION = '0.0.5'
DESCRIPTION = 'An imdb search API that retreives the title , rank and year of necessary keywords.'
LONG_DESCRIPTION = 'An imdb search API that retreives the title , rank and year of necessary keywords.'

setup(
    name="imdbwebscraper",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Vishal",
    author_email="vishalvenkat2604@gmail.com",
    license='MIT',
    packages=find_packages(),
      install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'imdb_scraper = imdb.imdb:main',
        ],
    },
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ],
   
)
