import streamlit as st

# Настройка вкладки в браузере
st.set_page_config(page_title="Для Маши ❤️", page_icon="✨", layout="centered")

# Инициализируем шаги сайта
if "step" not in st.session_state:
    st.session_state.step = 1

# --- ШАГ 1: Приветствие ---
if st.session_state.step == 1:
    st.markdown("<h1 style='text-align: center; margin-top: 30px;'>Привет, Маша! 👋</h1>", unsafe_allow_html=True)
    
    # Твой стикер "Хаю-Хай"
    st.image("https://ibb.co", use_container_width=True)
    
    st.write("") 
    if st.button("Далее ➡️", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# --- ШАГ 2: Главный вопрос ---
elif st.session_state.step == 2:
    st.markdown("<h2 style='text-align: center; margin-top: 30px;'>Ты свободна завтра? 🤔</h2>", unsafe_allow_html=True)
    
    # Твое фото-мем про 500 рублей
    st.image("https://ibb.co", use_container_width=True)
    
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
    
    # Гифка с танцующими котятами
    st.image("https://giphy.com", use_container_width=True)
    
    # Твое фото над кнопкой "Да" (Меллстрой с семьей)
    st.image("https://ibb.co", use_container_width=True)
    
    # Скрытый плеер с треком "5 УТРА"
    # Ссылка ведет на аудиопоток песни. Современные браузеры могут блокировать звук без клика, 
    # поэтому плеер снабжен элементами управления для подстраховки, если автозапуск заблокирован.
    track_url = "https://od.lk"
    st.markdown(
        f'<audio autoplay loop controls style="width: 100%; margin-top: 20px;"><source src="{track_url}" type="audio/mp3"></audio>',
        unsafe_allow_html=True
    )
    
    st.balloons() # Салют из воздушных шаров

# --- ШАГ 4: Если Маша ответила "Нет" ---
elif st.session_state.step == "closed":
    st.markdown("<h3 style='text-align: center; margin-top: 50px;'>Ну ладно... 🥺</h3>", unsafe_allow_html=True)
    
    # Грустная гифка с плачущим котиком
    st.image("https://giphy.com", use_container_width=True)
    
    # Автоматически закрываем вкладку через 4 секунды
    st.components.v1.html("<script>setTimeout(function(){ window.close(); }, 4000);</script>", height=0)
