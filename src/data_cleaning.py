import pandas as pd
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie les noms des colonnes.
    - Supprime les espaces au début et à la fin.
    - Convertit les noms de colonnes en minuscules. 
    - Remplace les espaces par des underscores.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame à nettoyer.

    Returns
    -------
    pd.DataFrame
        DataFrame avec des noms de colonnes normalisés.
    """
    df.columns = (df.columns
                  .str.strip()  # Supprime les espaces au début et à la fin
                  .str.replace(r"\s+", "_", regex=True)  # Remplace les espaces par des underscores
                  .str.lower())  # Convertit les noms de colonnes en minuscules
    # Renommage métier
    column_mapping = {
        "n": "id",
        "p.p.r.": "ppr",
        "matricule": "matricule",
        "noms_et_prénoms": "nom_prenom",
        "date_de_naissances": "date_naissance",
        "date_de_recrutement": "date_recrutement",
        "date_de_mise_à_la_retraite": "date_retraite",
        "sexe": "sexe",
        "c.i.n.": "cin",
        "date_de_titularisation": "date_titularisation",
        "n°_affiliation_à_la_c.m.r": "numero_affiliation_cmr",
        "date_d'affiliation_à_la_c.m.r.": "date_affiliation_cmr",
        "grade": "grade",
        "echelle": "echelle",
        "echellon": "echelon",
        "indice": "indice",
        "date_d'échelon": "date_echelon",
        "n°_d'arrêté": "numero_arrete",
        "date_d'arrêté": "date_arrete",
        "date_de_grade": "date_grade",
        "observations": "observations",
        "unnamed:_21": "unnamed_21",
        "@": "at",
        "statut": "statut",
    }

    df = df.rename(columns=column_mapping)
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Supprime les doublons dans le DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame à nettoyer.

    Returns
    -------
    pd.DataFrame
        DataFrame sans doublons.
    """
    return df.drop_duplicates() 

def drop_unused_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Supprime les colonnes qui ne sont pas utiles
    pour les analyses RH.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame à nettoyer.

    Returns
    -------
    pd.DataFrame
        DataFrame sans les colonnes inutiles.
    """

    columns_to_drop = [
        "Observations",
        "Unnamed: 21",
        "@",
        "Statut",
    ]

    # Supprime uniquement les colonnes qui existent
    df = df.drop(columns=columns_to_drop, errors="ignore")

    return df

def convert_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convertit les colonnes de dates en format datetime.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame à nettoyer.
    
    Returns
    -------
    pd.DataFrame
        DataFrame avec les colonnes de dates converties.
    """
    date_columns = [
        "Date de titularisation ",
        "Date d'affiliation à la C.M.R.",
        "Date d'échelon ",
    ]
    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    return df

