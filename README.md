# MLOps TP4 – CI/CD, Tests et Gouvernance

## 1. Présentation du projet

Ce projet consiste à mettre en place une pipeline MLOps pour industrialiser le cycle de vie d'un modèle de classification de sentiments.

L'objectif est d'intégrer des pratiques de tests automatisés, de contrôle qualité, de suivi des expériences, de gestion des versions du modèle et de promotion contrôlée, tout en automatisant les vérifications avec GitHub Actions.

Le modèle permet de classifier des avis textuels en deux catégories :
- `0` : sentiment négatif
- `1` : sentiment positif

## 2. Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python 3.11 | Langage principal |
| Scikit-learn | TF-IDF et Logistic Regression |
| MLflow | Suivi des expériences et Model Registry |
| Pytest | Tests automatisés |
| Coverage | Mesure de la couverture des tests |
| Ruff | Analyse statique et qualité du code |
| Bandit | Analyse de sécurité du code Python |
| pip-audit | Vérification des vulnérabilités des dépendances |
| Git / GitHub | Versionnement du code |
| GitHub Actions | Automatisation CI/CD |

## 3. Architecture du projet

```text
mlops-tp4-cictcd/
│
├── .github/
│   └── workflows/
│       └── mlops-pipeline.yml
│
├── data/
│   └── reviews.csv
│
├── src/
│   ├── data.py
│   └── model.py
│
├── tests/
│   ├── test_data.py
│   ├── test_model.py
│   └── test_unit.py
│
├── params.yaml
├── requirements.txt
├── model_card.md
├── promote.py
├── README.md
└── .gitignore
```

## 4. Installation

### Prérequis

- Python 3.11
- Git
- Un environnement virtuel Python

### Cloner le dépôt

```bash
git clone https://github.com/asmaebihkak24/mlops-tp4-cictcd.git
cd mlops-tp4-cictcd
```

### Créer et activer l'environnement virtuel

Sous Windows PowerShell :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Installer les dépendances

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Configuration du modèle

Les paramètres du projet sont centralisés dans `params.yaml`.

Ils comprennent notamment :
- La taille du jeu de test et la graine aléatoire.
- Les paramètres TF-IDF.
- Les hyperparamètres de Logistic Regression.
- Les seuils des Quality Gates.
- Les paramètres de suivi MLflow.

## 6. Tests et Quality Gates

Le projet intègre plusieurs contrôles automatiques :

| Quality Gate | Critère |
|---|---|
| G1 | Réussite des tests unitaires |
| G2 | Validation de la qualité des données |
| G3 | Accuracy minimale de 0.60 |
| G4 | F1-score minimal de 0.50 |
| G5 | Couverture minimale de 70 % |
| G6 | Vérifications de sécurité sans problème bloquant |

### Exécuter les tests

```bash
python -m pytest tests/ -v --cov=src --cov-report=term-missing
```

### Vérifier la qualité du code

```bash
ruff check .
```

### Analyse de sécurité

```bash
bandit -r src
pip-audit
```

### Résultats obtenus

- 11 tests réussis.
- Couverture de code : 100 %.
- Ruff : aucune erreur détectée.
- Bandit : aucun problème identifié.
- pip-audit : aucune vulnérabilité connue détectée.
- Quality Gates : validés.

## 7. Suivi des expériences avec MLflow

MLflow est utilisé pour suivre les expériences et gérer les versions du modèle.

### Démarrer le serveur MLflow

```bash
python -m mlflow server --host 127.0.0.1 --port 5000
```

L'interface est accessible à l'adresse :

http://127.0.0.1:5000

Dans un autre terminal :

```powershell
$env:MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"
```

Le modèle est enregistré dans le Model Registry sous le nom :

`sentiment-model`

La version 1 est associée aux informations suivantes :
- Validation : `passed`
- Approbation : `approved`
- Alias : `candidate` et `champion`

## 8. Promotion contrôlée du modèle

Le script `promote.py` permet de contrôler la promotion d'une version candidate vers l'alias `champion`.

Sans approbation :

```bash
python promote.py
```

Avec approbation explicite :

```bash
python promote.py --approve
```

La promotion nécessite que le modèle ait satisfait les conditions de validation. L'approbation est simulée par l'exécution explicite de la commande avec `--approve`.

## 9. Pipeline CI/CD avec GitHub Actions

Le workflow est défini dans :

`.github/workflows/mlops-pipeline.yml`

Il est déclenché lors :
- D'un push sur les branches `main` et `develop`.
- D'une Pull Request vers `main`.

Le pipeline comprend trois jobs :

### Quality
- Installation des dépendances.
- Vérification du code avec Ruff.
- Exécution des tests unitaires et des tests de données.
- Vérification des Quality Gates du modèle.
- Analyses de sécurité avec Bandit et pip-audit.

### Staging
Simulation du déploiement du candidat vers l'environnement Staging après réussite du job Quality.

### Production
Simulation du déploiement du modèle approuvé vers l'environnement Production après réussite du job Staging.

**Important :** les étapes Staging et Production utilisent des commandes de simulation (`echo`). Aucun déploiement réel n'est effectué.

## 10. Model Card et auditabilité

Le fichier `model_card.md` documente :
- Le cas d'utilisation du modèle.
- Les données et les méthodes utilisées.
- Les paramètres et les métriques.
- Les résultats des tests et des contrôles qualité.
- Les limites du modèle.
- Les informations de validation et d'approbation.
- Les identifiants MLflow et les empreintes SHA256.

Cette documentation permet de faciliter le suivi, la reproductibilité et l'audit du projet.

## 11. Limites du projet

- Le dataset pédagogique contient seulement 20 avis.
- Les performances obtenues ne permettent pas de conclure à une aptitude à un usage industriel.
- Les environnements Staging et Production sont simulés.
- Le processus d'approbation est déclenché manuellement par script et ne constitue pas un système complet de gouvernance en production.

## 12. Conclusion

Ce projet met en œuvre une chaîne MLOps intégrant les tests automatisés, les contrôles qualité, le suivi des expériences avec MLflow, la gestion des versions du modèle et un workflow CI/CD avec GitHub Actions.

Il permet de démontrer les principales étapes nécessaires pour fiabiliser et contrôler le cycle de vie d'un modèle de Machine Learning.
