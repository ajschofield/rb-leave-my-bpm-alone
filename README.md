# Rekordbox: Leave My BPM Alone!

Rekordbox 7 seems to have set the default analysis mode to `Auto`.
This resulted in me constantly fighting with the BPM slider as I
hadn't realised that some of my tracks had a dynamic BPM. This works
great for songs that have been ripped from vinyls, or poorly produced
since the early 00's, but bad for modern songs that have been exported
with a constant BPM.

This script is designed to analyse an exported Rekordbox library
in XML format to identify songs that have multiple BPM changes
that Rekordbox has supposedly identified.

# Requirements

Python >= 3.11

# Usage

```python
python3 run.py rekordbox.xml
```
