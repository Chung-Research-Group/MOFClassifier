import requests
from setuptools import setup, find_packages

setup(
        name="MOFClassifier",
        version="0.1.0",
        packages=find_packages(),
        description="A Machine Learning Approach for Validating Computation-Ready Metal-Organic Frameworks",
        author="Guobin Zhao",
        author_email="sxmzhaogb@gmai.com",
        url="https://github.com/Chung-Research-Group/MOFClassifier",
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        license="CC-BY-4.0",
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Scientific/Engineering :: Chemistry',
            'Programming Language :: Python :: 3.9',
        ],
        install_requires=[
                        "ase",
                        "numpy==1.26.4",
                        "torch==2.7.0",
                        "Pymatgen==2024.8.9",
                        "scikit-learn==1.3.2",
                        "tqdm==4.67.1",
                        "pandas==2.2.3"
                        ],        
        license_files = ("LICENSE",),
        python_requires='>=3.9, <4',
    )
