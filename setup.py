import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fido",
    description="End-to-end platform for robot development.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Julian Ho",
    author_email="julianho@brandeis.edu",
    url="https://github.com/hojulian/fido",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)
