from setuptools import setup, find_packages
import secrets

setup(
    name=secrets.name,
    version='0.1',
    packages=find_packages(),
    install_requires=secrets.packages,
    description=secrets.description,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        f'Operating System :: {secrets.opsy}',
    ],
    python_requires='>=3.6',
)
