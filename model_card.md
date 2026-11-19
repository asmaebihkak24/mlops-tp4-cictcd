\# Sentiment Model



\## Use Case

Classification binaire de sentiment permettant de distinguer les avis clients positifs et négatifs à partir de leur contenu textuel.



\## Version

\- Model name: sentiment-model

\- Model version: 1

\- Framework: Scikit-learn



\## Dataset

\- Source: data/reviews.csv

\- Description: jeu de données pédagogique contenant 20 avis.

\- Features: text

\- Target: label (0 = négatif, 1 = positif)

\- Distribution: 10 avis positifs et 10 avis négatifs.



\## Method

\- TF-IDF pour la représentation numérique des textes.

\- Logistic Regression pour la classification binaire.



\## Parameters

\- C = 10.0

\- max\_features = 5000

\- ngram\_range = \[1, 1]

\- max\_iter = 1000

\- test\_size = 0.25

\- random\_state = 42



\## Metrics

\- Accuracy = 0.60

\- F1 = 0.50



\## Quality Gates

\- Unit tests = PASSED (3 tests)

\- Data tests = PASSED (4 tests)

\- Model tests = PASSED (4 tests)

\- Total tests = 11 PASSED

\- Code coverage = 100%

\- Bandit = PASSED (no issues identified)

\- pip-audit = PASSED (no known vulnerabilities found)

\- Model Quality Gates = PASSED



\## Known Limitations

\- Petit jeu de données pédagogique.

\- Langue principalement française.

\- Évaluation non représentative d'un contexte industriel.

\- Performances limitées par la taille et la diversité du dataset.



\## Governance and Traceability



\- Model name: sentiment-model

\- Model version: 1

\- MLflow Run ID: d01de449cd3f4684b4299f97a665ffbd

\- MLflow Model ID: m-2d1e176d0fe540caaed0dd20e5f7831b

\- validation\_status: passed

\- approval\_status: approved

\- Model alias: champion

\- Promotion command: python promote.py --approve

\## Deployment Decision



La version 1 du modèle a satisfait les Quality Gates et a reçu une approbation explicite pour sa promotion vers l'alias champion.



La décision est documentée par les éléments suivants :



\- Code: dépôt GitHub versionné avec Git.

\- Data: data/reviews.csv.

\- Parameters: params.yaml.

\- Model: sentiment-model, version 1, enregistré dans MLflow.

\- Tests: 11 tests réussis avec une couverture de 100%.

\- Approval: approval\_status = approved.

\- Deployment: jobs Staging et Production validés dans GitHub Actions.



Final decision: APPROVED FOR SIMULATED DEPLOYMENT.



Le déploiement réel du modèle dans un environnement de production n'a pas été effectué.

\## Reproducibility and Integrity



\- Git commit: `b34d49a8d3f8be990abd5679bff83e1ad3117096`



\### Configuration integrity

\- File: `params.yaml`

\- SHA256: `2767135EF71B59199B4BC2E7DFB7B6D66B9240CB9B48154DF81518AAF72ABBA7`



\### Dataset integrity

\- File: `data/reviews.csv`

\- SHA256: `B422FB8D13A54E3A2A1827A1AAF60A79ECF3D0897D3FF57FA142072503191236`

