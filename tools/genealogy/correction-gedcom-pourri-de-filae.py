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
print("Done")                                    
            


# Traitement 2 : On fixe les lignes pourries (vides ou sans tag)
with open("tente02.ged", 'r') as f:
    with open("tente03.ged", 'w') as g:
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
    print("File cleaned")

    
# Traitement 3 : on crée des création des notes en remplaçant le premier tag CONT/CONC
with open("tente03.ged", 'r') as f:
    with open("tente04.ged", 'w') as g:
        slines = f.readlines()
        within = False
        for l in slines:
            if l.startswith("1 CONC") or l.startswith("1 CONT"):
                if within: #ce n'est pas le premier
                    g.write("2" + l[1:])
                else:
                    #c'est le premier
                    within = True
                    if len(l) > 7:
                        g.write("1 NOTE " + l[7:])
                    else:
                        g.write("1 NOTE\n")
            else:
                g.write(l)
                within = False
                
print("Done")                                    
            
                
