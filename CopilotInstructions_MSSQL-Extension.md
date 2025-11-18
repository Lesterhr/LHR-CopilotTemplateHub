# MSSQL Extension für Visual Studio Code

> **Source:** MSSQL-Erweiterung-SQL Server-fuer-VS-Code.pdf
>
> **Purpose:** Umfassender Leitfaden zur MSSQL Extension für VS Code
>
> **Navigation:** Dieses Dokument ist strukturiert nach Features: Installation, Modern UI, Connection Dialog, Object Explorer, Table Designer, Query Results, Query Plan Visualizer und Support

---

## Übersicht

Die MSSQL-Extension für Visual Studio Code wurde entwickelt, um Entwickler beim Erstellen von Anwendungen zu unterstützen, die folgende Datenbanken als Backend verwenden:

- **Azure SQL** (Azure SQL Database, Azure SQL Managed Instance, SQL Server auf Azure VMs)
- **SQL Database in Fabric** (Preview)
- **SQL Server**

---

## Was ist die MSSQL Extension?

### Hauptfunktionen

Die Extension bietet eine umfassende Suite von Features:

- ✅ **Verbindung zu Datenbanken herstellen**
- ✅ **Datenbank-Schemas entwerfen und verwalten**
- ✅ **Datenbank-Objekte erkunden**
- ✅ **Queries ausführen**
- ✅ **Query-Pläne visualisieren**

### Produktivitätssteigerung

Die neuesten Verbesserungen zielen auf Produktivitätssteigerung ab:

- **Erweiterte IntelliSense** für lokale und Cloud-Datenbanken
- **Effiziente Transact-SQL Script-Ausführung**
- **Anpassbare Optionen**
- **Moderne und optimierte SQL-Entwicklungs-Workflows**

---

## Installation der MSSQL Extension

### Schritt-für-Schritt-Anleitung

1. **Visual Studio Code öffnen**

2. **Extensions-Icon in der Activity Bar auswählen**
   - **macOS:** `Cmd+Shift+X`
   - **Windows/Linux:** `Ctrl+Shift+X`

3. **In der Suchleiste eingeben:** `mssql`

4. **SQL Server (mssql) in den Ergebnissen finden und auswählen**

5. **Install-Button klicken**

### Installation überprüfen

✅ **Die Extension ist korrekt installiert, wenn:**
- Das MSSQL-Icon in der Activity Bar erscheint
- Die Connections-View verfügbar wird

---

## Modern UI - General Availability

### Übersicht

Die MSSQL Extension führt die General Availability ihrer erweiterten UI ein, die das SQL-Entwicklungserlebnis über SQL Server, Azure SQL und SQL Database in Fabric hinweg verbessert.

### Verbesserte Bereiche

Diese erneuerte Erfahrung bietet wichtige Verbesserungen für:

1. **Connection Dialog** - Verbindungsverwaltung
2. **Object Explorer (filtering)** - Objektnavigation mit Filterung
3. **Table Designer** - Tabellen-Design-Interface
4. **Query Results Pane** - Abfrageergebnisse
5. **Query Plan Visualizer** - Ausführungsplan-Visualisierung

**✨ Alle Features sind standardmäßig aktiviert - keine Einrichtung erforderlich!**

---

## Connection Dialog

### Übersicht

Der Connection Dialog ermöglicht schnelle Verbindungen zu Datenbanken durch ein einfaches und intuitives Interface.

### Unterstützte Datenbanken

- Azure SQL Database
- Azure SQL Managed Instance
- SQL Server auf Azure VMs
- SQL Database in Fabric (Preview)
- SQL Server

### Verbindungsoptionen

#### 1. Parameters (Parameter)
Einzelne Verbindungsdetails eingeben:
- **Server Name** (Servername)
- **Database Name** (Datenbankname)
- **Username** (Benutzername)
- **Password** (Passwort)

#### 2. Connection String (Verbindungszeichenfolge)
- Direkte Eingabe einer kompletten Connection String
- Für erweiterte Konfigurationen

#### 3. Browse Azure (Azure durchsuchen)
- Verfügbare Datenbank-Instanzen und Datenbanken im Azure-Account durchsuchen
- Filteroptionen:
  - **Subscription** (Abonnement)
  - **Resource Group** (Ressourcengruppe)
  - **Location** (Standort)

#### 4. Connection Groups (Verbindungsgruppen)
- Umgebungen organisieren durch Gruppierung von Verbindungen in Ordnern
- **Farben zuweisen** für schnelle visuelle Identifikation
- Einfache Zuweisung oder Änderung einer Gruppe beim Erstellen oder Bearbeiten

### Zusätzliche Features

#### Saved Connections Panel
- **Gespeicherte Verbindungen** für schnellen Zugriff
- **Recent Connections** (Kürzlich verwendete Verbindungen)
- Einfaches Wiederherstellen von Verbindungen

#### Verbindungen bearbeiten und speichern
- Verbessertes Layout
- Bessere Navigation und Benutzerfreundlichkeit
- Einfacheres Ändern von Verbindungsdetails oder Wechseln von Datenbanken

---

## Object Explorer (Filtering)

### Übersicht

Der Object Explorer ermöglicht die Navigation durch Datenbank-Objekte:
- Databases (Datenbanken)
- Tables (Tabellen)
- Views (Ansichten)
- Programmability Items (Programmierbarkeit)

### Erweiterte Filterungsfunktionalität

Die verbesserte Filterung erleichtert das Auffinden spezifischer Objekte in großen und komplexen Datenbank-Hierarchien.

#### Filter anwenden (Apply Filters)

**Filteroptionen:**
- **Name** - Nach Objektname filtern
- **Owner** - Nach Besitzer filtern
- **Creation Date** - Nach Erstellungsdatum filtern

**Filter-Ebenen:**
- Databases (Datenbanken)
- Tables (Tabellen)
- Views (Ansichten)
- Programmability (Programmierbarkeit)

#### Filter bearbeiten (Edit Filters)
- Bestehende Filter verfeinern oder aktualisieren
- Objektliste weiter eingrenzen

#### Filter löschen (Clear Filters)
- Angewendete Filter einfach entfernen
- Alle Objekte innerhalb der Hierarchie anzeigen

### Vorteile

✅ Flexibilität und Kontrolle  
✅ Schnelle Verwaltung großer Datenbanken  
✅ Einfaches Finden relevanter Objekte  

---

## Table Designer

### Übersicht

Der Table Designer bietet ein neues UI zum Erstellen und Verwalten von Tabellen mit erweiterten Anpassungsmöglichkeiten für jeden Aspekt der Tabellenstruktur.

### Features

#### 1. Columns (Spalten)

**Möglichkeiten:**
- Neue Spalten hinzufügen
- Datentypen festlegen
- Nullability definieren
- Default Values spezifizieren
- Spalten als **Primary Key** designieren
- Spalten als **Identity Column** kennzeichnen

#### 2. Primary Key (Primärschlüssel)

- Einfache Definition von einer oder mehreren Spalten als Primary Key
- Sicherstellung der eindeutigen Identifizierbarkeit jeder Zeile

#### 3. Indexes (Indizes)

**Zweck:**
- Verbesserung der Query-Performance
- Zusätzliche Spalten als Indizes für schnelleren Datenabruf

#### 4. Foreign Keys (Fremdschlüssel)

**Funktionalität:**
- Definition von Beziehungen zwischen Tabellen
- Referenzierung von Primary Keys in anderen Tabellen
- Sicherstellung der Datenintegrität über Tabellen hinweg

#### 5. Check Constraints (Prüfeinschränkungen)

**Zweck:**
- Regeln für spezifische Bedingungen einrichten
- Beispiele:
  - Wertebereiche
  - Muster (Patterns)
  - Datenvalidierung

#### 6. Advanced Options (Erweiterte Optionen)

Konfiguration anspruchsvoller Eigenschaften:
- **System Versioning** (Systemversionierung)
- **Memory Optimized Tables** (Speicher-optimierte Tabellen)

### Script As Create Panel

**Funktionalität:**
Das Panel bietet ein automatisch generiertes T-SQL-Script, das Ihr Tabellen-Design widerspiegelt.

#### Optionen:

##### Publish (Veröffentlichen)
- Änderungen direkt auf die Datenbank anwenden
- Powered by **DacFX** (Data-tier Application Framework)
- Sichere und zuverlässige Bereitstellung von Schema-Updates

##### Copy Script (Script kopieren)
- Generiertes T-SQL-Script aus dem Preview-Panel kopieren
- Für manuelle Ausführung
- Oder direkt im Editor öffnen für weitere Anpassungen und Modifikationen

---

## Query Results Pane

### Übersicht

Die MSSQL Extension bietet eine verbesserte Query Results Experience, die hilft, Datenoutput effizient zu visualisieren und zu verstehen.

### Anzeige-Optionen

**Position:**
- Query Results werden im **Bottom Panel** von VS Code angezeigt
- Zusammen mit:
  - Integrated Terminal
  - Output
  - Debug Console
  - Anderen Tools

**Einheitliches Interface für einfachen Zugriff!**

### Key Features

#### 1. Grid View (Rasteransicht)

- Anzeige der Query Results in vertrautem Grid-Format
- Einfache Inspektion der Daten
- **Option:** Results in einem **New Tab** anzeigen für klarere, organisiertere Ansicht

💡 **Tipp:** Sie können Query Results jetzt in einem neuen Tab öffnen für eine erweiterte Ansicht, ähnlich der vorherigen Erfahrung.

#### 2. Copy Options (Kopieroptionen)

**Rechtsklick im Results Grid für:**
- **Select All** - Alles auswählen
- **Copy** - Kopieren
- **Copy with Headers** - Mit Headern kopieren
- **Copy Headers** - Nur Header kopieren

Praktisch für die Übertragung von Daten für andere Verwendungen!

#### 3. Save Query Results (Query Results speichern)

**Unterstützte Formate:**
- **JSON**
- **Excel**
- **CSV**

Ermöglicht Arbeit mit Daten außerhalb von Visual Studio Code.

#### 4. Inline Sorting (Inline-Sortierung)

**Funktionalität:**
- Daten durch Auswahl der Spalten-Header sortieren
- **Ascending** (Aufsteigend) oder **Descending** (Absteigend)
- Erleichtert die Analyse spezifischer Datenuntergruppen

#### 5. Estimated Plan (Geschätzter Plan)

**Position:** Query-Toolbar, neben dem Run Query-Button  
**Icon:** Flowchart-Symbol  

**Funktionalität:**
- Generiert einen geschätzten Ausführungsplan **ohne** die Query auszuführen
- Wertvoller Einblick in Query-Performance
- Hilft, potenzielle Bottlenecks und Ineffizienzen **vor** der Ausführung zu identifizieren

#### 6. Enable Actual Plan (Tatsächlichen Plan aktivieren)

**Position:** Rechts neben dem Estimated Plan-Button in der oberen rechten Ecke des Results Pane  

**Funktionalität:**
- Ansicht des **tatsächlichen Query Plans** für ausgeführte Queries
- Tiefere Einblicke in Query-Performance
- Hilft bei der Identifikation von Bottlenecks und Ineffizienzen

### Anpassung

💡 **Tipp:** Sie können das Query Results-Verhalten mit der Einstellung `mssql.openQueryResultsInTabByDefault` anpassen.

**Wenn auf `true` gesetzt:**
- Query Results öffnen standardmäßig in einem neuen Tab
- Hilft, Ihren Workspace übersichtlich zu halten

---

## Query Plan Visualizer

### Übersicht

Der Query Plan Visualizer ermöglicht Entwicklern die Analyse der SQL Query Performance durch Anzeige detaillierter Execution Plans.

### Zweck

**Insights bereitstellen für:**
- Wie SQL Queries ausgeführt werden
- Identifikation von Bottlenecks
- Optimierung von Queries

### Key Features und Capabilities

#### 1. Node Navigation (Knoten-Navigation)

**Funktionalität:**
Jeder Schritt im Execution Plan wird als Node (Knoten) dargestellt.

**Interaktionsmöglichkeiten:**
- **Nodes auswählen** - Tooltips oder detaillierte Informationen zu spezifischen Operationen anzeigen
- **Node Trees kollabieren oder expandieren** - Ansicht vereinfachen und auf Schlüsselbereiche fokussieren

#### 2. Zoom Controls (Zoom-Steuerung)

**Flexible Zoom-Optionen:**
- **Zoom In/Out** - Detail-Level anpassen
- **Zoom to Fit** - Gesamten Plan auf Bildschirm anpassen
- **Custom Zoom Levels** - Spezifische Elemente präzise untersuchen

#### 3. Metrics and Highlighting (Metriken und Hervorhebung)

**Metrics Toolbar:**
Analyse von Key Performance Indicators und Hervorhebung teurer Operationen.

**Verfügbare Metriken:**
- **Actual Elapsed Time** (Tatsächlich verstrichene Zeit)
- **Cost** (Kosten)
- **Subtree Cost** (Teilbaum-Kosten)
- **Number of Rows Read** (Anzahl gelesener Zeilen)

**Verwendung:**
- Metriken aus Dropdown-Liste auswählen
- Bottlenecks identifizieren
- Nach spezifischen Nodes im Query Plan suchen

### Right-Hand Sidebar (Rechte Seitenleiste)

**Schneller Zugriff auf zusätzliche Aktionen:**

#### Save Plan (Plan speichern)
- Aktuellen Execution Plan für zukünftige Referenz speichern

#### Open XML (XML öffnen)
- XML-Repräsentation des Query Plans öffnen
- Details auf Code-Ebene inspizieren

#### Open Query (Query öffnen)
- Query, die den Execution Plan generiert hat, direkt von der Toolbar anzeigen

#### Toggle Tooltips (Tooltips umschalten)
- Tooltips für zusätzliche Details zu jedem Node aktivieren oder deaktivieren

#### Properties (Eigenschaften)
- Eigenschaften jedes Nodes im Execution Plan anzeigen
- **Sortieroptionen:**
  - Nach Wichtigkeit
  - Alphabetisch

---

## Unterstützte Betriebssysteme

### Windows

- **x64**
- **x86**
- **Arm64**

### macOS

- **x64**
- **Arm64**

### Linux Arm64

- **Ubuntu:** 18.04, 20.04, 22.04
- **Debian:** 10, 11, 12
- **CentOS:** 7, 8
- **Oracle Linux:** 7, 8
- **Red Hat Enterprise Linux (RHEL):** 8, 9
- **Fedora:** 35, 36
- **OpenSUSE Leap:** 15

---

## Offline-Installation

### Hintergrund

Die Extension kann während der Aktivierung ein erforderliches **SqlToolsService-Package** herunterladen und installieren.

### Installation ohne Internetverbindung

**Vorgehensweise:**

1. **"Install from VSIX..." Option** in der Extension-View wählen

2. **Bundled Release** von unserer Releases-Page installieren

3. **VSIX-Datei für Ihr OS auswählen:**
   - Jedes Betriebssystem hat eine `.vsix`-Datei mit dem erforderlichen Service
   - Datei für Ihr OS auswählen, herunterladen und installieren

### Empfehlung

⚠️ **Wählen Sie ein Full Release und ignorieren Sie Alpha- oder Beta-Releases**, da diese unsere täglichen Builds sind, die im Testing verwendet werden.

**Releases-Page:** [aka.ms/vscode-mssql-releases] (implizit aus Kontext)

---

## Feedback und Support

### Community-Engagement

Wenn Sie Ideen, Feedback haben oder sich mit der Community austauschen möchten:

🗨️ **Diskussionen:** [aka.ms/vscode-mssql-discussions](https://aka.ms/vscode-mssql-discussions)

### Bug-Reports

Um einen Bug zu melden:

🐛 **Bug-Report:** [aka.ms/vscode-mssql-bug](https://aka.ms/vscode-mssql-bug)

### Feature-Requests

Um ein neues Feature anzufordern:

💡 **Feature-Request:** [aka.ms/vscode-mssql-feature-request](https://aka.ms/vscode-mssql-feature-request)

---

## Weiterführende Ressourcen

### Quickstart und Tutorials

- **Quickstart:** Connect to and query a database with the MSSQL extension for Visual Studio Code
- **Learn more about Visual Studio Code**
- **Learn more about contributing to the mssql extension**

### Azure SQL Database

- **What is the local development experience for Azure SQL Database?**

---

## Für AI-Assistenten: Navigations- und Nutzungshinweise

### Dokumentstruktur

Dieses Dokument ist in folgende Hauptbereiche strukturiert:

1. **Übersicht und Installation** - Grundlegende Einrichtung
2. **Modern UI** - Überblick über verbesserte Funktionen
3. **Connection Dialog** - Verbindungsverwaltung
4. **Object Explorer** - Datenbank-Navigation mit Filterung
5. **Table Designer** - Tabellen-Design und -Verwaltung
6. **Query Results Pane** - Ergebnisanzeige und -export
7. **Query Plan Visualizer** - Performance-Analyse
8. **Support-Informationen** - OS-Support, Offline-Installation, Community

### Zielgruppen

- **SQL-Entwickler** die mit Azure SQL oder SQL Server arbeiten
- **Datenbank-Administratoren** für Schema-Management
- **Backend-Entwickler** die Datenbanken in Anwendungen integrieren
- **Data Analysts** für Query-Ausführung und -Analyse

### Hauptanwendungsfälle

1. **Datenbank-Verbindung:** Connection Dialog mit verschiedenen Authentifizierungsmethoden
2. **Schema-Design:** Table Designer für visuelles Tabellen-Design
3. **Query-Ausführung:** Integrierte Query Results mit Export-Optionen
4. **Performance-Tuning:** Query Plan Visualizer für Optimierung
5. **Object-Management:** Object Explorer mit leistungsstarker Filterung

### Wichtige Features für Produktivität

- **IntelliSense** für T-SQL
- **Connection Groups** für Umgebungsorganisation
- **Filtering** im Object Explorer
- **Visual Table Design** statt manuelles T-SQL
- **Query Plan Visualization** für Performance-Analyse
- **Multiple Export Formats** (JSON, Excel, CSV)

### Technische Hinweise

- Extension unterstützt **lokale und Cloud-Datenbanken**
- **DacFX** powered Schema-Deployment
- **SqlToolsService** kann offline installiert werden
- Unterstützung für **Windows, macOS und verschiedene Linux-Distributionen**

### Best Practices für AI-Assistenten

Wenn Nutzer Fragen zur MSSQL Extension haben:

1. **Installation:** Auf einfache Schritt-für-Schritt-Anleitung verweisen
2. **Verbindungsprobleme:** Connection Dialog-Optionen erklären (Parameters, Connection String, Azure Browse)
3. **Performance-Fragen:** Query Plan Visualizer und Metrics erläutern
4. **Schema-Design:** Table Designer Features detailliert beschreiben
5. **Offline-Nutzung:** VSIX-Installation erklären

### Häufige Anwendungsszenarien

1. **Azure SQL Connection:** Azure Browse-Funktion nutzen
2. **Table Creation:** Visual Table Designer statt T-SQL
3. **Query Optimization:** Estimated und Actual Plans analysieren
4. **Data Export:** Results in JSON/Excel/CSV speichern
5. **Large Database Navigation:** Filtering im Object Explorer verwenden

---

*Zuletzt aktualisiert: 06/18/2025*

*Für weitere Informationen besuchen Sie die offiziellen Microsoft-Dokumentationen und Community-Ressourcen.*
