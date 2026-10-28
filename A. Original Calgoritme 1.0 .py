print  ("====================BIEVENU DANS CALGORITME=====================")
def calculatrice():
    while True:
        expression = input("Entrez votre calcul  : ")
        
        if expression.lower() == 'quitter':
            print("Au revoir !")
            break
            
        try:
            # Filtre pour n'accepter que les caractères mathématiques de base
            if not all(c in "0123456789+-*/. " for c in expression):
                print("Erreur : Caractères non autorisés.")
                continue
                
            resultat = eval(expression)
            print(f"Résultat : {resultat}")
            
        except ZeroDivisionError:
            print("Erreur : Division par zéro impossible.")
        except Exception:
            print("Erreur : Calcul invalide.")

if __name__ == "__main__":
    calculatrice()