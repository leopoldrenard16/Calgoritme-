import streamlit as st

st.title("🧮 Calgoritme")
st.write("Bienvenue dans Calgoritme !")

# Une case pour taper le calcul
expression = st.text_input("Entrez votre calcul :")

if expression:
    if expression.lower() == 'quitter':
        st.write("Au revoir !")
    else:
        # Filtre pour n'accepter que les caractères mathématiques de base
        if not all(c in "0123456789+-*/. " for c in expression):
            st.error("Erreur : Caractères non autorisés.")
        else:
            try:
                resultat = eval(expression)
                st.success(f"Résultat : {resultat}")
            except ZeroDivisionError:
                st.error("Erreur : Division par zéro impossible.")
            except Exception:
                st.error("Erreur : Calcul invalide.")


