# 🖥️ The Giving Tree - XML to Python Dictionary

**Course:** Cyber Security Analyst - Technical Foundation Basics | **Date:** 30 Juni 2025

---

## Task

**Objective:** Parse XML using `xml.etree.ElementTree` and convert it into a nested Python dictionary.

---

## Solution

### Python Script

```python
import xml.etree.ElementTree as ET

xml_data = """
<album title="Abbey Road" artist="The Beatles">
  <track number="1" duration="4:20">
    <title>Come Together</title>
    <genre>Rock</genre>
  </track>
  <track number="2" duration="3:29">
    <title>Something</title>
    <genre>Rock</genre>
  </track>
  <track number="7" duration="3:05" rating="5_stars">
    <title>Here Comes the Sun</title>
    <genre>Folk Rock</genre>
  </track>
</album>
"""

# Parse XML
root = ET.fromstring(xml_data)

# Build dictionary
album_dict = {
    "title": root.attrib["title"],
    "artist": root.attrib["artist"],
    "tracks": []
}

# Iterate through tracks
for track in root.findall("track"):
    track_dict = {
        "number": track.attrib["number"],
        "duration": track.attrib["duration"],
        "title": track.find("title").text,
        "genre": track.find("genre").text
    }
    # Add optional rating
    if "rating" in track.attrib:
        track_dict["rating"] = track.attrib["rating"]
    
    album_dict["tracks"].append(track_dict)

print(album_dict)
```

### Output

```python
{
    'title': 'Abbey Road',
    'artist': 'The Beatles',
    'tracks': [
        {'number': '1', 'duration': '4:20', 'title': 'Come Together', 'genre': 'Rock'},
        {'number': '2', 'duration': '3:29', 'title': 'Something', 'genre': 'Rock'},
        {'number': '7', 'duration': '3:05', 'title': 'Here Comes the Sun', 'genre': 'Folk Rock', 'rating': '5_stars'}
    ]
}
```

---

## Notes

- **`ET.fromstring()`:** Parses an XML string directly
- **`.attrib`:** Dictionary of all attributes of an element
- **`.find("tag")`:** Finds the first child element with this tag
- **`.findall("tag")`:** Finds all child elements with this tag
- **`.text`:** Text content of the element

