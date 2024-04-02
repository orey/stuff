# Correction à la main du header pourri de Filae
# 0 HEAD
# 1 SOUR FILAE.COM
# 2 CORP FILAE
# 3 ADDR 1 bis, avenue de la république
# 4 POST 75011
# 4 CITY Paris
# 4 CTRY FRANCE
# 1 DEST ANY
# 1 GEDC
# 2 VERS 5.5
# 2 FORM ANY
# 1 CHAR UTF-8
# 1 LANG FRENCH
# --- ces deux champs ont été supprimés
# 1 PLAC
# 2 FORM ANY

# Ensuite  3 traitements pour remettre le fichier decker

# Traitement 1 : remonter les tags CONT et CONC sous leur racine
with open("tente01.ged", 'r') as f:
    with open("tente02.ged", 'w') as g:
        slines = f.readlines()
        buff = []
        # pending a 4 valeurs
        # 0 : on écrit ligne à ligne
        # 1 : on parse les lignes de valeur 2 et on les bufferise
        # 2 : on écrit les CONC et CONT
        # 3 : on vide le buffer
        pending = 0
        start = False
        for l in slines:
            if not start:
                if l.startswith("0 "):
                    start = True
                g.write(l)
            else:
                if l.startswith("2 "):
                    buff.append(l)
                    if pending == 0:
                        # C'est le premier 2
                        pending = 1
                else:
                    if l.startswith("1 CONC") or l.startswith("1 CONT"):
                        if pending == 0:
                            # on doit écrire la ligne sans se poser de question
                            g.write(l)
                        elif pending == 1:
                            # on a fini de bufferiser les 2
                            g.write(l)
                            pending = 2
                        elif pending == 2:
                            # on continue de les écrire au bon endroit
                            g.write(l)
                        else:
                            print("Strange")
                    else:
                        #c'est un tag normal
                        if pending == 2 or pending == 1:
                            #il faut vider le buffer
                            for sl in buff:
                                g.write(sl)
                                buff = []
                                pending = 0
                            g.write(l)
                        else:
                            # on force pending = 0
                            pending = 0
                            # on écrit la ligne
                            g.write(l)
print("Done step 1")                                    
            

# Traitement 2 : on crée des création des notes en remplaçant le premier tag CONT/CONC
with open("tente02.ged", 'r') as f:
    with open("tente03.ged", 'w') as g:
        slines = f.readlines()
        TAGS = ["BIRT", "DEAT", "MARR", "BAPM", "CREM", "BURI", "EMIG", "EVEN", "RESI", "MARB", "CENS", "NATU", "EVEN", "GRAD"]
        for l in slines:
            tag = l[2:6]
            if tag in TAGS and len(l) > 7:
                nb = int(l[0]) + 1
                g.write(l[0:2] + tag + "\n")
                g.write(str(nb) + " NOTE " + l[7:])
            elif tag == "MILI":
                nb = int(l[0]) + 1
                g.write(l[0:2] + "EVEN" + "\n")
                g.write(str(nb) + " TYPE Militaire\n")
                if len(l) > 7:
                    g.write(str(nb) + " NOTE " + l[7:])
            else:
                g.write(l)
print("Done step 2")        


# Traitement 3 : On fixe les lignes pourries (vides ou sans tag)
with open("tente03.ged", 'r') as f:
    with open("tente04.ged", 'w') as g:
        slines = f.readlines()
        first = True
        for l in slines:
            if first:
                first = False
                g.write(l)
            else:
                if len(l) != 0 and len(l) != 1:
                    if (l[0] not in ["0", "1", "2"]) and (l[1] != " "):
                        g.write("1 CONT " + l)
                    else:
                        g.write(l)
print("Done step 3")

    
# Traitement 4 : on crée des création des notes en remplaçant le premier tag CONT/CONC
with open("tente04.ged", 'r') as f:
    with open("tente05.ged", 'w') as g:
        slines = f.readlines()
        within = False
        globalnote = False
        for l in slines:
            if ((l.startswith("0 ")) and (l.endswith("NOTE\n"))):
                globalnote = True
            if l.startswith("0 ") and not l.endswith("NOTE\n"):
                globalnote = False
            if l.startswith("1 CONC") or l.startswith("1 CONT"):
                if within and not globalnote: #ce n'est pas le premier
                    g.write("3" + l[1:])
                elif within and globalnote: #on ne touche rien
                    g.write(l)
                else:
                    if not globalnote:
                        #c'est le premier
                        within = True
                        if len(l) > 7:
                            g.write("2 NOTE " + l[7:])
                        else:
                            g.write("2 NOTE\n")
                    else:
                        g.write(l)
            else:
                g.write(l)
                within = False                
print("Done step 4")                                    
            

# Traitement 5 : on collapse les double NOTE
with open("tente05.ged", 'r') as f:
    with open("tente06.ged", 'w') as g:
        slines = f.readlines()
        previous = ""
        for l in slines:
            if l.startswith("1 NOTE @"):
               g.write(l)
               previous = l
               continue
            if previous[2:6] == "NOTE" and l[2:6] == "NOTE" and len(l) > 7:
                nb = int(l[0]) +1
                g.write(str(nb) + " CONT " + l[7:])
            else:
                g.write(l)
            previous = l
print("Done step 5")


# Traitement 6 : On met des Y
with open("tente06.ged", 'r') as f:
    with open("tente07.ged", 'w') as g:
        slines = f.readlines()
        suspect = False
        previous = ""
        for l in slines:
            if l[0:6] in ["1 DEAT", "1 BIRT"]:
                suspect = True
                previous = l
                continue
            else:
                if suspect == True:
                    p = int(previous[0])
                    c = int(l[0])
                    if c > p:
                        # il y a des records dessous :
                        # on ne fait rien mais on écrit la ligne previous
                        g.write(previous)
                    else:
                        # pas de fils
                        g.write(previous[0:6] + " Y\n")
                g.write(l)
                suspect = False
print("Done step 6")

