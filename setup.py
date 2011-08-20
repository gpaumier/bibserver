from setuptools import setup, find_packages

setup(
    name = 'bibserver',
    version = '0.3',
    packages = find_packages(),
    install_requires = [
        "Flask==0.7.2",
        "solrpy",
        ],
    url = 'http://bibserver.okfn.org/',
    author = 'Open Knowledge Foundation',
    author_email = 'openbiblio@okfn.org',
    description = 'BibServer is a RESTful bibliographic data server.',
    license = 'AGPL',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

