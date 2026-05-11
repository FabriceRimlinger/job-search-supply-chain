#!/bin/bash
# Lance le serveur JANUS dans un terminal et ouvre le dashboard dans Brave

PROJECT="/home/fabrice/Documents/Job_Search/Recherche Emploi Supply Chain"
PORT=8765

# Arrêter un éventuel serveur déjà en cours sur ce port
fuser -k ${PORT}/tcp 2>/dev/null
sleep 0.5

# Lancer le serveur dans un terminal visible
gnome-terminal --title="JANUS Server" -- bash -c "cd '$PROJECT' && python3 janus_server.py; read -p 'Serveur arrêté. Appuie sur Entrée pour fermer.'"

# Attendre que le serveur soit prêt
sleep 2

# Ouvrir dans Brave
flatpak run com.brave.Browser "http://localhost:${PORT}/janus.html" 2>/dev/null &
