# Python 3.6 or higher
# Grab the library
from pathlib import Path

# Where am I?
cwd = Path.cwd()
print(cwd)

# Combine parts to create path
new_file = Path.joinpath(cwd, 'new_file.txt')
print(new_file)

# Does this exist?
print(new_file.exists())