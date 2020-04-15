""" Anonymize dicom files

Usage:
    anonymize-dicom  (-h | --help)
    anonymize-dicom  [--compress_output] [--output_path=PATH] INPUT_PATH

Arguments:
    INPUT_PATH

Options:
    -h, --help                Prints out usage examples.
    -o, --output_path=PATH    Output Folder Path
    -c, --compress_output     Tar folder & gzip

Terminal Examples:
    anonymize-dicom dicom-folder
    anonymize-dicom -c dicom-folder
    anonymize-dicom -o dicom-folder-anonymized dicom-folder
    anonymize-dicom -c -o dicom-folder-anonymized dicom-folder
    python3 anonymize-dicom/anonymize_dicom/anonymize.py dicom-folder

Import Example:
    from anonymize_dicom import anonymize
    anonymized_dicom_file = anonymize(dicom_file)
"""
import os
from pathlib import Path
from shutil import copytree
import tarfile
from typing import Union, Dict, List, Tuple
import sys

from docopt import docopt
import pydicom

from .pathing import pathing


def anonymize(file: Union[str, Path]) -> pydicom.dataset.FileDataset:
    """ Anonymize dicom file.

    :param Union[str, Path] file: Path to dicom file.
    :return: pydicom dataset object with anonymity.
    :example:
    >>>dataset = anonymize('~/Desktop/dicom-file')
    >>>dataset.save_as('~/Desktop/dicomt-file-anonymized')
    """
    dataset = pydicom.dcmread(str(file))
    dataset.PatientName = None
    dataset.PatientBirthDate = None
    return dataset


def make_tarfile(output_filename, source_dir):
    """ Tar folder & gzip. """
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def main():
    # Command line inputs
    args = docopt(__doc__)
    output_folder = args.get('--output_path')
    input_folder = args['INPUT_PATH']
    if not output_folder:
        output_folder = input_folder + '-anonymized'

    # Pathing sanity checks
    output_folder = pathing(output_folder, new=True)
    input_folder = pathing(input_folder, new=False)

    # Copy folder as is.
    copytree(input_folder, output_folder)

    # Anonymize copy
    for file in output_folder.rglob('*'):
        if file.suffix == '.dcm':
            dataset = anonymize(file)
            dataset.save_as(str(file))

    # Compress
    if args.get('--compress'):
        make_tarfile(
            output_filename=str(output_folder)+'.tar.gz',
            source_dir=str(output_folder)
        )


if __name__ == '__main__':
    main()
