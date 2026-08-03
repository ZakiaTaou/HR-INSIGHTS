import plotly.express as px
import pandas as pd


def create_gender_pie_chart(df: pd.DataFrame):
    """
    Crée un graphique circulaire représentant
    la répartition des fonctionnaires par sexe.

    Parameters
    ----------
    df : pd.DataFrame
        Données RH.

    Returns
    -------
    plotly.graph_objects.Figure
        Figure Plotly.
    """

    gender_counts = (
        df["sexe"]
        .value_counts()
        .rename_axis("Sexe")
        .reset_index(name="Nombre")
    )

    fig = px.pie(
        gender_counts,
        names="Sexe",
        values="Nombre",
        title="Répartition des fonctionnaires par sexe",
        hole=0.4,
    )

    fig.update_traces(textposition="inside", textinfo="percent+label")

    return fig

def create_grade_bar_chart(df: pd.DataFrame):
    """
    Crée un graphique en barres représentant
    la répartition des fonctionnaires par grade.

    Parameters
    ----------
    df : pd.DataFrame
        Données RH.

    Returns
    -------
    plotly.graph_objects.Figure
        Figure Plotly.
    """

    grade_counts = (
        df["grade"]
        .value_counts()
        .reset_index()
    )

    grade_counts.columns = ["Grade", "Nombre"]

    fig = px.bar(
        grade_counts,
        x="Nombre",
        y="Grade",
        orientation="h",
        title="Répartition des fonctionnaires par grade",
        text="Nombre",
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        xaxis_title="Nombre de fonctionnaires",
        yaxis_title="Grade",
    )

    return fig

def create_scale_bar_chart(df: pd.DataFrame):
    """
    Crée un graphique en barres représentant
    la répartition des fonctionnaires par échelle.
    """

    order = ["6", "7", "8", "9", "10", "11", "EXP"]

    scale_counts = (
        df["echelle"]
        .astype(str)
        .value_counts()
        .reindex(order, fill_value=0)
        .reset_index()
    )

    scale_counts.columns = ["Echelle", "Nombre"]

    fig = px.bar(
        scale_counts,
        x="Echelle",
        y="Nombre",
        title="Répartition des fonctionnaires par échelle",
        text="Nombre",
    )

    fig.update_layout(
        xaxis_title="Échelle",
        yaxis_title="Nombre de fonctionnaires",
    )

    return fig

def create_step_bar_chart(df: pd.DataFrame):
    """
    Crée un graphique en barres représentant
    la répartition des fonctionnaires par échelon.
    """

    order = [str(i) for i in range(1, 14)]

    step_counts = (
        df["echelon"]
        .astype(str)
        .value_counts()
        .reindex(order, fill_value=0)
        .reset_index()
    )

    step_counts.columns = ["Echelon", "Nombre"]

    fig = px.bar(
        step_counts,
        x="Echelon",
        y="Nombre",
        title="Répartition des fonctionnaires par échelon",
        text="Nombre",
    )

    fig.update_layout(
        xaxis_title="Échelon",
        yaxis_title="Nombre de fonctionnaires",
    )

    return fig

def create_age_histogram(df: pd.DataFrame):
    """
    Crée un histogramme de la distribution des âges.
    """

    fig = px.histogram(
        df,
        x="age",
        nbins=15,
        title="Distribution des âges",
        labels={
            "age": "Âge",
            "count": "Nombre de fonctionnaires",
        },
    )

    fig.update_layout(
        xaxis_title="Âge",
        yaxis_title="Nombre de fonctionnaires",
    )

    return fig

def create_seniority_histogram(df: pd.DataFrame):
    """
    Crée un histogramme de la distribution de l'ancienneté.
    """

    fig = px.histogram(
        df,
        x="anciennete",
        nbins=15,
        title="Distribution de l'ancienneté",
        labels={
            "anciennete": "Ancienneté",
            "count": "Nombre de fonctionnaires",
        },
    )

    fig.update_layout(
        xaxis_title="Ancienneté (années)",
        yaxis_title="Nombre de fonctionnaires",
    )

    return fig