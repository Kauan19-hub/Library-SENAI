import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Editoras

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/autores.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")
        
    @transaction.atomic
    def handle(self, *a, **o):
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]
        # normaliza os nomes das colunas: tira espaços extras, deixa em minúsculo e remove o ufeff
        # o \ufeff é um caractere especial invisível
        
        if o["truncate"]: Editoras.objects.all().delete()
        
        df['nome'] = df['nome'].astype(str).str.strip()
        df['cnpj'] = df['cnpj'].astype(str).str.strip()
        df['endereco'] = pd.to_datetime(df["endereco"], errors="coerce", format="%Y-%m-%d").dt.date
        df['email'] = df.get('email',"").astype(str).str.strip()
        df['site'] = df.get('site',"").astype(str).str.strip()
        df['telefone'] = df.get('telefone',"").astype(str).str.strip()

        
        if o["update"]:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
                _, created = Editoras.objects.update_or_create(
                    nome = r.nome, cnpj = r.cnpj, endereco = r.endereco,
                    telefone = r.telefone, email = r.email, site = r.site,  

                )
                
                criados += int(created)
                atualizados += int(not created)
            self.stdout.write(self.style.SUCCESS(f'Criados: {criados} | Atualizados: {atualizados}'))
        else:
            objs = [Editoras(
                    nome = r.nome, cnpj = r.cnpj, endereco = r.endereco,
                    telefone = r.telefone, email = r.email, site = r.site,  
            ) for r in df.itertuples(index=False)
            ]
            
            self.stdout.write(self.style.SUCCESS(f'Criadodos: {len(objs)}'))
                
        # autor,s_autor,nasc,nacio
        