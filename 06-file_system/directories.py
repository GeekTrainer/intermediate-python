from pathlib import Path
cwd = Path.cwd()

# Get the parent directory
parent = cwd.parent

# Is this a directory?
print(parent.is_dir())

# Is this a file?
print(parent.is_file())

# List child directories
for child in parent.iterdir():
    if child.is_dir():
        print(child)
