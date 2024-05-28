from pathlib import Path
import os

print(Path.cwd())
# Diz se o caminho é absoluto
print(Path.cwd().is_absolute())

print(os.path.abspath('.'))
