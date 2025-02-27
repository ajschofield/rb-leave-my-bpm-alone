import xml.etree.ElementTree as xml
import sys
import os

def main(file):
    processed_only = os.environ.get("PROCESSED_ONLY", "false").lower() == 'true'
    collection = xml.parse(file)
    root = collection.getroot()

    processed_keys = set()
    for node in root.findall(".//NODE"):
        name = node.get("Name")
        if name is not None and "** Processed" in str(name):
            for track_ref in node.findall("TRACK"):
                key = track_ref.get("Key")
                if key:
                    processed_keys.add(key)
            break

    tracks = []
    for track in root.iter("TRACK"):
        if processed_only and track.get("TrackID") not in processed_keys:
            continue
        tempos = track.findall("TEMPO")
        if len(tempos) > 1:
            bpms = {float(tempo.get("Bpm", "0")) for tempo in tempos}
            if len(bpms) > 1:
                name = track.get("Name")
                tracks.append(name)

    for name in tracks:
        print(name)

if __name__ == "__main__":
    main(str(sys.argv[1]))
