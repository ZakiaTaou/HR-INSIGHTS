import pandas as pd
SCALE_ORDER = [
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "EXP",
]

STEP_ORDER = [str(i) for i in range(1, 14)]

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

    return df.shape[0]

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


def get_grade_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Retourne la répartition des fonctionnaires par grade.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.Series
        Nombre de fonctionnaires par grade.
    """

    return (
        df["grade"]
        .value_counts()
        .sort_values(ascending=False)
    )


def get_scale_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Retourne la répartition des fonctionnaires par échelle.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.Series
        Nombre de fonctionnaires par échelle.
    """

    scale_distribution = (
        df["echelle"]
        .astype(str)
        .value_counts()
    )


    return scale_distribution.reindex(SCALE_ORDER, fill_value=0)



def get_step_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Retourne la répartition des fonctionnaires par échelon.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.Series
        Nombre de fonctionnaires par échelon.
    """

    step_distribution = (
        df["echelon"]
        .astype(str)
        .value_counts()
    )

    return step_distribution.reindex(STEP_ORDER, fill_value=0)

def get_retirements_within_years(
    df: pd.DataFrame,
    years: int
) -> pd.DataFrame:
    """
    Retourne les fonctionnaires qui partiront à la retraite
    dans un nombre d'années donné.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    years : int
        Nombre d'années.

    Returns
    -------
    pd.DataFrame
        Fonctionnaires concernés.
    """
    columns = [
        "nom_prenom",
        "grade",
        "sexe",
        "echelle",
        "echelon",
        "age",
        "anciennete",
        "date_retraite",
        "annees_avant_retraite",
    ]

    return (
        df.loc[df["annees_avant_retraite"] <= years, columns]
          .sort_values("date_retraite")
          .reset_index(drop=True)
    )

def get_retirement_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Retourne un tableau de synthèse des départs à la retraite
    selon plusieurs horizons temporels.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les données RH.

    Returns
    -------
    pd.DataFrame
        Tableau récapitulatif.
    """

    horizons = [1, 3, 5, 10]

    summary = []

    for years in horizons:
        count = (df["annees_avant_retraite"] <= years).sum()

        summary.append(
            {
                "Horizon": f"≤ {years} an(s)",
                "Nombre de départs": count,
            }
        )

    return pd.DataFrame(summary)

def get_retirement_by_grade(
    df: pd.DataFrame,
    years: int
) -> pd.Series:
    """
    Retourne les départs à la retraite par grade.

    Parameters
    ----------
    df : pd.DataFrame
        Données RH.

    years : int
        Horizon en années.

    Returns
    -------
    pd.Series
        Nombre de départs par grade.
    """

    return (
        df[df["annees_avant_retraite"] <= years]
        ["grade"]
        .value_counts()
        .sort_values(ascending=False)
    )

def get_retirement_by_gender(
    df: pd.DataFrame,
    years: int
) -> pd.Series:
    """
    Retourne les départs à la retraite par sexe.
    """

    return (
        df[df["annees_avant_retraite"] <= years]
        ["sexe"]
        .value_counts()
    )

def get_retirement_by_scale(
    df: pd.DataFrame,
    years: int
) -> pd.Series:
    """
    Retourne les départs à la retraite par échelle.
    """

    scale_distribution = (
        df[df["annees_avant_retraite"] <= years]
        ["echelle"]
        .astype(str)
        .value_counts()
    )

    order = ["6", "7", "8", "9", "10", "11", "EXP"]

    return scale_distribution.reindex(order, fill_value=0)