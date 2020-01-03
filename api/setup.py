import os
from setuptools import setup, find_packages

cwd = os.path.abspath(os.path.dirname(__file__))

requires = ["Flask==1.0"]

setup(
    name="tswf",
    description="tasty shapes with friends.",
    classifiers=[
        "Development Status :: Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Internet People",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Internet :: Www/HTTP :: WSGI :: Application",
    ],
    author="@ptdel",
    url="https://github.com/ptdel/tswf",
    keywords="flask ffmpeg youtube-dl irc jorny",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="api",
    tests_require=["pytest"],
    install_requires=requires,
)
