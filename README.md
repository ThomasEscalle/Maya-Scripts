# Maya Scripts

Bienvenue dans mon dépôt de scripts Python pour Autodesk Maya ! 🎨

Ce dépôt contient tous les scripts que j'ai créés et que j'utilise quotidiennement dans mon travail sur Maya. Ces scripts sont conçus pour automatiser des tâches, améliorer les workflows et simplifier le travail dans Maya.

## Installation

1. Téléchargez chaque fichier `.py` qui vous intéresse.
2. Placez-le dans le répertoire scripts de Maya, ou installez le dans votre shelf.

## Modeling

- [Cleanup Mode](Modeling/Cleanup_mode/cleanup.py): Nettoie la scène en supprimant l'historique, en gelant les transformations et en optimisant la taille de la scène.
- [Rename Objects](Modeling/RenameObjects/RenameObjects.py): Ouvre une fenêtre pour renommer les objets sélectionnés dans la scène.

## Pipeline

- [Create Multiple References](Pipeline/CreateMultipleReferences/CreateMultipleReferences.py): Permet de créer plusieurs références d'un fichier dans la scène via une interface utilisateur.
- [Delete Node By Type](Pipeline/DeleteNodeByType/DeleteNodeByType.py): Supprime tous les objets d'un type spécifique, utile pour résoudre des problèmes liés à des plugins manquants.
- [Publish Scene](Pipeline/PublishScene/PublishScene.py): Sauvegarde la scène actuelle en tant que version "publish" (non utilisé actuellement, conservé pour référence).

## Surfacing

- [Basic Material Creator](Surfacing/BasicMaterialCreator/BasicMaterialCreator.py): Crée un shader PxrSurface avec des options pour le diffuse, la rugosité, le bump et le displacement.
- [Rename Hypershade Nodes](Surfacing/RenameHypershadeNodes/RenameHypershadeNodes.py): Ouvre une fenêtre pour renommer les nœuds dans l'Hypershade.
- [Toggle Lookdev Scene](Surfacing/ToogleLookdevScene/ToogleLookdevScene.py): Active ou désactive une scène de lookdev en créant ou supprimant un PxrDomeLight.
- [Workspace Replace](Surfacing/WsReplace/WsReplace.py): Modifie les chemins des nœuds PxrTexture pour les rendre relatifs au dossier `/sourceimages/`.

