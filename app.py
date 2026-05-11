import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Mechanical Unit Converter", page_icon="⚙️")

# --- HEADER SECTION ---
# Displaying your credentials as requested
st.title("⚙️ Mechanical Unit Converter & Density Checker")
st.markdown(f"""
**Developer:** MUHAMMAD ALI SHAH  
**Roll No:** 25-ME-148  
""")
st.divider()

# --- SIDEBAR NAVIGATION ---
option = st.sidebar.selectbox("Select Function", ["Unit Converter", "Material Density Checker"])

# --- FUNCTION 1: UNIT CONVERTER ---
if option == "Unit Converter":
    st.header("📏 Mechanical Unit Converter")
    
    conversion_type = st.selectbox("Choose Category", ["Length", "Pressure", "Force"])

    if conversion_type == "Length":
        val = st.number_input("Enter Value", value=1.0)
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From", ["Meters", "Millimeters", "Inches", "Feet"])
        with col2:
            to_unit = st.selectbox("To", ["Meters", "Millimeters", "Inches", "Feet"])
        
        # Conversion Dictionary (to Meters as base)
        length_map = {"Meters": 1.0, "Millimeters": 0.001, "Inches": 0.0254, "Feet": 0.3048}
        result = val * (length_map[from_unit] / length_map[to_unit])
        st.success(f"**Result:** {result:.4f} {to_unit}")

    elif conversion_type == "Pressure":
        val = st.number_input("Enter Value", value=1.0)
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From", ["Pascal (Pa)", "Bar", "PSI"])
        with col2:
            to_unit = st.selectbox("To", ["Pascal (Pa)", "Bar", "PSI"])
        
        # Conversion Dictionary (to Pa as base)
        press_map = {"Pascal (Pa)": 1.0, "Bar": 100000.0, "PSI": 6894.76}
        result = val * (press_map[from_unit] / press_map[to_unit])
        st.success(f"**Result:** {result:.4f} {to_unit}")

    elif conversion_type == "Force":
        val = st.number_input("Enter Value", value=1.0)
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From", ["Newton (N)", "Kilonewton (kN)", "Pound-force (lbf)"])
        with col2:
            to_unit = st.selectbox("To", ["Newton (N)", "Kilonewton (kN)", "Pound-force (lbf)"])
        
        # Conversion Dictionary (to N as base)
        force_map = {"Newton (N)": 1.0, "Kilonewton (kN)": 1000.0, "Pound-force (lbf)": 4.44822}
        result = val * (force_map[from_unit] / force_map[to_unit])
        st.success(f"**Result:** {result:.4f} {to_unit}")

# --- FUNCTION 2: DENSITY CHECKER ---
else:
    st.header("🧪 Material Density Checker")
    
    # Dictionary of materials (kg/m^3)
    densities = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Cast Iron": 7200,
        "Titanium": 4500,
        "Water": 1000
    }
    
    selected_material = st.selectbox("Select Material", list(densities.keys()))
    density_val = densities[selected_material]
    
    st.info(f"The density of **{selected_material}** is approximately **{density_val} kg/m³**.")
    
    st.subheader("Mass Calculator")
    vol = st.number_input("Enter Volume ($m^3$)", value=1.0, step=0.1)
    mass = density_val * vol
    st.write(f"The estimated mass of the object is **{mass:.2f} kg**.")

# --- FOOTER ---
st.divider()
st.caption("Developed for Mechanical Engineering Applications.")
