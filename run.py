import xml.etree.ElementTree as xml
import sys

def main(file):
    collection = xml.parse(file)
    root = collection.getroot()

    tracks = []

    for track in root.iter("TRACK"):
        tempos = track.findall("TEMPO")
        if len(tempos) > 1:
            name = track.get("Name")
            tracks.append(name)

    for name in tracks:
        print(name)

if __name__ == "__main__":
    main(str(sys.argv[1]))
