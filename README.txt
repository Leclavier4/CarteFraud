 README : Système de Détection de Fraude par Carte de Crédit

 Description du Projet
Ce projet propose une interface utilisateur interactive pour un système de détection de fraude par carte de crédit. Il simule la détection de transactions frauduleuses en fonction des données saisies par l'utilisateur. Bien que simplifiée, l'application offre une base pour une exploration plus approfondie des concepts liés à la sécurité financière et à la détection de fraude.


 Fonctionnalités Principales
1. Saisie des informations de transaction :
   - Numéro de carte de crédit
   - Montant de la transaction
   - Type de transaction (achat, retrait, transfert)
   - Heure de la transaction

2. Analyse de fraude simulée :
   - Le système vérifie les données saisies et utilise une logique simple pour déterminer si une transaction est potentiellement frauduleuse (exemple : montant > 1000).

3. Affichage des résultats :
   - Résultat clair et visuel dans l'interface :
     - "Fraude détectée !" (texte en rouge)
     - "Transaction légitime." (texte en vert)

4. Interface conviviale :
   - Utilisation de la bibliothèque Tkinter pour une interface graphique simple et accessible.

Instructions d'Utilisation

1. Prérequis :

   - Python 3.x installé.
   - Bibliothèque Tkinter (inclus par défaut avec Python standard).
   - Installer ttkbootrap  (pip install ttkbootstrap==1.10.1)
   
2. Exécution du programme :

   - Télécharger le fichier source.
   - Ouvrir un terminal ou une invite de commande.
   - Exécuter la commande :
     python <nom_du_fichier>.py

3. Utilisation de l'application :

   - Remplissez les champs obligatoires dans l'interface.
   - Cliquez sur le bouton "Analyser" pour vérifier la transaction.
   - Consultez le résultat affiché.


 Documentation Supplémentaire:
 Logique de Détection:

- Montant > 1000 : Les transactions au-delà de ce seuil sont considérées comme frauduleuses dans cette version simplifiée.
- Extension possible : La logique peut être remplacée par un modèle d'apprentissage automatique entraîné sur des données réelles.

 Technologies Utilisées:
- Python : Langage principal pour le développement.
- Tkinter : Création de l'interface utilisateur.

 Références:
- Documentation officielle de Python : [https://docs.python.org/](https://docs.python.org/)
- Tutoriels Tkinter : [https://tkdocs.com/](https://tkdocs.com/)
- ttkbootstrap : [https://ttkbootstrap.readthedocs.io/en/latest/themes/](https://ttkbootstrap.readthedocs.io/en/latest/themes/)
- Concepts de détection de fraude : Articles et recherches sur les modèles ML appliqués à la finance.

