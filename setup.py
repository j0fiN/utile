import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="utile",  # Replace with your own username
    version="v1.0",
    author="Jofin F Archbald",
    author_email="jofinfab@gmail.com",
    description="The python package which eases your <codeflow> using decorators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/j0fiN/utile.git",
    packages=setuptools.find_packages(),
    project_urls={
        'Documentation': 'https://utile.readthedocs.io/',
        'Say Thanks!': 'http://j0fiN.github.io/home/',
        'Source': 'https://github.com/j0fiN/utile/',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
