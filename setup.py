from setuptools import setup

# https://packaging.python.org/distributing/#packaging-your-project

def readme():
    with open('README.md') as f:
        return f.read()
setup(
    name = 'configserver',
    packages = ['adminserver'],
    version = '1.5',
    license='MIT',
    description = 'Configure your linux server with configserver',
    long_description = readme(),
    author = 'dylan14567',
    author_email = '',
    url = 'https://github.com/dylan14567/configserver',
    download_url="https://github.com/dylan14567/configserver/archive/1.6.tar.gz",
    scripts = ['configserver'],
    keywords = 'python server configserver admin', 
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
