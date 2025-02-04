# InfoPath

InfoPath is a Python program designed to simplify the process of zipping and unzipping files using native Windows capabilities. It leverages PowerShell to manage compressed files efficiently, providing a straightforward command-line interface for users.

## Features

- **Zip Files**: Compress a directory into a zip archive.
- **Unzip Files**: Extract a zip archive into a directory.

## Requirements

- Windows operating system
- Python 3.x
- PowerShell

## Installation

1. Clone the repository or download the `infopath.py` file.
2. Ensure Python and PowerShell are installed on your system.

## Usage

Run InfoPath from the command line using the following syntax:

### Zipping Files

```bash
python infopath.py zip <source_directory> <destination_archive>
```

- `<source_directory>`: Path to the directory you want to compress.
- `<destination_archive>`: Path where the zip file will be saved. (Add `.zip` if not included.)

### Unzipping Files

```bash
python infopath.py unzip <source_archive> <destination_directory>
```

- `<source_archive>`: Path to the zip file you want to extract.
- `<destination_directory>`: Path where files will be extracted.

### Examples

1. **Zip a Folder**

   ```bash
   python infopath.py zip C:\MyFiles C:\MyArchive.zip
   ```

2. **Unzip an Archive**

   ```bash
   python infopath.py unzip C:\MyArchive.zip C:\ExtractedFiles
   ```

## License

This project is licensed under the MIT License.