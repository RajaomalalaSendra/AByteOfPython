# To enter  the name and the surname
# Creation of the fonction tableau
vide = ''
def tableau_1(nom, prenom, tel):
    print("{0:*^50}".format(vide))
    print("{0}\t{1}\t{2}".format(nom, prenom, tel))
    print("{0:*^50}".format(vide))
def tableau_2(nom, prenom, tel):
    print("{0}\t{1}\t{2}".format(nom, prenom, tel))
    print("{0:*^50}".format(vide))
# To enter the data in the prompt
nomEtPrenom = dict({"nom":"...", "prenom":"...", "tel":"..."})
nom = input('Entrez votre nom ici s\'il vous plait: ')
nomEtPrenom["nom"] = nom
prenom = input('Entrez votre prenom ici s\'il vous plait: ')
nomEtPrenom["prenom"] = prenom
tel = input('Entrez votre numéro de téléphone ici s\'il vous plait: ')
nomEtPrenom["tel"] = tel
# Get the value from the data to show in the console 
valeur = [value for value in nomEtPrenom.values()]
cles = [key for key in nomEtPrenom.keys()]
tableau_1(cles[0], cles[1], cles[2])
tableau_2(valeur[0], valeur[1], valeur[2])