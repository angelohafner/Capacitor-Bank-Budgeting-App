import math
import streamlit as st
import json

# App Title
st.title("Capacitor Bank Budgeting App")

# Input Section
st.header("Inputs")
col1, col2, col3 = st.columns(3)

with col1:
    freq1 = st.number_input("Frequency (Hz)", value=60.0)
    v_can_rated = st.number_input("Voltage per can (kV)", value=6.928) * 1e3

with col2:
    v_three_phase = st.number_input("Phase to Phase Voltage (kV)", value=12.0) * 1e3
    ns = st.number_input("Number of capacitors in series", min_value=1, value=1, step=1)

with col3:
    q_three_phase = st.number_input("Reactive Power (MVAr)", value=14.5) * 1e6
    np = st.number_input("Number of capacitors in parallel", min_value=1, value=8, step=1)

# Calculations
omega1 = 2 * math.pi * freq1
v_phase = v_three_phase / math.sqrt(3)
q_phase = q_three_phase / 3
x_phase = (v_phase**2) / q_phase
i_phase = v_phase / x_phase
c_phase = 1 / (omega1 * x_phase)

c_can_rated = (c_phase / np) * ns
n_cap = ns * np * 3
x_can_rated = 1 / (omega1 * c_can_rated)
i_can_rated = v_can_rated / x_can_rated
q_can_rated = (v_can_rated**2) / x_can_rated
total_Q = n_cap * q_can_rated

# Data for Display
data = {
    "inputs": {
        "Frequency (Hz)": round(freq1, 2),
        "Phase to Phase Voltage (kV)": round(v_three_phase / 1e3, 2),
        "Reactive Power (MVAr)": round(q_three_phase / 1e6, 2),
        "Voltage per can (kV)": round(v_can_rated / 1e3, 2),
        "Number of capacitors in series": ns,
        "Number of capacitors in parallel": np,
    },
    "results": {
        "v_phase (kV)": round(v_phase / 1e3, 2),
        "i_phase (A)": round(i_phase, 2),
        "q_phase (MVAr)": round(q_phase / 1e6, 2),
        "x_phase (Ohms)": round(x_phase, 2),
        "c_phase (μF)": round(c_phase * 1e6, 2),
        "n_cap": n_cap,
        "c_can_rated (μF)": round(c_can_rated * 1e6, 2),
        "i_can_rated (A)": round(i_can_rated, 2),
        "x_can_rated (Ohms)": round(x_can_rated, 2),
        "q_can_rated (kVAr)": round(q_can_rated / 1e3, 2),
        "Total Reactive Power (MVAr)": round(total_Q / 1e6, 2),
    },
}

# Display Results
st.header("Results")
st.json(data)

# Warnings
if q_can_rated > 1.1e6:
    st.warning(f"Warning: Can may not exist (q_can_rated = {round(q_can_rated / 1e6, 1)} MVAr > 1.1 MVAr).")
if v_can_rated > 15e3:
    st.warning(f"Warning: Can may not exist (v_can_rated = {round(v_can_rated / 1e3, 1)} kV > 15 kV).")

# Download Results
data_json = json.dumps(data, indent=4)

st.download_button(
    label="Download Results as data.txt",
    data=data_json,
    file_name="data.txt",
    mime="text/plain",
)

st.download_button(
    label="Download Results as data.json",
    data=data_json,
    file_name="data.json",
    mime="application/json",
)
