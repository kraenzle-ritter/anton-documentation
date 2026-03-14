# Videoarchivierung

Diese Beispiel-Empfehlungen dienen als Orientierung für kleinere, private Archive, die kostenbewusst VHS Material digital archivieren wollen. Sie ersetzen keine interne Archivrichtlinie und sind nicht verbindlich.

Ziel: Ein praxisnahes, speichereffizientes Vorgehen bei weitgehender Wahrung archivischer Standards.

Die Archivierung von VHS-Digitalisaten erfolgt in zwei Qualitätsstufen. Die Bewertung erfolgt durch die Archivar:innen auf Grundlage der Bewertungskriterien.

## Bewertungskriterien

| Kriterium | A (Verlustfrei) | B (Visuell verlustfrei) |
|-----------|-----------------|-------------------------|
| Originalität | Originalaufnahmen / Unikate | Weitere Kopien vorhanden |
| Informations- und Dokumentationswert | sehr hoch | ja bitte|
| Urheberrechte / Nutzungsrechte | Beim Archiv | Nicht beim Archiv |
| Qualität der Aufnahme | Hoch | Geringer |
| Visuelle Relevanz für den Informationswert | Hoch oder Farben sind relevant| Nachrangig |
| Träger-Zustand | Schlechter physischer Zustand von Unikaten | – |
| Beispiele | – | Fernsehaufnahmen ohne direkten Archivierungsauftrag |

## Technische Spezifikation

| Eigenschaft | A: Verlustfrei (.mkv) | B: Visuell verlustfrei (.mp4) |
|-------------|----------------------|------------------------------|
| Container | Matroska (.mkv) | MPEG-4 (.mp4) |
| Video-Codec | FFV1 v3 (verlustfrei) | H.264 High Profile, CRF 19 |
| Audio-Codec | PCM 24-bit / 48 kHz | AAC 192 kbps |
| Grösse/Stunde | 20–30 GB | 3–5 GB |
| Besonderheit | integrierte CRC-Prüfsummen | Visuell unverändert, ca. 75 bis 85% Speicherersparnis |


<!--
```bash 
ffmpeg -i input.mkv \
-c:v libx264 \
-preset slow \
-crf 19 \
-profile:v high \
-pix_fmt yuv420p \
-c:a aac -b:a 192k \
-movflags +faststart \
output.mp4
```

Erklärung:
* -c:v libx264 → H.264 Video Codec  
* -preset slow → bessere Kompression, kleiner als medium, langsamer encode  
* -crf 19 → je höher der Wert desto grösser die Kompression (18: nahezu verlustfrei)  
* -profile:v high → hohe Kompatibilität  
* -pix_fmt yuv420p → Standard für MP4, maximale Abspielbarkeit  
* -c:a aac -b:a 192k → Stereo Audio  
* -movflags +faststart → MP4 kann sofort gestreamt werden  
-->

<br><br><br><br><br>

| Kriterium | A (Verlustfrei) | B (Visuell verlustfrei) |
|-----------|-----------------|-------------------------|
| Originalität / Seltenheit | Einmalige Aufnahmen, historische Unikate | Kopien oder TV-Sendungen, mehrfach vorhanden |
| Rechte | Verwertung/Nutzung gesichert | Eingeschränkte Nutzung |
| Signalqualität / Artefakte | Stark verrauschte, beschädigte oder hochwertige Originalbänder | Material ohne kritische Defekte, normale VHS-Qualität |
| Auflösung / Format | Hohe Auflösung (S-VHS, Betacam) oder ungewöhnliches Format | Standard VHS (PAL/NTSC) |
| Framerate / Interlacing | Interlaced original erhalten |Progressiv für Nutzung akzeptabel, optional deinterlaced |
| Farbtiefe / Farbtreue | Historisch relevante Farbinformation, Originalfarbraum YUV 4:2:2 | Normale Farbtreue ausreichend, YUV 4:2:0 |
| Träger-Zustand | Schlechte physische Kondition relevant | Guter Zustand, keine besondere Dringlichkeit |
| Zukünftige Nutzung / Bearbeitung | Professioneller Schnitt, Re-Encodes, wissenschaftliche Analyse | Hauptsächlich Sichtung, Streaming, Präsentation |
| Langzeitarchivierung / Risiko | Einzelstück, hohes Risiko bei Verlust | Kopien vorhanden, mehrfach gesichert |
| Speicher / Aufwand |  Große Datenmenge akzeptabel (~20–30 GB/h) | Speicher effizient (~3–5 GB/h), praktisch für viele Bänder |
| Abspielkompatibilität / Geräte| Archivorientiert, weniger relevant für sofortige Wiedergabe | Breite Kompatibilität für PC, TV, Browser |
| Metadaten / Dokumentation | Umfangreich vorhanden → unterstützt langfristige Nutzung | Wenige Metadaten, einfache Verwaltung | 
