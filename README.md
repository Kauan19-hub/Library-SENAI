**<h2>🖥️ API developed in Python and Django </h2>**

###

Feat: Initial setup with `env` virtual environment, automatic spreadsheets and organized projects! 

###

✅ Env development;<br>
✅ Installation of libraries: pandas and openpyxl for data manipulation and table creation with Excel;<br>
✅ Folder structure in Insonmia or Postman for API testing;<br>
✅ Automation scripts for generating spreadsheet readings using pandas and openpyxl;<br>
✅ File and directory organization;<br>
✅ Examples of how to use Django and JSON for API integration;<br>
✅ Documentation explaining the project.<br>

---

Spreadsheet automation using `pandas` and `openpyxl` 

###

Creation of the virtual environment: 

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

**<h2>🥇 Organization:</h2>**

###

- `planilhas/`: Has files  `.xlsx` gerados;
- `scripts/`: scripts for automations of spreadsheet;
- `api/`: Example of API with Django.

---

###

**<h2>💡 Quick tip :</h2>**

###
```python
variavel1 = diretório (link)  ## xlsx table path 
variavel2 = pd.read_csv(variavel)  ## Call the path in another variable 

print(arquivo.head()) ## Start of spreadsheet 
print(arquivo.shape()) ## Middle of the spreadsheet 
print(arquivo.dtypes()) ## End of spreadsheet 

arquivo_caminho = r'T:\ (full path of files) 
print('Currently Used Directory :', os.getcwd())   ## Remember to import the  (OS) - import os
print('This file exists?', os.path.isfile(arquivo_caminho)  ## if exist, print 'TRUE', else, 'FALSE'
```

---

Clone this repository: 

###
```powershell
git clone https://github.com/Kauan19-hub/Library-SENAI.git
```


