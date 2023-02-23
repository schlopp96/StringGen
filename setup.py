import pathlib
from setuptools import setup, find_packages

readme = pathlib.Path("readme.md").read_text()
reqs = pathlib.Path("requirements.txt").read_text()
setup(
    name="StringGen",
    version="0.8.0",
    description=
    "Generates specifically chosen number of random words pulled from a dictionary file.",
    url='https://github.com/schlopp96/StringGen',
    author='schlopp96',
    author_email='schloppdaddy@gmail.com',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[reqs],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Environment :: Console ",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords=[
        'StringGen', 'string', 'word', 'random', 'generation', 'generated',
        'password', 'python', 'passwords', 'beginner', 'project'
    ])
