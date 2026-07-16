# Korrespondenzen

Die Korrespondenzansicht bündelt Briefe zu Briefwechseln: Sie zeigt, wer mit wem
korrespondiert hat, wie viele Briefe erhalten sind und über welchen Zeitraum. Von
dort lässt sich der Briefwechsel chronologisch durchblättern — vor und zurück
bleibt dabei innerhalb desselben Briefwechsels.

Die Ansicht liegt unter `/correspondences`. Sie ist nicht in der Navigation
verlinkt; Archive, die sie nutzen, hängen sie selbst ins Menü.

## Ein Briefwechsel entsteht von selbst

Es gibt nichts anzuklicken und nichts anzulegen. Anton leitet die
Briefwechsel **automatisch aus den [Ereignissen](antonevents.md) ab**:

> Trägt eine Verzeichnungseinheit ein Ereignis **Entstehungszeitraum** mit
> Akteur A und ein Ereignis **Empfang** mit Akteur B, so gilt sie als Brief von
> A an B.

Der Absender wird also als Akteur des Entstehungs-Ereignisses erfasst, der
Empfänger als Akteur des Empfangs-Ereignisses. Sobald genügend solche Paare
vorliegen, erscheint der Briefwechsel in der Liste. Umgekehrt gilt: Wer die
Ansicht nutzen will, muss beim Erschliessen konsequent beide Ereignisse setzen —
ein Brief, dem das Empfangs-Ereignis fehlt, taucht nirgends auf.

Die Verzeichnungsstufe spielt keine Rolle.

!!! note "Mindestzahl an Briefen"
    Ein Akteurspaar erscheint erst ab einer Mindestzahl von Briefen — im
    Standard fünf. Vereinzelte Briefe bleiben also aussen vor. Die Schwelle ist
    pro Archiv einstellbar; für Anpassungen ist k & r zuständig.

## Für wen sich das lohnt

Die Ansicht richtet sich an Archive mit Briefbeständen — Nachlässe, Sammlungen
von Gelehrtenkorrespondenz. Sie ist auf jeder Installation vorhanden, bleibt
aber leer, solange nicht in dieser Systematik erschlossen wird. Für ein Archiv
ohne Briefe hat sie keinen Nutzen.
