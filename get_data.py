import pandas as pd
import json

FILENAME = 'tracking.csv'
OUT_FILE = 'data.js'
columns = [
    'Nome',
    'Curso',
    'Sexo',
    'Último orientador',
    'ANO DEFESA',
    'SetorNivel1',
    'SetorNivel2', 
    'Abrangencia', 
    'Tracking Egresso - Ocupacao'
]

data = pd.read_csv(FILENAME, encoding='utf8')
data = data[columns]
data.set_index('Nome')
data = data.sample(10).to_dict('records')

js_code = f'''var data = {json.dumps(data, indent=4, ensure_ascii=False)};\n'''

with open(OUT_FILE, 'w', encoding='utf-8') as f:
    f.write(js_code)

print(f'{OUT_FILE} created.')
