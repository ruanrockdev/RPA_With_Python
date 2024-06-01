# Testando chamar outro arquivo de outro lugar, como o arquivo está nessa mesma pasta, basta especificar o nome do arquivo

# Método Simples
# with open("inputOneLine.py", encoding="utf-8") as file:
#     code = file.read()
#     exec(code)

# Método mais robusto:
import os

caminho = os.path.join(os.path.dirname(__file__),
                       'exemplo.py')

with open(caminho, encoding="utf-8") as f:
    code = f.read()
    exec(code)
