#/bin/bash
LOCAL=/home/olivier/JDR-RPG
#REMOTE=/run/user/1000/gvfs/ftp:host=ls-wxl271.local/array1/DisqueBuffaloRaid1/JDR-RPG
REMOTE=/run/user/1000/gvfs/ftp:host=192.168.1.35/array1/DisqueBuffaloRaid1/JDR-RPG

FILESYNC=/home/olivier/olivier-repos/github/stuff/tools/file-manipulations/filesync
GARBAGE=/home/olivier/temp/

ROOT="TTRPG/Esper Genesis/"

echo "=== Analyzing the 2 folders ==="
python3 $FILESYNC/filesync.py -s $LOCAL/"$ROOT" -t $REMOTE/"$ROOT" -g $GARBAGE -a

function yes_or_no {
    while true; do
        read -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) return 0  ;;  
            [Nn]*) echo "Aborted" ; return  1 ;;
        esac
    done
}

yes_or_no "Synchronize? " && python3 $FILESYNC/filesync.py -s $LOCAL/"$ROOT" -t $REMOTE/"$ROOT" -g $GARBAGE

echo "=== Done ==="

