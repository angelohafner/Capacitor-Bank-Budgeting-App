
# Capacitor Bank Budgeting App

This application calculates various parameters related to capacitor bank budgeting. 
It provides insights into the design and requirements of a capacitor bank based on user-defined inputs.

## Features

- Input parameters for frequency, voltage, reactive power, and capacitor configurations.
- Automated calculations of phase voltage, reactance, capacitance, and total reactive power.
- Warnings for invalid or non-standard configurations.
- Option to download results in JSON or plain text format.

## How to Use

1. Run the application using Streamlit:
   ```bash
   streamlit run app.py
   ```
2. Input the required parameters in the provided fields.
3. View the calculated results in the "Results" section.
4. Download the results for further analysis.

## Inputs

- **Frequency (Hz):** Operating frequency.
- **Phase to Phase Voltage (kV):** Voltage between phases.
- **Reactive Power (MVAr):** Required reactive power.
- **Voltage per can (kV):** Voltage rating of a single capacitor can.
- **Number of capacitors in series:** Number of capacitors connected in series.
- **Number of capacitors in parallel:** Number of capacitors connected in parallel.

## Results

The app calculates:
- Phase voltage, reactance, and capacitance.
- Total number of capacitors required.
- Reactive power per capacitor and overall.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/capacitor-bank-app.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the app with Streamlit.

## Download Options

Results can be downloaded in:
- Plain text (`data.txt`)
- JSON format (`data.json`)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Feel free to submit issues or pull requests for improvements.

---
Developed by Angelo Alfredo Hafner
