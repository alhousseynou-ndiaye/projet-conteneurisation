# Projet DevOps – Application ETL conteneurisée

**Auteur :** Alhousseynou Ndiaye  
**Objectif :** Démontrer un cycle DevOps complet (Dev → Docker → Kubernetes → CI/CD)

---

## 1️⃣ Pitch du projet

### Qu’est-ce que fait l’application ?

- Application ETL simple
- Extraction de données météo depuis une API publique (Open-Meteo)
- Transformation des données (nettoyage)
- Chargement et persistance dans une base SQLite
- Visualisation via un frontend web

### Pourquoi ce projet ?

- Mettre en pratique les concepts DevOps
- Simuler un environnement proche de la production
- Comprendre le rôle DevOps de bout en bout

---

## 2️⃣ Architecture globale

### Microservices

- **Frontend**
  - HTML / JavaScript
  - Servi par Nginx
- **Backend**
  - API Python avec FastAPI
  - Gère le processus ETL
- **Base de données**
  - SQLite
  - Persistée via un volume Kubernetes

### Communication

Utilisateur → Frontend → Backend → SQLite

---

## 3️⃣ Technologies utilisées

- Python / FastAPI
- SQLite
- Docker / Docker Compose
- Kubernetes
- Git / GitHub
- GitHub Actions (CI/CD)
- GitHub Container Registry (images Docker)

---

## 4️⃣ Workflow Git & CI/CD

### Git Flow

- `feature/*` → développement de fonctionnalités
- `develop` → intégration continue
- `main` → production

### CI (branche develop)

- Build des images Docker
- Vérification du backend

### CD (tag sur main)

- Push des images Docker versionnées
- Déploiement automatique sur Kubernetes

---

## 5️⃣ Déploiement sur Kubernetes

### Ressources Kubernetes

- Deployment (frontend, backend)
- Service (NodePort, ClusterIP)
- ConfigMap (configuration)
- Secret (variables sensibles)
- PersistentVolumeClaim (SQLite)

### Objectifs

- Haute disponibilité
- Redémarrage automatique
- Séparation configuration / code

---

## 6️⃣ Démonstration Kubernetes

### Application en fonctionnement

- Pods en état `Running`
- Frontend accessible via NodePort

### Auto-réparation

- Suppression manuelle d’un pod
- Kubernetes recrée automatiquement le pod

### Scalabilité

- Possibilité de scaler dynamiquement les pods

---

## 7️⃣ Sécurité et bonnes pratiques

- Variables sensibles stockées dans des Secrets
- Images Docker versionnées
- Aucune donnée sensible dans Git
- Séparation des environnements (dev / prod)
- Probes de santé (liveness / readiness)

---

## 8️⃣ Défis rencontrés

- Différences entre Docker Compose et Kubernetes
- Gestion du réseau entre services
- Configuration Nginx selon l’environnement
- Compréhension des pipelines CI/CD

### Solutions

- Utilisation de ConfigMap
- Nommage clair des services
- Tests progressifs en local puis en cluster

---

## 9️⃣ Axes d’amélioration

- Ajouter un Ingress Kubernetes
- Monitoring (Prometheus / Grafana)
- Base de données PostgreSQL
- Tests automatisés
- Déploiement sur un cloud public

---

## 🔟 Conclusion

### Ce que ce projet m’a appris

- Comprendre le rôle DevOps
- Automatiser le déploiement d’une application
- Travailler avec Docker et Kubernetes
- Expliquer des choix techniques
