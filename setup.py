from setuptools import setup, find_packages

setup(
    name='pythoniserjava',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author='Louka Noves',
    author_email='your-email@example.com',
    description='This is a new version of java that is interpreted in python grammar/syntax.',
    url='https://github.com/LoukaNoves/pythoniserjava',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)