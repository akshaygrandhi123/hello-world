import streamlit as st
from demo import area_of_circle
import plotly.graph_objects as go
import math
import time

# Animated gradient background and custom fonts
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
    body, .main {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        font-family: 'Montserrat', sans-serif;
        animation: bgmove 10s ease-in-out infinite alternate;
    }
    @keyframes bgmove {
        0% {background-position: 0% 50%;}
        100% {background-position: 100% 50%;}
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff6a00 0%, #ee0979 100%);
        color: white;
        font-size: 20px;
        border-radius: 12px;
        padding: 12px 28px;
        font-family: 'Montserrat', sans-serif;
        box-shadow: 0 4px 14px 0 rgba(255,106,0,0.2);
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.07);
        box-shadow: 0 6px 20px 0 rgba(238,9,121,0.2);
    }
    .stSlider>div>div>div>div {
        background: linear-gradient(90deg, #ee0979 0%, #ff6a00 100%);
    }
    .fade-in {
        animation: fadeIn 1.2s;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.8);}
        to { opacity: 1; transform: scale(1);}
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='font-size:3rem; color:#ee0979; font-family:Montserrat, sans-serif;'>✨ Hello World App: Circle Area Calculator ✨</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='color:#ff6a00; font-family:Montserrat, sans-serif;'>Calculate the area of a circle and flex your math skills! 🔥</h4>",
    unsafe_allow_html=True
)

# Animated emoji GIF (replace with your own if you want)
st.image("https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif", width=120)

radius = st.slider(
    "Pick your circle's vibe (radius):",
    min_value=0.0, max_value=100.0, value=1.0, step=0.1
)

if radius < 0:
    st.error("Radius can't be negative, fam.")
else:
    if st.button("💥 Calculate Area 💥"):
        area = area_of_circle(radius)
        # Animated area result
        st.markdown(
            f"<div class='fade-in'><span style='color:#ee0979;font-size:2rem;font-family:Montserrat, sans-serif;'>Area: {area:.2f} units²</span> <span style='font-size:2rem;'>🎉</span></div>",
            unsafe_allow_html=True
        )
        # Store history in session state
        if "history" not in st.session_state:
            st.session_state["history"] = []
        st.session_state["history"].append((radius, area))

        # Animate the circle plot (radius grows)
        fig = go.Figure()
        theta = [i for i in range(361)]
        frames = []
        for r in [radius * i / 20 for i in range(1, 21)]:
            x = [r * math.cos(math.radians(t)) for t in theta]
            y = [r * math.sin(math.radians(t)) for t in theta]
            frames.append(go.Frame(data=[go.Scatter(x=x, y=y, mode='lines', fill='toself')]))
        x = [radius * math.cos(math.radians(t)) for t in theta]
        y = [radius * math.sin(math.radians(t)) for t in theta]
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', fill='toself', name='Circle', line=dict(color='#ee0979', width=4)))
        fig.frames = frames
        fig.update_layout(
            title="Circle Glow Up ✨",
            xaxis=dict(scaleanchor="y", scaleratio=1, visible=False),
            yaxis=dict(scaleanchor="x", scaleratio=1, visible=False),
            width=400, height=400,
            plot_bgcolor="rgba(0,0,0,0)",
            updatemenus=[{
                "type": "buttons",
                "showactive": False,
                "buttons": [{
                    "label": "Play",
                    "method": "animate",
                    "args": [None, {"frame": {"duration": 40, "redraw": True}, "fromcurrent": True}]
                }]
            }]
        )
        st.plotly_chart(fig, use_container_width=True)

    # Show history
    if "history" in st.session_state and st.session_state["history"]:
        st.markdown("<h4 style='color:#ff6a00;'>History 📜</h4>", unsafe_allow_html=True)
        for idx, (r, a) in enumerate(reversed(st.session_state["history"]), 1):
            st.write(f"{idx}. Radius: {r}, Area: {a:.2f}")

st.markdown(
    "<hr><p style='color:gray;font-size:16px;font-family:Montserrat, sans-serif;'>Made with ❤️ for the 'Instagram using Streamlit</p>",
    unsafe_allow_html=True
)