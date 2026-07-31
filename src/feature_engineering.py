import pandas as pd


def calculate_age(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcule l'âge des employés à partir de leur date de naissance.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.DataFrame
        DataFrame avec une nouvelle colonne 'age'.
    """

    today = pd.Timestamp.today()

    df["age"] = (
        (today - df["date_naissance"])
        .dt.days // 365
    )

    return df

def calculate_seniority(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcule l'ancienneté des employés.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.DataFrame
        DataFrame avec une nouvelle colonne 'anciennete'.
    """

    today = pd.Timestamp.today()

    df["anciennete"] = (
        (today - df["date_recrutement"]).dt.days // 365
    )

    return df

def extract_recruitment_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extrait l'année de recrutement.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.DataFrame
        DataFrame avec une nouvelle colonne 'annee_recrutement'.
    """

    df["annee_recrutement"] = df["date_recrutement"].dt.year

    return df

def extract_retirement_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extrait l'année de départ à la retraite.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.DataFrame
        DataFrame avec une nouvelle colonne 'annee_retraite'.
    """

    df["annee_retraite"] = df["date_retraite"].dt.year

    return df

def years_until_retirement(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcule le nombre d'années restantes avant la retraite.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.DataFrame
        DataFrame avec une nouvelle colonne 'annees_avant_retraite'.
    """

    current_year = pd.Timestamp.today().year

    df["annees_avant_retraite"] = (
        df["annee_retraite"] - current_year
    )

    return df


def apply_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applique toutes les étapes de Feature Engineering.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.DataFrame
        DataFrame enrichi avec les nouvelles variables.
    """

    df = calculate_age(df)
    df = calculate_seniority(df)
    df = extract_recruitment_year(df)
    df = extract_retirement_year(df)
    df = years_until_retirement(df)

    return df