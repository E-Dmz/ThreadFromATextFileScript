tweets = [
    "[🤖 ThreadFromATextFile] Here I show how you can write a thread in a txt file and publish it.",
    "This thread itself has been generated with this method. Noteworthily, the numeration of the tweets is automatic.",
    "First, have a look at the text file. It contains two lists: tweets and media",
    "'tweets' is a list of strings. Each string in tweets is one tweet",

    "A tweet can contain a URL, for example the address to this project's repo: ",
    "'media' is a list of lists. It contains the relative paths (strings) of up to 4 PNG/JPG files (or 1 GIF file) you want to embed.",
    "There's as many elements in tweets as in media: you should use an empty list if you don't want to embed an image.",
    "Next, have a look at the script. Here in a Jupyter notebook: "


]

media = [
    ["../Output/Type0/France-incidence hebdo.png", "../Output/Type0/France-taux hosp.png", "../Output/Type0/France-taux rea.png", "../Output/Type0/France-taux décès.png"],
    ["../Output/Type1/régions métropolitaines 1 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    ["../Output/Type1/régions métropolitaines 2 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"], 
    ["../Output/Type1/régions métropolitaines 3 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    
    [],
    ["../Output/Type1/zoom régions métropolitaines 1 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    ["../Output/Type0/Occitanie-incidence hebdo.png","../Output/Type0/Occitanie-taux hosp.png","../Output/Type0/Occitanie-taux rea.png","../Output/Type0/Occitanie-taux décès.png"],
    ["../Output/Type1/zoom régions métropolitaines 2 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png", "../Output/Type1/zoom régions métropolitaines 3 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    # ["../Output/Type0/Corse-incidence hebdo.png", "../Output/Type0/Corse-taux hosp.png", "../Output/Type0/Corse-taux rea.png", "../Output/Type0/Corse-taux décès.png"],
    # ["../Output/Type0/Occitanie-incidence hebdo.png", "../Output/Type0/Occitanie-taux hosp.png", "../Output/Type0/Occitanie-taux rea.png", "../Output/Type0/Occitanie-taux décès.png"],
    # ["../Output/Type0/Provence-Alpes-Côte d'Azur-incidence hebdo.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux hosp.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux rea.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux décès.png"],
    # ["../Output/Type0/Île-de-France-incidence hebdo.png", "../Output/Type0/Île-de-France-taux hosp.png", "../Output/Type0/Île-de-France-taux rea.png", "../Output/Type0/Île-de-France-taux décès.png"],
    ["../Output/Type1/régions d'outre-mer, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    [],
    ["../Output/Type0/Martinique-incidence hebdo.png", "../Output/Type0/Martinique-taux hosp.png", "../Output/Type0/Martinique-taux rea.png", "../Output/Type0/Martinique-taux décès.png"],
    [],
    # ["../Output/Type0/Guyane-incidence hebdo.png", "../Output/Type0/Guyane-taux hosp.png", "../Output/Type0/Guyane-taux rea.png", "../Output/Type0/Guyane-taux décès.png"],
    # ["../Output/Type0/Mayotte-incidence hebdo.png", "../Output/Type0/Mayotte-taux hosp.png", "../Output/Type0/Mayotte-taux rea.png", "../Output/Type0/Mayotte-taux décès.png"],
    # [],
    # [],
    # [],
    # [],
    # [],
    # [],
    # [],
]