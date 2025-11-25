from setuptools import find_packages
from setuptools import setup

setup(
    name="theancient",
    version="0.1.0",
    license="BSD",

    author="TheBurb",
    author_email="twentyfiveex+theancient@gmail.com",

    description="The Ancient is a fan-made Discord bot for the Arkheron "
                "gaming community audience. Arkheron s a game currently "
                "in development by Bonfire Studios. This bot is not a "
                "product of Bonfire Studios."

    packages=find_packages(exclude=('tests',)),

    install_requires=[

    ],

    test_suite="tests",

    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: Apache Software License',
    ],

    entry_points={
        'console_scripts': [
            'theancient = theancient:main',
        ],
    }
)
