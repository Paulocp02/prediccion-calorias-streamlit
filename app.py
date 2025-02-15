import streamlit as st
import requests

# URL de la API desplegada en Render
API_URL = "https://api-prediccion-calorias.onrender.com/predict"

# Configuración de la página
st.set_page_config(page_title="Predicción de Calorías", layout="centered")

# Título de la aplicación
st.title("🔥 Predicción de Calorías Quemadas 🔥")

# Formulario de entrada de datos
st.sidebar.header("📋 Ingresar Datos del Usuario")

age = st.sidebar.number_input("Edad", min_value=10, max_value=100, value=25)
weight = st.sidebar.number_input("Peso (kg)", min_value=30.0, max_value=200.0, value=70.0)
height = st.sidebar.number_input("Altura (m)", min_value=1.2, max_value=2.2, value=1.75)
max_bpm = st.sidebar.number_input("Frecuencia Cardíaca Máx (BPM)", min_value=100, max_value=220, value=180)
avg_bpm = st.sidebar.number_input("Frecuencia Cardíaca Prom (BPM)", min_value=50, max_value=200, value=120)
resting_bpm = st.sidebar.number_input("Frecuencia en Reposo (BPM)", min_value=40, max_value=100, value=60)
session_duration = st.sidebar.number_input("Duración de la Sesión (horas)", min_value=0.1, max_value=3.0, value=1.0)
workout_type = st.sidebar.selectbox("Tipo de Entrenamiento", ["Cardio", "Fuerza"], index=0)
fat_percentage = st.sidebar.number_input("Porcentaje de Grasa (%)", min_value=5.0, max_value=50.0, value=20.0)
water_intake = st.sidebar.number_input("Consumo de Agua (litros)", min_value=0.5, max_value=5.0, value=2.0)
workout_frequency = st.sidebar.slider("Frecuencia de Entrenamiento (días/semana)", 1, 7, 4)

# Variables calculadas
bmi = weight / (height ** 2)
intensity = avg_bpm / max_bpm
bmi_workout = bmi * workout_frequency
calories_per_hour = weight * intensity * 10

# Botón para hacer la predicción
if st.sidebar.button("🔮 Predecir Calorías"):
    # Crear el JSON con los datos del usuario
    input_data = {
        "Age": age,
        "Weight": weight,
        "Height": height,
        "Max_BPM": max_bpm,
        "Avg_BPM": avg_bpm,
        "Resting_BPM": resting_bpm,
        "Session_Duration": session_duration,
        "Workout_Type": 0 if workout_type == "Cardio" else 1,  
        "Fat_Percentage": fat_percentage,
        "Water_Intake": water_intake,
        "Workout_Frequency": workout_frequency,
        "BMI": bmi,
        "Intensity": intensity,
        "BMI_Workout": bmi_workout,
        "Calories_per_hour": calories_per_hour
    }

    # Hacer la solicitud a la API
    response = requests.post(API_URL, json=input_data)

    # Mostrar la respuesta
    if response.status_code == 200:
        prediction = response.json()["Calories_Burned_Predicted"]
        st.success(f"🔥 Calorías Quemadas Estimadas: **{prediction:.2f} kcal**")
    else:
        st.error("❌ Error en la predicción. Intenta de nuevo.")

