import pandas as pd
from pykml import parser
import pandas as pd

"""
    Parses .kml exported file and extracts the latitude and longitude
    Also, generates a final file (result.csv) with all the data for each person 
"""


FILENAME = "egressos.kml"
CSV_FILE = "egressos.csv"


def parse_kml(kml_file: str) -> pd.DataFrame:

    with open(kml_file) as f:
        doc = parser.parse(f).getroot()

    coords_info = {}
    for e in doc.Document.Folder.Placemark:
        lat, long, _ = e.Point.coordinates.text.split(",")
        name = e.name.text
        coords_info[name] = {
            "lat": lat,
            "long": long,
        }

    coords_df = pd.DataFrame.from_dict(coords_info, orient="index")
    coords_df = pd.DataFrame(
        data={
            "Nome": coords_df.index,
            "lat": coords_df["lat"],
            "long": coords_df["long"],
        }
    )
    return coords_df
