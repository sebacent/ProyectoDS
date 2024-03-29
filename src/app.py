import streamlit as st
import diccionarios
import joblib
import numpy as np
from joblib import load
from pickle import load


#cargo el modelo optimizado
model = load(open('models/prueba2.sav', "rb"))
print(type(model))
#cargo los diccionarios
#
# ESTILO DE LA PÁGINA
# custom_css = """
#     <style>
#         body {
#             background-image: url({'https://png.pngtree.com/png-clipart/20221224/original/pngtree-basketball-png-image_8801838.png'});
#             background-size: cover;
#         }
#     </style>
# """

# # Agrega el estilo CSS personalizado a la aplicación Streamlit
# st.markdown(custom_css, unsafe_allow_html=True)


# st.title('Prediccion de puntos para un jugador')
# player = st.selectbox('Jugador',list(players_dict.values()))

# st.write("Promedios de estadísticas ofensivas")
# panel_izquierdo, panel_derecho = st.columns(2, gap='large')

# # Agregar contenido al panel izquierdo

# with panel_izquierdo:
#     pts_prom = st.slider("Puntos", min_value=0.0, max_value=46.0,step=0.5)
    
#     fgm_prom = st.slider("Tiros de campo convertidos", min_value=0.0, max_value=46.0,step=0.5)
#     fga_prom = st.slider("Tiros de campo intentados", min_value=0.0, max_value=46.0,step=0.5)
    
#     f3m_prom = st.slider("Tiros de 3 convertidos", min_value=0.0, max_value=46.0,step=0.5)
#     f3a_prom = st.slider("Tiros de 3 intentados", min_value=0.0, max_value=46.0,step=0.5)

#     ftm_prom = st.slider("Tiros libres convertidos", min_value=0.0, max_value=46.0,step=0.5)
#     fta_prom = st.slider("Tiros libres intentados", min_value=0.0, max_value=46.0,step=0.5)



# # Agregar contenido al panel derecho
# with panel_derecho:
#     min_prom = st.slider("Minutos", min_value=0.0, max_value=46.0,step=0.5)

#     ast_prom = st.slider("Asistencias", min_value=0.0, max_value=46.0,step=0.5)
#     orb_prom = st.slider("Rebotes ofensivos", min_value=0.0, max_value=46.0,step=0.5)
#     stl_prom = st.slider("Robos", min_value=0.0, max_value=46.0,step=0.5)

#     pfd_prom = st.slider("Faltas recibidas", min_value=0.0, max_value=46.0,step=0.5)
#     blka_prom = st.slider("Bloqueos recibidos", min_value=0.0, max_value=46.0,step=0.5)

# panel_izquierdo2, panel_derecho2 = st.columns(2, gap='large')

# # Agregar contenido al panel izquierdo
# with panel_izquierdo2:
#     st.write("Estadísticas generales")
#     tov_prom = st.slider("Pérdidas", min_value=0.0, max_value=46.0,step=0.5)
#     plsmin_prom = st.slider("+/-", min_value=0.0, max_value=46.0,step=0.5)


# # Agregar contenido al panel derecho
# with panel_derecho2:
#     st.write("Estadísticas defensivas")
#     dreb_prom = st.slider("Rebotes defensivos", min_value=0.0, max_value=46.0,step=0.5)
#     pf_prom = st.slider("Faltas cometidas", min_value=0.0, max_value=46.0,step=0.5)
#     blk_prom = st.slider("Bloqueos", min_value=0.0, max_value=46.0,step=0.5)


# if st.button("Predecir puntos"):
#     # -- Obtengo la key del jugador

#     player_key = next((clave for clave, valor in players_dict.items() if valor == player), None)
#     #st.write(type(player_key))
#     #st.write(scaler.transform(player_key))
#     a = 115.500000
#     b = 123.500000
#     c = 0.25000
#     valores = np.array([player_key, min_prom, fgm_prom, fga_prom, f3m_prom,
#                         f3a_prom, ftm_prom, fta_prom, orb_prom, dreb_prom,
#                         ast_prom, tov_prom, stl_prom, blk_prom, blka_prom, pf_prom,
#                         pfd_prom, pts_prom, plsmin_prom,a,b,c])

#     prediction = str(model.predict([valores])[0])                        
#     # prediction = str(model.predict([[
#     #     scaler.transform(player_key),
#     #     scaler.transform(min_prom),
#     #     scaler.transform(fgm_prom),
#     #     scaler.transform(fga_prom),
#     #     scaler.transform(f3m_prom),
#     #     scaler.transform(f3a_prom),
#     #     scaler.transform(ftm_prom),
#     #     scaler.transform(fta_prom),
#     #     scaler.transform(oreb_prom),
#     #     scaler.transform(dreb_prom),
#     #     scaler.transform(ast_prom),
#     #     scaler.transform(tov_prom),
#     #     scaler.transform(stl_prom),
#     #     scaler.transform(blk_prom),
#     #     scaler.transform(blka_prom),
#     #     scaler.transform(pf_prom),
#     #     scaler.transform(pfd_prom),
#     #     scaler.transform(pts_prom),
#     #     scaler.transform(plus_minus_prom),
        		
#     #     scaler.transform(115.500000), # ELIMINAR LUEGO
#     #     scaler.transform(123.500000),
#     #     scaler.transform(0.25000),
#     # ]])[0])
    
#     st.write("Predicción:", prediction)