# Créer un programme qui parcourt le contenu du fichier “domains.xml” et qui compte le
# nombre d’extension de domaines qui s’y trouvent (.com, .net, etc ...).
import xml.etree.ElementTree as ET

# Ouvrir le fichier XML
tree = ET.parse("./domains.xml")
root = tree.getroot()

# Initialiser un dictionnaire pour stocker les extensions de domaine et leur nombre
domain_counts = {}

# Parcourir tous les éléments <domain> dans le fichier XML
for column in root.iter("column"):
    if column.attrib.get("name") == "domain":
        extension = column.text.split(".")[-1]
        if extension in domain_counts:
            domain_counts[extension] += 1
        else:
            domain_counts[extension] = 1


# Afficher le nombre d'extensions de domaine différentes et leur nombre respectif
total = sum(domain_counts.values())
print("Nombre total d'extensions de domaine différentes : ", total)
