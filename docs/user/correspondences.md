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
> Akteur:in A und ein Ereignis **Empfang** mit Akteur:in B, so gilt sie als Brief von
> A an B.

Die absendende Person wird also als Akteur:in des Entstehungs-Ereignisses erfasst, die
empfangende Person als Akteur:in des Empfangs-Ereignisses. Sobald genügend solche Paare
vorliegen, erscheint der Briefwechsel in der Liste. Umgekehrt gilt: Wer die
Ansicht nutzen will, muss beim Erschliessen konsequent beide Ereignisse setzen —
ein Brief, dem das Empfangs-Ereignis fehlt, taucht nirgends auf.

Die Verzeichnungsstufe spielt keine Rolle.

!!! note "Mindestzahl an Briefen"
    Ein Akteurspaar erscheint erst ab einer Mindestzahl von Briefen — im
    Standard fünf. Vereinzelte Briefe bleiben also aussen vor. Die Schwelle ist
    pro Archiv einstellbar, aber im Admin-Bereich nicht änderbar; bei Anton as a
    Service ist dafür k & r zuständig.

## Für wen sich das lohnt

Die Ansicht richtet sich an Archive mit Briefbeständen — Nachlässe, Sammlungen
von Gelehrtenkorrespondenz. Sie ist auf jeder Installation vorhanden, bleibt
aber leer, solange nicht in dieser Systematik erschlossen wird. Für ein Archiv
ohne Briefe hat sie keinen Nutzen.
