## Aufgabenbeschreibung
Die Daten sollen in einer Datenbank gespeichert werden.

1. **DB aufsetzen**: Die Datenbank wird eingerichtet, um Daten zu speichern.
2. **Struktur der Datenbank mittels semantisches ER-Diagramm**: Das semantische ER-Diagramm wird erstellt, um die Struktur der Datenbank zu visualisieren.
3. **Datenbank aufsetzen und Daten einfügen**: Die Datenbank wird erstellt und Daten werden eingefügt.
4. **Daten mittels SQL-Querys bearbeiten (nicht über xampp-oberfläche)**:
   a) **Hinzufügen**: Neue Daten werden der Datenbank hinzugefügt.
   b) **Löschen**: Daten werden aus der Datenbank gelöscht.
   c) **Bearbeiten**: Bestehende Daten werden in der Datenbank bearbeitet.
   d) **Auslesen**: Daten werden aus der Datenbank abgerufen.

### Fragen:

### **Welche Datenbanken gibt es?**  
- **SQL-Datenbanken** (z.B. MySQL, PostgreSQL, Microsoft SQL Server).  
- **NoSQL** (z.B. MongoDB, CouchDB).

---

### **Wann macht welcher Typ Sinn?**  
- **SQL**: Sinnvoll bei großen Datenmengen und gleichbleibenden Attributen, z.B. für Unternehmenssysteme.  
- **NoSQL**: wenn sich Datenstrukturen oft verändern, bei großen Datenmengen, hohe Geschwindigkeit oder z.b. bei Cloud Umgebungen.

---

### **Was ist ein Primary Key und was ein Foreign Key?**  
- **Primary Key**: Eindeutiger Identifikator für ein Element in der Datenbank  
- **Foreign Key**: Ein Attribut, das auf einen Primary Key in der Datenbank verweist.  

---

### **Was ist ein nativer und was ein künstlicher Primary Key?**  
- **Nativer Primary Key**: Ein existierendes Attribut, dessen Wert immer einzigartig ist.  
- **Künstlicher Primary Key**: Ein neu generiertes Attribut, z.B. eine automatische ID.  

---

### **Welche Beziehungstypen zwischen Tabellen gibt es?**  
1. **1:1**: Ein Datensatz aus einer Tabelle hat genau eine Verbindung zu einem anderen Datensatz in einer Tabelle. 
2. **1:n**: Ein Datensatz aus einer Tabelle hat mehrere Verbindung zu einem anderen Datensatz in einer Tabelle.  
3. **n:m**: Mehrere Datensatz aus einer Tabelle können mehrere Verbindung zu einem anderen Datensatz in einer Tabelle. 

---

### **Welche Wildcards gibt es in MySQL und was bedeuten sie?**  
- **%**: Platzhalter für beliebig viele Zeichen (z.B. `LIKE 'A%', '%A'` findet alles, was mit A beginnt oder alles was ein A am ende hat).  
- **_**: Platzhalter für genau ein Zeichen (z.B. `LIKE '_b, b_'` findet alles, wo "b" der zweite und letzte Buchstabe ist oder wo "b" der erste Buchstabe mit einem beliebigen darauffolgenden ist).  

---

### **Was ist ein Join?**  
Ein **Join** verbindet zwei oder mehr Tabellen in SQL, indem man festlegt, wie sie zusammenpassen (z. B. gleiche Werte in einer Spalte). Das Ziel ist es, relevante Daten aus beiden Tabellen zu kombinieren.

### Arten von Joins:
- **INNER JOIN**: Zeigt nur übereinstimmende Daten aus beiden Tabellen.
- **LEFT JOIN**: Zeigt alle Daten aus der linken Tabelle, auch wenn rechts nichts passt.
- **RIGHT JOIN**: Umgekehrt zum LEFT JOIN.
- **CROSS JOIN**: Alle möglichen Kombinationen.
- **FULL JOIN**: Alles aus beiden Tabellen, auch ohne Übereinstimmung. 

---

### **Was ist ein left- und was ein right-Join?**  
- **Left Join**: Gibt alle Zeilen der linken Tabelle aus, auch wenn es keine Übereinstimmungen in der rechten Tabelle gibt.  
- **Right Join**: Gibt alle Zeilen der rechten Tabelle aus, auch wenn es keine Übereinstimmungen in der linken Tabelle gibt.  

---

### **Was ist das kartesische Produkt zweier Tabellen?**  
Das Ergebnis einer Verknüpfung ohne Bedingung, bei der jede Zeile der ersten Tabelle mit jeder Zeile der zweiten Tabelle kombiniert wird.  

---

### **Was ist Kaskadierung?**  
Eine Regel, die festlegt, wie verbundene Daten behandelt werden:  
- **On Delete Cascade**: Löscht verbundene Daten automatisch, wenn eine Referenz gelöscht wird.  
- **On Update Cascade**: Aktualisiert verbundene Daten automatisch, wenn eine Referenz geändert wird.  

---

### **Wann werden Gruppierungen benötigt?**  
Wenn Daten nach bestimmten Kriterien zusammengefasst werden sollen, z.B. zur Summen- oder Durchschnittsberechnung (`GROUP BY`).  

---

### **Was ist ein DBMS?**  
Ein **Datenbankmanagementsystem (DBMS)** ist Software, die die Speicherung, Abfrage und Verwaltung von Datenbanken ermöglicht (z.B. MySQL, SQLite).  

---

### **Was versteht man unter Datenintegrität?**  
Datenintegrität stellt sicher, dass Daten korrekt, konsistent und fehlerfrei sind, z.B. durch Constraints wie PRIMARY KEY oder UNIQUE.  

---

### **Was ist Normalisierung?**  
Normalisierung ist der Prozess, Daten zu strukturieren, um Redundanzen zu vermeiden und Konsistenz zu gewährleisten.  

---

### **Was sind Aggregationsfunktionen und welche gibt es?**  
Aggregationsfunktionen fassen Werte aus mehreren Zeilen zusammen:  
1. **SUM()**: Addiert Werte.  
2. **AVG()**: Berechnet den Durchschnitt.  
3. **COUNT()**: Zählt Einträge.  