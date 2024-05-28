from pathlib import Path
import os

print(Path.cwd())
# Diz se o caminho é absoluto
print(Path.cwd().is_absolute())

print(os.path.abspath('.'))

# Extrair partes do arquivo
p = Path("c:/aulas/python/scripts.py")
print(p.anchor)
print(p.drive)
print(p.parent)
print(p.stem)
print(p.suffix)
print(p.parents)
