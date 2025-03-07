import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='edge2vec',
        description='involving edge semantics into node embedding ',
        long_description='transition matrixs with skip gram model',
        url='https://github.com/RoyZhengGao/edge2vec',
        license='BSD 3-Clause License',
        packages=setuptools.find_packages(),
        python_requires='>=3.6',
        install_requires=[
            'numpy',
            'pandas',
            'scipy',
            'sklearn',
            'gensim',
            'networkx',
            'matplotlib',
        ],
    )
