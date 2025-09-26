**<h2>🖥️ Area Project - Library</h2>**

###

✨ Feat: Initial setup with `env` virtual environment, automatic spreadsheets and organized projects! 

###

**<h2>🔗 Connection Back-End ↔ Front-End</h2>**

- The Back-End (`API`) provides data in format JSON - (Documentation);
- The Front-End consumes this data via requests `HTTP` using `fetch` or `axios`.

---

`endpoint` example:

###
```js
GET http://localhost:3000/api/livros
```

Consumes example in the Front-End

###
```js
fetch("http://localhost:3000/api/livros")
  .then(res => res.json())
  .then(data => console.log(data));
```

###

✅ Env development;<br>
✅ Installation of libraries: pandas and openpyxl for data manipulation and table creation with Excel;<br>
✅ Folder structure in Insonmia or Postman for API testing;<br>
✅ Automation scripts for generating spreadsheet readings using pandas and openpyxl;<br>
✅ File and directory organization;<br>
✅ Using Front-End and Back-End<br>
✅ Examples with Node.JS, Angular.JS and Express<br>
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

- `spreadsheets/`: Has files  `.xlsx` generated;
- `scripts/`: scripts for automations of spreadsheet;
- `api/`: Example of API with Django.

---

###

**<h2>💡 Quick tip :</h2>**

###
```python
var1 = dir (link)  ## xlsx table path 
var2 = pd.read_csv(var)  ## Call the path in another variable 

print(file.head()) ## Start of spreadsheet 
print(file.shape()) ## Middle of the spreadsheet 
print(file.dtypes()) ## End of spreadsheet 

path_file = r'T:\ (full path of files) 
print('Currently Used Directory :', os.getcwd())   ## Remember to import the  (OS) - import os
print('This file exists?', os.path.isfile(arquivo_caminho)  ## if exist, print 'TRUE', else, 'FALSE'
```

---

Clone this repository: 

###
```powershell
git clone https://github.com/Kauan19-hub/Library-SENAI.git
cd Library-SENAI
```

###

Back-End (`Node.js` + `Express`)

###
```powershell
cd backend
npm install
npm start
```

###

Front-End (`Angular` or `React`)

###
```powershell
cd frontend
npm install
npm start
```

###

API `Django` (Optional)

###
```powershell
cd api
pip install -r requirements.txt
python manage.py runserver
```

###

**<h2>📌 Versions</h2>**

###

- Python: `3.13`;
- Node.js: `node -v`;
- NPM: `npm -v`.

###

**<h2>📌 Main Dependencies:</h2>**

###

- `pandas`, `openpyxl`;
- `Django Rest Framework`;
- `Express`.

###

**Tools for Tests**: [Insomnia](https://insomnia.rest/download) and/or [Postman](https://www.postman.com/downloads/)

###

---

**<h2>🤝 Contributions**

###

Issues and contributions are welcome! Feel free to suggest improvements or contribute to the project!

---

```pgsql
   👤 User
       │
       ▼
 ┌─────────────────────────────┐
 │      Front-End (UI)         │
 │  Angular / React / HTML+CSS │
 └─────────────────────────────┘
       │   Requisition HTTP
       │  (GET, POST, PUT, DELETE)
       ▼
 ┌─────────────────────────────┐
 │    Back-End (API REST)      │
 │  Node.js + Express / Django │
 │  Endpoints: /api/livros     │
 └─────────────────────────────┘
       │    SQL Queries
       ▼
 ┌─────────────────────────────┐
 │     Data Base (DB)          │ 
 │ MySQL / PostgreSQL / SQLite │
 └─────────────────────────────┘
       ▲
       │   Datas (JSON Response)
       │
       └───────────────────────────────→ Back to Front-End
```

###

The flow of the application follows the model below: the user interacts through the Front-End, which consumes the data via API (Back-End),
responsible for processing and querying the database. The response is sent in JSON, displayed again in the interface.

---

**<h3>- Front-End</h3>**

###

<div align="left">
  <img src="https://skillicons.dev/icons?i=ts" height="30" alt="typescript logo" title="TypeScript" />
  <img width="2" />
  <img src="https://skillicons.dev/icons?i=angular" height="30" alt="angularjs logo"  title="Angular.JS" />
  <img width="2" />
  <img src="https://skillicons.dev/icons?i=tailwind" height="30" alt="tailwindcss logo" title="TailwindCSS" />
  <img width="2" />
  <img src="https://skillicons.dev/icons?i=nodejs" height="30" alt="nodejs logo" title="Node.JS"  />
  <img width="2" />
  <img src="https://skillicons.dev/icons?i=html" height="30" alt="html5 logo" title="HTML5"  />
  <img width="2" />
  <img src="https://skillicons.dev/icons?i=css" height="30" alt="css logo" title="CSS3" />
  <img width="2" />
  <img src="https://skillicons.dev/icons?i=react" height="30" alt="react logo" title="React" />
</div>

###

**<h3>- Back-End</h3>**

###

<div align="left">
  <img src="https://skillicons.dev/icons?i=py" height="30" alt="python logo"  title="Python" />
  <img width="2" />
  <img src="https://skillicons.dev/icons?i=django" height="30" alt="django logo" title="Django" />
  <img width="2" />
  <img src="https://skillicons.dev/icons?i=mysql" height="30" alt="mysql logo" title="MySQL | SQL"  />
</div>

###

**<h3>- Tools</h3>**

###

<div align="left">
  <img src="https://skillicons.dev/icons?i=vscode" height="30" alt="vscode logo" title="Visual Studio Code"  />
  <img width="2" />
  <img src="https://skillicons.dev/icons?i=git" height="30" alt="git logo" title="Git" />
  <img width="2" />
  <img src="https://skillicons.dev/icons?i=github" height="30" alt="github logo" title="GitHub" />
  <img width="2" />
  <img src="https://skillicons.dev/icons?i=postman" height="30" alt="postman logo" title="Postman" />
</div>







