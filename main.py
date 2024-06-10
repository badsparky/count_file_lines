import os

target_dir = r""
target_extension = ".py"

def get_filesInDir(directory):
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))
        for dirname in dirnames:
            files.extend(get_filesInDir(dirname))
    return files


files=[file for file in get_filesInDir(target_dir) if file.endswith(target_extension)]
total_count=0

for file in files:
    try:
        with open(file, 'r', encoding="utf-8") as f:
            total_count += sum([1 for line in f])
    except UnicodeDecodeError:
        print(f"Could not decode file {file} in utf-8. Skipping this file.")

print(f"lines in the directory that has extension {target_extension} ", total_count)        