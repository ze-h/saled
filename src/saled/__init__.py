import os
import tomllib

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', '..', 'pyproject.toml')
file_path = os.path.abspath(file_path)
with open(file_path, 'r') as file:
    content = file.read()
_pyproj = tomllib.loads(content)

__version__ = _pyproj["tool"]["poetry"]["version"]
