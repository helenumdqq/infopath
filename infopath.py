import os
import subprocess
import argparse

def zip_files(source, destination):
    """Zips the source folder into the destination archive."""
    if not os.path.exists(source):
        raise FileNotFoundError(f"The source path {source} does not exist.")
    
    if not destination.endswith(".zip"):
        destination += ".zip"

    command = f'powershell Compress-Archive -Path "{source}" -DestinationPath "{destination}"'
    subprocess.run(command, shell=True, check=True)
    print(f"Files from {source} have been zipped to {destination}")

def unzip_files(source, destination):
    """Unzips the source archive into the destination folder."""
    if not os.path.exists(source):
        raise FileNotFoundError(f"The source archive {source} does not exist.")
    
    if not source.endswith(".zip"):
        raise ValueError("The source file must be a .zip archive.")

    if not os.path.exists(destination):
        os.makedirs(destination)

    command = f'powershell Expand-Archive -Path "{source}" -DestinationPath "{destination}"'
    subprocess.run(command, shell=True, check=True)
    print(f"Files from {source} have been unzipped to {destination}")

def main():
    parser = argparse.ArgumentParser(description='Simplifies the zipping and unzipping of files using native Windows capabilities.')
    
    parser.add_argument('action', choices=['zip', 'unzip'], help='Action to perform: zip or unzip')
    parser.add_argument('source', help='Source file or directory')
    parser.add_argument('destination', help='Destination file or directory')

    args = parser.parse_args()

    if args.action == 'zip':
        zip_files(args.source, args.destination)
    elif args.action == 'unzip':
        unzip_files(args.source, args.destination)

if __name__ == "__main__":
    main()