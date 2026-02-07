from setuptools import setup, find_packages

setup(
    name="strongsort",
    version="0.2.2",
    python_requires=">=3.9",
    install_requires=[
        "torch>=1.12",
        "numpy>=1.21,<2",
        "scipy>=1.7",
        "scikit-learn>=0.24",
        "opencv-python>=4.6,<5",
    ],
    packages=find_packages(include=[
        "strongsort",
        "strongsort.*",
        "deep_sort",
        "deep_sort.*",
        "AFLink",
        "AFLink.*",
        "application_util",
        "application_util.*",
    ]),
)