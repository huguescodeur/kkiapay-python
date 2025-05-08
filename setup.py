import os
import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kkiapay",
    version="0.0.5",
    author="Junior Gantin",
    author_email="nioperas06@gmail.com",
    description="Community-driven Admin KkiaPay Sdk for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PythonBenin/kkiapay-python",
    packages=setuptools.find_packages(),
    # install_requires=required,
    install_requires=[
    "appdirs==1.4.4",
    "atomicwrites==1.4.1",
    "attrs==25.3.0",
    "black==25.1.0",
    "bleach==6.2.0",
    "certifi==2023.11.17",  # remplacé (2025.4.26 → 2023.11.17)
    "chardet==5.2.0",       # version déjà identique
    "charset-normalizer==3.3.2",  # remplacé (3.4.2 → 3.3.2)
    "click==8.1.7",         # remplacé (8.1.8 → 8.1.7)
    "colorama==0.4.6",      # version déjà identique
    "docutils==0.21.2",
    "id==1.5.0",
    "idna==3.6",            # remplacé (3.10 → 3.6)
    "importlib_metadata==8.7.0",
    "iniconfig==2.1.0",
    "jaraco.classes==3.4.0",
    "jaraco.context==6.0.1",
    "jaraco.functools==4.1.0",
    "keyring==25.6.0",
    "markdown-it-py==3.0.0",  # version déjà identique
    "mdurl==0.1.2",           # version déjà identique
    "mock==5.2.0",
    "more-itertools==10.7.0",
    "mypy_extensions==1.1.0",
    "nh3==0.2.21",
    "packaging==23.2",       # remplacé (25.0 → 23.2)
    "pathspec==0.12.1",
    "pkginfo==1.12.1.2",
    "platformdirs==4.3.8",
    "pluggy==1.5.0",
    "py==1.11.0",
    "Pygments==2.17.2",      # remplacé (2.19.1 → 2.17.2)
    "pyparsing==3.1.4",      # remplacé (3.2.3 → 3.1.4)
    "pytest==8.3.5",
    "pywin32-ctypes==0.2.3",
    "readme_renderer==44.0",
    "requests==2.31.0",      # remplacé (2.32.3 → 2.31.0)
    "requests-mock==1.12.1",
    "requests-toolbelt==0.10.1",  # remplacé (1.0.0 → 0.10.1)
    "rfc3986==2.0.0",
    "rich==13.7.0",          # remplacé (14.0.0 → 13.7.0)
    "six==1.16.0",           # remplacé (1.17.0 → 1.16.0)
    "toml==0.10.2",
    "tqdm==4.67.1",
    "twine==6.1.0",
    "urllib3==1.26.20",      # remplacé (2.4.0 → 1.26.20)
    "wcwidth==0.2.13",
    "webencodings==0.5.1",
    "zipp==3.21.0"
],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
