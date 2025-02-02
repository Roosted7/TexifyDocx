# setup.py

from setuptools import setup, find_packages

setup(
    name='TexifyDocx',
    version='1.0.0',
    author='Thomas Roos (Roosted7)',
    description='Convert LaTeX formulas to math objects in Word documents seamlessly.',
    packages=find_packages(),
    install_requires=[
        'python-docx',
        'latex2mathml',
        'mathml2omml'
    ],
    entry_points={
        'console_scripts': [
            'texifydocx=texifydocx.converter:convert_docx',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
