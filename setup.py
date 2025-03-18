from setuptools import setup, find_packages

setup(
    name='llm_framework',
    version='0.1.0',
    author='Pat Joyce',
    author_email='joyce.pat@gmail.com',
    description='A framework for interacting with Large Language Models (LLMs).',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        # e.g., 'numpy', 'requests', etc.
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)