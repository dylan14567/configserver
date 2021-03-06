import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="configserver", 
    version="1.10",
    author="dylan14567",
    author_email="dylanmeca70@yahoo.com",
    description="Configure your linux server and check for vulnerabilities with configserver.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dylan14567/configserver",
    scripts = ['configserver'],
    project_urls={
        "Bug Tracker": "https://github.com/dylan14567/configserver/issues",
    },
    install_requires=[
        "colorama",
        "requests",
        "wheel",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="server",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
)
