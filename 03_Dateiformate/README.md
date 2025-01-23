## Aufgabenbeschreibung

1. Erstelle aus den Daten eine YAML-Datei.
2. Erstelle ein XML-File aus der JSON.
3. Validiere das XML-File mittels XSD.

### Fragen:
1. **Unterschiede bei Datentypen:**
   - Textformate (z. B. XML, JSON): Gut lesbar für Menschen, aber größere Dateien.
   - Binärformate: Kleinere Dateien, schnell für Computer, aber nicht direkt lesbar.

2. **Vor- und Nachteile der Dateiformate:**
   - XML:
        + Sehr geordnet und flexibel
        + kann mithilfe des xsd schemas gegengeprüft werden
        - Braucht viel Platz und ist umständlich
   
   - JSON:
        + Einfach, leicht verständlich und gut mit JavaScript nutzbar
        - Weniger Möglichkeiten zur Prüfung (kein XSD möglich)
   
   - YAML:
        + Super lesbar, übersichtlich, mit Kommentaren
        - Etwas schwerer zu verarbeiten, Leerzeichen können die Struktur und die funktionalität beeinflussen
   
   - Binärformate (z.B. JPG, PNG):
        + Speziell optimiert für Bilder
        + JPG: Kleine Dateigröße durch Kompression
        + PNG: Verlustfreie Kompression
        - Nicht ohne spezielle Programme lesbar/editierbar
        - JPG: Verlust an Bildqualität möglich

3. **Wofür nutzt man XML?**
    - Datenaustausch zwischen Systemen
    - Einstellungen speichern
    - Um Daten in Web-Dienste zu transportieren z.B (SOAP)
    - Dokumentformate wie DocX (Word) oder SVG (Grafiken)

4. **Kann man in XML eigene Tags machen?**
    - Ja, du kannst eigene Tags erstellen, man muss nur darauf achten, dass man diese auch sauber definiert (Öffnen/Schließen)
    - Regeln dafür kann man mit XSD festlegen 

5. **Wann nutzt man welchen Datentyp?**
    - XML: Für komplizierte Daten mit vielen Ebenen
    - JSON: Perfekt für Web-APIs und JavaScript
    - Binär: Für große Daten und schnelle Verarbeitung

6. **Was ist eine XSD-Datei?**
    - XSD steht für XML Schema Definition
    - Sie legt fest, wie XML-Daten aufgebaut sein sollen
    - Dient zur Prüfung (Validierung) von XML-Dateien, damit kann man sichergehen, das die XML Daten genau dem Schema entsprechen was zuvor festgelegt wurde

7. **Was heißt Validierung?**
    - Daten prüfen, ob sie korrekt sind
    - Sie werden mit vorgegebenen Regeln(XSD-Datei/Schema) verglichen
    - So stellt man sicher, dass die Daten passen bevor man sie weiter verarbeitet

8. **Wie sieht eine XML-Datei aus?**
    - Ähnelt HTML
    - Daten sind in einer Baumstruktur organisiert
    - Alles ist in Tags verschachtelt (siehe data.xml)

9. **Was bedeutet Parsen?**
    - Text in eine verständliche Form für Computer umwandeln
    - Struktur des Textes analysieren
    - Daten so aufbereiten, dass sie weiterverarbeitet werden können
    - z.B das lesen eines JSON-Strings umd umwandeln in ein Python-Dictionary





