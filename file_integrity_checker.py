import os
import hashlib
import json

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while True:
                data = f.read(65536)
                if not data:
                    break
                sha256_hash.update(data)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Could not read '{file_path}' — Error: {e}")
        return None

def scan_directory(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            rel_path = os.path.relpath(file_path, directory)
            hash_val = calculate_sha256(file_path)
            if hash_val:
                file_hashes[rel_path] = hash_val
                print(f"File: {rel_path}\n    SHA-256: {hash_val}\n")
    return file_hashes

def compare_hashes(old, new):
    modified = [f for f in new if f in old and new[f] != old[f]]
    added = [f for f in new if f not in old]
    deleted = [f for f in old if f not in new]
    return modified, added, deleted

def main():
    directory = input("Enter the directory path to check integrity: ").strip()
    if not os.path.isdir(directory):
        print(f" ! Directory '{directory}' does not exist.")
        return

    hash_file = 'hashes.json'
    print("\nScanning files and calculating hashes...\n")
    new_hashes = scan_directory(directory)

    if not os.path.exists(hash_file):
        with open(hash_file, 'w') as f:
            json.dump(new_hashes, f, indent=2)
        print("Initial hash snapshot saved.")
    else:
        with open(hash_file, 'r') as f:
            old_hashes = json.load(f)

        modified, added, deleted = compare_hashes(old_hashes, new_hashes)

        print("\n=== Integrity Check Report ===")
        print(f"Modified files: {modified or 'None'}")
        print(f"Added files: {added or 'None'}")
        print(f"Deleted files: {deleted or 'None'}")

        update = input("\nUpdate saved hashes with current scan? (y/n): ").strip().lower()
        if update == 'y':
            with open(hash_file, 'w') as f:
                json.dump(new_hashes, f, indent=2)
            print("Hashes updated.")

if __name__ == "__main__":
    main()
