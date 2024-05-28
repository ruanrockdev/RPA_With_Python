import os
from pathlib import Path

# Validando se diretório existe para apagar e não dar erro no comando de criar da linha 14
d = "c:/teste/makedir"
if os.path.exists(d):
    print("O Diretório existe e será apagado")
    os.rmdir(d)
else:
    print("O Diretório não existe")

# Criando todas as pastas
os.makedirs("c:/teste/makedir")

# Listando os arquivos da pasta, se não direcionar ele irá buscar na pasta atual
print(os.listdir())

# obtendo o tamanho do arquivo da pasta padrão
print(os.path.getsize("README.md"))

# Buscar por arquivo na pasta
p = Path()
for filename in p.glob("*.md"):
    print(filename)
