from pathlib import Path
import streamlit as st
from src.data_loader import load_excel
from src.data_cleaning import (
    clean_column_names,
    drop_unused_columns,
    convert_date_columns,
)
from src.feature_engineering import (
    calculate_age,
    calculate_seniority,
    extract_recruitment_year,
    extract_retirement_year,
    years_until_retirement,
)
from src.business_metrics import (
    get_total_employees,
    get_gender_distribution,
    get_average_age,
    get_average_seniority,
)


st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 HR Analytics Dashboard")
st.subheader("Université Ibn Zohr")

# Chargement des données
df = load_excel(Path("data/raw/situation_administrative.xlsx"))

# Nettoyage
df = clean_column_names(df)
df = drop_unused_columns(df)
df = convert_date_columns(df)

# Feature Engineering
df = calculate_age(df)
df = calculate_seniority(df)
df = extract_recruitment_year(df)
df = extract_retirement_year(df)
df = years_until_retirement(df)

st.success("Les données ont été chargées avec succès.")
st.dataframe(df.head())
# ==========================
# Business Metrics
# ==========================

total_employees = get_total_employees(df)

gender_distribution = get_gender_distribution(df)

male_count = gender_distribution.get("H", 0)

female_count = gender_distribution.get("F", 0)

average_age = get_average_age(df)

average_seniority = get_average_seniority(df)

st.divider()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Fonctionnaires", total_employees)
col2.metric("Hommes", male_count)
col3.metric("Femmes", female_count)
col4.metric("Âge moyen", f"{average_age:.1f} ans")
col5.metric("Ancienneté", f"{average_seniority:.1f} ans")