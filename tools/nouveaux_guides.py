# Nouveaux guides et pages par type de travaux (octobre 2026).
# Importé par build.py : chaque entrée est passée à article() ou page().

SRC = '<p style="font-size: 15px !important; color: #5b6784 !important;">'

# ---------------------------------------------------------------- Guides
GUIDES = []
GUIDE_FAQS = {}

# ---------- Décennale
GUIDES.append(dict(
 slug="guide-verifier-assurance-decennale",
 title="Assurance décennale : vérifier l'attestation d'un artisan",
 h1="Assurance décennale : comment vérifier l'attestation de votre artisan",
 desc="Activités couvertes, validité, assureur, zone couverte : les 5 points à contrôler sur l'attestation décennale avant de signer un devis.",
 lead="Une attestation décennale jointe au devis ne prouve pas grand-chose si elle couvre une autre activité, une autre période ou une autre entreprise. Voici comment la lire en deux minutes.",
 readtime=6,
 body='''<h2>À quoi sert la garantie décennale</h2>
<p>Pendant <strong>10 ans après la réception</strong> des travaux, l'entreprise est responsable des dommages qui compromettent la solidité de l'ouvrage ou le rendent impropre à son usage : infiltrations par la toiture, fissures structurelles, étanchéité de douche défaillante qui ruine un plancher. Son assurance décennale paie les réparations, même si l'entreprise a disparu entre-temps.</p>
<p>Elle s'ajoute à deux autres garanties qui démarrent aussi à la réception : la <strong>garantie de parfait achèvement</strong> (1 an, tous les défauts signalés) et la <strong>garantie de bon fonctionnement</strong> (2 ans minimum, pour les équipements dissociables comme un radiateur ou une porte intérieure).</p>
<h2>L'attestation doit être jointe au devis</h2>
<p>Depuis le 1er juillet 2016, une entreprise soumise à l'assurance décennale doit <strong>joindre son attestation</strong> à ses devis et factures, selon un modèle fixé par arrêté. Le devis lui-même doit mentionner l'assurance souscrite, les coordonnées de l'assureur et la couverture géographique.</p>
<div class="note"><p><strong>Pas d'attestation, pas de signature.</strong> Une entreprise qui ne la fournit pas, ou qui promet de l'envoyer « après », ne respecte pas une obligation légale. C'est un signal d'alerte, quel que soit le prix.</p></div>
<h2>Les 5 points à vérifier</h2>
<ol><li><strong>Le nom de l'assuré</strong> : c'est exactement l'entreprise qui signe le devis (même raison sociale, même numéro SIREN). Une attestation au nom d'un confrère ou d'une ancienne société ne vous couvre pas.</li>
<li><strong>Les activités couvertes</strong> : l'attestation liste des activités précises. Une attestation « plomberie » ne couvre pas la pose de carrelage ou la reprise d'une charpente. Chaque poste important du devis doit correspondre à une activité listée.</li>
<li><strong>La période de validité</strong> : c'est l'assurance en vigueur <strong>à l'ouverture du chantier</strong> qui compte. Si l'attestation expire avant le démarrage prévu, demandez la nouvelle.</li>
<li><strong>La couverture géographique</strong> : elle porte souvent sur la France métropolitaine seule. En outre-mer, vérifiez qu'elle inclut bien le territoire de vos travaux.</li>
<li><strong>L'assureur</strong> : son nom et ses coordonnées doivent figurer. Méfiez-vous des assureurs étrangers inconnus : plusieurs ont fait faillite ces dernières années, laissant les clients sans couverture. En cas de doute, appelez l'assureur avec le numéro de contrat.</li></ol>
<h2>Les travaux qui ne sont pas concernés</h2>
<p>Tous les travaux ne relèvent pas de la décennale. La peinture purement décorative ou le simple entretien, par exemple, n'en dépendent pas forcément. En revanche, dès que les travaux touchent au clos et couvert, à la structure, à l'étanchéité ou à des équipements indissociables du bâti (plomberie encastrée, chape, carrelage collé), l'attestation est attendue.</p>
<h2>Et l'assurance dommages-ouvrage ?</h2>
<p>C'est l'assurance du <strong>maître d'ouvrage</strong>, donc la vôtre. Elle préfinance les réparations relevant de la décennale sans attendre de savoir qui est responsable. Elle est obligatoire avant des travaux de construction, y compris pour un particulier, mais le particulier qui fait construire pour lui-même n'encourt pas de sanction pénale s'il ne la souscrit pas. En pratique, elle concerne la construction d'une maison, les extensions et les rénovations lourdes (structure, étanchéité). Son coût est élevé : posez la question pour ces chantiers-là.</p>
<h2>Ce que je vérifie sur votre devis</h2>
<p>La présence de l'attestation, la concordance entre l'entreprise, les activités couvertes et les postes du devis, et les dates de validité. Voir aussi <a href="guide-mentions-obligatoires-devis.html">les mentions obligatoires d'un devis</a> et <a href="modeles-messages-artisan.html">le message type pour demander l'attestation</a>.</p>
''' + SRC + '''Article d'information générale, à jour au 27 octobre 2026. Sources : articles 1792 à 1792-6 du Code civil, articles L241-1, L242-1 et L243-2 du Code des assurances, article 22-2 de la loi n° 96-603 du 5 juillet 1996, arrêté du 5 janvier 2016 (modèle d'attestation), INC (inc-conso.fr).</p>''',
))
GUIDE_FAQS["guide-verifier-assurance-decennale"] = [
 ("L'attestation décennale est-elle obligatoire sur un devis ?",
  "Oui, pour les travaux soumis à l'assurance décennale : depuis le 1er juillet 2016, l'attestation doit être jointe aux devis et aux factures, et le devis doit mentionner l'assureur et la couverture géographique."),
 ("Quelle date de validité compte sur l'attestation ?",
  "Celle de l'ouverture du chantier. L'assurance en vigueur au démarrage des travaux couvre l'ouvrage pendant 10 ans après la réception, même si l'entreprise change d'assureur ou cesse son activité ensuite."),
 ("Que faire si l'artisan refuse de fournir son attestation ?",
  "Ne signez pas. La fournir est une obligation, pas une faveur. Un refus ou un « je vous l'envoie plus tard » doit vous faire choisir une autre entreprise."),
]

# ---------- Négocier
GUIDES.append(dict(
 slug="guide-negocier-devis-travaux",
 title="Devis de travaux trop cher : comment le négocier",
 h1="Devis de travaux trop cher : comment le négocier intelligemment",
 desc="Détailler les forfaits, comparer poste par poste, vérifier TVA et aides, revoir l'échéancier : les leviers pour faire baisser un devis.",
 lead="Demander « un geste » sur le total marche rarement, et quand ça marche, la différence se retrouve souvent ailleurs. On négocie mieux un devis quand on sait ligne par ligne ce qu'on paie.",
 readtime=6,
 body='''<h2>D'abord, savoir ce que vous payez</h2>
<p>On ne négocie pas un forfait. Pour les travaux de dépannage, de réparation et d'entretien, la réglementation impose un devis détaillé : prestations, quantités, prix unitaires, taux de TVA. Pour les autres travaux, rien ne vous empêche d'exiger le même niveau de détail avant de signer. Une ligne « Rénovation salle de bain : 9 800 € » doit devenir une dizaine de postes chiffrés.</p>
<div class="note"><p><strong>Le bon réflexe :</strong> demandez le détail <em>avant</em> de parler prix. C'est en voyant les quantités que l'on repère une surface surestimée ou un poste compté deux fois.</p></div>
<h2>Comparer poste par poste, pas les totaux</h2>
<p>Deux devis à 12 000 € et 14 000 € ne décrivent souvent pas les mêmes travaux. Mettez-les côte à côte avec <a href="comparer-ses-devis.html">le tableau comparatif gratuit</a> : vous verrez qu'un des deux oublie la dépose, l'autre compte une étanchéité complète. Le moins cher n'est pas forcément le plus avantageux une fois les oublis réintégrés.</p>
<p>Un écart de prix sur un même poste, à prestation égale, est en revanche un vrai argument : « L'autre entreprise chiffre la même faïence, même surface, 20 % moins cher. Pouvez-vous vous aligner sur ce poste ? »</p>
<h2>Vérifier la TVA et les aides avant de négocier</h2>
<p>Un taux de TVA mal appliqué peut peser plus lourd qu'une remise. Dans un logement achevé depuis plus de 2 ans, la plupart des travaux relèvent du taux de 10 %, et la rénovation énergétique de 5,5 %, sous réserve d'une mention que vous certifiez sur le devis ou la facture. Détails dans <a href="guide-tva-travaux-renovation.html">le guide TVA</a>.</p>
<p>Pour les travaux d'économie d'énergie, vérifiez aussi les aides (MaPrimeRénov', primes CEE) et la qualification RGE de l'entreprise, qui conditionne ces aides. Leurs règles ont beaucoup changé en 2026 : faites le point avec un conseiller France Rénov', gratuit, avant de signer.</p>
<h2>Les leviers qui fonctionnent</h2>
<ul><li><strong>Ajuster le périmètre</strong> : faire vous-même la dépose ou la peinture finale, conserver un équipement en bon état, choisir une gamme de faïence plus courante.</li>
<li><strong>Grouper les travaux</strong> : un chantier plus gros, ou deux lots confiés à la même entreprise, réduit ses frais fixes (déplacements, installation).</li>
<li><strong>Être souple sur la date</strong> : une entreprise qui a un trou dans son planning acceptera plus facilement un effort.</li>
<li><strong>Négocier les conditions plutôt que le prix</strong> : un acompte plus faible (l'usage est d'environ 30 % à la signature), un échéancier calé sur l'avancement, une retenue de garantie de 5 % au plus, prévue au devis et consignée chez un tiers (voir <a href="guide-reception-travaux-reserves.html">le guide sur la réception</a>). Voir <a href="guide-acompte-paiement-devis-travaux.html">le guide sur l'acompte</a>.</li></ul>
<h2>Ce qu'il ne faut pas négocier</h2>
<p>L'étanchéité, la ventilation, la protection électrique, l'épaisseur d'isolant : ce sont les postes qui coûtent cher à reprendre et que l'entreprise sera tentée de rogner si vous serrez trop le prix global. Une remise obtenue en supprimant un poste indispensable n'est pas une économie.</p>
<h2>Et si l'entreprise refuse ?</h2>
<p>Un refus argumenté n'est pas mauvais signe : il montre souvent que le prix a été calculé, pas gonflé pour laisser de la marge à la négociation. Si l'écart reste important avec d'autres devis à prestation égale, demandez simplement ce qui le justifie, avec <a href="modeles-messages-artisan.html">les modèles de messages</a>.</p>
<h2>Ce que je vérifie sur votre devis</h2>
<p>Les quantités, les prix unitaires comparés à des ordres de grandeur récents, la TVA, les oublis et les postes à faire préciser. Le rapport se termine par les questions à poser à l'artisan, que vous pouvez utiliser telles quelles pour négocier.</p>
''' + SRC + '''Article d'information générale, à jour au 27 octobre 2026. Sources : arrêté du 24 janvier 2017 relatif à la publicité des prix des prestations de dépannage, de réparation et d'entretien dans le secteur du bâtiment, article L111-1 du Code de la consommation, articles 278-0 bis A et 279-0 bis du Code général des impôts, ecologie.gouv.fr (MaPrimeRénov' 2026).</p>''',
))
GUIDE_FAQS["guide-negocier-devis-travaux"] = [
 ("Peut-on négocier un devis de travaux ?",
  "Oui, tant qu'il n'est pas signé. Le plus efficace est de faire détailler les forfaits, de comparer poste par poste avec d'autres devis et d'ajuster le périmètre, plutôt que de demander une remise sur le total."),
 ("Un artisan peut-il faire payer son devis ?",
  "Oui, à condition de vous en informer avant de l'établir. Son montant est souvent déduit si vous signez. Pour un dépannage, le devis doit indiquer s'il est gratuit ou payant, et son prix."),
 ("Quel acompte verser à la signature ?",
  "Il n'existe pas de plafond général pour l'acompte, mais si vous avez signé chez vous, aucun paiement n'est possible pendant 7 jours. L'usage est d'environ 30 % à la signature. Au-delà de 40 à 50 %, demandez pourquoi et proposez un échéancier lié à l'avancement du chantier."),
]

# ---------- Dépassement du devis
GUIDES.append(dict(
 slug="guide-depassement-devis-travaux-supplementaires",
 title="Facture supérieure au devis : les suppléments sont-ils dus ?",
 h1="L'artisan dépasse le devis : que faire face aux travaux supplémentaires",
 desc="Devis signé, forfait, imprévu, avenant écrit : quand un supplément est dû ou non, et les recours si la facture dépasse le devis.",
 lead="Le devis disait 8 000 €, la facture en annonce 9 400 €. Avant de payer ou de refuser, il faut savoir une chose : qu'avez-vous accepté, et par écrit ?",
 readtime=7,
 body='''<h2>Un devis signé engage l'artisan</h2>
<p>Une fois signé, le devis est un <strong>contrat</strong>. L'entreprise ne peut pas modifier seule ni le prix ni le contenu des travaux. Si elle facture plus, c'est à elle de prouver que vous avez accepté ce supplément. Pour un particulier, au-delà de 1 500 €, cette preuve doit en principe être écrite.</p>
<h2>Le marché à forfait : la protection la plus forte</h2>
<p>Quand le devis fixe un <strong>prix global et forfaitaire</strong> pour des travaux décrits précisément, la loi vous protège fortement : en principe, l'entrepreneur ne peut demander aucune augmentation, ni pour la hausse de la main-d'œuvre ou des matériaux, ni pour des changements ou ajouts, <strong>sauf si ces changements ont été autorisés par écrit et leur prix convenu avec vous</strong> (article 1793 du Code civil). Pour une rénovation, les juges vérifient au cas par cas qu'il s'agit bien d'un forfait.</p>
<div class="note"><p><strong>En pratique :</strong> un supplément annoncé à l'oral sur le chantier, puis découvert sur la facture, n'est en principe pas dû dans un marché à forfait. Votre silence ne vaut pas accord.</p></div>
<h2>Devis au métré ou « selon état » : plus de marge pour l'artisan</h2>
<p>Si le devis fixe des <strong>prix unitaires</strong> (au m², au mètre linéaire, à la pièce) plutôt qu'un prix global, la facture suit les quantités réellement exécutées. Elle peut donc dépasser le devis si les quantités augmentent, à condition qu'elles soient justifiées. Les lignes « selon état » ou « hors imprévus » ne sont pas un chèque en blanc, mais elles affaiblissent votre position : c'est pour cela qu'il faut les faire chiffrer avant de signer.</p>
<h2>L'imprévu de chantier</h2>
<p>Une poutre pourrie derrière un doublage, une canalisation en plomb sous un carrelage : les vraies surprises existent. Mais aucun texte ne permet à l'artisan de les facturer de son propre chef. La bonne pratique, et votre protection, c'est :</p>
<ol><li>l'entreprise vous prévient <strong>avant</strong> d'engager les travaux supplémentaires, photos à l'appui ;</li>
<li>elle vous remet un <strong>avenant ou un devis complémentaire chiffré</strong> ;</li>
<li>vous le signez, ou vous le refusez et discutez d'une autre solution.</li></ol>
<p>Une erreur de métré ou de chiffrage de l'entreprise n'est pas un imprévu : c'est à elle de l'assumer.</p>
<h2>Révision de prix : seulement si le devis la prévoit</h2>
<p>Le prix d'un devis ne s'indexe pas automatiquement sur la hausse des matériaux. Une révision n'est possible que si le contrat la prévoit expressément, avec une formule et un indice de référence en lien avec les travaux (les index BT du bâtiment, par exemple). En principe, une telle clause joue aussi à la baisse.</p>
<h2>La facture dépasse le devis : les étapes</h2>
<ol><li><strong>Demandez par écrit le détail</strong> du supplément et le document par lequel vous l'auriez accepté.</li>
<li><strong>Payez ce qui est dû selon le devis</strong> et contestez le reste par écrit, en expliquant pourquoi. Ne bloquez pas l'intégralité sans raison : ce serait vous mettre en tort.</li>
<li><strong>Envoyez une mise en demeure</strong> par lettre recommandée avec accusé de réception si le désaccord persiste.</li>
<li><strong>Saisissez le médiateur de la consommation</strong> de l'entreprise : tout professionnel doit en désigner un et vous communiquer ses coordonnées (site internet, conditions générales, devis ou bon de commande). Il faut d'abord avoir fait une réclamation écrite, et le saisir dans l'année qui suit.</li>
<li><strong>Le conciliateur de justice</strong>, gratuit, est une autre voie. Pour un litige de 5 000 € ou moins, une tentative de règlement amiable est en principe obligatoire avant de saisir le tribunal.</li></ol>
<p>Vous pouvez aussi faire un signalement sur SignalConso : il ne règle pas votre litige, mais il aide la DGCCRF à cibler ses contrôles.</p>
<h2>Ce que je vérifie sur votre devis</h2>
<p>Le type de prix (forfait ou unitaire), les lignes « selon état », « hors imprévus » ou « à définir », et les postes oubliés qui deviendront des suppléments. Chaque rapport les liste avec la question à poser pour les faire chiffrer avant de signer. Voir aussi <a href="modeles-messages-artisan.html">les modèles de messages à l'artisan</a>.</p>
''' + SRC + '''Article d'information générale, à jour au 27 octobre 2026, qui ne remplace pas un conseil juridique sur votre situation. Sources : articles 1103, 1359 et 1793 du Code civil, articles L612-1 et L612-2 du Code de la consommation (médiation), Code de procédure civile (tentative amiable préalable), economie.gouv.fr, inc-conso.fr.</p>''',
))
GUIDE_FAQS["guide-depassement-devis-travaux-supplementaires"] = [
 ("Un artisan peut-il facturer plus cher que le devis signé ?",
  "Pas de lui-même. Dans un marché à forfait, un supplément n'est dû que si vous l'avez autorisé par écrit et que son prix a été convenu avec vous. Avec des prix unitaires, la facture peut suivre les quantités réellement exécutées, à condition qu'elles soient justifiées."),
 ("Un accord oral suffit-il pour des travaux supplémentaires ?",
  "Dans un marché à forfait, non : la loi exige une autorisation écrite. Dans les autres cas, c'est à l'artisan de prouver votre accord, en principe par écrit au-delà de 1 500 €. Exigez toujours un avenant chiffré avant les travaux."),
 ("Que faire si la facture dépasse le devis ?",
  "Payez ce qui correspond au devis, contestez le supplément par écrit, puis envoyez une mise en demeure si le désaccord persiste. Ensuite, saisissez le médiateur de la consommation de l'entreprise ou un conciliateur de justice."),
]

# ---------- Annuler un devis signé
GUIDES.append(dict(
 slug="guide-annuler-devis-signe-retractation",
 title="Annuler un devis signé : rétractation et cas sans retour",
 h1="Devis signé : peut-on encore annuler ou se rétracter ?",
 desc="Signé à domicile, en magasin, sur un salon ou en ligne, avec un crédit : quand annuler un devis signé est possible, et ce que ça coûte.",
 lead="Vous avez signé, et vous le regrettez. Tout dépend d'un détail que l'on oublie souvent : l'endroit où vous avez signé.",
 readtime=7,
 body='''<h2>Signé chez vous : 14 jours pour changer d'avis</h2>
<p>Un devis signé à votre domicile (ou ailleurs que dans les locaux de l'entreprise, à la suite d'une visite) est un contrat <strong>hors établissement</strong>. Vous disposez de <strong>14 jours</strong> pour vous rétracter, sans motif et sans frais. Pour des travaux, le délai court en principe à partir du lendemain de la signature. Si le devis porte surtout sur la livraison d'un équipement, il peut courir à partir de sa livraison.</p>
<ul><li>L'entreprise doit vous remettre un <strong>formulaire de rétractation</strong>. Vous pouvez l'utiliser, ou envoyer un courrier recommandé avec accusé de réception.</li>
<li>Pendant les <strong>7 premiers jours</strong>, elle ne peut encaisser <strong>aucun paiement</strong> : ni acompte, ni chèque, même daté plus tard, ni autorisation de prélèvement, sauf pour des réparations urgentes que vous avez demandées.</li>
<li>Si vous vous rétractez, elle doit vous rembourser sous 14 jours.</li></ul>
<div class="note"><p><strong>Le formulaire manque ?</strong> Si l'entreprise ne vous a pas informé de votre droit de rétractation, le délai est prolongé de 12 mois. Et selon la Cour de justice de l'Union européenne (2023), si vous vous rétractez dans ce cas, vous ne devez rien pour les travaux déjà réalisés.</p></div>
<h2>Les travaux ont commencé pendant le délai</h2>
<p>Si vous avez demandé expressément que les travaux démarrent avant la fin des 14 jours, vous pouvez toujours vous rétracter, mais vous payez la part déjà réalisée. Plus de rétractation possible, en revanche, pour une prestation entièrement exécutée avec votre accord, pour des travaux d'entretien ou de réparation <strong>urgents</strong> que vous avez demandés, ou pour un bien fabriqué selon vos spécifications. Cette dernière exception est souvent invoquée pour une cuisine ou des menuiseries sur mesure ; elle se discute quand le contrat comprend aussi la pose et l'installation, d'où l'intérêt de lire la clause avant de signer.</p>
<h2>Signé en magasin, en agence ou chez l'artisan : pas de rétractation</h2>
<p>Si vous vous êtes déplacé pour signer, la loi ne prévoit <strong>aucun délai de rétractation</strong>. Le devis vous engage dès la signature, sauf si l'entreprise vous a accordé contractuellement un délai : vérifiez les conditions générales.</p>
<h2>Signé sur une foire ou un salon : pas de rétractation non plus</h2>
<p>C'est le piège classique des salons de l'habitat. Aucun délai de rétractation, et le vendeur doit l'afficher clairement sur son stand et l'écrire en tête du contrat. Seule exception : si les travaux sont financés par un <strong>crédit affecté</strong> souscrit sur place.</p>
<h2>Signé à distance (internet, téléphone) : 14 jours</h2>
<p>Un devis accepté en ligne ou par téléphone, sans rencontre physique, ouvre droit au même délai de 14 jours.</p>
<h2>Les travaux sont financés par un crédit</h2>
<p>Vous pouvez renoncer au crédit affecté dans les <strong>14 jours</strong> suivant l'acceptation de l'offre. Cette rétractation <strong>annule automatiquement le contrat de travaux</strong>, sans indemnité. Attention, si vous avez demandé une exécution immédiate des travaux, ce délai peut être réduit à 3 jours.</p>
<h2>Hors de ces cas : annuler a un coût</h2>
<p>Tout dépend de ce que vous avez versé, et du mot employé sur le devis :</p>
<ul><li><strong>Des arrhes</strong> : vous pouvez renoncer en les perdant (l'entreprise, elle, rembourserait le double). Si le devis ne précise rien, les sommes versées d'avance sont considérées comme des arrhes.</li>
<li><strong>Un acompte</strong> : le contrat est ferme. Annuler vous expose à indemniser l'entreprise.</li></ul>
<p>Pour un <strong>marché à forfait</strong>, la loi vous permet de résilier à tout moment, même travaux commencés, mais vous devez alors dédommager l'entreprise : ses dépenses, les travaux déjà faits et le bénéfice qu'elle aurait tiré du chantier (article 1794 du Code civil). Si l'entreprise a commis une faute, la situation est différente : faites-vous conseiller.</p>
<h2>Démarchage pour la rénovation énergétique</h2>
<p>Le démarchage téléphonique pour des travaux de rénovation énergétique est interdit depuis 2020, sauf contrat en cours, et un contrat conclu en violation de cette règle est nul. La loi du 30 juin 2025 contre la fraude aux aides publiques a étendu ces interdictions aux SMS, courriels et réseaux sociaux. Depuis le 11 août 2026, tout démarchage téléphonique suppose en outre votre accord préalable.</p>
<h2>Le meilleur moment pour annuler, c'est avant de signer</h2>
<p>Un devis relu à tête reposée, c'est un regret en moins. Je vérifie la présence du formulaire de rétractation quand il est obligatoire, la nature des sommes demandées (arrhes ou acompte), l'échéancier et les conditions de résiliation. Voir aussi <a href="guide-acompte-paiement-devis-travaux.html">le guide sur l'acompte</a>.</p>
''' + SRC + '''Article d'information générale, à jour au 27 octobre 2026, qui ne remplace pas un conseil juridique sur votre situation. Sources : articles L221-10, L221-18, L221-20, L221-25, L221-28, L224-59, L312-19 et L214-1 du Code de la consommation, articles 1590 et 1794 du Code civil, loi n° 2025-594 du 30 juin 2025, CJUE 17 mai 2023 (C-97/22), service-public.gouv.fr (fiche F23224), anil.org.</p>''',
))
GUIDE_FAQS["guide-annuler-devis-signe-retractation"] = [
 ("Peut-on se rétracter après avoir signé un devis ?",
  "Oui si le devis a été signé à domicile ou à distance : vous avez 14 jours. Non s'il a été signé en magasin, chez l'artisan ou sur une foire ou un salon, sauf clause contraire ou crédit affecté."),
 ("L'artisan peut-il encaisser un acompte juste après la signature à domicile ?",
  "Non. Pendant les 7 jours qui suivent la signature hors établissement, il ne peut recevoir aucun paiement, sous aucune forme, sauf pour des travaux urgents de réparation demandés par le client."),
 ("Que se passe-t-il si j'annule un devis signé en magasin ?",
  "Vous n'avez pas de droit de rétractation. Si vous avez versé des arrhes, vous les perdez. Avec un acompte, le contrat est ferme et l'entreprise peut demander une indemnisation."),
]

# ---------------------------------------------------------------- Pages par type de travaux
# (slug, title, h1, desc, lead, body sans le bloc CTA, kicker, nom du service, FAQ, libellé court, résumé carte)
JOB_PAGES = []

JOB_PAGES.append(dict(
 slug="analyse-devis-cuisine",
 title="Analyse de devis cuisine par un ingénieur BTP",
 h1="Analyse de devis cuisine",
 desc="TVA 10 % ou 20 %, raccordements, circuits électriques, hotte, dépose, prise de cotes : ce qu'un ingénieur BTP vérifie sur un devis de cuisine.",
 lead="Un devis de cuisine mélange du mobilier, de l'électroménager et des travaux. C'est là que se cachent les erreurs de TVA et les raccordements oubliés.",
 kicker="Cuisine", cta="de cuisine", service="Analyse de devis de cuisine",
 card="TVA mixte, raccordements, circuits spécialisés, hotte.",
 body="""<h2>La TVA : 10 % pour certains éléments, 20 % pour d'autres</h2>
<p>Dans un logement achevé depuis plus de 2 ans, une cuisine posée par une entreprise n'est pas taxée d'un bloc. Selon la doctrine fiscale :</p>
<ul><li><b>Au taux réduit (10 %)</b> : le plan de travail, l'évier, les meubles sous plan adaptés à votre cuisine et fixés au bâti (une fixation vissée suffit), et leur pose, à condition que l'entreprise réalise un aménagement complet. Si vous finissez vous-même une partie de la pose, tout passe à 20 %.</li>
<li><b>Au taux normal (20 %)</b> : l'électroménager, même encastré (four, plaque, hotte, lave-vaisselle, réfrigérateur), les meubles simplement posés ou fixés pour la stabilité, et la main-d'œuvre pour les installer.</li></ul>
<p>Un devis qui applique 10 % sur l'ensemble, ou 20 % sur tout, mérite une question. L'entreprise doit répartir le prix ligne par ligne entre les deux taux. Détails dans <a href="guide-tva-travaux-renovation.html">le guide TVA</a>.</p>
<h2>Les points techniques à retrouver sur le devis</h2>
<ul><li><b>La prise de cotes sur place</b>, avant fabrication, par l'entreprise qui s'engage sur les dimensions.</li>
<li><b>La dépose et l'évacuation de l'ancienne cuisine</b> : souvent oubliées, elles reviennent en supplément.</li>
<li><b>Les raccordements</b> : arrivées d'eau, évacuation, et qui les réalise (le cuisiniste, un plombier, vous ?).</li>
<li><b>L'électricité</b> : la plaque de cuisson exige un circuit dédié (32 A en monophasé) et le four, le lave-vaisselle et le lave-linge ont chacun leur circuit. Si votre tableau ne les a pas, le devis doit le prévoir.</li>
<li><b>La hotte</b> : extraction vers l'extérieur (avec la gaine et la traversée de mur) ou recyclage. Une hotte à extraction sans gaine prévue, c'est un supplément assuré.</li>
<li><b>La crédence et les finitions</b> : plinthes, joues, fileurs, éclairage sous meuble.</li>
<li><b>Les références exactes</b> de l'électroménager et du plan de travail, pour comparer.</li></ul>
<h2>Signé en magasin ou sur un salon : pas de rétractation</h2>
<p>La plupart des cuisines se signent en magasin ou sur une foire. Dans ces deux cas, il n'y a <strong>pas de délai de rétractation</strong> légal : relisez le devis avant de signer, pas après. Attention : si vous signez chez vous, par exemple après la visite du métreur, le délai de rétractation de 14 jours s'applique en principe. Certains vendeurs invoquent l'exception des biens fabriqués sur mesure : elle se discute quand le contrat comprend aussi la pose, alors lisez la clause du bon de commande et faites-vous confirmer vos droits par écrit avant de signer. Voir <a href="guide-annuler-devis-signe-retractation.html">le guide sur l'annulation d'un devis</a>. Le contrat doit aussi indiquer une date ou un délai de livraison.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Pose et raccordements : forfait 1 200 € TTC. » Raccordement électrique compris ou non ? Création des circuits spécialisés ? Évacuation de la hotte ? À demander : la liste des raccordements inclus, et le taux de TVA appliqué à chaque partie.</p>
""",
 faq=[
  ("Quelle TVA s'applique à une cuisine équipée ?",
   "Dans un logement de plus de 2 ans, 10 % sur les éléments incorporés au bâti (plan de travail, évier, meubles sous plan fixés et adaptés) et leur pose, 20 % sur l'électroménager, même encastré, et sur les meubles simplement posés."),
  ("La plaque de cuisson a-t-elle besoin d'un circuit électrique dédié ?",
   "Oui. La norme NF C 15-100 impose un circuit spécialisé pour la plaque de cuisson (32 A en monophasé), et un circuit chacun pour le four et le lave-vaisselle. Vérifiez que le devis le prévoit si votre installation ne les a pas."),
  ("Peut-on annuler une cuisine commandée en magasin ?",
   "Non, il n'y a pas de délai de rétractation légal pour un achat en magasin ou sur une foire. Seule une clause du contrat, ou un crédit affecté auquel vous renoncez, permet d'annuler sans frais."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-electricite",
 title="Analyse de devis électricité par un ingénieur BTP",
 h1="Analyse de devis électricité",
 desc="Norme NF C 15-100, tableau, différentiels, circuits spécialisés, terre, Consuel : ce qu'un ingénieur BTP vérifie sur un devis de rénovation électrique.",
 lead="« Mise aux normes de l'installation : 6 500 € » ne dit rien de ce que vous allez obtenir. Un devis d'électricité se lit en nombre de circuits, de points et de protections.",
 kicker="Électricité", cta="d'électricité", service="Analyse de devis d'électricité",
 card="Tableau, différentiels, circuits, terre, Consuel.",
 body="""<h2>La référence : la norme NF C 15-100</h2>
<p>Une nouvelle version de la norme a été publiée en 2024. Elle s'applique aux travaux dont le permis, la déclaration ou le contrat est postérieur au 31 août 2025. Elle n'oblige pas à refaire une installation existante, mais tout ce qui est créé ou refait doit la respecter. Le devis devrait indiquer la version appliquée.</p>
<h2>Les points à retrouver sur le devis</h2>
<ul><li><b>Le tableau électrique</b> : type, nombre de rangées, et au moins 20 % de place libre pour les évolutions en maison individuelle. En neuf ou en rénovation complète, il doit être placé dans une gaine technique logement, manettes entre 0,90 et 1,80 m du sol.</li>
<li><b>Les interrupteurs différentiels 30 mA</b> : au moins deux, avec leur type. Le type A est exigé pour la plaque de cuisson et le lave-linge. Une borne de recharge a son propre différentiel, dont le type dépend du modèle de borne.</li>
<li><b>Les circuits spécialisés</b> : plaque, four, lave-linge, lave-vaisselle, chauffe-eau, et le cas échéant pompe à chaleur ou borne de recharge.</li>
<li><b>Le nombre de prises et de points lumineux par pièce</b>, plutôt qu'un total global.</li>
<li><b>La prise de terre</b> et sa mesure, et la liaison équipotentielle de la salle de bain.</li>
<li><b>Les saignées, rebouchages et finitions</b> : qui les fait, et sont-ils compris ?</li></ul>
<h2>Le Consuel : obligatoire dans certains cas</h2>
<p>L'attestation de conformité visée par le Consuel est exigée avant la mise sous tension par le gestionnaire de réseau pour une installation neuve, ou pour une rénovation complète lorsque l'alimentation a été coupée par le gestionnaire. Si votre chantier est concerné, le devis doit dire qui la demande et qui la paie.</p>
<h2>La TVA</h2>
<p>Dans un logement achevé depuis plus de 2 ans, les travaux d'électricité relèvent en principe du taux de 10 %.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Remplacement du tableau électrique : forfait. » Combien de rangées, combien de différentiels et de quel type, combien de disjoncteurs, mise à la terre vérifiée ? À demander : le schéma du tableau prévu, circuit par circuit.</p>
""",
 faq=[
  ("Faut-il refaire toute l'installation électrique aux normes ?",
   "Non, la norme NF C 15-100 n'est pas rétroactive. Mais tout ce qui est créé ou refait doit la respecter, et une installation dangereuse (absence de terre, pas de différentiel 30 mA) doit être sécurisée en priorité."),
  ("Quand l'attestation Consuel est-elle obligatoire ?",
   "Pour une installation neuve, et pour une rénovation complète quand le gestionnaire de réseau a coupé l'alimentation. Une rénovation partielle n'en demande en principe pas."),
  ("Comment comparer deux devis d'électricité ?",
   "Comparez le nombre de circuits, de prises et de points lumineux, le nombre et le type de différentiels, et ce qui est compris en saignées et finitions. Un prix global sans ce détail ne se compare pas."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-fenetres",
 title="Analyse de devis fenêtres par un ingénieur BTP",
 h1="Analyse de devis fenêtres",
 desc="Uw et Sw, TVA 5,5 %, pose en rénovation ou dépose totale, entrées d'air, aides 2026 : ce qu'un ingénieur BTP vérifie sur un devis de fenêtres.",
 lead="Deux devis de fenêtres au même prix peuvent cacher des performances, une pose et une TVA très différentes. Et les aides ont changé à l'automne 2026.",
 kicker="Fenêtres", cta="de fenêtres", service="Analyse de devis de fenêtres",
 card="Uw/Sw, type de pose, entrées d'air, TVA, aides 2026.",
 body="""<h2>Les performances : Uw et Sw</h2>
<p>Le devis doit indiquer, pour chaque fenêtre, le <strong>coefficient Uw</strong> (isolation de la fenêtre entière, plus il est bas mieux c'est) et le <strong>facteur solaire Sw</strong> (apports de chaleur du soleil). Pour bénéficier de la TVA à 5,5 %, il faut au minimum Uw ≤ 1,3 W/m².K et Sw ≥ 0,3, ou Uw ≤ 1,7 et Sw ≥ 0,36. Sans ces valeurs, le taux réduit n'est pas justifié.</p>
<h2>Pose en rénovation ou dépose totale</h2>
<ul><li><b>Pose en rénovation</b> : la nouvelle fenêtre se fixe sur l'ancien dormant conservé. C'est plus rapide et moins cher, mais la surface vitrée diminue, et l'état du dormant conservé conditionne le résultat.</li>
<li><b>Dépose totale</b> : l'ancien dormant est retiré. Plus de travaux (reprises de maçonnerie, d'enduit, de tableaux), mais un meilleur clair de vitrage et une étanchéité refaite à neuf.</li></ul>
<p>Le devis doit dire clairement lequel des deux est prévu, et ce qui est compris en finitions intérieures et extérieures.</p>
<h2>Ne pas oublier la ventilation</h2>
<p>Des fenêtres neuves rendent le logement beaucoup plus étanche à l'air. Avec une VMC simple flux, les pièces principales doivent disposer d'<strong>entrées d'air</strong>, placées sur la fenêtre, le coffre de volet roulant ou le mur. Avec une double flux, non. Sans ventilation adaptée, attention à la condensation et aux moisissures.</p>
<h2>Les aides en 2026 : ce qui a changé</h2>
<p>Depuis le 1er septembre 2026, <strong>MaPrimeRénov' par geste ne finance plus le remplacement des fenêtres</strong> pour les nouvelles demandes. Les fenêtres restent finançables dans une rénovation d'ampleur, et l'éco-prêt à taux zéro reste possible. La prime CEE est réservée au remplacement de fenêtres en <strong>simple vitrage</strong> (dormant compris) ou à la pose d'une double fenêtre, par une entreprise RGE, dans un logement de plus de 2 ans. Méfiez-vous d'un devis qui déduit une aide sans préciser laquelle.</p>
<h2>Les démarches</h2>
<p>Changer l'aspect extérieur (matériau, couleur, dessin des petits-bois) demande en principe une déclaration préalable en mairie, et des règles plus strictes s'appliquent en secteur protégé.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Fourniture et pose de 6 fenêtres PVC double vitrage : 7 200 € TTC. » Quelles dimensions, quel Uw, quel Sw, quelle pose, quelles finitions ? À demander : une ligne par fenêtre avec ses dimensions et ses performances, et le type de pose.</p>
""",
 faq=[
  ("Quelles performances pour la TVA à 5,5 % sur des fenêtres ?",
   "Uw ≤ 1,3 W/m².K et Sw ≥ 0,3, ou Uw ≤ 1,7 W/m².K et Sw ≥ 0,36, dans un logement achevé depuis plus de 2 ans. Ces valeurs doivent figurer sur le devis."),
  ("MaPrimeRénov' finance-t-elle encore les fenêtres ?",
   "Plus en parcours par geste pour les demandes déposées depuis le 1er septembre 2026. Les fenêtres restent finançables dans une rénovation d'ampleur, et via l'éco-prêt à taux zéro. La prime CEE est réservée au remplacement de fenêtres en simple vitrage ou à la pose d'une double fenêtre, par une entreprise RGE."),
  ("Pose en rénovation ou dépose totale : que choisir ?",
   "La pose en rénovation est moins chère mais réduit la surface vitrée et dépend de l'état de l'ancien dormant. La dépose totale coûte plus cher mais donne une meilleure luminosité et une étanchéité refaite à neuf."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-terrasse",
 title="Analyse de devis terrasse par un ingénieur BTP",
 h1="Analyse de devis terrasse",
 desc="Dalle béton, carrelage, bois ou composite : préparation du sol, épaisseur, pente, évacuation des eaux, structure et démarches. Ce qu'un ingénieur BTP vérifie sur un devis de terrasse.",
 lead="Une terrasse se juge sur ce qu'on ne voit plus une fois finie : le sol préparé, la dalle ou la structure, la pente. C'est aussi là que les devis sont les plus vagues.",
 kicker="Terrasse", cta="de terrasse", service="Analyse de devis de terrasse",
 card="Préparation du sol, dalle ou structure, pente, évacuation, démarches.",
 body="""<h2>La préparation du sol</h2>
<p>C'est le poste le plus souvent noyé dans un forfait. Le devis doit dire si le <strong>décaissement</strong> (terrassement) est prévu, sur quelle profondeur, et si l'<strong>évacuation des terres</strong> est comprise : quelques mètres cubes de terre à sortir et à mettre en décharge pèsent vite dans la facture.</p>
<h2>Terrasse béton ou carrelée</h2>
<ul><li><b>Le support</b> : hérisson (couche de cailloux) et son épaisseur, film, puis dalle béton avec son <b>épaisseur</b> et son <b>ferraillage</b> (treillis soudé).</li>
<li><b>La pente</b> : une pente éloignée de la maison, en général d'au moins 1,5 % pour un carrelage collé (selon la norme de pose), évite que l'eau stagne ou rentre sous la porte-fenêtre.</li>
<li><b>Les joints de fractionnement</b> sur les grandes surfaces, pour limiter les fissures.</li>
<li><b>Le carrelage</b> : collé sur dalle ou posé sur plots, et un carrelage adapté à l'extérieur (résistance au gel, antidérapant).</li></ul>
<h2>Terrasse bois ou composite</h2>
<ul><li><b>La structure</b> : plots, pieux ou longrines, et l'entraxe des lambourdes, à adapter à l'épaisseur des lames.</li>
<li><b>Le bois</b> : essence et classe d'emploi adaptée à l'extérieur (classe 3 au minimum pour des lames hors sol bien ventilées, classe 4 pour les lambourdes et tout bois en contact avec le sol ou l'eau), ou la référence exacte du composite.</li>
<li><b>La ventilation sous les lames</b> et la visserie inox : deux oublis qui réduisent beaucoup la durée de vie.</li></ul>
<h2>L'évacuation des eaux</h2>
<p>Où part l'eau de pluie ? Caniveau, drain, regard : si la terrasse est contre la maison ou au-dessus d'une pièce, ce point doit être traité et chiffré, pas laissé « selon besoin ».</p>
<h2>Les démarches et l'assurance</h2>
<p>Une terrasse de plain-pied non couverte ne demande en principe pas d'autorisation, sous réserve des règles de votre commune (PLU, secteur protégé). Une terrasse <strong>surélevée de plus de 60 cm</strong> ou <strong>couverte</strong> crée de l'emprise au sol : déclaration préalable à partir de 5 m², permis au-delà de 20 m² (40 m² dans certaines zones couvertes par un PLU). Pour une terrasse maçonnée, demandez l'attestation d'assurance décennale couvrant cette activité. Au-delà d'environ 1 m de hauteur de chute, un garde-corps est à prévoir (norme NF P01-012).</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Réalisation d'une terrasse béton 25 m² : forfait 4 500 €. » Quelle préparation, quelle épaisseur de dalle, quel ferraillage, quelle pente, qui évacue les terres ? À demander : le détail par poste (terrassement, hérisson, dalle, finition) avec les quantités.</p>
""",
 faq=[
  ("Faut-il une autorisation pour construire une terrasse ?",
   "Une terrasse de plain-pied non couverte n'en demande en principe pas, sauf règles locales (PLU, secteur protégé). Surélevée de plus de 60 cm ou couverte, elle crée de l'emprise au sol : déclaration préalable à partir de 5 m², permis de construire au-delà de 20 m² (40 m² dans certaines zones d'un PLU)."),
  ("Que doit détailler un devis de terrasse béton ?",
   "Le décaissement et l'évacuation des terres, le hérisson, l'épaisseur et le ferraillage de la dalle, la pente, les joints et la finition, avec une quantité et un prix pour chaque poste."),
  ("Comment faire relire mon devis de terrasse ?",
   "Envoyez-le en PDF ou en photo après avoir commandé l'analyse en ligne : vous recevez sous 48 h un rapport avec les postes manquants, les prix à vérifier et les questions à poser."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-extension",
 title="Analyse de devis extension de maison par un ingénieur BTP",
 h1="Analyse de devis extension",
 desc="Permis ou déclaration, architecte, RE2020, fondations, TVA à 20 %, dommages-ouvrage : ce qu'un ingénieur BTP vérifie sur un devis d'extension de maison.",
 lead="Une extension, c'est un petit bâtiment neuf collé à l'ancien. Le devis doit couvrir tout ce qui va des fondations au raccordement avec l'existant, et c'est là que les oublis coûtent cher.",
 kicker="Extension", cta="d'extension", service="Analyse de devis d'extension",
 card="Démarches, fondations, jonction avec l'existant, RE2020.",
 body="""<h2>Les démarches avant tout</h2>
<ul><li><b>Jusqu'à 5 m²</b> : déclaration préalable, car l'aspect extérieur change.</li>
<li><b>De 5 à 20 m²</b> : déclaration préalable, et jusqu'à 40 m² en zone urbaine d'un PLU.</li>
<li><b>Au-delà</b> : permis de construire.</li>
<li><b>Seuil des 150 m²</b> : en zone urbaine d'un PLU, une extension de 20 à 40 m² qui porte la surface totale au-delà de 150 m² demande un permis de construire. Dès que vous déposez un permis et que la surface totale dépasse 150 m², l'architecte est obligatoire.</li></ul>
<p>Les travaux ne doivent pas commencer avant l'obtention de l'autorisation, et idéalement après le délai de recours des tiers. Vérifiez qui prépare le dossier et si ce coût est inclus.</p>
<h2>La réglementation thermique</h2>
<p>Pour une maison individuelle, une extension jusqu'à 50 m² doit respecter des exigences élément par élément (isolation, menuiseries, ventilation). De 50 à 80 m², trois indicateurs de la RE2020 s'appliquent (besoin bioclimatique, confort d'été, carbone des matériaux), et à partir de 80 m², la RE2020 complète. Ces seuils portent sur la surface de référence de l'extension. Le devis doit préciser les isolants et leurs performances, comme pour une construction neuve.</p>
<h2>Les postes à retrouver sur le devis</h2>
<ul><li><b>Les terrassements et les fondations</b>, dimensionnés selon le sol. Dans les zones exposées au retrait-gonflement des argiles, demandez sur quelle base les fondations ont été conçues.</li>
<li><b>La jonction avec l'existant</b> : ouverture dans le mur porteur (avec son linteau ou sa poutre et son étaiement), raccord de toiture, étanchéité entre l'ancien et le neuf. C'est le poste le plus souvent sous-estimé.</li>
<li><b>Les réseaux</b> : prolongement de l'électricité, du chauffage, de la plomberie et des évacuations.</li>
<li><b>Le clos et couvert complet</b> : murs, isolation, menuiseries, toiture, gouttières.</li>
<li><b>Les finitions intérieures</b> : sont-elles comprises, ou s'arrête-t-on au hors d'eau, hors d'air ?</li></ul>
<h2>TVA, assurances et taxe</h2>
<p>Une extension est au <strong>taux de TVA de 20 %</strong>, quelle que soit sa surface, même dans un logement ancien. La règle des 10 % de surface en plus concerne l'aménagement de surfaces existantes, comme des combles. Exigez l'attestation décennale de chaque entreprise (<a href="guide-verifier-assurance-decennale.html">voir le guide</a>), et posez-vous la question de l'assurance dommages-ouvrage, obligatoire pour ce type de travaux (sans sanction pénale pour un particulier qui fait construire pour lui-même). Prévoyez aussi la taxe d'aménagement, calculée sur la surface créée.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Création d'une ouverture dans le mur existant : forfait. » Quelle largeur, quel linteau ou quelle poutre, qui le dimensionne, étaiement compris ? À demander : la description de l'ouverture (linteau ou poutre, appuis, étaiement) et la note de calcul si le mur est porteur.</p>
""",
 faq=[
  ("Faut-il un permis de construire pour une extension ?",
   "Au-delà de 20 m² (40 m² en zone urbaine d'un PLU), oui. En dessous, une déclaration préalable suffit en général, y compris pour une petite extension de 5 m² ou moins. Dès qu'un permis est nécessaire et que la surface totale dépasse 150 m² après travaux, l'architecte est obligatoire."),
  ("Quelle TVA pour une extension de maison ?",
   "20 %, quelle que soit sa surface, même dans un logement ancien : une extension est une addition de construction, exclue des taux réduits."),
  ("Quel poste est le plus souvent oublié sur un devis d'extension ?",
   "La jonction avec l'existant : ouverture dans le mur porteur avec sa poutre et son étaiement, raccord de toiture et étanchéité entre l'ancien et le neuf."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-ravalement-facade",
 title="Analyse de devis ravalement de façade par un ingénieur BTP",
 h1="Analyse de devis ravalement de façade",
 desc="Surfaces, diagnostic du support, fissures, enduit, échafaudage, obligation d'isoler, TVA : ce qu'un ingénieur BTP vérifie sur un devis de ravalement.",
 lead="Sur un ravalement, l'écart entre deux devis vient souvent des mètres carrés comptés et de ce qui est fait avant la peinture. Ce sont les deux premières choses à vérifier.",
 kicker="Ravalement", cta="de ravalement", service="Analyse de devis de ravalement de façade",
 card="Surfaces, fissures, enduit, échafaudage, isolation.",
 body="""<h2>Les surfaces : ouvertures déduites ?</h2>
<p>Le ravalement se facture au m². Le devis doit indiquer la surface de chaque façade et préciser si les ouvertures (fenêtres, portes) sont déduites. Recalculez-la grossièrement : longueur × hauteur, moins les ouvertures. Un écart de 15 % sur les surfaces, c'est jusqu'à 15 % sur la facture.</p>
<h2>Ce qui se passe avant la finition</h2>
<ul><li><b>Le diagnostic du support</b> : nature du mur, état de l'enduit existant, humidité. Il conditionne tout le reste.</li>
<li><b>Le nettoyage</b> : lavage, traitement anti-mousse, décapage si nécessaire.</li>
<li><b>Le traitement des fissures</b> : au mètre linéaire, avec la méthode (simple rebouchage ou ouverture, pontage, armature). Un forfait « reprise des fissures » est à faire préciser.</li>
<li><b>La finition</b> : peinture, revêtement semi-épais ou enduit, avec la marque, la référence et la classe du produit.</li>
<li><b>Les points singuliers</b> : appuis de fenêtre, corniches, soubassement, descentes d'eau à démonter et reposer.</li></ul>
<h2>L'échafaudage et le chantier</h2>
<p>Montage, démontage, durée de location, protections des sols et des menuiseries, nettoyage final. Si l'échafaudage empiète sur la voie publique, une autorisation d'occupation de la voirie (permis de stationnement), en général délivrée par la mairie, est nécessaire : le devis doit dire qui la demande.</p>
<h2>Obligation d'isoler et démarches</h2>
<p>Lorsque l'enduit est refait ou le parement remplacé sur <strong>plus de 50 % d'une façade</strong> (hors ouvertures), la loi impose en principe d'en profiter pour isoler, sauf exceptions (impossibilité technique, contrainte patrimoniale, retour sur investissement de plus de 10 ans). Un simple nettoyage ou une remise en peinture ne déclenche pas cette obligation. Elle ne concerne que les murs en béton, en parpaing, en brique industrielle ou en bardage métallique, pas la pierre ni le pisé. Une déclaration préalable est nécessaire si vous changez l'aspect de la façade (couleur, matériau), si vous isolez par l'extérieur, en secteur protégé, ou si la commune l'impose. Un ravalement à l'identique en est dispensé ailleurs : renseignez-vous en mairie.</p>
<h2>La TVA</h2>
<p>Dans un logement achevé depuis plus de 2 ans, un ravalement relève en principe du taux de 10 %. Une isolation thermique par l'extérieur peut être à 5,5 % si l'isolant atteint une résistance thermique R ≥ 3,7 m².K/W. Attention : depuis le 1er janvier 2026, l'isolation des murs n'est plus aidée par MaPrimeRénov' par geste. Elle reste finançable dans une rénovation d'ampleur et par l'éco-prêt à taux zéro.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Ravalement complet façades : 180 m², 48 € le m². » Quelles façades, ouvertures déduites ou non, quel traitement des fissures, quelle finition, échafaudage compris ? À demander : une ligne par opération, avec les surfaces façade par façade.</p>
""",
 faq=[
  ("Faut-il isoler lors d'un ravalement de façade ?",
   "En principe oui, si l'enduit est refait ou le parement remplacé sur plus de 50 % de la façade hors ouvertures, sauf exceptions (impossibilité technique, contrainte patrimoniale ou retour sur investissement trop long). Un nettoyage ou une peinture ne déclenche pas cette obligation, qui ne vise que les murs en béton, parpaing, brique industrielle ou bardage métallique."),
  ("Faut-il une autorisation pour un ravalement ?",
   "Oui si vous changez l'aspect de la façade (couleur, matériau), si vous isolez par l'extérieur, en secteur protégé, ou si la commune l'a imposée par délibération. Si l'échafaudage empiète sur la voie publique, un permis de stationnement est aussi requis."),
  ("Pourquoi deux devis de ravalement sont-ils si différents ?",
   "Le plus souvent à cause des surfaces comptées (ouvertures déduites ou non) et de la préparation : nettoyage, traitement des fissures, type de finition. Comparez poste par poste et recalculez les surfaces."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-plomberie-chauffe-eau",
 title="Analyse de devis plomberie et chauffe-eau par un ingénieur BTP",
 h1="Analyse de devis plomberie et chauffe-eau",
 desc="Chauffe-eau électrique ou thermodynamique, groupe de sécurité, évacuations, forfaits, TVA 10 % ou 5,5 % : ce qu'un ingénieur BTP vérifie sur un devis de plomberie.",
 lead="En plomberie, le devis tient souvent en une ligne au forfait. C'est justement ce qu'il faut ouvrir avant de signer.",
 kicker="Plomberie", cta="de plomberie", service="Analyse de devis de plomberie et de chauffe-eau",
 card="Forfaits, chauffe-eau, groupe de sécurité, évacuations, TVA.",
 body="""<h2>Le forfait, à faire détailler</h2>
<p>« Plomberie : forfait 1 500 € » ne permet de rien vérifier. Le devis doit lister ce qui est prévu : alimentations (cuivre, multicouche, PER), évacuations (diamètres, pentes), nombre de points d'eau, robinets d'arrêt, raccordements des appareils, et ce qui reste à votre charge.</p>
<h2>Le remplacement d'un chauffe-eau</h2>
<ul><li><b>La capacité</b> en litres, adaptée au nombre de personnes, et la référence exacte de l'appareil.</li>
<li><b>Le groupe de sécurité</b> neuf, obligatoire sur un chauffe-eau à accumulation, avec son raccordement à l'évacuation.</li>
<li><b>La dépose et l'évacuation de l'ancien ballon</b>, souvent oubliées.</li>
<li><b>Le support</b> : fixation murale adaptée au poids, ou trépied, et l'accès pour l'entretien.</li>
<li><b>Pour un chauffe-eau thermodynamique</b> : l'emplacement (volume du local, gaines vers l'extérieur si nécessaire), l'évacuation des condensats et le bruit.</li></ul>
<h2>La TVA et les aides</h2>
<p>Dans un logement achevé depuis plus de 2 ans, un chauffe-eau électrique classique et sa pose relèvent en principe du taux de 10 %. Un chauffe-eau thermodynamique répondant aux critères de performance peut relever de 5,5 %. Depuis le 1<sup>er</sup> septembre 2026, MaPrimeRénov' « par geste » ne finance plus l'installation seule d'un système d'eau chaude : une prime CEE peut rester possible. Voir <a href="guide-tva-travaux-renovation.html">le guide TVA</a>.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Remplacement chauffe-eau 200 L, fourniture et pose : 1 450 € TTC. » Quelle marque et quelle référence ? Groupe de sécurité neuf ? Dépose et évacuation de l'ancien ballon ? Mise aux normes du raccordement électrique ? À demander : le détail fourniture, pose et accessoires.</p>
""",
 faq=[
  ("Le groupe de sécurité doit-il être changé avec le chauffe-eau ?",
   "Oui, un groupe de sécurité neuf est à poser avec un chauffe-eau à accumulation neuf. Vérifiez qu'il figure sur le devis, avec son raccordement à l'évacuation."),
  ("Quelle TVA pour un remplacement de chauffe-eau ?",
   "Dans un logement de plus de 2 ans, en principe 10 % pour un chauffe-eau électrique classique et sa pose, et 5,5 % pour un chauffe-eau thermodynamique qui répond aux critères de performance."),
  ("Comment faire relire mon devis de plomberie ?",
   "Envoyez-le en PDF ou en photo après avoir commandé l'analyse en ligne : vous recevez sous 48 h un rapport avec les postes à détailler, les oublis et les questions à poser."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-carrelage",
 title="Analyse de devis carrelage par un ingénieur BTP",
 h1="Analyse de devis carrelage",
 desc="Préparation du support, ragréage, colle, surfaces et chutes, plinthes, joints, carrelage extérieur : ce qu'un ingénieur BTP vérifie sur un devis de carrelage.",
 lead="Le prix au m² du carreau n'est qu'une partie du devis. Ce qui fait la différence, c'est la préparation du support et ce qui est compté autour.",
 kicker="Carrelage", cta="de carrelage", service="Analyse de devis de carrelage",
 card="Support, ragréage, surfaces, chutes, plinthes, joints.",
 body="""<h2>La préparation du support</h2>
<p>C'est le poste le plus souvent oublié ou laissé « selon état ». Le devis doit dire ce qui est prévu : dépose de l'ancien revêtement, piquage, ragréage (avec l'épaisseur), primaire d'accrochage, traitement des fissures. Un carrelage posé sur un support mal préparé finit par sonner creux ou se fissurer.</p>
<h2>Les quantités</h2>
<ul><li><b>La surface</b> en m², cohérente avec la pièce, sans compter deux fois les zones occupées par un receveur, une baignoire ou des meubles fixes.</li>
<li><b>Les chutes</b> : une marge de quelques pour cent est normale, davantage pour une pose en diagonale ou un grand format. Elle doit être visible, pas cachée dans la surface.</li>
<li><b>Les plinthes</b> en mètres linéaires, et les découpes particulières (seuils, marches, nez de marche).</li></ul>
<h2>Les produits et la pose</h2>
<ul><li><b>La référence du carrelage</b> (format, épaisseur, classement d'usage et antidérapant si besoin), ou un prix de fourniture plafond si vous le choisissez plus tard.</li>
<li><b>La colle</b> adaptée au support et au format, le type de pose (simple ou double encollage pour les grands formats) et les joints.</li>
<li><b>En pièce humide</b> : l'étanchéité sous carrelage en zone de douche, à chiffrer à part.</li>
<li><b>En extérieur</b> : un carrelage résistant au gel et une pente pour l'écoulement des eaux. Voir aussi <a href="analyse-devis-terrasse.html">la page terrasse</a>.</li></ul>
<h2>La TVA</h2>
<p>Dans un logement achevé depuis plus de 2 ans, la pose de carrelage relève en principe du taux de 10 %, fourniture comprise quand elle est facturée par l'entreprise.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Pose carrelage 45 m², fourniture et pose : 3 600 € TTC. » Quel carrelage ? Ragréage compris ? Plinthes ? Dépose de l'ancien sol ? À demander : le détail préparation, fourniture, pose, plinthes, avec les quantités.</p>
""",
 faq=[
  ("Le ragréage est-il toujours nécessaire ?",
   "Non, mais il est indispensable quand le support n'est pas plan. Le devis doit dire s'il est prévu, sur quelle surface et quelle épaisseur, plutôt que « selon état »."),
  ("Faut-il compter des chutes sur un devis de carrelage ?",
   "Oui, une marge est normale, plus forte pour une pose en diagonale ou en grand format. Elle doit apparaître clairement, en quantité ou en pourcentage."),
  ("Comment faire relire mon devis de carrelage ?",
   "Envoyez-le en PDF ou en photo après avoir commandé l'analyse en ligne : vous recevez sous 48 h un rapport avec les postes manquants, les quantités à vérifier et les questions à poser."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-panneaux-solaires",
 title="Analyse de devis panneaux solaires photovoltaïques par un ingénieur BTP",
 h1="Analyse de devis panneaux solaires",
 desc="Puissance, production estimée, onduleur, raccordement, démarches, TVA 5,5 % sous conditions, démarchage : ce qu'un ingénieur BTP vérifie sur un devis de photovoltaïque.",
 lead="Le photovoltaïque est le secteur où les devis promettent le plus. Avant de signer, vérifiez ce qui est vraiment fourni, et ce que l'installation produira chez vous.",
 kicker="Photovoltaïque", cta="de panneaux solaires", service="Analyse de devis de panneaux solaires",
 card="Puissance, production, onduleur, démarches, TVA, démarchage.",
 body="""<aside class="cp-alert"><p class="t">Démarché pour des panneaux solaires ?</p><p>Les offres « autofinancées » ou « rentables dès la première année » sont des signaux d'alerte classiques. Avant de signer, comparez avec au moins un autre devis, et prenez le temps de vérifier la qualification de l'installateur dans l'<a href="https://france-renov.gouv.fr/annuaire-rge" target="_blank" rel="noopener">annuaire officiel des entreprises RGE</a>.</p></aside>
<h2>Ce que le devis doit préciser</h2>
<ul><li><b>La puissance</b> en kWc, le nombre, la marque et la référence des panneaux.</li>
<li><b>L'onduleur</b> (central ou micro-onduleurs), sa marque, sa référence et sa garantie.</li>
<li><b>La production estimée</b> en kWh par an, avec l'orientation et l'inclinaison de votre toiture, et l'hypothèse d'autoconsommation retenue.</li>
<li><b>La pose</b> : intégration ou surimposition, fixations, étanchéité de la toiture, câblage et protections électriques.</li>
<li><b>Les démarches</b> : déclaration préalable en mairie, demande de raccordement, attestation de conformité électrique, et qui s'en charge.</li></ul>
<h2>La TVA et les aides</h2>
<p>Depuis le 1<sup>er</sup> octobre 2025, une installation de 9 kWc ou moins sur un logement peut relever du taux de 5,5 %, à des conditions précises : empreinte carbone des panneaux, faible teneur en métaux, système de gestion de l'énergie, certification. Le devis doit justifier ces conditions s'il applique 5,5 %. La prime à l'autoconsommation et le rachat du surplus dépendent aussi de règles précises : demandez-en le détail par écrit plutôt que des montants « garantis ».</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Centrale solaire 6 kWc clés en main : 14 900 € TTC. » Quels panneaux, quel onduleur ? Quelle production estimée et sur quelle base ? Démarches et raccordement inclus ? Taux de TVA justifié ? À demander : le détail matériel, pose, démarches, et l'étude de production.</p>
""",
 faq=[
  ("Quelle TVA pour des panneaux solaires en 2026 ?",
   "Depuis le 1er octobre 2025, 5,5 % pour une installation de 9 kWc ou moins sur un logement, si les panneaux et l'installation remplissent des conditions précises (empreinte carbone, métaux, gestion de l'énergie, certification). Le devis doit le justifier."),
  ("Comment repérer un devis photovoltaïque douteux ?",
   "Une production ou des économies présentées comme garanties, une offre « autofinancée », un financement signé le jour même ou l'absence de détail sur le matériel sont des signaux d'alerte."),
  ("Comment faire relire mon devis de panneaux solaires ?",
   "Envoyez-le en PDF ou en photo après avoir commandé l'analyse en ligne : vous recevez sous 48 h un rapport avec les points à vérifier et les questions à poser."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-vmc",
 title="Analyse de devis VMC par un ingénieur BTP",
 h1="Analyse de devis VMC",
 desc="Simple flux autoréglable ou hygroréglable, double flux, bouches, entrées d'air, rejet, entretien, TVA : ce qu'un ingénieur BTP vérifie sur un devis de ventilation.",
 lead="Une ventilation mal choisie ou mal posée, c'est de l'humidité, de la condensation et des moisissures. Le devis doit dire exactement quel système, et comment il sera installé.",
 kicker="VMC", cta="de VMC", service="Analyse de devis de VMC",
 card="Simple ou double flux, bouches, entrées d'air, rejet, entretien.",
 body="""<h2>Quel système ?</h2>
<ul><li><b>Simple flux autoréglable</b> : débit constant, le plus simple.</li>
<li><b>Simple flux hygroréglable</b> (type A ou B) : le débit s'adapte à l'humidité. En type B, les entrées d'air sont aussi hygroréglables.</li>
<li><b>Double flux</b> : récupère la chaleur de l'air extrait, mais demande un réseau de gaines pour l'insufflation, de la place et un entretien régulier des filtres.</li></ul>
<p>Le devis doit donner la marque et la référence du caisson, son type, et sa consommation.</p>
<h2>Les points à retrouver sur le devis</h2>
<ul><li><b>Les bouches d'extraction</b> dans chaque pièce humide (cuisine, salle de bain, WC), et leur type.</li>
<li><b>Les entrées d'air</b> dans les pièces principales, sur les fenêtres, les coffres de volets ou les murs, pour une simple flux.</li>
<li><b>Le réseau de gaines</b> : longueurs, isolation des gaines en combles froids, accessibilité du caisson.</li>
<li><b>Le rejet</b> vers l'extérieur (sortie de toiture ou de mur), jamais dans les combles.</li>
<li><b>Le raccordement électrique</b> et la dépose de l'ancienne VMC.</li></ul>
<h2>La TVA</h2>
<p>Dans un logement achevé depuis plus de 2 ans, certaines VMC liées à la rénovation énergétique peuvent relever du taux de 5,5 % si elles répondent aux critères de performance, sinon le taux de 10 % s'applique en principe. Voir <a href="guide-tva-travaux-renovation.html">le guide TVA</a>.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Installation VMC hygro, fourniture et pose : 1 200 € TTC. » Hygro A ou B ? Combien de bouches, où ? Entrées d'air comprises ? Sortie de toiture ? À demander : la référence du caisson et le détail des bouches, entrées d'air, gaines et rejet.</p>
""",
 faq=[
  ("VMC hygroréglable A ou B : quelle différence ?",
   "En hygro A, seules les bouches d'extraction s'adaptent à l'humidité. En hygro B, les entrées d'air des pièces principales sont aussi hygroréglables. Le devis doit préciser le type."),
  ("La VMC peut-elle rejeter l'air dans les combles ?",
   "Non, l'air extrait doit être rejeté vers l'extérieur, par une sortie de toiture ou de mur. Vérifiez que le devis prévoit ce rejet."),
  ("Comment faire relire mon devis de VMC ?",
   "Envoyez-le en PDF ou en photo après avoir commandé l'analyse en ligne : vous recevez sous 48 h un rapport avec les points à vérifier et les questions à poser."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-mur-porteur",
 title="Analyse de devis ouverture de mur porteur par un ingénieur BTP",
 h1="Analyse de devis ouverture de mur porteur",
 desc="Étude de structure, note de calcul, étaiement, poutre ou IPN, appuis, autorisations, décennale : ce qu'un ingénieur BTP vérifie sur un devis d'ouverture de mur porteur.",
 lead="Ouvrir un mur porteur, c'est modifier la structure de la maison. Le devis doit montrer que ce qui tient la maison pendant et après les travaux a été prévu et chiffré.",
 kicker="Mur porteur", cta="d'ouverture de mur porteur", service="Analyse de devis d'ouverture de mur porteur",
 card="Étude de structure, étaiement, poutre, appuis, autorisations.",
 body="""<h2>L'étude de structure, avant tout</h2>
<p>Le dimensionnement de la poutre et de ses appuis relève d'une <strong>note de calcul</strong>, établie par un bureau d'études structure ou par l'entreprise si elle en a la compétence. Le devis doit dire qui la réalise et si elle est comprise. Une ouverture « dimensionnée à l'œil » est un risque, pour vous comme pour l'entreprise.</p>
<h2>Les points à retrouver sur le devis</h2>
<ul><li><b>L'étaiement</b> provisoire pendant les travaux, avec sa durée.</li>
<li><b>La poutre</b> : matériau (acier, béton, bois lamellé), profil et dimensions issus de la note de calcul, et sa protection (peinture, protection au feu si nécessaire).</li>
<li><b>Les appuis</b> : sommiers ou poteaux, et leur fondation si les charges l'imposent.</li>
<li><b>La démolition et l'évacuation des gravats</b>, et la protection du logement.</li>
<li><b>Les finitions</b> : reprise des enduits, des sols, de l'électricité ou des réseaux qui passaient dans le mur.</li></ul>
<h2>Autorisations et assurance</h2>
<p>En copropriété, toucher un mur porteur demande en principe l'autorisation de l'assemblée générale. Si l'ouverture modifie une façade, une déclaration préalable en mairie peut être nécessaire. Demandez l'attestation d'assurance décennale de l'entreprise et vérifiez qu'elle couvre les travaux de gros œuvre.</p>
<h2>Ce que je vérifie, et ce que je ne fais pas</h2>
<p>Je vérifie que le devis prévoit et chiffre l'étude, l'étaiement, la poutre, les appuis et les reprises, et que rien d'essentiel n'est laissé « selon état ». Je ne réalise pas moi-même le calcul de structure : c'est le rôle du bureau d'études.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Ouverture mur porteur 2,40 m avec IPN : forfait 3 800 € TTC. » Note de calcul comprise ? Quel profil ? Étaiement, sommiers, reprises d'enduit ? À demander : le détail par poste et la note de calcul avant le démarrage.</p>
""",
 faq=[
  ("Faut-il une étude de structure pour ouvrir un mur porteur ?",
   "Oui, le dimensionnement de la poutre et des appuis relève d'une note de calcul. Le devis doit dire qui la réalise et si elle est comprise."),
  ("Faut-il une autorisation pour ouvrir un mur porteur ?",
   "En copropriété, en principe celle de l'assemblée générale. Si la façade est modifiée, une déclaration préalable en mairie peut aussi être nécessaire."),
  ("Comment faire relire mon devis d'ouverture de mur porteur ?",
   "Envoyez-le en PDF ou en photo après avoir commandé l'analyse en ligne : vous recevez sous 48 h un rapport avec les postes manquants et les questions à poser."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-veranda",
 title="Analyse de devis véranda par un ingénieur BTP",
 h1="Analyse de devis véranda",
 desc="Fondations, dalle, raccord au mur, vitrages, surchauffe, autorisation d'urbanisme, TVA à 20 % : ce qu'un ingénieur BTP vérifie sur un devis de véranda.",
 lead="Une véranda est un agrandissement de la maison : elle a besoin de fondations, d'un raccord étanche au mur existant et souvent d'une autorisation. Le devis doit couvrir tout cela, pas seulement la structure vitrée.",
 kicker="Véranda", cta="de véranda", service="Analyse de devis de véranda",
 card="Dalle, raccord au mur, vitrages, urbanisme, TVA.",
 body="""<h2>Une véranda, c'est un agrandissement</h2>
<p>Close et couverte, une véranda crée de la surface. En principe, il faut une <strong>déclaration préalable</strong> entre 5 et 20 m² d'emprise au sol ou de surface de plancher, seuil porté à 40 m² dans les zones urbaines couvertes par un plan local d'urbanisme, et un <strong>permis de construire</strong> au-delà. Si la surface de la maison dépasse 150 m² après travaux, le permis et le recours à un architecte deviennent obligatoires. Votre mairie confirme les règles de votre terrain ; le devis doit dire qui prépare le dossier.</p>
<h2>Les points à retrouver sur le devis</h2>
<ul><li><b>Les fondations et la dalle</b> : nature, épaisseur, isolant sous dalle. Un devis « structure seule » laisse souvent la dalle à votre charge.</li>
<li><b>Le raccord au mur existant</b> : solin ou bande d'étanchéité, et la reprise de la toiture ou de la gouttière si la véranda vient dessous.</li>
<li><b>La structure</b> : matériau (aluminium à rupture de pont thermique, bois, PVC) et sections adaptées à la neige et au vent de votre région.</li>
<li><b>Les vitrages</b> : coefficient Ug, vitrage feuilleté de sécurité en toiture, et protection contre la surchauffe (vitrage à contrôle solaire, stores, ouvrants).</li>
<li><b>La ventilation</b>, pour limiter la condensation l'hiver et la chaleur l'été.</li>
<li><b>Les eaux pluviales</b> : chéneau, descentes et raccordement.</li>
<li><b>L'électricité et le chauffage</b> s'ils sont prévus, et ce que devient la porte ou la fenêtre qui donnait sur l'extérieur.</li></ul>
<h2>Taxe et impôts</h2>
<p>Une véranda close et couverte entre en principe dans le calcul de la taxe d'aménagement, et elle se déclare aux impôts dans les 90 jours qui suivent l'achèvement. Le devis ne la chiffre pas, mais votre budget doit la prévoir.</p>
<h2>Assurance et TVA</h2>
<p>La véranda relève de la garantie décennale : demandez l'attestation de l'entreprise, avec cette activité couverte. Comme toute extension, elle est taxée au taux normal de 20 %, quel que soit l'âge de la maison (voir <a href="guide-tva-travaux-renovation.html">le guide TVA</a>).</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Véranda aluminium 15 m², fourniture et pose : 24 000 € TTC. » Dalle comprise ? Raccord d'étanchéité au mur ? Quel vitrage en toiture ? Évacuation des eaux pluviales ? Dossier d'urbanisme ? À demander : le détail par poste et les références des vitrages.</p>
""",
 faq=[
  ("Faut-il un permis de construire pour une véranda ?",
   "En principe, une déclaration préalable suffit entre 5 et 20 m², ou jusqu'à 40 m² en zone urbaine d'un PLU. Au-delà, ou si la maison dépasse 150 m² après travaux, il faut un permis de construire. La mairie confirme les règles de votre terrain."),
  ("Quelle TVA pour une véranda ?",
   "20 %, comme toute extension qui crée de la surface, quel que soit l'âge de la maison."),
  ("Comment faire relire mon devis de véranda ?",
   "Envoyez-le en PDF ou en photo après avoir commandé l'analyse en ligne : vous recevez sous 48 h un rapport avec les postes manquants, les points d'étanchéité à vérifier et les questions à poser."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-piscine",
 title="Analyse de devis piscine par un ingénieur BTP",
 h1="Analyse de devis piscine",
 desc="Terrassement, évacuation des terres, structure, filtration, sécurité obligatoire, autorisation, TVA à 20 % : ce qu'un ingénieur BTP vérifie sur un devis de piscine.",
 lead="Un devis de piscine annonce souvent un prix « bassin ». Le terrassement, l'évacuation des terres, les plages, les raccordements et la sécurité peuvent pourtant peser autant que le bassin lui-même.",
 kicker="Piscine", cta="de piscine", service="Analyse de devis de piscine",
 card="Terrassement, structure, filtration, sécurité, urbanisme.",
 body="""<h2>Ce que couvre vraiment le prix</h2>
<ul><li><b>Le terrassement et l'évacuation des terres</b> : volume, accès des engins, et ce qui se passe si le sol est rocheux ou humide. Un « selon terrain » sans prix ouvre la porte aux suppléments.</li>
<li><b>La structure du bassin</b> : béton, blocs, panneaux ou coque, le radier, et le revêtement (liner, membrane armée, carrelage).</li>
<li><b>La filtration</b> : pompe, filtre, skimmers, refoulements, local technique, et le chauffage ou le traitement s'ils sont prévus.</li>
<li><b>Les raccordements</b> : électricité avec sa protection dédiée, arrivée d'eau, évacuation des eaux de lavage du filtre.</li>
<li><b>Les plages et margelles</b>, souvent chiffrées à part.</li>
<li><b>La mise en eau et la mise en route</b>.</li></ul>
<h2>La sécurité est obligatoire</h2>
<p>Une piscine enterrée privative non close doit être équipée d'au moins un <strong>dispositif de sécurité normalisé</strong> contre la noyade : barrière (NF P90-306), alarme (NF P90-307), couverture (NF P90-308) ou abri (NF P90-309). Le devis doit dire lequel est prévu, avec sa norme, ou préciser que vous le prenez en charge.</p>
<h2>Autorisation, taxe et impôts</h2>
<p>En principe, un bassin de plus de 10 m² et jusqu'à 100 m² demande une déclaration préalable en mairie, et un permis de construire au-delà ou avec un abri de plus de 1,80 m de haut. Le plan local d'urbanisme peut ajouter des règles, comme la distance aux limites du terrain. La piscine entre dans le calcul de la taxe d'aménagement et se déclare aux impôts dans les 90 jours qui suivent l'achèvement.</p>
<h2>Assurance et TVA</h2>
<p>Une piscine enterrée relève de la garantie décennale : demandez l'attestation de l'entreprise, avec cette activité couverte. La construction d'une piscine est taxée au taux normal de 20 %.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Piscine 8 × 4 m clés en main : 32 000 € TTC. » Terrassement et évacuation des terres compris, sur quelle hypothèse de sol ? Plages, local technique, dispositif de sécurité ? À demander : le détail par poste, et le prix prévu si le sol est rocheux.</p>
""",
 faq=[
  ("Faut-il une autorisation pour construire une piscine ?",
   "En principe, une déclaration préalable pour un bassin de plus de 10 m² et jusqu'à 100 m², un permis de construire au-delà ou avec un abri de plus de 1,80 m. Le PLU de votre commune peut ajouter des règles."),
  ("Quelle sécurité est obligatoire autour d'une piscine ?",
   "Pour une piscine enterrée privative non close, au moins un dispositif normalisé : barrière, alarme, couverture ou abri. Le devis doit préciser lequel."),
  ("Comment faire relire mon devis de piscine ?",
   "Envoyez-le en PDF ou en photo après avoir commandé l'analyse en ligne : vous recevez sous 48 h un rapport avec les postes manquants et les questions à poser. Pour un devis de plus de 30 000 €, demandez d'abord le pré-diagnostic gratuit."),
 ],
))

JOB_PAGES.append(dict(
 slug="analyse-devis-poele",
 title="Analyse de devis poêle à bois ou à granulés par un ingénieur BTP",
 h1="Analyse de devis poêle à bois ou à granulés",
 desc="Conduit de fumée, tubage, sortie de toit, amenée d'air, performances, TVA 5,5 %, RGE : ce qu'un ingénieur BTP vérifie sur un devis de poêle.",
 lead="Sur un devis de poêle, l'appareil n'est qu'une partie du prix. Le conduit de fumée, son raccordement et sa sortie de toit font la sécurité de l'installation.",
 kicker="Poêle", cta="de poêle", service="Analyse de devis de poêle à bois ou à granulés",
 card="Conduit, tubage, sortie de toit, amenée d'air, TVA.",
 body="""<h2>Le conduit de fumée, cœur du devis</h2>
<p>La pose d'un poêle et de son conduit suit le DTU 24.1 (travaux de fumisterie) et la notice du fabricant. Le devis doit préciser :</p>
<ul><li><b>Conduit existant ou neuf</b> : tubage d'un conduit maçonné, ou conduit isolé neuf, avec sa référence.</li>
<li><b>Le contrôle du conduit existant</b> avant tubage : ramonage, état, étanchéité.</li>
<li><b>Les distances de sécurité</b> aux matériaux combustibles (charpente, plancher, cloisons), données par le fabricant du conduit.</li>
<li><b>La sortie de toit</b> : en principe au moins 40 cm au-dessus du faîtage, ou de tout obstacle situé à moins de 8 m, et la reprise d'étanchéité de la couverture.</li>
<li><b>L'amenée d'air</b> : une entrée d'air dédiée, ou un appareil étanche raccordé à l'extérieur, surtout si le logement a une VMC.</li>
<li><b>La plaque de protection du sol</b> si le sol est combustible, et pour un poêle à granulés, l'alimentation électrique.</li></ul>
<p>À la réception, demandez la notice de l'appareil et la plaque signalétique du conduit. Le ramonage est ensuite obligatoire, souvent deux fois par an selon le règlement sanitaire de votre département.</p>
<h2>Les performances et la TVA</h2>
<p>Dans un logement achevé depuis plus de 2 ans, un poêle fourni et posé par l'entreprise relève de 5,5 % s'il respecte des critères de performance : efficacité énergétique saisonnière d'au moins 65 % pour un appareil à bûches, d'au moins 79 % pour un appareil à granulés, et des émissions plafonnées. Sinon, c'est 10 %. Le devis doit indiquer ces valeurs ou joindre la fiche du produit, et vous certifiez vous-même sur le devis ou la facture que les conditions sont remplies. Le conduit posé avec l'appareil suit en principe le même taux.</p>
<h2>Aides et RGE</h2>
<p>Depuis le 1<sup>er</sup> septembre 2026, <strong>MaPrimeRénov' « par geste » ne finance plus les poêles à bois ni à granulés</strong> pour les nouvelles demandes (décret n° 2026-822 et arrêtés du 25 août 2026). Une prime CEE (« prime énergie ») peut rester possible si l'appareil atteint les performances exigées, en général pour remplacer un appareil de chauffage moins performant. Elle se demande avant de signer le devis et exige un installateur RGE avec une qualification adaptée au bois. Vérifiez cette qualification dans l'annuaire officiel des entreprises RGE, et méfiez-vous d'un devis qui déduit une MaPrimeRénov' ou une prime sans préciser laquelle.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Poêle à granulés 8 kW posé, tubage compris : 5 900 € TTC. » Quel modèle, quelle efficacité saisonnière ? Tubage sur combien de mètres, quelle sortie de toit ? Amenée d'air prévue ? À demander : la fiche technique du poêle, le détail du conduit et le taux de TVA ligne par ligne.</p>
""",
 faq=[
  ("Quelle TVA pour un poêle à bois ou à granulés ?",
   "Dans un logement de plus de 2 ans, 5,5 % si l'appareil fourni et posé par l'entreprise respecte les critères de performance (efficacité saisonnière d'au moins 65 % en bûches, 79 % en granulés, émissions plafonnées), sinon 10 %."),
  ("Que doit dire le devis sur le conduit de fumée ?",
   "S'il est tubé ou neuf, sa référence, les distances de sécurité aux matériaux combustibles, la sortie de toit et la reprise d'étanchéité, ainsi que l'amenée d'air du poêle."),
  ("MaPrimeRénov' finance-t-elle encore un poêle ?",
   "Plus en parcours par geste pour les demandes déposées depuis le 1er septembre 2026. Une prime CEE peut rester possible si l'appareil respecte les performances exigées et qu'il est posé par une entreprise RGE ; elle se demande avant de signer le devis."),
  ("Comment faire relire mon devis de poêle ?",
   "Envoyez-le en PDF ou en photo après avoir commandé l'analyse en ligne : vous recevez sous 48 h un rapport avec les postes manquants et les questions à poser."),
 ],
))
