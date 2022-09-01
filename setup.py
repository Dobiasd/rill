import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rill",
    version="0.1.0",
    author="Tobias Hermann",
    author_email="editgym@gmail.com",
    description="Simple text-stream processing functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/Dobiasd/rill",
    package_data={"rill": ["py.typed"]},
    packages=["rill"],
    python_requires=">=3",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
