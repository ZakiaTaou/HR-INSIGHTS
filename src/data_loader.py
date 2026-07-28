# Pandas permet de lire et manipuler des données tabulaires (Excel, CSV, SQL...)
import pandas as pd
# la classe Path permet de manipuler les chemins de fichiers de manière fiable
from pathlib import Path
# fonction reçoit le chemin d'un fichier Excel  et retourne son contenu sous forme de DataFrame Pandas.

def load_excel(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        # Si le fichier n'existe pas, on arrête le programme
        # en générant une erreur explicite.
        raise FileNotFoundError(
            f"Le fichier '{file_path}' est introuvable."
        )
    # Si le fichier existe, Pandas le lit
    # puis retourne les données sous forme de DataFrame.
    return pd.read_excel(file_path)