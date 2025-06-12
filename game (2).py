import streamlit as st
import random

# Daftar kata-kata 5 huruf (kamu bisa tambah lagi)
WORDS = [
    'karet', 'motor', 'kelas', 'hutan', 'jalan', 'rumah', 'botol', 'peluk',
    'kerja', 'tebak', 'pohon', 'pisau', 'gadis', 'hitam', 'merah'
]

MAX_GUESS = 6

# Inisialisasi session state
if "target_word" not in st.session_state:
    st.session_state.target_word = random.choice(WORDS)
    st.session_state.guesses = []
    st.session_state.game_over = False
    st.session_state.success = False

def get_feedback(guess, target):
    feedback = []
    target_letters = list(target)
    for i in range(5):
        if guess[i] == target[i]:
            feedback.append(("🟩", guess[i]))  # Benar & posisi benar
            target_letters[i] = None
        else:
            feedback.append(("", guess[i]))  # Placeholder

    for i in range(5):
        if feedback[i][0] == "":
            if guess[i] in target_letters:
                feedback[i] = ("🟨", guess[i])  # Ada tapi posisi salah
                target_letters[target_letters.index(guess[i])] = None
            else:
                feedback[i] = ("⬜", guess[i])  # Tidak ada
    return feedback

# UI Streamlit
st.title("🟩🟨 Wordle Versi Python di Streamlit")

if st.session_state.game_over:
    if st.session_state.success:
        st.success("🎉 Selamat! Kamu menebak katanya!")
    else:
        st.error(f"😞 Game Over! Kata yang benar adalah: **{st.session_state.target_word.upper()}**")
    if st.button("Main lagi"):
        st.session_state.target_word = random.choice(WORDS)
        st.session_state.guesses = []
        st.session_state.game_over = False
        st.session_state.success = False
    st.stop()

# Form input tebakan
with st.form("guess_form", clear_on_submit=True):
    guess = st.text_input("Masukkan tebakan (5 huruf):", max_chars=5).lower()
    submitted = st.form_submit_button("Tebak")

    if submitted:
        if len(guess) != 5 or not guess.isalpha():
            st.warning("Tebakan harus terdiri dari 5 huruf.")
        elif guess not in WORDS:
            st.warning("Kata tidak ditemukan di kamus.")
        else:
            st.session_state.guesses.append(guess)
            if guess == st.session_state.target_word:
                st.session_state.success = True
                st.session_state.game_over = True
            elif len(st.session_state.guesses) >= MAX_GUESS:
                st.session_state.game_over = True

# Tampilkan semua tebakan
st.subheader("Tebakan kamu:")
for guess in st.session_state.guesses:
    feedback = get_feedback(guess, st.session_state.target_word)
    feedback_str = "".join([f"{symbol}{letter.upper()}" for symbol, letter in feedback])
    st.write(feedback_str)
