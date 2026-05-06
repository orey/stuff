#/bin/bash
IFS=' '
IPA=$(hostname -I)
read -ra TOKENS <<<"$IPA"
MYIP=${TOKENS[0]}
echo "The server will be launched on http://localhost:8080 or http://${MYIP}:8080"
open-webui serve