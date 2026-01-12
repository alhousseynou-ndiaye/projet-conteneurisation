# Projet DevOps – Application ETL conteneurisée et déployée sur Kubernetes

## 👤 Auteur

- Nom : Alhousseynou Ndiaye
- Profil : Étudiant / Débutant DevOps

---

## 🎯 Objectif du projet

L’objectif de ce projet est de simuler le **cycle de vie complet d’une application moderne**, depuis le développement jusqu’au déploiement en production, en appliquant les **bonnes pratiques DevOps**.

Ce projet met en œuvre :

- une architecture en microservices
- la conteneurisation avec Docker
- l’orchestration avec Kubernetes
- l’automatisation via un pipeline CI/CD
- la résilience et la scalabilité d’une application

---

## 🏗️ Architecture de l’application

### Composants

- **Frontend**

  - Application web simple (HTML / JavaScript)
  - Servie par Nginx
  - Permet de déclencher le processus ETL et d’afficher les données

- **Backend**

  - API Python développée avec FastAPI
  - Réalise un ETL :
    - Extraction de données depuis une API publique
    - Transformation (nettoyage et sélection de champs)
    - Chargement dans une base de données SQLite

- **Base de données**
  - SQLite
  - Persistée via un **Persistent Volume Kubernetes**

---

## 🧰 Technologies utilisées

- **Backend** : Python, FastAPI, SQLite
- **Frontend** : HTML, JavaScript, Nginx
- **Conteneurisation** : Docker, Docker Compose
- **Orchestration** : Kubernetes
- **CI/CD** : GitHub Actions
- **Registry d’images** : GitHub Container Registry (GHCR)

---

## 🐳 Lancement en local (Docker Compose)

```bash
docker-compose up --build

Frontend : http://localhost:8080

Backend : http://localhost:8000

☸️ Déploiement sur Kubernetes
Ressources Kubernetes utilisées

Deployment (frontend, backend)

Service (ClusterIP, NodePort)

ConfigMap (configuration non sensible)

Secret (variables sensibles)

PersistentVolumeClaim (persistance SQLite)

Déploiement
kubectl apply -f deploy/

Vérification
kubectl get pods
kubectl get svc
kubectl get deploy

🔁 CI/CD – Automatisation
CI (Intégration Continue)

Déclenchée à chaque push sur la branche develop

Étapes :

installation des dépendances backend

vérification de l’import de l’application FastAPI

build des images Docker (backend et frontend)

CD (Déploiement Continu)

Déclenché par la création d’un tag Git sur la branche main (ex: v1.0.1)

Étapes :

build des images Docker

push vers GitHub Container Registry

déploiement automatique sur Kubernetes

mise à jour des images via rolling update

Exemple de déclenchement
git tag v1.0.1
git push origin v1.0.1

♻️ Résilience et Scalabilité
Auto-réparation Kubernetes
kubectl delete pod -l app=etl-backend
kubectl get pods
➡️ Kubernetes recrée automatiquement le pod supprimé grâce au Deployment.

Scalabilité
kubectl scale deployment etl-backend --replicas=2
kubectl get pods

📌 Conclusion

Ce projet m’a permis de :

comprendre le rôle DevOps de bout en bout

manipuler Docker et Kubernetes

mettre en place un pipeline CI/CD fonctionnel

apprendre à expliquer et justifier des choix techniques
```
