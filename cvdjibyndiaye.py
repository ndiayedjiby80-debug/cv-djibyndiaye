import streamlit as st
st.set_page_config(page_title="Mon CV", page_icon="📄", layout="wide")
st.subheader("expert en Informatique geomatique | Passionné de cybersécurité")

st.markdown("---")

st.write("""Geomaticien specialiste des etudes geospatial et des cartographies numeriques.Competances averées en informatique et gestion des systemes de données géographiques.Capaciter a travailer en équipe sur des projets d'étude et de realisation de cartographie numerique""")

st.header("Compétences")
col1, col2 = st.columns(2)

with col1:
    st.write("- Python")
    st.write("- Java")
    st.write("- Réseaux")
    st.write("- geomatique")

with col2:
    st.write("- Cybersécurité")
    st.write("- WinDev")
    st.write("- Base de données")

st.header(" Expériences professionnelles")
st.write("""
**Stagiaire maintenance-service **  
- Maintenance informatique  
- Sécurisation du réseau  
""")

st.header(" Formation")
st.write("""
**Licence en Informatique genie logiciel**  
institut communautaire Africaine de gestion et d'ingeniereie(2022 - 2025)
""")

st.header(" Langues")
st.write("""
 ANGLAIS   
 ESPANIOL
""")
with st.sidebar:
    
    st.header("DJIBY NDIAYE")
    st.subheader("Technicien superieur en géomatique") 
    st.write("""
    
      Grand-yoff Dakar, Sénégal
      
      ndiayedjiby80@email.com   """)

    
