# converter-excel-to-mysql-query

**converter-excel-to-mysql-query** é uma ferramenta desenvolvida em Python para converter arquivos Excel (.xlsx) em queries SQL compatíveis com MySQL. Este projeto foi criado para facilitar a migração de dados de planilhas para bancos de dados MySQL, gerando automaticamente comandos de inserção (INSERT).

O conversor é compativel com os seguintes tipos de arquivos: 
- `.xls`
- `.xlsx`
- `.xlsm`
- `.xlsb`
- `.odf`
- `.ods`
- `.odt`

## Requisitos

Certifique-se de ter Python 3.7 ou superior instalado em seu sistema. As seguintes bibliotecas Python são necessárias para executar o projeto:


- `pandas`
- `pyperclip`


## Como Usar

1. Certifique-se de que o arquivo Excel que você deseja converter esteja nos formatos permitidos e esteja localizado na mesma pasta em que converter.py.
2. Execute o script principal do projeto:
   ```bash
   python converter.py
   ```
3. Siga as instruções fornecidas no terminal para selecionar o arquivo Excel e gerar as queries MySQL.
4. As queries geradas serão copiadas diretamente para a área de transferência.
