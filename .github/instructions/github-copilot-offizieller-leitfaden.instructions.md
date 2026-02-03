# GitHub Copilot - Offizieller Leitfaden: Tipps & Tricks Vol. 1

> **Source:** GitHub-Copilot-offiziellerLeitfaden.pdf
>
> **Purpose:** Praktischer Leitfaden mit 16 professionellen Tipps und Tricks für GitHub Copilot
>
> **Navigation:** Dieser Leitfaden ist in 16 einzelne Tipps gegliedert, die von verschiedenen Expert*innen verfasst wurden. Jeder Tipp fokussiert sich auf ein spezifisches Anwendungsgebiet.

---

## Übersicht

Dieser offizielle Leitfaden präsentiert 16 praktische Tipps und Tricks für GitHub Copilot, zusammengestellt von Expert*innen aus der Praxis. Die Tipps decken verschiedene Anwendungsbereiche ab - von der Testgenerierung über Accessibility bis hin zu Prompt Engineering.

---

## Inhaltsverzeichnis - Die 16 Tipps

1. [Unit Tests generieren](#tipp-6-unit-tests-generieren)
2. [Proaktive Fehlerbehebung mit Intune-Remediation-Skripten](#tipp-7-proaktive-fehlerbehebung-mit-intune-remediation-skripten)
3. [Cross-Language Entwicklung](#tipp-8-cross-language-entwicklung)
4. [Automatisierung mit GitHub Copilot Chat](#tipp-9-automatisierung-mit-github-copilot-chat)
5. [Bessere Prompts für besseren Code](#tipp-10-bessere-prompts-für-besseren-code)
6. [Aussagekräftige Funktionsnamen & Variablen](#tipp-11-aussagekräftige-funktionsnamen--variablen)
7. [Unterstützung bei der Testfallerstellung](#tipp-12-unterstützung-bei-der-testfallerstellung)
8. [Evaluierung von GitHub Copilot in Unternehmen](#tipp-13-evaluierung-von-github-copilot-in-unternehmen)
9. [Barrierefreie Software entwickeln](#tipp-14-barrierefreie-software-entwickeln)
10. [Von der Anforderung zur Komponente](#tipp-15-von-der-anforderung-zur-komponente)
11. [Chat-Syntax: Chat-Teilnehmer, Chat-Variablen, Slash-Befehle](#tipp-16-chat-syntax)

---

## Tipp 6: Unit Tests generieren

**Autor:** *Informationen aus PDF nicht vollständig extrahiert*

### Konzept

GitHub Copilot kann automatisch Unit Tests für bestehenden Code generieren. Dies beschleunigt den Entwicklungsprozess erheblich und hilft dabei, verschiedene Testfälle abzudecken.

### Praktisches Beispiel

Wenn Sie eine Methode haben, die Werktage zwischen einem Start- und Enddatum im ISO-Standard berechnet, können Sie durch Auswahl der gewünschten Methode und dem Aufruf des `/tests`-Befehls im GitHub Copilot Chat innerhalb weniger Sekunden sieben unterschiedliche Testfälle erhalten.

### Wichtiger Hinweis

**⚠️ Die Tests sollten Sie in jedem Fall im Anschluss korrigieren.** 

Fehler in der Implementierung können dazu führen, dass GitHub Copilot andere Erwartungen an die Ergebnisse hat als Sie und entsprechend falsche Annahmen in den Tests formuliert.

### Best Practices

- Überprüfen Sie alle generierten Tests auf Korrektheit
- Passen Sie die Erwartungswerte an Ihre Geschäftslogik an
- Nutzen Sie die generierten Tests als Grundlage und erweitern Sie sie bei Bedarf

---

## Tipp 7: Proaktive Fehlerbehebung mit Intune-Remediation-Skripten

**Autor:** Jannik Reinhard  
**Rolle:** Senior System Engineer und Microsoft MVP (Enterprise Mobility)  
**Expertise:** #DevOpsEngineer #PowerShell #EnterpriseMobility #DeviceManagement #Analytics #Remediation

### Hintergrund: Microsoft Intune

Microsoft Intune ist eine Unified Endpoint Management- und Sicherheitsplattform, die es Unternehmen ermöglicht, ihre mobilen Endgeräte zu verwalten und zu schützen:
- Smartphones
- Desktops
- HoloLens
- Viele andere Geräte

### Proaktive Remediation-Skripte

Eine zentrale Komponente von Intune sind proaktive Remediation-Skripte, die:
1. **Detection-Skript:** Überprüft Geräte auf Probleme
2. **Remediation-Skript:** Behebt Probleme automatisch basierend auf dem Rückgabewert

### Einsatz von GitHub Copilot

GitHub Copilot hilft enorm bei der Erstellung dieser PowerShell-Skripte. Sie müssen lediglich beschreiben:
- Dass es sich um ein Remediation-Skript handelt
- Auf welchen Fehler das Skript prüfen soll

### Praktisches Beispiel: Windows-Ereignisprotokoll

**Ziel:** Überprüfen, ob Ereignisse mit ID 1000 oder 1001 (Stabilitätsprobleme von Anwendungen) in den letzten 24 Stunden aufgetreten sind.

#### Schritt 1: Detection-Skript erstellen

```powershell
# Intune proactive remediation script to detect if events 1000 and 1001
# are present in the last 24 hours.
```

Nach dem Hinzufügen dieses Kommentars und mehrmaligem Drücken von "Tab" generiert GitHub Copilot das komplette Skript.

#### Schritt 2: Spezifische Filterung

Um nur auf Probleme mit dem Teams-Client zu filtern, präzisieren Sie den Kommentar:

```powershell
# Filter for Teams client crashes only
```

#### Schritt 3: Remediation-Skript

```powershell
# Intune proactive remediation script to remediate team crashes 
# with cleaning the team cache.
```

GitHub Copilot erstellt daraufhin ein Skript, das den Teams-Cache leert.

### Vorteile

- **Zeitersparnis:** Schnelle Erstellung von Skripten ohne mühsame Recherche
- **Proaktivität:** Automatische Problemerkennung und -behebung
- **Reduzierung von Support-Tickets**
- **Besseres Benutzererlebnis**

### Best Practices

- Geben Sie GitHub Copilot klaren Kontext durch präzise Kommentare
- Seien Sie spezifisch in Ihren Anforderungen
- Überprüfen Sie die generierten Skripte auf Ihre spezifischen Bedürfnisse
- Testen Sie die Skripte vor dem Rollout

---

## Tipp 8: Cross-Language Entwicklung

**Autor:** Holger Sirtl  
**Rolle:** Cloud Solution Architect bei Microsoft, Quantum Ambassador  
**Expertise:** #Developer #CrossLanguage

### Die Herausforderung

Als Cloud Solution Architect steht man oft vor zwei großen Herausforderungen:

1. **Zeitdruck:** Wenig Zeit für eigene Programmierung bei häufig wechselnden Kundenszenarien
2. **Viele Programmiersprachen:** Entwicklung in mehreren verschiedenen Programmiersprachen erforderlich

### Typische Fragen

- Wie iteriere ich in Python über ein Array?
- Wie erstelle ich eine Baumstruktur in C# oder Java?
- Wie gebe ich den Inhalt einer Umgebungsvariablen in der PowerShell aus?
- Wie mache ich das unter Linux in der Bash?

### Die Lösung: GitHub Copilot

GitHub Copilot ermöglicht es, das gewünschte Codebeispiel über Kommentare zu formulieren. Das bedeutet:
- Sie müssen nicht jedes Detail der Programmiersprache im Kopf haben
- Fokus auf Logik und Algorithmus statt Syntax
- Einfache Erstellung kleiner Demos und Codebeispiele

### Cheat Sheet: Kommentare in wichtigen Sprachen

| Sprache | Einzeilige Kommentare | Mehrzeilige Kommentare |
|---------|----------------------|------------------------|
| **Bash** | `# Kommentar` | `: ' Kommentar '` |
| **C#** | `// Kommentar` | `/* Kommentar */` |
| **C++** | `// Kommentar` | `/* Kommentar */` |
| **CSS** | `/* Kommentar */` | `/* Kommentar */` |
| **HTML** | `<!-- Kommentar -->` | `<!-- Kommentar -->` |
| **Java** | `// Kommentar` | `/* Kommentar */` |
| **JavaScript** | `// Kommentar` | `/* Kommentar */` |
| **PHP** | `// Kommentar` | `/* Kommentar */` |
| **PowerShell** | `# Kommentar` | `<# Kommentar #>` |
| **Python** | `# Kommentar` | `""" Kommentar """` |

### Grenzen des Ansatzes

Dieser Ansatz hat natürlich seine Grenzen:
- Für größere Softwarelösungen ist Kenntnis der Sprachstruktur unerlässlich
- Aber für kleinere Projekte, schnelle Lösungen und Ergänzungen ist GitHub Copilot eine enorme Hilfe

### Fazit

> "Am Ende des Tages geht es beim Programmieren nicht nur darum, Code zu schreiben, sondern Probleme zu lösen und Ideen umzusetzen. Und genau dabei hilft GitHub Copilot."

---

## Tipp 9: Automatisierung mit GitHub Copilot Chat

**Autor:** Robin-Manuel Thiel  
**Rolle:** Global Black Belt für Cloud-Native-Architekturen und AI-Anwendungen bei Microsoft  
**Expertise:** #Automation #Chat #Developer #Transformation  
**Podcast:** http://todocast.io

### Das Problem

Repetitive Aufgaben in der Softwareentwicklung sind:
- Zeitaufwändig
- Fehleranfällig
- Unbeliebt bei Entwickler*innen

Beispiel: Konvertieren von Code beim Wechsel zwischen verschiedenen Technologien.

### Die Lösung: GitHub Copilot Chat

GitHub Copilot Chat bietet ein Textinterface für die Kommunikation mit der KI in natürlicher Sprache. Wichtige Aspekte:
- Einbeziehung von Quellcode-Dateien oder -abschnitten
- Prompt Engineering für bessere Ergebnisse

### Prompt Engineering - Wichtige Aspekte

Um einen Prompt bestmöglich für die KI aufzubereiten:

1. **Beispiele mitgeben**
2. **Prompts durch Trennzeichen strukturieren** (Anfrage von Kontextinformationen trennen)
3. **Codeblöcke mit Markdown markieren**

### Praktisches Beispiel: Enum zu SQL-Tabellen

#### Ausgangssituation

Ein umfangreiches Enum mit Sentiment-Auswertungen:

```typescript
enum Sentiment {
  Happy = 'happy',
  Excited = 'excited',
  Content = 'content',
  Joyful = 'joyful',
  Optimistic = 'optimistic',
  Amused = 'amused',
  Pleased = 'pleased',
  Relieved = 'relieved',
  Grateful = 'grateful',
  Inspired = 'inspired',
  Proud = 'proud',
  Playful = 'playful',
  Satisfied = 'satisfied',
  Hopeful = 'hopeful',
  Serene = 'serene',
  Jubilant = 'jubilant',
  Ecstatic = 'ecstatic',
  Elated = 'elated',
  Blissful = 'blissful',
  Radiant = 'radiant',
  Merry = 'merry',
  Enthusiastic = 'enthusiastic',
  Cheerful = 'cheerful',
  Whimsical = 'whimsical',
  Eager = 'eager'
}
```

#### Erster Prompt (Ungenügend)

```
Create an SQL script that creates a new table for each value of the enum.
The table name should be the enum value itself. The table consists of the
following columns: ID (primary key), Text, Score.
```

**Ergebnis:** Nur ein einzelner SQL-Befehl für einen Enum-Wert mit falscher Schreibweise.

#### Verbesserter Prompt mit Beispiel

```
Create an SQL script that creates a new table for each value of the enum.
The table name should be the enum value itself. The table consists of the
following columns: ID (primary key), Text, Score.
---
Example:
```sql
CREATE TABLE Happy (
  ID INT PRIMARY KEY,
  Text VARCHAR(255),
  Score INT
);
CREATE TABLE Excited (
  ID INT PRIMARY KEY,
  Text VARCHAR(255),
  Score INT
);
```
```

**Ergebnis:** Perfektes Skript mit allen Enum-Werten und korrekter Groß-/Kleinschreibung!

### Fazit

Die wahre Stärke von GitHub Copilot Chat:
- Verständnis des vorhandenen Codes
- Semantische Umwandlungen zwischen Technologien
- Zeitersparnis und Fehlerminimierung
- Fokus auf interessante und herausfordernde Aufgaben

> "Den langweiligen Teil überlassen wir ab jetzt der KI."

---

## Tipp 10: Bessere Prompts für besseren Code

**Autor:** Christian Wenz  
**Rolle:** Webpionier, Technologiespezialist, Unternehmer, Microsoft MVP seit 2004  
**Expertise:** #Developer #Prompts

### Das Problem

In der Praxis ist die Arbeit mit GitHub Copilot nicht immer so einfach wie in Produktdemos:
- Triviale Aufgaben wechseln sich mit komplexen Anforderungen ab
- Nicht für jeden Anwendungsfall uneingeschränkt geeignet
- Codegenerierung funktioniert nicht immer reibungslos

### Die Lösung: Prompt Engineering

> "Garbage in, garbage out" - oder positiv gewendet: Die Qualität des Prompts hat großen Einfluss auf die Qualität des generierten Codes.

### 5 Grundlegende Richtlinien

#### 1. Klar und eindeutig bleiben

**Problem:** Vage Anforderungen führen zu unerwarteten Ergebnissen.

**Lösung:**
- Präzise Anforderungen formulieren
- Irrelevante Details weglassen (außer für Kontext)
- Keine Verneinungen, sondern klare Anweisungen
- Anforderungen eindeutig und umsetzbar formulieren

**Beispiel:** Statt "Erstelle eine To-do-App" besser "Erstelle eine To-do-App mit React, TypeScript, Local Storage Persistierung und Prioritäts-Tags für Tasks"

#### 2. Der Kontext ist König(in)

**Best Practice:** Prompt wie eine User Story beginnen

**Struktur:**
1. **Kontext erklären:** Was soll der Code tun?
2. **Existierende Lösungen berücksichtigen**
3. **Konzept definieren**
4. **Einzelne Funktionalitäten auflisten**

**Beispiel:**
```
Ich erstelle eine To-do-Liste-Anwendung für kleine Teams.
Die Anwendung soll folgende Funktionen haben:
- Aufgaben erstellen und zuweisen
- Prioritäten setzen
- Fälligkeitsdaten verwalten
```

#### 3. Schritt für Schritt zum Erfolg

**Prinzip:** Codeunterstützung ist ein iterativer Prozess

**Vorteile des schrittweisen Vorgehens:**
- Frühere Korrekturmöglichkeiten
- Bessere Kontrolle über den Prozess
- Gezielte Verbesserungen möglich

**Beispiel bei API-Erstellung:**
1. Zuerst: Datenmodell generieren
2. Dann: Endpunkte implementieren
3. Anschließend: Validierung hinzufügen

#### 4. Mit Beispielen vorgehen

**Zweck:** Selbstverständliches für andere verständlich machen

**Nutzen:**
- Festlegung der Ausgabestruktur
- Definition der Datenstruktur
- Code-Hygiene (Namensschemata, Code-Stil)
- GitHub Copilot generiert Code in Ihrem Stil

**Beispiel:**
```
Erstelle eine Funktion zur Benutzervalidierung.
Beispiel-Ausgabe:
{
  isValid: true,
  errors: [],
  user: { id: 123, name: "Max Mustermann" }
}
```

#### 5. Bitte und danke sagen

**Warum?**
- Verbessert die eigene Stimmung
- Fördert den persönlichen Umgang
- Hat positive Auswirkungen auf die Interaktion

**Bonus:** Der zusätzliche Tippaufwand wird durch schnell generierte Ergebnisse wieder eingespart!

---

## Tipp 11: Aussagekräftige Funktionsnamen & Variablen

**Autor:** Suad Wolgram  
**Rolle:** Junior Software- und Cloud-Entwickler bei white duck GmbH, Student der Informatik (TH-Rosenheim)  
**Expertise:** #Developer

### Der entscheidende Faktor

Ein entscheidender Faktor für die effektive Nutzung von GitHub Copilot ist die **Verwendung aussagekräftiger Funktionsnamen**.

### Beispiel 1: Star Wars API - Charaktere abrufen

#### ❌ Schlechtes Beispiel

```javascript
function fetch() {
    // GitHub Copilot versteht nicht, was wir wollen
}
```

**Problem:** GitHub Copilot kann nicht verstehen, welches Ziel mit der generischen Methode `fetch()` verfolgt wird.

#### ✅ Gutes Beispiel

```javascript
function fetchStarWarsCharacters() {
    // GitHub Copilot liefert sofort passende Vorschläge
}
```

**Ergebnis:** Sobald der Kontext klar ist, liefert GitHub Copilot unverzüglich Vorschläge zur Erreichung des gewünschten Ziels.

**Bonus:** GitHub Copilot erkennt sogar die Variable `starWarsUrl` und integriert sie in die Lösung!

### Beispiel 2: Anzahl der Bewohner eines Planeten

#### Besserer Ansatz

```javascript
function getPlanetCitizenCountObservable() {
    const planetCitizenCount = 0;
    // GitHub Copilot erkennt aufgrund des Methodennamens 
    // und der Variablennamen den Kontext
}
```

**Vorteile:**
- Aussagekräftiger Methodenname
- Klare Rückgabetype-Definition
- Passende Variablennamen
- GitHub Copilot schlägt die entsprechende Implementierung vor
- Richtige Verwendung der Variablen aufgrund des klaren Kontexts

### Kernprinzip

> **Klare, aussagekräftige Namen = Bessere GitHub Copilot Vorschläge**

### Best Practices für Benennung

1. **Methodennamen:** Beschreiben Sie, was die Methode tut
2. **Variablennamen:** Verwenden Sie selbsterklärende Namen
3. **Konsistenz:** Halten Sie sich an Namenskonventionen
4. **Spezifität:** Seien Sie so spezifisch wie möglich

---

## Tipp 12: Unterstützung bei der Testfallerstellung

**Autor:** Joël Zimmerli  
**Rolle:** Full-Stack-Softwareentwickler  
**Expertise:** #CSharp #UnitTest #Developer #XUnit  
**Schwerpunkt:** Testgetriebene Entwicklung (TDD)

### Das Szenario

**Beispiel-Applikation:** Dotnet-Anwendung zur Verwaltung von Immobilien mit Verkaufspreisen

**Feature:** Suchfunktion mit Filterung nach Preisspanne

### Die Implementierung

```csharp
static Expression<Func<HouseDocument, bool>> PriceIsInRangeFilter(
    int? minPrice, int? maxPrice)
{
    var expressionBuilder = PredicateBuilder.New<HouseDocument>(true);
    if (minPrice.HasValue)
        expressionBuilder.And(PriceHigherThanFilter(minPrice.Value));
    if (maxPrice.HasValue)
        expressionBuilder.And(PriceLowerThanFilter(maxPrice.Value));

    return expressionBuilder;
}
```

### Schritt 1: Test-Namen erstellen

**Namensstruktur (Best Practice):**
- Welches Objekt wird getestet
- Welche Funktion wird aufgerufen
- Welches Ergebnis wird erwartet

```csharp
[Fact]
public void HouseQueryToExpression_ShouldEvaluateCorrectly()
{
    // GitHub Copilot generiert automatisch den kompletten Test!
}
```

**Ergebnis:**

```csharp
[Fact]
public void HouseQueryToExpression_ShouldEvaluateCorrectly()
{
    // Arrange
    var query = new HouseQuery()
    {
        UpperPriceLimit = 100,
        LowerPriceLimit = 0
    };
    var house = new HouseDocument()
    {
        Id = "house",
        Name = "house",
        Price = 50
    };

    // Act
    var expression = query.ToExpression();
    var result = expression.Invoke(house);

    // Assert
    result.Should().BeTrue();
}
```

### Schritt 2: Parametrisierte Tests

```csharp
[Theory]
public void HouseQueryToExpression_ShouldEvaluateCorrectly(
    int? upperLimit, 
    int? lowerLimit, 
    int housePrice, 
    bool expected)
{
    // GitHub Copilot kann auch die Teststruktur anpassen
}
```

### Schritt 3: Test-Parameter generieren

GitHub Copilot kann auch die Prüfparameter generieren:

```csharp
[Theory]
[InlineData(100, 0, 50, true)]
[InlineData(100, 0, 99, true)]
[InlineData(100, 0, 1, true)]
[InlineData(100, 0, 150, false)]
[InlineData(100, 50, 150, false)]
[InlineData(100, 150, 200, false)]
[InlineData(100, 0, 0, false)]
[InlineData(100, 100, 100, false)]
[InlineData(100, 100, 0, false)]
[InlineData(null, null, 0, true)]
[InlineData(100, null, 0, true)]
[InlineData(100, null, 101, false)]
[InlineData(null, 100, 101, true)]
[InlineData(null, 100, 99, false)]
public void HouseQueryToExpression_ShouldEvaluateCorrectly(
    int? upperLimit, int? lowerLimit, int housePrice, bool expected)
{
    // ...
}
```

### Wichtiger Hinweis

⚠️ **Es ist ratsam, die generierte Liste sorgfältig zu prüfen und zu überdenken.**

### Vorteile

- Effiziente Testerstellung
- Verschiedene Szenarien werden abgedeckt
- Zeitersparnis bei der TDD-Entwicklung
- Umfassende Testabdeckung

---

## Tipp 13: Evaluierung von GitHub Copilot in Unternehmen

**Autor:** Tobias Deekens  
**Rolle:** Entwickler, Mentor und Sprecher mit Frontend-Entwicklungs-Expertise  
**Unternehmen:** commercetools  
**Expertise:** #Evaluation #Adaption

### Warum evaluieren?

**Frage:** Warum drei Monate testen statt einfach einführen?

**Antwort:** Pragmatischer Ansatz bei der KI-Einführung
- Bewertung von unten nach oben
- Teams sollen selbst beurteilen und entscheiden
- Praktische Meinung derer einbeziehen, die das Tool nutzen

### Die Fülle von KI-Tools

Wichtige Fragen:
- Ist es sinnvoll, Replit Ghostwriter, Codeium, CodeComplete und GitHub Copilot zusammen zu verwenden?
- Oder sollte man eines dieser Tools durch Mintlify oder Wrap ergänzen?

**Antwort:** Nur durch Praxis-Tests, nicht durch Marketing-Websites!

### Evaluierungs-Setup bei commercetools

#### Technologie-Stack

- Scala, TypeScript, PHP, Go, Rust
- 150 Entwickler*innen gesamt
- Fundierte Technologieentscheidungen
- Starker Fokus auf Kollaboration

#### Evaluierungs-Parameter

**Dauer:**
- 3 Monate über zwei Quartale
- Umfasst Quartalsende mit neuen Feature-Releases

**Stichprobengröße:**
- 30-35 Entwickler*innen (20-25% Beteiligung)
- Heterogene Gruppe aus verschiedenen Disziplinen
- Verschiedene Tools und Sprachen

**Teilnehmer:**
- Frontend- & Backend-Entwickler*innen
- Site Reliability Engineers
- Test Automation Engineers
- Dokumentations-Teams

#### Prozess

1. **Anmeldung:** Google-Formular, 34 Anmeldungen nach einer Woche
2. **Kommunikation:** E-Mail-Liste und Slack-Kanal
3. **Zugriff:** Spezielles GitHub-Team
4. **Check-in:** Nach einer Woche Installation verifiziert
5. **Austausch:** Eindrücke und Codebeispiele über Slack/Pull Requests
6. **Kontakt:** Hintergrund-Kommunikation mit GitHub

### Die Umfrage

#### 3 Hauptbereiche

1. **Wurde GitHub Copilot durchgängig genutzt?**
2. **Macht uns GitHub Copilot produktiver?**
3. **Stellt GitHub Copilot keine größeren Risiken dar?**

#### Detailierte Fragen

1. Wie oft hast du GitHub Copilot während unserer Testphase verwendet?
2. Hat sich deine Nutzung im Laufe der drei Monate verändert?
3. Wie oft musstest du die Vorschläge anpassen?
4. Bei welchen Aufgaben hast du die größte Produktivitätssteigerung festgestellt?
5. Sollten wir andere Tools mit generativer KI evaluieren?

### Die Ergebnisse

#### Quantitative Erkenntnisse

- **57%** nutzten GitHub Copilot jeden Tag
- **95%** gaben an, dass GitHub Copilot sie produktiver macht
- **63%** gaben an, dass ihre Nutzung im Laufe der Zeit zugenommen hat
- **67%** gaben an, dass die Vorschläge hilfreich waren
- **82%** gaben an, dass die Vorschläge selten problematisch waren
- **60%** gaben an, dass GitHub Copilot als KI-Assistent geeignet ist
- **80%** erwarten nicht, dass andere Tools wesentlich besser sind
- **100%** wollen GitHub Copilot weiterhin nutzen

#### Qualitative Erkenntnisse

**✅ GitHub Copilot glänzt bei:**
- Schreiben von Tests (72%)
- Refactoring von Code (42%)
- Automatische Vervollständigung (~60%)
- Boilerplate und Scaffolding (~60%)

**⚠️ Herausforderungen:**
- Schwierigkeiten mit komplexer Geschäftslogik (82%)
- Nicht besonders leistungsstark bei wichtigem Code-Kontext (43%)
- Vorsicht bei leistungs-/sicherheitsrelevanten Themen (27%)
- Nicht hilfreich bei hochspezialisierten/modernen Frameworks (14%)

#### Zitate aus der Evaluierung

> "Es schreibt Versionshinweise für mich! Das ist das Beste überhaupt!"  
> — Ein Mitarbeiter beim morgendlichen Kaffee

> "Es gab ein tägliches Ringen zwischen GitHub Copilot und dem regulären IntelliSense."  
> — Eine Testperson

> "Manchmal scheint GitHub Copilot zu schlafen, wenn viele VS Code-Fenster geöffnet sind. Anschließend wird man mit 50 Codezeilen zugeschüttet."  
> — Eine Testperson

> "GitHub Copilot ist intelligent genug, um zuweilen auch gefährlich zu sein."  
> — Eine Testperson (nach Vorschlag, 40.000 Entitäten einzeln aus DB zu laden)

### Verbesserungspotenzial

Identifizierte Bereiche für Verbesserungen:
- Man kann noch kein Feedback zu einem Vorschlag geben
- Keine Konfiguration für bestimmte Ordner oder Situationen
- Funktioniert nicht sehr gut über Dateigrenzen hinweg
- Homogenes Refactoring über größere Codebasis schwierig

### Fazit und Entscheidung

**Entscheidung:** Einführung von GitHub Copilot im gesamten Unternehmen

**Gründe:**
- Kontinuierliche und zunehmende Nutzung
- Vorschläge wurden häufig angenommen
- Gute Qualität der Vorschläge
- Problemlose Einbindung in bestehende Arbeitsumgebungen
- Enorme Produktivitätsgewinne

**Ausblick:** Weiterer Ausbau in den nächsten Monaten

---

## Tipp 14: Barrierefreie Software entwickeln

**Autor:** Dennis Gassen  
**Rolle:** Go to Market Manager für Digital & Application Innovation bei Microsoft Deutschland  
**Expertise:** #Accessibility #WCAG #PromptEngineering

### Hintergrund

**Wichtige Fakten:**
- Weltweit leben etwa **1,3 Milliarden Menschen** mit einer Behinderung
- Das sind etwa **16% der Weltbevölkerung**
- Zugang zu Informationsangeboten ist essenziell wichtig

### Web Content Accessibility Guidelines (WCAG)

**Status:**
- Internationaler Standard für barrierefreie Internetangebote
- In der EU verbindlich seit:
  - September 2019: Neue Webseiten
  - September 2020: Bestehende Webseiten
  - Juni 2021: Mobile Anwendungen

**Geschichte:**
- 1999: WCAG 1.0 veröffentlicht
- Dezember 2008: WCAG 2.0 als ISO-Standard
- Aktuell: WCAG 2.2 empfohlen

### GitHub Copilot für Accessibility

#### Einfache Frage (generelle Tipps)

```
How can GitHub Copilot help me develop accessible applications?
```

**Ergebnis:** Generelle Tipps, die als Ausgangspunkt dienen.

#### Besserer Prompt mit Kontext

```
I want to learn more about accessibility standards and need to write
code that confirms with WCAG 2.2 defined at https://www.w3.org/TR/
WCAG22/. Please act as my accessibility coach to make sure I stick to
the most common accessibility standards and guidelines. When you answer
accessibility related questions, please also use sources like w3.org
and webaim.org. Please also provide links and references in your answers 
whenever possible. When you suggest code, use semantic HTML and follow 
the ARIA Authoring Practices Guide and related design patterns.
```

**Der Prompt enthält:**
1. Erweiterte Kontextinformationen
2. Definition der Rolle von GitHub Copilot
3. Hinweis auf seriöse Quellen (w3.org, webaim.org)
4. Anforderung zu weiteren Ressourcen und Quellen

**Ergebnis:** Detaillierte, kontextbezogene Antworten mit Quellenangaben!

### Praktische Beispiele

#### Beispiel 1: Probleme identifizieren

**Prompt:**
```
Show me examples where accessibility standards are not being followed.
```

GitHub Copilot zeigt konkrete Code-Beispiele mit Problemen und schlägt sofort passende Lösungen vor!

#### Beispiel 2: Testing

**Prompt:**
```
How can I test if my application is accessible for a screen reader?
```

**Antwort enthält:**
1. **Automated Testing:** axe, Lighthouse, WAVE
2. **Manual Testing:** NVDA, JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
3. **Keyboard Navigation:** Alle interaktiven Elemente prüfen
4. **Semantic HTML:** Korrekte HTML-Elemente verwenden
5. **Descriptive Text:** Alt-Text, Labels, beschreibender Link-Text

#### Beispiel 3: Best Practices

**Prompt:**
```
What are best practices to incorporate accessibility testing in the 
whole application lifecycle?
```

**Antwort beinhaltet:**
1. Integration von Anfang an
2. Automated Testing in CI/CD Pipeline
3. Manuelles Testing
4. Code Reviews mit Accessibility-Fokus
5. Training und Awareness
6. Regelmäßige Audits
7. WCAG als Leitfaden

#### Beispiel 4: Barrierefreie Tabellen

**Prompt:**
```
What are best practices for creating accessible tables in HTML?
```

**Best Practices:**
1. `<th>` für Headers verwenden
2. `scope`-Attribut nutzen (col/row)
3. `<caption>` für Tabellenbeschreibung
4. `<thead>`, `<tbody>`, `<tfoot>` verwenden
5. Komplexe Layouts vermeiden
6. Hohen Kontrast sicherstellen

### Weitere nützliche Prompts

#### Testing in Application Lifecycle

```
What are best practices to incorporate accessibility testing in the 
whole application lifecycle?
```

Umfassende Antwort zu:
- Integration von Anfang an
- Automatisierte Tests
- Manuelle Tests
- Code Reviews
- Training
- Audits

#### Screen Reader Testing

```
How can I test if my application is accessible for a screen reader?
```

Detaillierte Anleitung zu:
- Tool-Empfehlungen
- Testmethoden
- Worauf zu achten ist

### Zusammenfassung

**Vorteile von Prompt Engineering für Accessibility:**
- Deutliche Verbesserung der GitHub Copilot Chat Ergebnisse
- Aufbau von Wissen und Verständnis für Barrierefreiheit
- Zusätzliche Referenzen und Beispiele auf Anfrage

**Wichtig:**
- Erwarten Sie keine perfekten Ergebnisse
- GitHub Copilot ist ein "Co-Pilot", kein Ersatz
- Überprüfung der Vorschläge ist immer Aufgabe der Entwickler*innen
- Fragen Sie nach weiteren Beispielen und Referenzen

**Ressourcen:**
- w3.org
- webaim.org
- WCAG Guidelines
- ARIA Authoring Practices Guide

---

## Tipp 15: Von der Anforderung zur Komponente

**Autoren:** Syrine Chelly & Tobias Wittenburg  
**Rollen:** Cloud Solution Architect Developer Advocates bei Microsoft  
**Expertise:** #Developer

### Die Vision seit den 50er Jahren

Seit der Einführung von Cobol in den 50er Jahren träumt die Softwareindustrie davon:
- Programmierung in natürlicher Sprache
- Englisch als Programmiersprache
- Direkte Erstellung von Geschäftsanwendungen

**Jetzt:** Mit LLMs (Large Language Models) wird dieser Traum Wirklichkeit!

### Typische erste Nutzung von GitHub Copilot

1. **Inline-Code aus Kommentaren generieren**
2. **Fragen zu Code, Sprachen, Prozessen oder Frameworks stellen**

#### Beispiel in C#

```csharp
// Calculate the sum of two numbers
public int Add(int a, int b)
{
    return a + b;  // Vorschlag in Grau
}
```

### GitHub Copilot berücksichtigt Kontext

**Automatischer Kontext:**
- Aktuell geöffnete Datei
- Metadaten (Programmiersprache)
- Benachbarte Tabs

**Zusätzlicher Kontext durch Prompts:**
- Absicht mitteilen
- Angaben zum gewünschten Ergebnis

### Praktisches Beispiel: Timer-Komponente für Workshops

#### Der strukturierte Prompt

```
I am going to build a website for trainers that can be used during IT
Workshops. This website should have a couple of smaller tools that you
can pull up in between the sessions.

The website is being built in React with JavaScript.

The first component that I want to build is a timer for a coffee break.
Please help me building that timer. Here are the features:
 - Customizable duration for a break
 - Some buttons for a default break duration (5 min, 10 min, 15 min, 
   45 min, 1 hour)
 - A Button "Timer Start"
 - Upon clicking "Timer Start" the timer should start and count down.
 - When the timer is up an alarm should go off.

Can you build that component for me?
```

**Prompt-Struktur:**
1. **Kontext:** Was wollen wir tun? (Website für Trainer*innen)
2. **Technologie:** Welche Tech-Stack? (React mit JavaScript)
3. **Anforderungen:** Konkrete Features auflisten

**Ergebnis:** Eine voll funktionsfähige React-Komponente!

#### Nachbesserung

Falls eine Funktion fehlt:

```
Please toggle the button to "Timer Stop" after the timer has started.
Also change the JavaScript code to stop the timer once the "Timer Stop"
Button has been pushed.
```

### Alternative: Kommentare im Code

Eine weitere leistungsstarke Möglichkeit: Funktionalität direkt in Kommentaren beschreiben.

```javascript
// Timer Component for Coffee Breaks
// Features:
// - Customizable duration for a break
// - Default buttons: 5 min, 10 min, 15 min, 45 min, 1 hour
// - Start/Stop button that toggles
// - Countdown display
// - Alarm when timer finishes
```

**Vorteil:** Detaillierte Anweisungen in der Codebasis selbst einbetten.

### Dokumentation erstellen

GitHub Copilot kann auch Kommentare für Dokumentation erstellen:

```javascript
/**
 * Describe the function here...
 */
function timerComponent() {
    // GitHub Copilot vervollständigt die Beschreibung
}
```

**Vorteile:**
- Bessere Code-Lesbarkeit
- Erleichterte Wartung
- Verständnis von Bibliotheken

### Best Practices

1. **Kontext bereitstellen:** Was wollen Sie erreichen?
2. **Technologie spezifizieren:** Welche Sprache/Framework?
3. **Features auflisten:** Konkrete Anforderungen
4. **Iterativ verfeinern:** Bei Bedarf nachbessern
5. **Kommentare nutzen:** Als Alternative oder Ergänzung

### Fazit

Von der natürlichsprachlichen Anforderung zur fertigen Komponente:
- Klare Beschreibung der Absicht
- Strukturierte Anforderungen
- GitHub Copilot generiert funktionierenden Code
- Iterative Verbesserung möglich

---

## Tipp 16: Chat-Syntax: Chat-Teilnehmer, Chat-Variablen, Slash-Befehle {#tipp-16-chat-syntax}

**Autor:** Maxim Salnikov  
**Rolle:** Leiter Geschäftsbereich Developer Productivity, Community-Engagierter  
**Expertise:** #CopilotChat #ChatSyntax #Developer #Components  
**Standort:** Oslo, Norwegen

### Überblick

GitHub Copilot Chat funktioniert vollständig in natürlicher Sprache, aber **spezielle Chat-Funktionen** können die Produktivität erheblich steigern:

- Chat-Teilnehmer (@)
- Slash-Befehle (/)
- Kontextvariablen (#)

**Hinweis:** Diese Funktionen sind primär unter VS Code verfügbar!

### Chat-Teilnehmer (@)

Sprechen Sie KI-basierte "Domain-Experten" an, indem Sie @ vor den Teilnehmernamen setzen.

#### Verfügbare Chat-Teilnehmer

##### @workspace
- **Expertise:** Kennt den gesamten Code im geöffneten Arbeitsbereich
- **Anwendung:** Lösungsweite Abfragen
- **Hinweis:** Nicht der gesamte Code wird gesendet, nur relevante Teile

**Beispiel:**
```
@workspace Tell me about the backend architecture of this project
```

**Produktivitätstipp:** Verwenden Sie `Strg + Enter` (statt nur `Enter`), und `@workspace` wird automatisch vor Ihre Nachricht eingefügt!

**Verwendete Referenzen prüfen:**
Erweitern Sie die Zeile "Used references" um zu sehen, welche Dateien und Codezeilen für den Prompt verwendet wurden.

##### @terminal
- **Expertise:** Kennt die integrierte Terminal-Shell
- **Weiß über:** Inhalt und Buffer des Terminals

**Beispiel:**
```
@terminal Explain the last command that was executed
```

##### @vscode
- **Expertise:** Kennt den VS Code Editor
- **Weiß über:** Befehle und Funktionen von VS Code

**Beispiel:**
```
@vscode How do I configure keyboard shortcuts?
```

#### Vergleich: Mit und ohne Chat-Teilnehmer

**Ohne @workspace:**
Allgemeine Antwort ohne Projekt-Kontext

**Mit @workspace:**
Spezifische Antwort basierend auf Ihrem aktuellen Projekt

### Chat-Variablen (#)

Verwenden Sie # um auf spezifische Kontexte zu verweisen.

#### Verfügbare Chat-Variablen

| Variable | Beschreibung |
|----------|-------------|
| `#file` | Verweist auf eine bestimmte Datei im Arbeitsbereich |
| `#codebase` | Gesamter Inhalt des geöffneten Arbeitsbereichs |
| `#editor` | Quellcode im sichtbaren Teil des Editors |
| `#git` | Aktuelles Git-Repository (Branch, Remotes, Pfad, etc.) |
| `#selection` | Der aktuell ausgewählte Code |
| `#terminalLastCommand` | Der letzte ausgeführte Befehl im Terminal |
| `#terminalSelection` | Auswahl im Terminal des Editors |

#### Praktisches Beispiel

**Aufgabe:** Methodennamen in einer bestimmten Datei verbessern

```
Help me improve the method names in #file:src/utils/helpers.js
Make sure to consider the entire file content.
```

**Produktivitätstipp:** 
- Verwenden Sie Pfeiltasten zur Auswahl der Chat-Variable nach Eingabe von #
- Bei #file: Verwenden Sie Tastatur zur Auswahl der vorgeschlagenen Dateien

### Slash-Befehle (/)

Häufig verwendete Aktionen mit praktischen Tastenkombinationen aufrufen.

#### Verfügbare Slash-Befehle

| Befehl | Beschreibung |
|--------|-------------|
| `/help` | Hilfe zu verfügbaren Slash-Befehlen, Chat-Teilnehmern, Chat-Variablen |
| `/doc` | Erstellung einer Dokumentation für den Code |
| `/explain` | Erklärung, wie der Code funktioniert |
| `/fix` | Optimierung und/oder Behebung von Problemen im Code |
| `/tests` | Erstellung von Unit-Tests für den Code |
| `/new` | Erstellung eines Gerüsts für einen neuen Arbeitsbereich |

#### Praktisches Beispiel: Reguläre Ausdrücke erklären

**Vorgang:**
1. Wählen Sie die Codezeile mit dem regulären Ausdruck aus
2. Verwenden Sie den Slash-Befehl:

```
/explain
```

**Ergebnis:** Detaillierte Erklärung des regulären Ausdrucks

#### Vorteile von Slash-Befehlen

1. **Schneller als natürliche Sprache**
2. **Keine Mehrdeutigkeit:** GitHub Copilot versteht die Absicht zu 100%
3. **Konsistente Ergebnisse**
4. **Einfache Bedienung:** Pfeiltasten zur Auswahl

### Inline-Chat-Modus

**Produktivitätstipp:** Probieren Sie den Inline-Modus aus!

**Tastenkombination:** `Strg+I` (Windows) oder `Cmd+I` (Mac)

**Vorteile:**
- Kleines Overlay-Dialogfeld
- Erscheint direkt über der Cursor-Position
- Keine Ablenkung durch Seitenfenster
- Schneller Zugriff

### Kombinierte Nutzung

Sie können Chat-Teilnehmer, Variablen und Befehle kombinieren:

```
@workspace /explain #selection
```

Das erklärt den ausgewählten Code im Kontext des gesamten Arbeitsbereichs.

### Best Practices

1. **@workspace für lösungsweite Fragen verwenden**
2. **#file für spezifische Datei-Referenzen nutzen**
3. **Slash-Befehle für häufige Aktionen**
4. **Inline-Chat für schnellen Zugriff**
5. **"Used references" überprüfen** um zu sehen, welcher Kontext verwendet wurde
6. **Kombinationen nutzen** für präzise Anfragen

### Zusammenfassung

**Durch die Verwendung von:**
- **Chat-Teilnehmern (@):** Volle Kontrolle über den Gesprächskontext
- **Chat-Variablen (#):** Präzise Kontext-Spezifikation
- **Slash-Befehlen (/):** Schneller Zugriff auf häufige Aktionen

**Erreichen Sie:**
- Korrektes und konsistentes Verständnis Ihrer Absichten
- Schnelleres Chatten und Programmieren
- Höhere Produktivität

---

## Weiterführende Ressourcen

### Offizielle Microsoft & GitHub Ressourcen

- **Features von GitHub Copilot**
- **Dokumentation zu GitHub Copilot**
- **Quickstart für GitHub Copilot**
- **GitHub Copilot in VS Code**
- **GitHub Copilot Labs**
- **GitHub Copilot Trust Center**
- **GitHub Blog**

### Lernressourcen

- **GitHub Copilot Fundamentals:** Grundlegendes zum KI Pair-Programmierer
- **Erste Schritte mit GitHub und Visual Studio Code**
- **Was ist die GitHub Copilot-Erweiterung für Visual Studio?**

### Azure & Cloud

- **Azure-Developer-Productivity** | Microsoft Azure
- **Azure-Vertrieb kontaktieren** | Microsoft Azure
- **Erfahrene Azure-Partner finden** | Microsoft Azure

---

## Starten Sie noch heute

### Kontaktmöglichkeiten

1. **Microsoft Account Manager kontaktieren**
2. **Azure-Vertrieb kontaktieren**
3. **Einen kompetenten Microsoft Partner finden**

### Weitere Informationen

Besuchen Sie die Azure-Developer-Productivity Seite für mehr Informationen zum Thema Developer Productivity.

---

## Nutzen Sie GitHub Copilot für Ihre Projekte

### Das Potenzial

Diese 16 Tipps bieten einen guten Einblick in die faszinierenden Möglichkeiten von GitHub Copilot. Die vorgestellten Beispiele sind allerdings nur die **Spitze des Eisbergs**!

### Ihre Erfahrungen sind wertvoll

Wir sind gespannt auf Ihre Erfahrungen und Tipps im Umgang mit GitHub Copilot!

**Teilen Sie Ihre Erkenntnisse:**
- E-Mail: techwiese@microsoft.com
- Ihre wertvollen Einblicke könnten in der nächsten Ausgabe erscheinen
- Helfen Sie anderen Entwickler*innen, das Beste aus GitHub Copilot herauszuholen

### Innovation und Zukunft

> Innovation steht im Zentrum der Softwareentwicklung und GitHub Copilot ist zweifellos eine bahnbrechende Bereicherung.

**Nutzen Sie diese Gelegenheit:**
- Verbessern Sie Ihr Coding-Erlebnis
- Gestalten Sie gemeinsam die Zukunft der Softwareentwicklung

---

## Für AI-Assistenten: Navigations- und Nutzungshinweise

### Dokumentstruktur

- **16 thematisch getrennte Tipps** von verschiedenen Expert*innen
- Jeder Tipp ist eigenständig und in sich geschlossen
- Tipps bauen nicht aufeinander auf - können in beliebiger Reihenfolge gelesen werden

### Wichtige Themenbereiche

1. **Testing:** Tipps 6, 12
2. **Automation:** Tipps 7, 9
3. **Cross-Language Development:** Tipp 8
4. **Prompt Engineering:** Tipps 10, 14, 15
5. **Code Quality:** Tipp 11
6. **Enterprise Adoption:** Tipp 13
7. **Accessibility:** Tipp 14
8. **Chat-Funktionen:** Tipp 16

### Anwendungsgebiete

- **DevOps & System Management:** Tipp 7
- **Frontend & Backend Development:** Tipps 8, 15
- **Testing & Quality Assurance:** Tipps 6, 12
- **Accessibility & Inclusive Design:** Tipp 14
- **Enterprise Evaluation:** Tipp 13
- **Produktivitätssteigerung:** Alle Tipps

### Zielgruppen

- Software-Entwickler*innen aller Erfahrungsstufen
- DevOps Engineers
- Test Engineers
- Solution Architects
- Team Leads und Entscheidungsträger
- Accessibility Specialists

---

*© 2024 Microsoft. Alle Rechte vorbehalten. Namen und Produkte anderer Firmen können eingetragene Warenzeichen der jeweiligen Rechteinhaber sein.*
