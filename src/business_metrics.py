import pandas as pd


def get_total_employees(df: pd.DataFrame) -> int:
    """
    Retourne le nombre total de fonctionnaires.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    int
        Nombre total de fonctionnaires.
    """

    return len(df)

def get_gender_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Retourne la répartition des fonctionnaires par sexe.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.Series
        Nombre de fonctionnaires par sexe.
    """

    return df["sexe"].value_counts()

def get_gender_percentage(df: pd.DataFrame) -> pd.Series:
    """
    Retourne le pourcentage de fonctionnaires par sexe.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.Series
        Pourcentage des fonctionnaires par sexe.
    """

    return (
        df["sexe"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )

def get_average_age(df: pd.DataFrame) -> float:
    """
    Calcule l'âge moyen des fonctionnaires.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    float
        Âge moyen des fonctionnaires.
    """

    return round(df["age"].mean(), 1)


def get_average_seniority(df: pd.DataFrame) -> float:
    """
    Calcule l'ancienneté moyenne des fonctionnaires.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    float
        Ancienneté moyenne des fonctionnaires.
    """

    return round(df["anciennete"].mean(), 1)