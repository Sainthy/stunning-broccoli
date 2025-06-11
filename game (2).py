import streamlit as st
import random

# Simbol slot yang digunakan (bisa diganti)
symbols = ["🍒", "🍋", "🔔", "💎", "🍀", "7️⃣"]

st.set_page_config(page_title="🎰 Slot Machine Game", layout="centered")

st.title("🎰 Slot Machine Game")
st.caption("By OpenAI & Streamlit")

# CSS sederhana untuk mempercantik tampilan
st.markdown("""
<style>
.slot-box {
    font-size: 72px;
    text-align: center;
    padding: 10px;
    border: 2px solid #ccc;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Buat kolom untuk slot
col1, col2, col3 = st.columns(3)

# Fungsi untuk melakukan spin slot
def spin_slots():
    return [random.choice(symbols) for _ in range(3)]

# Tombol Spin
if st.button("🎲 Spin!"):
    result = spin_slots()
    
    # Tampilkan hasil slot di masing-masing kolom
    with col1:
        st.markdown(f"<div class='slot-box'>{result[0]}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='slot-box'>{result[1]}</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='slot-box'>{result[2]}</div>", unsafe_allow_html=True)

    # Logika kemenangan
    if result[0] == result[1] == result[2]:
        st.success("🎉 SUPER GACOR!!⚡⚡")
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        st.info("✨ Nice! You got a pair!")
    else:
        st.warning("😢 Try again!")

else:
    # Tampilan awal sebelum spin
    with col1:
        st.markdown(f"<div class='slot-box'>❔</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='slot-box'>❔</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='slot-box'>❔</div>", unsafe_allow_html=True)
