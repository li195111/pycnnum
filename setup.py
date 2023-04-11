import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
    name="pycnnum",
    version="1.1",
    author="Yue Li",
    author_email="green07111@gmail.com",
    description="Chinese number <-> Arabic number conversion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zcold/pycnnum",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
