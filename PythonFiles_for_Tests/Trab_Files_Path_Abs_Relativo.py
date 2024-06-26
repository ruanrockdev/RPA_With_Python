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
# Nome do Arquivo sem a extensão
print(p.stem)
# Nome da extensão do arquivo
print(p.suffix)
# Nome do caminho inteiro em um array
print(p.parents)

# Nome do arquivo com extenção:
file = "c:\\users\\prof\\exercicio.py"
print(os.path.basename(file))

# Retorna o diretório do arquivo
print(os.path.dirname(file))

# retornar uma tupla com 1 elemento é o caminho e o 2 é o nome com extensão do arquivo
print(os.path.split(file))
