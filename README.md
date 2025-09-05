**<h2>🖥️ API desenvolvida em Python e Django</h2>**

###

Feat: Setup inicial com ambiente virtual `env`, planilhas automáticas e projetos organizados!

###

✅ Desenvolvimento da `env`;<br>
✅ Instalaçao de bibliotecas: `pandas` e `openpyxl` para manipulação de dados e criação de tabelas com Excel;<br>
✅ Estrutura de pastas no Insonmia ou Postman para testes de API;<br>
✅ Scripts voltados para automação com objetivo de gerar leituras de planilhas pelo `pandas` + `openpyxl`;<br>
✅ Organização de arquivos e diretórios;<br>
✅ Exemplos de como usar o `Django` e o `JSON` para integração com APIs;<br>
✅ Documentação explicando sobre o projeto.

---

Automação de plailhas usando o `pandas` e `openpyxl`

###

Criação do ambiente virtual:

###
```powershell
python -m venv env
```

###
```powershell
source env/bin/activate ## MacOS/Linux
```
###
```powershell
.\env\Scripts\activate ## Windows
```

---

**<h2>🥇 Organização:</h2>**

###

- `planilhas/`: Possui arquivos `.xlsx` gerados;
- `scripts/`: scripts para automação de planilhas;
- `api/`: Exemplo de API com Django.

---

###

**<h2>💡 Dica rápida:</h2>**

###
```python
variavel1 = diretório (link)  ## Caminho da tabela xlsx
variavel2 = pd.read_csv(variavel)  ## Chama o caminho em uma outra variável

print(arquivo.head()) ## Início da planilha
print(arquivo.shape()) ## Meio da planilha
print(arquivo.dtypes()) ## Final da planilha

arquivo_caminho = r'T:\ (caminho completo dos arquivos)
print('Diretório Usado Atualmente:', os.getcwd())   ## Lembre-se de importar o (OS) - import os
print('Esse arquivo existe?', os.path.isfile(arquivo_caminho)  ## Se existir, imprime 'TRUE', senão, 'FALSE'
```

---

Clone este repositório:

###
```powershell
git clone https://github.com/Kauan19-hub/Library-SENAI.git
```


