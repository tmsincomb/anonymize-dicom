from setuptools import setup, find_packages

setup(
    name='anonymize_dicom',
    version='0.0.1',
    description='Anonymize dicom files for HIPAA guidelines',
    long_description='',
    url='https://github.com/tmsincomb/anonymize-dicom',
    author='Troy Sincomb',
    author_email='troysincomb@gmail.com',
    license='MIT',
    keywords='anonymize dicom',
    packages=find_packages('anonymize_dicom'),
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'docopt',
        'pathlib',
        'pydicom',
    ],
    entry_points={
        'console_scripts': [
            'anonymize-dicom=anonymize_dicom.anonymize:main',
        ],
    },
)
