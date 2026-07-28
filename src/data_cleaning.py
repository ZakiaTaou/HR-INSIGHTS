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
                  .str.replace(' ', '_')  # Remplace les espaces par des underscores
                  .str.lower())  # Convertit les noms de colonnes en minuscules
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

