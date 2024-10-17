from setuptools import setup, find_packages
import secrets

setup(
    name=name,
    version='0.1',
    packages=find_packages(),
    install_requires=packages,
    description=description,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        f'Operating System :: {opsy}',
    ],
    python_requires='>=3.6',
)
