from setuptools import setup, find_packages

# Lire le fichier requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="kkiapay",
    version="0.0.5",
    author="Junior Gantin",
    author_email="nioperas06@gmail.com",
    description="Community-driven Admin KkiaPay SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PythonBenin/kkiapay-python",
    packages=find_packages(),
    install_requires=required,  # Dépendances lues à partir de requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
