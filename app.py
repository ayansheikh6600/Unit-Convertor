import streamlit as st

# Unit categories and conversions
units = {
    "Length": {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254,
    },
    "Mass": {
        "kilogram": 1,
        "gram": 0.001,
        "milligram": 0.000001,
        "pound": 0.453592,
        "ounce": 0.0283495,
    },
    "Temperature": {
        "celsius": "celsius",
        "fahrenheit": "fahrenheit",
        "kelvin": "kelvin"
    }
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return value * 9 / 5 + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5 / 9
        elif to_unit == "kelvin":
            return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9 / 5 + 32

def main():
    st.title("🌐 Google-style Unit Converter")

    category = st.selectbox("Select Category", list(units.keys()))
    from_unit = st.selectbox("From", list(units[category].keys()))
    to_unit = st.selectbox("To", list(units[category].keys()))
    value = st.number_input("Enter value", value=0.0, format="%.5f")

    if st.button("Convert"):
        if category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            base = units[category][from_unit]
            target = units[category][to_unit]
            result = value * base / target

        st.success(f"{value} {from_unit} = {result:.5f} {to_unit}")

if __name__ == "__main__":
    main()
