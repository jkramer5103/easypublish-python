from setuptools import setup, find_packages

setup(
    name='jlkutils',
    version='0.15',
    packages=find_packages(),
    install_requires=[
        "cryptography", "opencv-python", "openai", "tkinter", "ast",
    ],   author='Jaron Kramer',
    description='Allgemeine Library für allen moglichen Praktischen Stuff',
    url='https://github.com/jkramer5103/jlkutils',  # Optional: URL zu deinem Projekt
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
