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

**<h2>📁 Estrutura de pastas:</h2>**

###
```powershell
/projeto/
│
├── env/                     
├── planilhas/              
├── scripts/                 
│   ├── gerar_planilha.py
│   └── ler_dados.py
├── api/                    
│   ├── models.py
│   ├── views.py
│   └── serializers.py
├── insomnia/                
│   └── collection.json
├── README.md                
└── requirements.txt        
```

###

**<h2>🗃️ Como testar a API?</h2>**

###

Automação de plailhas usando o `pandas` e `openpyxl`

###

1️⃣- Criação do ambiente virtual:

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

###

2️⃣- Instale as dependências:

###
```powershell
pip install pandas openpyxl
```

###

3️⃣- Rode os scripts em `scripts/` para exibir ou ler planilhas;<br>

4️⃣- Teste sua API utilizando:

###

<div align="left">
  <a href="https://www.postman.com/downloads" />
  <img src="https://img.shields.io/badge/Postman-FF6C37?logo=postman&logoColor=black&style=for-the-badge" height="25" alt="postman logo" title="Baixe o Postman e teste sua API!" />
  <img width="1" />
  <a href="https://insomnia.rest/download" />
  <img src="https://img.shields.io/badge/insomnia-5E00D3?logo=insomnia&logoColor=white&style=for-the-badge" height="25" alt="insomnia logo" title="Baixe o Insomnia e teste sua API!"  />
</div>

###

> 💡 Caso prefira, utilize apenas uma das duas ferramentas.

---

**<h2>⚙️ Ferramentas usadas:</h2>**

###

- Pandas;
- Openpyxl;
- Insomnia/Postman;
- Django;
- Python;
- JSON;
- GitHub.

###

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

**<h2>🤔 Como rodar o projeto?</h2>**

###

Clone este repositório:

###
```bash
git clone (nome_do_arquivo)
```

###

<h3>👋 Muito obrigado! Espero que goste!</h3>


