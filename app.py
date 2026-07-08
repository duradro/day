import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Для Маши ❤️", page_icon="✨", layout="centered")

# Инициализируем шаг, если сайт только открылся
if "step" not in st.session_state:
    st.session_state.step = 1

# --- ШАГ 1: Приветствие ---
if st.session_state.step == 1:
    st.markdown("<h1 style='text-align: center; margin-top: 30px;'>Привет, Маша! 👋</h1>", unsafe_allow_html=True)
    
    # Картинка "Хаю-Хай" через официальный CDN
    st.image("https://unsplash.com", caption="Тут должен быть твой стикер Хаю-Хай", use_container_width=True)
    
    st.write("") 
    if st.button("Далее ➡️", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# --- ШАГ 2: Вопрос про завтра ---
elif st.session_state.step == 2:
    st.markdown("<h2 style='text-align: center; margin-top: 30px;'>Ты свободна завтра? 🤔</h2>", unsafe_allow_html=True)
    
    # Попытка загрузить мем, если ссылка заблокирована — выводим красивую заглушку
    try:
        st.image("https://ibb.co", use_container_width=True)
    except:
        st.warning("⚠️ Картинка-мем временно недоступна из-за блокировки хостинга")
    
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

# --- ШАГ 3: Если Маша ответила "Да" (Финальный экран) ---
elif st.session_state.step == 3:
    st.markdown("<h2 style='text-align: center; margin-top: 30px;'>Давай встретимся, хочу кое-чо сказать... 👀</h2>", unsafe_allow_html=True)
    
    # Танцующие котята
    st.image("https://giphy.com", use_container_width=True)
    
    # Фото с Меллстроем
    try:
        st.image("https://ibb.co", use_container_width=True)
    except:
        st.info("🖼 Здесь отображается твое фото с Меллстроем")

    st.write("🎵 **Включай трек ниже и слушай:**")
    
    # Плеер YouTube с нужным треком. Он гарантированно работает на любых устройствах и телефонах
    st.video("https://youtube.com")
    
    st.balloons() 

# --- ШАГ 4: Если Маша нажала "Нет" ---
elif st.session_state.step == "closed":
    st.markdown("<h3 style='text-align: center; margin-top: 50px;'>Ну ладно... 🥺</h3>", unsafe_allow_html=True)
    st.image("https://giphy.com", use_container_width=True)
    
    st.components.v1.html("<script>setTimeout(function(){ window.close(); }, 5000);</script>", height=0)
