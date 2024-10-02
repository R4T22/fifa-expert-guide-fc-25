import os
import cssmin

def minify_css(input_file, output_file):
    with open(input_file, 'r') as f:
        css = f.read()
    minified_css = cssmin.cssmin(css)
    with open(output_file, 'w') as f:
        f.write(minified_css)

# Exemple d'utilisation
minify_css('style.css', 'style.min.css')
import requests
from bs4 import BeautifulSoup

def check_seo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string if soup.title else 'Pas de balise titre'
    meta_description = soup.find('meta', attrs={'name': 'description'})
    description = meta_description['content'] if meta_description else 'Pas de méta-description'

    print(f'Titre : {title}')
    print(f'Méta-description : {description}')

# Exemple d'utilisation
check_seo('https://votre-site.com')
<script async src="https://www.googletagmanager.com/gtag/js?id=VOTRE_ID_DE_SUIVI"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'VOTRE_ID_DE_SUIVI');
</script>
document.querySelectorAll('img').forEach((img) => {
    if (!img.hasAttribute('alt')) {
        console.warn('Image sans attribut alt :', img.src);
    }
});
import sqlite3

# Créer une connexion à la base de données
conn = sqlite3.connect('fc25.db')
cursor = conn.cursor()

# Créer des tables pour les ligues et les équipes
cursor.execute('''
CREATE TABLE IF NOT EXISTS ligues (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS equipes (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    ligue_id INTEGER,
    FOREIGN KEY (ligue_id) REFERENCES ligues (id)
)
''')

# Insérer des données fictives
cursor.execute("INSERT INTO ligues (nom) VALUES ('Ligue 1')")
cursor.execute("INSERT INTO ligues (nom) VALUES ('Ligue 2')")
cursor.execute("INSERT INTO ligues (nom) VALUES ('Premier League')")
cursor.execute("INSERT INTO ligues (nom) VALUES ('La Liga')")

cursor.execute("INSERT INTO equipes (nom, ligue_id) VALUES ('Paris SG', 1)")
cursor.execute("INSERT INTO equipes (nom, ligue_id) VALUES ('Olympique de Marseille', 1)")
cursor.execute("INSERT INTO equipes (nom, ligue_id) VALUES ('Olympique Lyonnais', 1)")
cursor.execute("INSERT INTO equipes (nom, ligue_id) VALUES ('Chelsea', 3)")
cursor.execute("INSERT INTO equipes (nom, ligue_id) VALUES ('Manchester City', 3)")
cursor.execute("INSERT INTO equipes (nom, ligue_id) VALUES ('Barcelona', 4)")

# Valider les changements
conn.commit()
import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('fc25.db')
cursor = conn.cursor()

# Récupérer toutes les ligues
cursor.execute("SELECT * FROM ligues")
ligues = cursor.fetchall()

print("Ligues:")
for ligue in ligues:
    print(f"- {ligue[1]}")  # ligue[1] contient le nom de la ligue

# Récupérer toutes les équipes
cursor.execute("SELECT equipes.nom, ligues.nom FROM equipes JOIN ligues ON equipes.ligue_id = ligues.id")
equipes = cursor.fetchall()

print("\nÉquipes:")
for equipe in equipes:
    print(f"- {equipe[0]} (Ligue: {equipe[1]})")  # equipe[0] est le nom de l'équipe, equipe[1] est le nom de la ligue

# Fermer la connexion
conn.close()
import random

def afficher_menu():
    print("=== Conseils pour FIFA 25 ===")
    print("1. Conseils de jeu")
    print("2. Gestion de l'équipe")
    print("3. Techniques de tir")
    print("4. Quitter")

def conseils_de_jeu():
    conseils = [
        "Utilisez la touche de sprint avec parcimonie pour éviter de perdre le ballon.",
        "Maîtrisez le dribble pour contourner les défenseurs adverses.",
        "Jouez en équipe et utilisez les passes en profondeur pour créer des occasions.",
        "Faites attention à votre positionnement défensif pour éviter les contre-attaques."
    ]
    return random.choice(conseils)

def gestion_de_lequipe():
    conseils = [
        "Assurez-vous d'équilibrer votre équipe avec des attaquants rapides et des milieux de terrain solides.",
        "Investissez dans de jeunes talents pour le futur de votre équipe.",
        "N'oubliez pas de gérer la condition physique de vos joueurs, utilisez le banc de touche à bon escient.",
        "Soyez stratégique dans vos transferts, recherchez des joueurs dont les contrats expirent bientôt."
    ]
    return random.choice(conseils)

def techniques_de_tir():
    conseils = [
        "Utilisez le tir placé (R1/RB + Tir) pour des tirs plus précis.",
        "Pour les frappes de loin, maintenez la touche de tir enfoncée plus longtemps.",
        "Apprenez à utiliser les coups francs en pratiquant dans le mode d'entraînement.",
        "Faites attention à la position de votre joueur avant de tirer pour maximiser vos chances de marquer."
    ]
    return random.choice(conseils)

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-4) : ")
        
        if choix == '1':
            print("Conseil de jeu : ", conseils_de_jeu())
        elif choix == '2':
            print("Conseil de gestion de l'équipe : ", gestion_de_lequipe())
        elif choix == '3':
            print("Conseil de techniques de tir : ", techniques_de_tir())
        elif choix == '4':
            print("Merci d'utiliser le script ! À bientôt.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
python fifa_tips.py
import random

def afficher_menu():
    print("\n=== Conseils pour FIFA 25 ===")
    print("1. Conseils de jeu")
    print("2. Gestion de l'équipe")
    print("3. Techniques de tir")
    print("4. Joueurs à acheter")
    print("5. SBC recommandés")
    print("6. Meilleures tactiques")
    print("7. Quitter")

def conseils_de_jeu():
    conseils = [
        "Utilisez la touche de sprint avec parcimonie pour éviter de perdre le ballon.",
        "Maîtrisez le dribble pour contourner les défenseurs adverses.",
        "Jouez en équipe et utilisez les passes en profondeur pour créer des occasions.",
        "Faites attention à votre positionnement défensif pour éviter les contre-attaques."
    ]
    return random.choice(conseils)

def gestion_de_lequipe():
    conseils = [
        "Assurez-vous d'équilibrer votre équipe avec des attaquants rapides et des milieux de terrain solides.",
        "Investissez dans de jeunes talents pour le futur de votre équipe.",
        "N'oubliez pas de gérer la condition physique de vos joueurs, utilisez le banc de touche à bon escient.",
        "Soyez stratégique dans vos transferts, recherchez des joueurs dont les contrats expirent bientôt."
    ]
    return random.choice(conseils)

def techniques_de_tir():
    conseils = [
        "Utilisez le tir placé (R1/RB + Tir) pour des tirs plus précis.",
        "Pour les frappes de loin, maintenez la touche de tir enfoncée plus longtemps.",
        "Apprenez à utiliser les coups francs en pratiquant dans le mode d'entraînement.",
        "Faites attention à la position de votre joueur avant de tirer pour maximiser vos chances de marquer."
    ]
    return random.choice(conseils)

def joueurs_a_acheter():
    joueurs = [
        "Jude Bellingham (Real Madrid) - Milieu talentueux avec un excellent potentiel.",
        "Erling Haaland (Manchester City) - Attaquant rapide et puissant, parfait pour marquer.",
        "Kylian Mbappé (Paris SG) - Un des meilleurs attaquants, idéal pour les contre-attaques.",
        "Rúben Dias (Manchester City) - Défenseur solide pour renforcer votre défense.",
        "Pedri (FC Barcelone) - Jeune milieu de terrain créatif avec un grand potentiel."
    ]
    return random.choice(joueurs)

def sbc_recommandes():
    sbc = [
        "SBC Player of the Month - Souvent des joueurs avec des stats améliorées, idéal à réaliser.",
        "SBC Icon - Échangez des joueurs pour obtenir des icônes légendaires, souvent très appréciées.",
        "SBC Liga - Pour obtenir un joueur de la Liga, échangez des joueurs de cette ligue.",
        "SBC Nationalité - Créez des équipes avec des joueurs de la même nationalité pour de bons packs."
    ]
    return random.choice(sbc)

def meilleures_tactiques():
    tactiques = [
        "4-3-3 : Formation équilibrée avec de bonnes options offensives et défensives.",
        "4-2-3-1 : Idéale pour un milieu de terrain solide et des ailes dynamiques.",
        "3-5-2 : Permet de contrôler le milieu de terrain avec des attaques rapides.",
        "5-3-2 : Défense solide avec des contre-attaques rapides.",
        "4-4-2 : Simple mais efficace, bonne pour un jeu de passes."
    ]
    return random.choice(tactiques)

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-7) : ")
        
        if choix == '1':
            print("Conseil de jeu : ", conseils_de_jeu())
        elif choix == '2':
            print("Conseil de gestion de l'équipe : ", gestion_de_lequipe())
        elif choix == '3':
            print("Conseil de techniques de tir : ", techniques_de_tir())
        elif choix == '4':
            print("Joueur à acheter : ", joueurs_a_acheter())
        elif choix == '5':
            print("SBC recommandé : ", sbc_recommandes())
        elif choix == '6':
            print("Meilleure tactique : ", meilleures_tactiques())
        elif choix == '7':
            print("Merci d'utiliser le script ! À bientôt.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
python fifa_tips.py
