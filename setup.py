from setuptools import setup
import huffman

setup(
    name='huffman',
    version=huffman.__version__,
    description='Generate Huffman codebooks',
    long_description=open('README.rst').read(),
    url='https://github.com/nicktimko/huffman',

    author='Nick Timkovich',
    author_email='npt@u.northwestern.edu',

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='encoding huffman compression binary',
    packages=['huffman'],
)
