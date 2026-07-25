import xml.etree.ElementTree as ET
tree = ET.parse('snippet.xml')
root = tree.getroot()

# # Holt das 1 Element (album) 
# if root.tag == "album":
#     album_title = root.attrib.get("title")
#     album_artist = root.attrib.get("artist")
#     print("Titel:", album_title)
#     print("Interpret:", album_artist)

# # Holt das 2 Element (track)
# for child in root:
#     print(child.tag, child.attrib)

# # Holt die Attribute "Titel" & "Genre"
#     # print(root[0][0].text)
#     # print(root[0][1].text)

# for track in root.findall('track'):
#     title = track.find('title').text
#     genre = track.find('genre').text
#     print(f"Title: {title}, Genre: {genre}")

# ----------------------- Complete Code 

album_dict = {}

if root.tag == "album":
    album_dict["title"] = root.attrib.get("title")
    album_dict["artist"] = root.attrib.get("artist")
    album_dict["tracks"] = []

    for track in root.findall('track'):
        track_data = {
            "number": track.attrib.get("number"),
            "duration": track.attrib.get("duration"),
            "rating": track.attrib.get("rating"),  # Wird None, falls nicht vorhanden
            "title": track.find('title').text,
            "genre": track.find('genre').text
        }
        album_dict["tracks"].append(track_data)

print(album_dict)



# **Ziel**

# Verwenden Sie das Python-Modul `xml.etree.ElementTree`, 
# um ein XML-Snippet zu analysieren und seine Struktur und 
# Daten in ein verschachteltes Python-Wörterbuch zu konvertieren, 
# das die Hierarchie genau darstellt und sowohl Elementtext als 
# auch Attribute enthält.

# **Anweisungen**

# Verwenden Sie Python, um die folgenden XML-Daten zu analysieren, 
# die ein Musikalbum darstellen. Schreiben Sie ein Skript, 
# das diese XML-Struktur in ein Python-Wörterbuch umwandelt. 
# Das Wörterbuch sollte die Attribute des Albums`(Titel`, `Interpret`) 
# erfassen und eine Liste der Titel enthalten. Jeder Titel in 
# der Liste sollte ein Wörterbuch sein, das seine Attribute`
# (Nummer`, `Dauer`, `Bewertung`, falls vorhanden) und seine 
# verschachtelten Elementdaten`(Titel`, `Genre`) enthält.