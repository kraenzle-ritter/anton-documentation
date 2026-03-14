# Gewichtete Suche

Die gewichtete Suche verbessert die Suchergebnisse in Listenansichten, indem Treffer nach ihrer Relevanz sortiert werden. Je besser ein Suchbegriff mit einem Datensatz übereinstimmt, desto weiter oben erscheint er in der Ergebnisliste.

## Anwendungsbereiche

Die gewichtete Suche ist verfügbar für:

- **Akteur:innen** (Actors)
- **Orte** (Places)
- **Schlagwörter** (Keywords)

## Funktionsweise

Das System bewertet Treffer nach verschiedenen Kriterien:

| Trefferart | Bewertung |
|------------|-----------|
| **Exakte Übereinstimmung** | Höchste Relevanz (3×) |
| **Treffer am Wortanfang** | Hohe Relevanz (2×) |
| **Treffer enthält Suchbegriff** | Basis-Relevanz (1×) |

**Beispiel**: Bei der Suche nach "Müller" wird:

1. Ein Akteur namens "Müller" (exakt) ganz oben angezeigt
2. Gefolgt von "Müller-Weber" (beginnt mit)
3. Dann "Anna Müller" (enthält)

Zusätzlich werden verschiedene Felder unterschiedlich gewichtet. Der Name eines Akteurs zählt beispielsweise mehr als ein Treffer in der Beschreibung.

## Aktivierung

### In der Listenansicht

1. Öffne die gewünschte Listenansicht (z.B. Akteur:innen)
2. Gib einen Suchbegriff in das Filterfeld ein
3. Unter dem Suchfeld erscheint die Checkbox **"Nach Relevanz sortieren"**
4. Aktiviere die Checkbox, um die Ergebnisse nach Relevanz zu sortieren

!!! note "Hinweis"
    Die Checkbox erscheint nur, wenn eine Suche aktiv ist.

### Als Standardeinstellung in den Benutzereinstellungen

Du kannst die gewichtete Suche als Standardeinstellung aktivieren:

1. Klicke auf dein Profil (oben rechts)
2. Wähle **Profil / Account**
3. Gehe zu **Einstellungen**
4. Aktiviere **"Gewichtete Suche aktivieren"**

Wenn diese Option aktiviert ist, wird die Checkbox "Nach Relevanz sortieren" in den Listenansichten automatisch vorausgewählt.

## Tipps

- Die gewichtete Suche ist besonders nützlich bei **häufigen Namen** oder **allgemeinen Begriffen**
- Bei der Suche nach **exakten Signaturen** oder **IDs** ist die normale Sortierung oft hilfreicher
- Die Einstellung kann jederzeit pro Suche über die Checkbox umgeschaltet werden
