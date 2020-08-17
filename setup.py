import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="namdout-mvondomaros",
    version="0.1",
    author="Michael von Domaros",
    author_email="mvondomaros@gmail.com",
    description="Read NAMD screen output into a pandas dataframe.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mvondomaros/namdout",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)
