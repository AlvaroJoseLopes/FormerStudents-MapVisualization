import pandas as pd

import re
from collections import defaultdict

FILENAME = "data/egressos_ccmc_ateh_2022_com_endereco.xlsx"
OUT_FILE = "data/egressos.csv"
columns = [
    "Nome",
    "Curso",
    "Sexo",
    "Último orientador",
    "ANO DEFESA",
    "SetorNivel1",
    "SetorNivel2",
    "Abrangencia",
    "Tracking Egresso - Ocupacao",
    "endereco_normalizado",
]

data = pd.read_excel(FILENAME)
data.set_index("Nome")
data = data.dropna(subset=["Nome", columns[-1]])

person_info = defaultdict(dict)
for _, row in data.iterrows():
    name = row["Nome"]
    address = row["endereco_normalizado"]
    for column in columns[1:-1]:
        person_info[name][column] = row[column]

    # Parseando endereço normalizado
    itens = address.split("\n")
    for item in itens:
        match = re.match(r"(\w+):\s(.+)", item)
        if match:
            field = match.group(1)
            value = match.group(2)
            if value not in ["Not specified", "Not provided", "N/A", "Not mentioned"]:
                person_info[name][field] = value

df = pd.DataFrame.from_dict(person_info, orient="index")

df["Nome"] = df.index
df.to_csv(OUT_FILE, index=False)
print(f"Successfully created file {OUT_FILE}")
