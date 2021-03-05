from setuptools import setup

# https://packaging.python.org/distributing/#packaging-your-project

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

setup(
    name = 'configserver',
    packages = ['adminserver'],
    include_package_data=True,
    version = '1.7',
    license='MIT',
    description = 'Configure your linux server with configserver',
    long_description=README,
    long_description_content_type="text/markdown",
    author = 'dylan14567',
    author_email = '',
    url = 'https://github.com/dylan14567/configserver',
    download_url="https://github.com/dylan14567/configserver/archive/1.6.tar.gz",
    scripts = ['configserver'],
    keywords = ['python', 'server', 'configserver', 'admin'], 
    install_requires=[
        "colorama",
        "requests",
    ],
    classifiers = (
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3'
    )
)
