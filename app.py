import streamlit as st
import os

# Настройка страницы
st.set_page_config(page_title="Для Маши ❤️", page_icon="✨", layout="centered")

# Инициализируем шаг сайта
if "step" not in st.session_state:
    st.session_state.step = 1

# Проводник для локальных файлов
def get_file_path(filename):
    if os.path.exists(filename):
        return filename
    return None

# --- ШАГ 1: Приветствие ---
if st.session_state.step == 1:
    st.markdown("<h1 style='text-align: center; margin-top: 30px;'>Привет, Маша! 👋</h1>", unsafe_allow_html=True)
    
    # Твоя картинка "Хаю-Хай" с новым именем
    img = get_file_path("image-Photoroom (10).png")
    if img:
        st.image(img, use_container_width=True)
    else:
        st.info("🖼 Стикер 'Хаю-Хай' загружается...")
    
    st.write("") 
    if st.button("Далее ➡️", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# --- ШАГ 2: Главный вопрос ---
elif st.session_state.step == 2:
    st.markdown("<h2 style='text-align: center; margin-top: 30px;'>Ты свободна завтра? 🤔</h2>", unsafe_allow_html=True)
    
    # Загрузка локального мема
    img = get_file_path("masha-text.jpg")
    if img:
        st.image(img, use_container_width=True)
    else:
        st.info("🖼 Мем 'Про 500 рублей' загружается...")
    
    st.write("") 
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Да 🥰", use_container_width=True):
            st.session_state.step = 3
            st.rerun()
            
    with col2:
        if st.button("Нет 🥺", use_container_width=True):
            st.session_state.step = "closed"
            st.rerun()

# --- ШАГ 3: Если Маша ответила "Да" ---
elif st.session_state.step == 3:
    st.markdown("<h2 style='text-align: center; margin-top: 30px;'>Давай встретимся, хочу кое-чо сказать... 👀</h2>", unsafe_allow_html=True)
    
    # Гифка танцующих котят (работает всегда)
    st.image("https://giphy.com", use_container_width=True)
    
    # Твое фото с Меллстроем
    img = get_file_path("mellstroy-family.jpg")
    if img:
        st.image(img, use_container_width=True)
    else:
        st.info("🖼 Фото с Меллстроем загружается...")
    
    st.write("🎵 **Слушай трек:**")
    
    # Включается встроенный плеер, если загружен track.mp3, иначе — YouTube видеоплеер
    audio_file = get_file_path("track.mp3")
    if audio_file:
        st.audio(audio_file, format="audio/mp3", autoplay=True, loop=True)
    else:
        st.video("https://youtube.com")
        
    st.balloons()

# --- ШАГ 4: Если Маша ответила "Нет" ---
elif st.session_state.step == "closed":
    st.markdown("<h3 style='text-align: center; margin-top: 50px;'>Ну ладно... 🥺</h3>", unsafe_allow_html=True)
    st.image("https://giphy.com", use_container_width=True)
    st.components.v1.html("<script>setTimeout(function(){ window.close(); }, 4000);</script>", height=0)

