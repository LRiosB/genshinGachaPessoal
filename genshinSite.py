import streamlit as st
from pathlib import Path
from streamlit.source_util import (
    page_icon_and_name, 
    calc_md5, 
    get_pages,
    _on_pages_changed
)

st.set_page_config(
    page_title="Página principal",
    page_icon="👋",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
#st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def delete_page(main_script_path_str, page_name):

    current_pages = get_pages(main_script_path_str)

    for key, value in current_pages.items():
        if value['page_name'] == page_name:
            del current_pages[key]
            break
        else:
            pass
    _on_pages_changed.send()

def add_page(main_script_path_str, page_name):
    
    pages = get_pages(main_script_path_str)
    main_script_path = Path(main_script_path_str)
    pages_dir = main_script_path.parent / "pages"
    script_path = [f for f in pages_dir.glob("*.py") if f.name.find(page_name) != -1][0]
    script_path_str = str(script_path.resolve())
    pi, pn = page_icon_and_name(script_path)
    psh = calc_md5(script_path_str)
    pages[psh] = {
        "page_script_hash": psh,
        "page_name": pn,
        "icon": pi,
        "script_path": script_path_str,
    }
    _on_pages_changed.send()

if "firstTimeRunningMain" not in st.session_state:
    st.session_state["firstTimeRunningMain"] = True


if(st.session_state["firstTimeRunningMain"]):
    delete_page("./GenshinSite.py", "SessionState")






st.markdown("<h1 style='text-align: center; color: black;'>Gacha wishing simulator</h1>", unsafe_allow_html=True)

#st.title("Gacha wishing simulator")

with st.expander("Starting situation"):

    columnsFirst = st.columns(3)

    with columnsFirst[0]:
        
        numberWishingEvents = st.number_input("How many wishing events?", min_value=1, value=1)
        numberPrimogems = st.number_input("How many primogems at start?", min_value=0, value=0)
        
    with columnsFirst[1]:
        numberWishesLimited = st.number_input("Limited banner wish history", min_value=0, max_value=89, value=0, help="Put here the number of pulls you did on limited banner (any of them), since the last time you got a five star character (both the limited and the default ones) until now.")
        numberStarglitter = st.number_input("How many starglitter at start?", min_value=0, value=0)
        
    with columnsFirst[2]:
        numberWishesWeapon = st.number_input("Weapon banner wish history", min_value=0, max_value=79, value=0, help="Put here the number of pulls you did on weapon banner since the last time you got a five star weapon (both the limited and the default ones) until now.")
        numberStardust = st.number_input("How many stardust at start?", min_value=0, value=0)

    boolReinvestStarglitter = st.checkbox("Check if you wish to reinvest starglitter when out of primos")
    bool5050 = st.checkbox("Check if you are currently on 50/50 on limited banner")





st.text("Estamos com %d eventos, %d gemas, %d tiros dados no limitado, %d tiros dados na arma, %d starglitter e %d stardust"%(numberWishingEvents, numberPrimogems, numberWishesLimited, numberWishesWeapon, numberStarglitter, numberStardust))

st.session_state["dict"] = dict()
st.session_state["dict"]["batata"] = 1
st.session_state["dict"]["arroz"] = 1

if st.button("Deletar pagina"):
    delete_page("./GenshinSite.py", "SessionState")

if st.button("Adicionar pagina"):
    add_page("./GenshinSite.py", "SessionState")



















st.session_state["firstTimeRunningMain"] = False