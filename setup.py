import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="configserver", 
    version="0.0.1",
    author="dylan14567",
    author_email="",
    description="configure your server with configserver",
    long_description=README.md,
    long_description_content_type="text/markdown",
    url="https://github.com/dylan14567/configserver",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords="configserver",
    install_requires=["colorama"],
    include_package_data=True,
)
