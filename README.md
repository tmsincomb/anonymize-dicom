# anonymize-dicom
Wish to share your dicom files to collaborators, but you don't want to break HIPAA? Well this is the tool for you! This will create a copy of a folder and strip and HIPAA related meta data from the dicom files! Specifically it removes patients name and date of birth from the headers.


# Requirements
```
python==3.7+
pydicom==1.4.2+
docopt==0.6.2+
```

# Installation
```markdown
$ git clone git@github.com:tmsincomb/anonymize-dicom.git
$ pip3 install -e ./anonymize-dicom
```

# Simple Guide : Anonymize & Compress
Copy folder, anonymize each dicom file and then compress the copied folder into a tar.gz file. Default output folder is "output_folder + '-anonymized" in the same directory. Same for the compressed output.
```bash
$ anonymize-dicom -c dicom-folder
$ ls
dicom-folder dicom-folder-anonymized dicom-folder-anonymized.tar.gz
```

# Complete Guide
```markdown
Anonymize dicom files

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

Import Example:
    from anonymize_dicom import anonymize
    anonymized_dicom_file = anonymize(dicom_file)
```


# Thoughts
Please feel free to use this as a reference in how to read/modifiy dicom datasets using pydicom.
