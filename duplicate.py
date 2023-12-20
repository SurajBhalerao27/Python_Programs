import os
import hashlib
import ctypes
import string

def get_file_hash(file_path):
    """
    Calculate the hash value of a file.
    """
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as file:
            buffer = file.read(65536)  # Read the file in chunks of 64KB
            while len(buffer) > 0:
                hasher.update(buffer)
                buffer = file.read(65536)
    except (IOError, OSError):
        return None

    return hasher.hexdigest()

def scan_directory(directory):
    """
    Scan the given directory and identify duplicate files.
    """
    file_dict = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = get_file_hash(file_path)
            if file_hash is not None:
                if file_hash in file_dict:
                    file_dict[file_hash].append(file_path)
                else:
                    file_dict[file_hash] = [file_path]
    return file_dict

def remove_duplicates(file_dict, delete_duplicates):
    """
    Remove duplicate files based on the provided dictionary.
    """
    total_duplicates = 0
    for file_hash, file_paths in file_dict.items():
        if len(file_paths) > 1:
            total_duplicates += 1
            print(f"Duplicate Files ({file_hash}):")
            for i, file_path in enumerate(file_paths):
                print(f"{i + 1}. {file_path}")
            if delete_duplicates:
                for i in range(1, len(file_paths)):
                    print(f"Deleting {file_paths[i]}")
                    os.remove(file_paths[i])
                    print("Deleted.")
                print()
            else:
                print("Choose the file to keep (enter number or 0 to keep all):")
                choice = input("> ")
                if choice == '0':
                    continue
                else:
                    choice = int(choice)
                    for i in range(1, len(file_paths)):
                        if i != choice:
                            print(f"Deleting {file_paths[i]}")
                            os.remove(file_paths[i])
                            print("Deleted.")
                    print()

    print(f"Total duplicate files found: {total_duplicates}")

if __name__ == '__main__':
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    delete_duplicates = False  # Set to True to delete duplicates

    for drive in drives:
        directory_to_scan = drive + ":\\"
        print(f"Scanning directory: {directory_to_scan}\n")
        file_dict = scan_directory(directory_to_scan)
        remove_duplicates(file_dict, delete_duplicates)
