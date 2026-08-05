from pathlib import Path

import pandas as pd


def export_processed_data(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Exporte les données nettoyées vers un fichier Excel.

    Parameters
    ----------
    df : pd.DataFrame
        Données à exporter.

    output_path : Path
        Chemin du fichier de sortie.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_excel(
        output_path,
        index=False,
    )

    print(
        f"Dataset exporté : {output_path}"
    )