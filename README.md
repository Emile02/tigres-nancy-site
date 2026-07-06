# 🐯 Tigres de Nancy — Site officiel

Site vitrine du **S.L.U.C. Tigres Nancy Football Américain** (Division 2), en HTML/CSS/JS statique — aucun framework, aucune dépendance, hébergeable gratuitement sur GitHub Pages.

## Structure du projet

```
├── index.html            # Page d'accueil
├── equipe.html           # Roster D2
├── calendrier.html       # Calendrier & résultats
├── club.html             # Histoire, staff, comité de direction
├── inscription.html      # Inscriptions saison 2026-2027
├── partenaires.html      # Partenaires / sponsors
├── actualites.html       # Actualités du club
├── assets/
│   ├── css/style.css     # Toute la charte graphique (variables en haut du fichier)
│   ├── js/main.js        # Menu mobile + animations au scroll
│   └── img/              # Vos photos, logos, visuels
└── tools/
    └── build_pages.py    # Générateur des pages secondaires (header/footer communs)
```

## Charte graphique

Définie en variables CSS en haut de `assets/css/style.css` :

| Variable | Valeur | Usage |
|---|---|---|
| `--noir` | `#0c0b0a` | Fond principal |
| `--orange` | `#f26b1d` | Couleur du club |
| `--orange-vif` | `#ff8a2a` | Survols, accents |
| `--creme` | `#f3eee6` | Texte |

Typographies (Google Fonts) : **Anton** pour les titres, **Barlow** pour le texte, **Barlow Condensed** pour les labels.

## Mettre à jour le contenu

- **Matchs** : section « Prochains matchs » dans `index.html` + tableau dans `calendrier.html`
- **Roster** : blocs `.joueur` dans `equipe.html`
- **Partenaires** : blocs `.partenaire` — remplacer le texte par `<img src="assets/img/logo-partenaire.png" alt="Nom">`
- **Lien d'inscription** : bouton « S'inscrire en ligne » dans `inscription.html` → mettre le lien SportEasy/HelloAsso
- **Réseaux sociaux** : liens dans la topbar et le footer (actuellement génériques)
- **Email de contact** : `contact@tigres-nancy.fr` (placeholder, à remplacer partout)

### Modifier le header/footer sur toutes les pages secondaires d'un coup

Les pages secondaires sont générées par `tools/build_pages.py`. Modifiez `HEADER`, `FOOTER` ou le contenu des pages dans ce fichier, puis :

```bash
python3 tools/build_pages.py
```

(`index.html` est indépendant du générateur — à modifier directement.)

## Tester en local

Ouvrez simplement `index.html` dans un navigateur, ou lancez un petit serveur :

```bash
python3 -m http.server 8000
# puis http://localhost:8000
```

## Mettre en ligne (GitHub Pages, gratuit)

1. Créez un dépôt sur GitHub (ex. `tigres-nancy-site`)
2. Poussez ce projet :
   ```bash
   git remote add origin https://github.com/VOTRE_COMPTE/tigres-nancy-site.git
   git push -u origin main
   ```
3. Sur GitHub : **Settings → Pages → Source : Deploy from a branch → main / (root)**
4. Le site sera en ligne sur `https://VOTRE_COMPTE.github.io/tigres-nancy-site/`
5. (Optionnel) Ajoutez un domaine personnalisé type `tigres-nancy.fr` dans les mêmes réglages

## À faire

- [ ] Remplacer les placeholders (roster, staff, matchs, partenaires)
- [ ] Ajouter le vrai logo du club (`assets/img/`) à la place du badge SVG
- [ ] Ajouter des photos de matchs et d'entraînements
- [ ] Brancher le lien d'inscription SportEasy/HelloAsso
- [ ] Mettre les vrais liens réseaux sociaux et l'email de contact
- [ ] Compléter le calendrier D2 2026-2027 dès publication
