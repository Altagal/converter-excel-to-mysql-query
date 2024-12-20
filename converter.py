import os, sys
import pandas as pd
import pyperclip

# TIPOS DE ARQUIVOS PERMITIDOS
allowed_file_types = ['xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']

# NOME DO ARQUIVO A SER PROCURADO NA MESMA PASTA ONDE O converter.py ESTA LOCALIZADO
file_name = input("Nome do arquivo: ")
file = False
for file_item in os.listdir():
    if file_item.split(".")[0] == file_name and file_item.split(".")[-1] in allowed_file_types:
        file = file_item
        break

# SE O ARQUIVO NAO FOR ENCONTRADO, ENCERRA PROGRAMA
if not file:
    print("Não foram encontrados arquivos comptaiveis com o conversor na pasta expecificada.")
    sys.exit()


df = pd.read_excel(file, sheet_name=0)

# NOME DA TABELA, SE FOR VAZIO OU SO ESPAÇOS, ENCERRA PROGRAMA
table_name = input("Nome da tabela: ")
print()

if not table_name or table_name.isspace():
    print("Sem o nome da tabela não é possivel realizar a conversão.")
    sys.exit()


# INICIA A QUERY
query = ""
for row in df.values:
    # NOME DA TABELA
    query += f"INSERT INTO {table_name} ("
    
    # NOME DAS COLUNAS
    first_loop = True
    for col in df.columns:
        if not first_loop:
            query += f", {col}"
        else:
            first_loop = False
            query += f"{col}"
    # VALUE
    query += f") VALUES ("

    # VALORES DOS CAMPOS
    first_loop = True
    for value in row:
        if not first_loop:
            query += f", {value}"
        else:
            first_loop = False
            query += f"{value}"

    # FECHAMENTO DA QUERY
    query += f");\n"
    
print(query)

pyperclip.copy(query)
print("Query mysql copiada para a área de transferencia.")

want_file = input("Importar query gerada para um arquivo de texto? [Y/N]: ")
if want_file == "Y" or want_file == "y":
    with open(file_name + "_querys.txt", "w") as arquivo:
        arquivo.write(query)
    print(f"Query salva no arquivo {file_name}_querys.txt.")
