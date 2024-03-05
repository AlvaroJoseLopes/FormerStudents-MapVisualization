import pandas as pd
import json
import argparse
from utils.parse_kml import parse_kml

CSV_FILE = "data/egressos.csv"
KML_FILE = "data/egressos.kml"
OUT_FILE = "visualization/data.js"
RESULT_FILE = "data/result.csv"
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
    coords_df = parse_kml(args.kml_file)
    info_df = pd.read_csv(args.csv_file, encoding="utf8")
    # Merging former student info with coordinates
    df_result = pd.merge(coords_df, info_df, how="inner", on="Nome")

    if args.save:
        df_result.to_csv(RESULT_FILE, index=False)

    df_result = df_result[columns]
    df_result.set_index("Nome")
    df_result = df_result.sample(frac=args.sample_fraction)
    df_result = df_result.to_dict("records")

    js_code = f"""var data = {json.dumps(df_result, indent=4, ensure_ascii=False)};\n"""

    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(js_code)

    print(f"{OUT_FILE} created.")


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Script to generate data.js file")
    argparser.add_argument(
        "-csv", "--csv_file", type=str, default=CSV_FILE, help=".csv input file"
    )
    argparser.add_argument(
        "-kml", "--kml_file", type=str, default=KML_FILE, help=".kml input file"
    )
    argparser.add_argument(
        "-out", "--output_file", type=str, default=OUT_FILE, help=".js output file name"
    )
    argparser.add_argument(
        "-s", "--sample_fraction", type=float, default=1, help="Sample fraction"
    )
    argparser.add_argument(
        "-save",
        "--save",
        action="store_true",
        help="save merged file as data/result.csv",
    )
    args = argparser.parse_args()

    main(args)
