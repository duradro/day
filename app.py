import streamlit as st
import time

# Настройка страницы (вкладка в браузере)
st.set_page_config(page_title="Для Маши ❤️", page_icon="✨", layout="centered")

# Инициализируем шаг, если сайт только открылся
if "step" not in st.session_state:
    st.session_state.step = 1

# --- ШАГ 1: Приветствие ---
if st.session_state.step == 1:
    st.markdown("<h1 style='text-align: center; margin-top: 50px;'>Привет, Маша! 👋</h1>", unsafe_allow_html=True)
    st.write("") # Пустая строка для отступа
    
    # Кнопка "Далее"
    if st.button("Далее ➡️", use_container_width=True):
        st.session_state.step = 2
        st.rerun() # Перезапускаем интерфейс, чтобы перейти к следующему шагу

# --- ШАГ 2: Вопрос про завтра ---
elif st.session_state.step == 2:
    st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Ты свободна завтра? 🤔</h2>", unsafe_allow_html=True)
    st.write("")
    
    # Создаем две колонки для кнопок "Да" и "Нет" в один ряд
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Да ✅", use_container_width=True):
            st.session_state.step = 3
            st.rerun()
            
    with col2:
        if st.button("Нет ❌", use_container_width=True):
            st.session_state.step = "closed"
            st.rerun()

# --- ШАГ 3: Если Маша ответила "Да" ---
elif st.session_state.step == 3:
    st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Давай встретимся, хочу кое-чо сказать... 👀</h2>", unsafe_allow_html=True)
    st.balloons() # Эффект разлетающихся праздничных шаров на весь экран

# --- ЕСЛИ НАЖАЛА "НЕТ" (Закрытие сайта) ---
elif st.session_state.step == "closed":
    st.markdown("<h3 style='text-align: center; margin-top: 50px; color: gray;'>Сайт закрыт... 🚪</h3>", unsafe_allow_html=True)
    # Скрипт, который пытается закрыть вкладку браузера (работает в большинстве современных браузеров)
    st.components.v1.html("<script>window.close();</script>", height=0)
