import pandas as pd
import json
import argparse

FILENAME = "result.csv"
OUT_FILE = "data.js"
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
    "lat",
    "long",
]


def main(args):

    data = pd.read_csv(args.input_file, encoding="utf8")
    data = data[columns]
    data.set_index("Nome")
    data = data.sample(frac=args.sample_fraction)
    data = data.to_dict("records")

    js_code = f"""var data = {json.dumps(data, indent=4, ensure_ascii=False)};\n"""

    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(js_code)

    print(f"{OUT_FILE} created.")


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Script to generate data.js file")
    argparser.add_argument(
        "-in", "--input_file", type=str, default=FILENAME, help=".csv input file"
    )
    argparser.add_argument(
        "-out", "--output_file", type=str, default=OUT_FILE, help=".js output file name"
    )
    argparser.add_argument(
        "-s", "--sample_fraction", type=float, default=1, help="Sample fraction"
    )
    args = argparser.parse_args()

    main(args)
