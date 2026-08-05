# Pandas permet de lire et manipuler des données tabulaires (Excel, CSV, SQL...)
import pandas as pd
# la classe Path permet de manipuler les chemins de fichiers de manière fiable
from pathlib import Path
# fonction reçoit le chemin d'un fichier Excel  et retourne son contenu sous forme de DataFrame Pandas.

def load_excel(file_path: str | Path) -> pd.DataFrame:
    """
    Charge un fichier Excel.

    Parameters
    ----------
    file_path : str | Path
        Chemin du fichier Excel.

    Returns
    -------
    pd.DataFrame
        Données chargées.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Le fichier '{file_path}' est introuvable."
        )

    return pd.read_excel(file_path)