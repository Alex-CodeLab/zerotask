import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zerotask", # Replace with your own username
    version="0.0",
    author="Alex",
    description="Easy backgound tasks scheduler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alex-codeLab/zerotask",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
