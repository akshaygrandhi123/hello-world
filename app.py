import streamlit as st
from demo import area_of_circle
import plotly.graph_objects as go
import math

# Custom CSS for colors and styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f4f8;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px 24px;
    }
    .stSlider>div>div>div>div {
        background: linear-gradient(90deg, #4CAF50 0%, #2196F3 100%);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🟢 Hello World App: Circle Area Calculator")
st.markdown(
    "<h4 style='color:#2196F3;'>Calculate the area of a circle and visualize it!</h4>",
    unsafe_allow_html=True
)

radius = st.slider(
    "Select the radius of the circle:",
    min_value=0.0, max_value=100.0, value=1.0, step=0.1
)

# Input validation
if radius < 0:
    st.error("Radius cannot be negative.")
else:
    if st.button("Calculate Area"):
        area = area_of_circle(radius)
        st.success(f"The area of the circle is: <span style='color:#4CAF50;font-size:22px'>{area:.2f}</span> units²", icon="✅")
        # Store history in session state
        if "history" not in st.session_state:
            st.session_state["history"] = []
        st.session_state["history"].append((radius, area))

        # Plot the circle
        fig = go.Figure()
        theta = [i for i in range(361)]
        x = [radius * math.cos(math.radians(t)) for t in theta]
        y = [radius * math.sin(math.radians(t)) for t in theta]
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', fill='toself', name='Circle'))
        fig.update_layout(
            title="Circle Visualization",
            xaxis=dict(scaleanchor="y", scaleratio=1),
            yaxis=dict(scaleanchor="x", scaleratio=1),
            width=400, height=400,
            plot_bgcolor="#f0f4f8"
        )
        st.plotly_chart(fig, use_container_width=True)

    # Show history
    if "history" in st.session_state and st.session_state["history"]:
        st.markdown("#### Area Calculation History")
        for idx, (r, a) in enumerate(reversed(st.session_state["history"]), 1):
            st.write(f"{idx}. Radius: {r}, Area: {a:.2f}")

st.markdown(
    "<hr><p style='color:gray;font-size:14px;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)