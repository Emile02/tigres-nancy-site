#!/usr/bin/env python3
"""
Générateur de pages — Tigres de Nancy
Usage : python3 tools/build_pages.py
Génère les pages secondaires à partir d'un header/footer commun.
Modifiez HEADER/FOOTER ici pour mettre à jour toutes les pages d'un coup.
"""

HEADER = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Tigres de Nancy — Football Américain</title>
  <meta name="description" content="{description}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600&family=Barlow+Condensed:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

  <div class="topbar">
    <div class="container">
      <span class="topbar__devise">Une ville. Une meute. Les Tigres.</span>
      <div class="topbar__social">
        <a href="https://www.instagram.com/" aria-label="Instagram">Instagram</a>
        <a href="https://www.facebook.com/" aria-label="Facebook">Facebook</a>
        <a href="https://www.youtube.com/" aria-label="YouTube">YouTube</a>
        <a href="https://www.tiktok.com/" aria-label="TikTok">TikTok</a>
      </div>
    </div>
  </div>

  <header class="header">
    <div class="container">
      <a class="logo" href="index.html">
        <svg class="logo__badge" viewBox="0 0 44 44" aria-hidden="true">
          <polygon points="22,2 42,12 42,32 22,42 2,32 2,12" fill="#16130f" stroke="#f26b1d" stroke-width="2"/>
          <path d="M12 12 L20 32 M19 10 L26 32 M27 10 L34 28" stroke="#f26b1d" stroke-width="3.5" stroke-linecap="round" fill="none"/>
        </svg>
        <span>Tigres <em>de Nancy</em></span>
      </a>

      <button class="burger" aria-expanded="false" aria-controls="nav-principale">Menu</button>

      <nav class="nav" id="nav-principale" aria-label="Navigation principale">
        <div class="nav__item">
          <button class="nav__parent" aria-haspopup="true">Équipe D2</button>
          <div class="nav__sous">
            <a href="equipe.html"{cur_equipe}>Roster</a>
            <a href="calendrier.html"{cur_calendrier}>Calendrier &amp; résultats</a>
          </div>
        </div>
        <div class="nav__item">
          <button class="nav__parent" aria-haspopup="true">Le club</button>
          <div class="nav__sous">
            <a href="club.html"{cur_club}>Histoire &amp; valeurs</a>
            <a href="club.html#staff">Staff</a>
            <a href="club.html#bureau">Comité de direction</a>
          </div>
        </div>
        <a href="actualites.html"{cur_actualites}>Actualités</a>
        <a href="partenaires.html"{cur_partenaires}>Partenaires</a>
        <a class="btn btn--plein" href="inscription.html" style="padding:10px 22px;">S'inscrire</a>
      </nav>
    </div>
  </header>

  <section class="hero" style="min-height:auto;">
    <div class="container">
      <div class="hero__inner" style="padding:64px 0 72px;">
        <span class="eyebrow">{eyebrow}</span>
        <h1 style="font-size:clamp(2.4rem,6vw,4.6rem);margin-top:14px;">{page_h1}</h1>
      </div>
    </div>
  </section>
"""

FOOTER = """
  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div>
          <h4>Tigres de Nancy</h4>
          <p>S.L.U.C. Tigres Nancy Football Américain<br>Club de football américain — Division 2<br>Nancy, Meurthe-et-Moselle</p>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:contact@tigres-nancy.fr">contact@tigres-nancy.fr</a></li>
            <li><a href="inscription.html">S'inscrire</a></li>
            <li><a href="partenaires.html">Devenir partenaire</a></li>
          </ul>
        </div>
        <div>
          <h4>Liens rapides</h4>
          <ul>
            <li><a href="equipe.html">Roster D2</a></li>
            <li><a href="calendrier.html">Calendrier</a></li>
            <li><a href="actualites.html">Actualités</a></li>
            <li><a href="club.html">Le club</a></li>
          </ul>
        </div>
        <div>
          <h4>Suivez-nous</h4>
          <ul>
            <li><a href="https://www.instagram.com/">Instagram</a></li>
            <li><a href="https://www.facebook.com/">Facebook</a></li>
            <li><a href="https://www.youtube.com/">YouTube</a></li>
            <li><a href="https://www.tiktok.com/">TikTok</a></li>
          </ul>
        </div>
      </div>
      <div class="footer__legal">
        <span>© 2026 Tigres de Nancy — Tous droits réservés</span>
        <span>Association loi 1901</span>
      </div>
    </div>
  </footer>

  <script src="assets/js/main.js"></script>
</body>
</html>
"""

PAGES = {
    "equipe.html": {
        "title": "Roster D2",
        "description": "Le roster de l'équipe senior des Tigres de Nancy, engagée en Division 2.",
        "eyebrow": "Équipe D2",
        "page_h1": "Le roster des <em>Tigres</em>",
        "current": "equipe",
        "body": """
  <section class="section">
    <div class="container">
      <div class="section__head reveal">
        <h2>Effectif 2026–2027</h2>
        <p class="muted">Remplacez les fiches ci-dessous par vos joueurs (numéro, nom, poste). Chaque fiche est un bloc <code>.joueur</code> — dupliquez-le autant de fois que nécessaire.</p>
      </div>
      <div class="roster">
        <article class="joueur reveal"><span class="numero">#00</span><p class="nom">Prénom Nom</p><p class="poste">Quarterback</p></article>
        <article class="joueur reveal"><span class="numero">#00</span><p class="nom">Prénom Nom</p><p class="poste">Running back</p></article>
        <article class="joueur reveal"><span class="numero">#00</span><p class="nom">Prénom Nom</p><p class="poste">Wide receiver</p></article>
        <article class="joueur reveal"><span class="numero">#00</span><p class="nom">Prénom Nom</p><p class="poste">Wide receiver</p></article>
        <article class="joueur reveal"><span class="numero">#00</span><p class="nom">Prénom Nom</p><p class="poste">Offensive line</p></article>
        <article class="joueur reveal"><span class="numero">#00</span><p class="nom">Prénom Nom</p><p class="poste">Defensive line</p></article>
        <article class="joueur reveal"><span class="numero">#00</span><p class="nom">Prénom Nom</p><p class="poste">Linebacker</p></article>
        <article class="joueur reveal"><span class="numero">#00</span><p class="nom">Prénom Nom</p><p class="poste">Defensive back</p></article>
      </div>
    </div>
  </section>
""",
    },
    "calendrier.html": {
        "title": "Calendrier & résultats",
        "description": "Calendrier des matchs et résultats des Tigres de Nancy en Division 2, saison 2026-2027.",
        "eyebrow": "Saison 2026–2027",
        "page_h1": "Calendrier &amp; <em>résultats</em>",
        "current": "calendrier",
        "body": """
  <section class="section">
    <div class="container">
      <div class="section__head reveal">
        <h2>Matchs de la saison</h2>
        <p class="muted">Complétez le tableau dès la publication du calendrier officiel D2. Ajoutez le score dans la colonne résultat une fois le match joué.</p>
      </div>
      <div class="reveal" style="overflow-x:auto;">
        <table class="tableau">
          <thead>
            <tr><th>Journée</th><th>Date</th><th>Match</th><th>Lieu</th><th>Résultat</th></tr>
          </thead>
          <tbody>
            <tr><td>J1</td><td>À confirmer</td><td>Tigres de Nancy vs —</td><td>Domicile</td><td>—</td></tr>
            <tr><td>J2</td><td>À confirmer</td><td>— vs Tigres de Nancy</td><td>Extérieur</td><td>—</td></tr>
            <tr><td>J3</td><td>À confirmer</td><td>Tigres de Nancy vs —</td><td>Domicile</td><td>—</td></tr>
            <tr><td>J4</td><td>À confirmer</td><td>— vs Tigres de Nancy</td><td>Extérieur</td><td>—</td></tr>
            <tr><td>J5</td><td>À confirmer</td><td>Tigres de Nancy vs —</td><td>Domicile</td><td>—</td></tr>
            <tr><td>J6</td><td>À confirmer</td><td>— vs Tigres de Nancy</td><td>Extérieur</td><td>—</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
""",
    },
    "club.html": {
        "title": "Le club",
        "description": "Histoire, valeurs, staff et comité de direction des Tigres de Nancy, club de football américain en Division 2.",
        "eyebrow": "Le club",
        "page_h1": "Histoire &amp; <em>valeurs</em>",
        "current": "club",
        "body": """
  <section class="section">
    <div class="container">
      <div class="grille-2">
        <div class="reveal">
          <h2 style="margin-bottom:20px;">Le club des Tigres</h2>
          <p class="muted">Les Tigres de Nancy (S.L.U.C. Tigres Nancy Football Américain) sont le club de football américain de la ville de Nancy. Engagé en Division 2, le club porte fièrement le noir et l'orange et nourrit une ambition régionale forte dans l'Est de la France.</p>
          <p class="muted" style="margin-top:16px;">Formation des jeunes, développement du flag football, engagement bénévole : le club repose sur une communauté soudée, la meute, qui fait vivre le football américain en Lorraine.</p>
          <p class="muted" style="margin-top:16px;"><em>Complétez cette section avec l'histoire détaillée du club : dates de fondation, titres, montées, moments marquants.</em></p>
        </div>
        <div class="encart reveal">
          <h3>Nos valeurs</h3>
          <ul>
            <li><strong>Combativité</strong> — sur le terrain comme en dehors</li>
            <li><strong>Meute</strong> — personne ne joue seul</li>
            <li><strong>Formation</strong> — faire grandir chaque tigre</li>
            <li><strong>Ancrage</strong> — Nancy et le Grand Est au cœur</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt" id="staff">
    <div class="container">
      <div class="section__head reveal">
        <span class="eyebrow">Encadrement</span>
        <h2>Le staff</h2>
        <p class="muted">Ajoutez ici vos coachs : head coach, coordinateurs offensif et défensif, coachs de position.</p>
      </div>
      <div class="roster">
        <article class="joueur reveal"><p class="nom">Prénom Nom</p><p class="poste">Head coach</p></article>
        <article class="joueur reveal"><p class="nom">Prénom Nom</p><p class="poste">Coordinateur offensif</p></article>
        <article class="joueur reveal"><p class="nom">Prénom Nom</p><p class="poste">Coordinateur défensif</p></article>
        <article class="joueur reveal"><p class="nom">Prénom Nom</p><p class="poste">Coach receveurs</p></article>
      </div>
    </div>
  </section>

  <section class="section" id="bureau">
    <div class="container">
      <div class="section__head reveal">
        <span class="eyebrow">Association</span>
        <h2>Comité de direction</h2>
      </div>
      <div class="roster">
        <article class="joueur reveal"><p class="nom">Prénom Nom</p><p class="poste">Président·e</p></article>
        <article class="joueur reveal"><p class="nom">Prénom Nom</p><p class="poste">Trésorier·ère</p></article>
        <article class="joueur reveal"><p class="nom">Prénom Nom</p><p class="poste">Secrétaire</p></article>
        <article class="joueur reveal"><p class="nom">Prénom Nom</p><p class="poste">Communication</p></article>
      </div>
    </div>
  </section>
""",
    },
    "inscription.html": {
        "title": "Inscription",
        "description": "Rejoignez les Tigres de Nancy : inscriptions ouvertes pour la saison 2026-2027, football américain et flag, toutes catégories.",
        "eyebrow": "Saison 2026–2027",
        "page_h1": "Rejoins la <em>meute</em>",
        "current": "inscription",
        "body": """
  <section class="section">
    <div class="container">
      <div class="grille-2">
        <div class="reveal">
          <h2 style="margin-bottom:20px;">Comment s'inscrire ?</h2>
          <p class="muted">Les inscriptions pour la saison 2026–2027 se font en ligne. Que tu sois débutant complet ou joueur confirmé, il y a une place pour toi chez les Tigres.</p>
          <p style="margin:28px 0;"><a class="btn btn--plein" href="#">S'inscrire en ligne</a></p>
          <p class="muted"><em>Remplacez le lien du bouton ci-dessus par votre lien SportEasy ou HelloAsso d'inscription.</em></p>
        </div>
        <div style="display:flex;flex-direction:column;gap:24px;">
          <div class="encart reveal">
            <h3>Documents nécessaires</h3>
            <ul>
              <li><strong>Certificat médical</strong> de non contre-indication à la pratique du football américain en compétition</li>
              <li><strong>Photo d'identité</strong> récente</li>
              <li><strong>Autorisation parentale</strong> pour les mineurs</li>
            </ul>
          </div>
          <div class="encart reveal">
            <h3>Entraînements</h3>
            <ul>
              <li><strong>Lieu</strong> — à compléter</li>
              <li><strong>Horaires</strong> — à compléter</li>
              <li><strong>Séance d'essai</strong> — gratuite, matériel prêté</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
""",
    },
    "partenaires.html": {
        "title": "Partenaires",
        "description": "Les partenaires des Tigres de Nancy. Devenez sponsor du club et associez votre image au football américain en Lorraine.",
        "eyebrow": "Partenaires",
        "page_h1": "Ils font rugir les <em>Tigres</em>",
        "current": "partenaires",
        "body": """
  <section class="section">
    <div class="container">
      <div class="section__head reveal">
        <h2>Nos partenaires</h2>
        <p class="muted">Remplacez chaque bloc par le logo du partenaire (balise <code>&lt;img&gt;</code> dans le bloc <code>.partenaire</code>) et un lien vers son site.</p>
      </div>
      <div class="partenaires reveal">
        <a class="partenaire" href="#">Votre logo</a>
        <a class="partenaire" href="#">Votre logo</a>
        <a class="partenaire" href="#">Votre logo</a>
        <a class="partenaire" href="#">Votre logo</a>
        <a class="partenaire" href="#">Votre logo</a>
        <a class="partenaire" href="#">Votre logo</a>
        <a class="partenaire" href="#">Votre logo</a>
        <a class="partenaire" href="#">Votre logo</a>
      </div>
    </div>
  </section>

  <section class="cta-inscription">
    <div class="container">
      <h2>Envie d'associer votre marque aux Tigres ?</h2>
      <a class="btn" href="mailto:contact@tigres-nancy.fr">Nous contacter</a>
    </div>
  </section>
""",
    },
    "actualites.html": {
        "title": "Actualités",
        "description": "Toute l'actualité des Tigres de Nancy : résultats, événements, vie du club.",
        "eyebrow": "Actualités",
        "page_h1": "La vie du <em>club</em>",
        "current": "actualites",
        "body": """
  <section class="section">
    <div class="container">
      <div class="section__head reveal">
        <h2>Dernières actualités</h2>
        <p class="muted">Ajoutez un bloc <code>.equipe</code> par article. Vous pouvez aussi relier chaque bloc vers un post Instagram ou Facebook.</p>
      </div>
      <div class="equipes">
        <article class="equipe reveal">
          <h3>Titre de l'article</h3>
          <p>Résumé de l'actualité en deux ou trois lignes. Date, contexte, lien vers le détail.</p>
          <a class="lien" href="#">Lire la suite →</a>
        </article>
        <article class="equipe reveal">
          <h3>Titre de l'article</h3>
          <p>Résumé de l'actualité en deux ou trois lignes. Date, contexte, lien vers le détail.</p>
          <a class="lien" href="#">Lire la suite →</a>
        </article>
        <article class="equipe reveal">
          <h3>Titre de l'article</h3>
          <p>Résumé de l'actualité en deux ou trois lignes. Date, contexte, lien vers le détail.</p>
          <a class="lien" href="#">Lire la suite →</a>
        </article>
      </div>
    </div>
  </section>
""",
    },
}


def build():
    import pathlib
    root = pathlib.Path(__file__).resolve().parent.parent
    for filename, page in PAGES.items():
        cur = {f"cur_{k}": "" for k in ["equipe", "calendrier", "club", "actualites", "partenaires"]}
        key = f"cur_{page['current']}"
        if key in cur:
            cur[key] = ' aria-current="page"'
        html = HEADER.format(
            title=page["title"],
            description=page["description"],
            eyebrow=page["eyebrow"],
            page_h1=page["page_h1"],
            **cur,
        ) + page["body"] + FOOTER
        (root / filename).write_text(html, encoding="utf-8")
        print(f"✔ {filename}")


if __name__ == "__main__":
    build()
