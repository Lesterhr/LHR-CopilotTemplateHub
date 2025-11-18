# Transact-SQL Support in Visual Studio Code

> **Source:** Transact-SQL-Support-in-VS-Code.pdf
>
> **Purpose:** Leitfaden für die Verwendung von Transact-SQL (T-SQL) in Visual Studio Code
>
> **Navigation:** Dieses Dokument beschreibt die T-SQL Features in VS Code: Installation, Verbindung, Ausführung, IntelliSense, Linting, Navigation und Snippets

---

## Übersicht

Verwandeln Sie Visual Studio Code in einen leistungsstarken Editor für **Transact-SQL (T-SQL)** Entwicklung mit der **mssql Extension**, verfügbar im VS Code Marketplace.

**Official Marketplace:** [aka.ms/mssql-marketplace](https://aka.ms/mssql-marketplace)

---

## Optimiert für

Die mssql Extension ist optimiert für:

- ✅ **SQL Server on-premises** (lokal)
- ✅ **SQL Server in any cloud** (in jeder Cloud)
- ✅ **Azure SQL Database**
- ✅ **Azure SQL Data Warehouse**

---

## Hauptfunktionen

### Kernfähigkeiten

1. **Verbindung zu SQL-Datenbanken herstellen**
2. **T-SQL Code schreiben**
3. **T-SQL Code ausführen**
4. **Ergebnisse anzeigen**
5. **Ergebnisse als JSON oder CSV speichern**

### Erweiterte Features

Während Sie T-SQL Code schreiben, erhalten Sie:

- 🎯 **T-SQL IntelliSense** (Code-Vervollständigung)
- 🎨 **Syntax Highlighting** (Syntax-Hervorhebung)
- 🔍 **Linting** (Code-Analyse)
- 🧭 **Code Navigation**
- 📝 **Code Snippets**

---

## Erste Schritte

### Voraussetzung: VS Code herunterladen

Falls Sie VS Code noch nicht heruntergeladen haben:

**Download:** [code.visualstudio.com/download](https://code.visualstudio.com/download)

**Verfügbar für:**
- Linux
- macOS
- Windows

---

## Installation der T-SQL Support

### Schritt-für-Schritt-Anleitung

#### 1. Extensions-View öffnen

**Tastenkombination:** `Ctrl+Shift+X`

**Oder:** Von der VS Code Side Bar

#### 2. Nach "mssql" suchen

In der Suchleiste `mssql` eingeben

#### 3. Installieren

- **"Install" klicken**
- **VS Code neu laden**, wenn dazu aufgefordert

**Extension:** [mssql im Marketplace](https://aka.ms/mssql-marketplace)

---

## Verbinden und T-SQL ausführen

### Einfache Verbindung

Verbinden Sie sich einfach mit:

- SQL Server on-premises
- SQL Server in any cloud
- Azure SQL Database
- Azure SQL Data Warehouse

### T-SQL Statements und Batches ausführen

**Funktionalität:**
- T-SQL Statements ausführen
- Batches ausführen
- Ergebnisse und Nachrichten anzeigen - alles innerhalb von VS Code

### Verbindungs-Historie

✅ **Ihre letzten Verbindungen werden über Sessions hinweg gespeichert**

**Vorteil:** Schnelle erneute Verbindung zu Ihren Datenbanken

---

## Ergebnisse anzeigen und speichern

### Ergebnisse anzeigen

**Beim Ausführen von T-SQL Code sehen Sie:**
- Ergebnisse der Abfrage
- Nachrichten vom Server
- Direkt in VS Code

### Ergebnisse speichern

**Unterstützte Formate:**
- 📄 **JSON** - Für programmatische Verwendung
- 📊 **CSV** - Für Tabellenkalkulation und Datenanalyse

**Anwendung:**
Mit nur wenigen Klicks können Sie die Daten in Ihren Anwendungen verwenden!

---

## T-SQL IntelliSense

### Intelligente Code-Vervollständigung

Während Sie T-SQL Code im Editor schreiben, bietet VS Code:

#### 1. T-SQL Keywords (Schlüsselwörter)
- Intelligente Vervollständigung für T-SQL Syntax
- Kontextbezogene Vorschläge

#### 2. Schema Object Names (Schema-Objektnamen)
**Vorschläge für:**
- Tables (Tabellen)
- Columns (Spalten)
- Views (Ansichten)

#### 3. Parameter Help (Parameter-Hilfe)
**Für:**
- Functions (Funktionen)
- Procedures (Prozeduren)

### Voraussetzung

⚠️ **IntelliSense funktioniert, wenn Sie mit einer Datenbank verbunden sind**

---

## Linting

### Was ist Linting?

**Definition:** Analyse Ihres T-SQL Codes auf potenzielle Syntax-Fehler

### Funktionalität in VS Code

**Real-time Feedback:**
- Schnelle Navigation zu Fehlern und Warnungen
- Während Sie T-SQL Code schreiben
- Fehler werden sofort angezeigt

### Vorteile

✅ Fehler frühzeitig erkennen  
✅ Code-Qualität verbessern  
✅ Produktivität steigern  

---

## Peek Definition / Go to Definition

### Funktionsübersicht

**Schnelles Durchsuchen der Definition von Schema-Objekten:**

#### Unterstützte Objekte

- Tables (Tabellen)
- Functions (Funktionen)
- Procedures (Prozeduren)

### Verwendung

#### Peek Definition
- **Vorschau der Definition** direkt im Code
- Kein Verlassen der aktuellen Datei

#### Go to Definition
- **Sprung zur Definition** des Objekts
- Öffnet die Definition in einem neuen Tab/Fenster

### Anwendungsfall

**Während Sie T-SQL Code schreiben:**
- Schnelle Referenz auf Tabellen-Strukturen
- Überprüfung von Prozedur-Parametern
- Ansicht von Function-Implementierungen

---

## Snippets

### Was sind T-SQL Snippets?

**Definition:** Code-Templates für häufig verwendete T-SQL Statements

### Verwendung

**Snippet-Liste aufrufen:**
1. Tippen Sie `sql` im Editor
2. Liste der T-SQL Snippets wird angezeigt
3. Wählen Sie das gewünschte Snippet aus

### Vorteile

- ⚡ Schnelleres Schreiben von Standard-SQL
- 📝 Konsistente Code-Struktur
- ✅ Weniger Tippfehler

### Beispiele für verfügbare Snippets

Typische Snippets könnten sein:
- `SELECT` Statements
- `INSERT` Statements
- `UPDATE` Statements
- `CREATE TABLE` Statements
- `CREATE PROCEDURE` Templates
- `JOIN` Patterns

*(Spezifische Snippet-Liste durch `sql` + Autocomplete anzeigen)*

---

## Nächste Schritte

### 1. SQL Server herunterladen

**Download:** [SQL Server 2017 Developer Edition](https://www.microsoft.com/sql-server/sql-server-downloads)

**Hinweis:** Kostenlos verfügbar!

### 2. Extension installieren

**Marketplace:** [mssql Extension](https://aka.ms/mssql-marketplace)

### 3. App mit SQL Server entwickeln

**Tutorial:** [Build an app using SQL Server](https://aka.ms/sqldev)

**Unterstützt:**
- macOS
- Linux
- Windows

**Verfügbar für:**
- Ihre bevorzugte Programmiersprache

### 4. Zur Extension beitragen

**GitHub Repository:** [github.com/microsoft/vscode-mssql](https://github.com/microsoft/vscode-mssql)

**Möglichkeiten:**
- 🐛 **Bug Report einreichen**
- 💡 **Feature Suggestion machen**

**Issue Tracker:** [github.com/microsoft/vscode-mssql/issues](https://github.com/microsoft/vscode-mssql/issues)

---

## Weiterführende Dokumentation

### SQL Server Ressourcen

#### Allgemeine Dokumentation
📚 **[SQL Server Documentation](https://learn.microsoft.com/sql/sql-server)**

#### SQL Server auf Linux
🐧 **[SQL Server on Linux Documentation](https://learn.microsoft.com/sql/linux/sql-server-linux-overview/)**

#### Blog
📝 **[SQL Server Blog](https://blogs.technet.microsoft.com/dataplatforminsider/)**

---

## Community und Support

### Fragen stellen

💬 **[Stack Overflow](https://stackoverflow.com/questions/tagged/vscode)**  
Tag: `vscode` und `mssql`

### Folgen Sie VS Code

#### Social Media
- 🐦 **Twitter:** [@code](https://go.microsoft.com/fwlink/?LinkID=533687)
- 💼 **LinkedIn:** [VS Code Showcase](https://www.linkedin.com/showcase/vs-code)
- 🦋 **Bluesky:** [vscode.dev](https://bsky.app/profile/vscode.dev)
- 📱 **TikTok:** [@vscode](https://www.tiktok.com/@vscode)

#### Weitere Kanäle
- 🎥 **YouTube:** [@code](https://www.youtube.com/@code)
- 🎙️ **Podcast:** [VS Code Podcast](https://www.vscodepodcast.com)
- 💬 **Reddit:** [r/vscode](https://www.reddit.com/r/vscode/)

### Feature Requests und Bug Reports

#### Features anfordern
💡 **[Request Features](https://go.microsoft.com/fwlink/?LinkID=533482)**

#### Issues melden
🐛 **[Report Issues](https://www.github.com/Microsoft/vscode/issues)**

#### Videos ansehen
🎬 **[Watch Videos](https://www.youtube.com/channel/UCs5Y5_7XK8HLDX0SLNwkd3w)**

---

## Support-Ressourcen

### Microsoft Support

**Business Support:** [Support for Business](https://support.serviceshub.microsoft.com/supportforbusiness/create?sapId=d66407ed-3967-b000-4cfb-2c318cad363d)

### Rechtliches

- **Privacy:** [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?LinkId=521839)
- **Manage Cookies:** Cookie-Einstellungen
- **Terms of Use:** [Microsoft Terms of Use](https://www.microsoft.com/legal/terms-of-use)
- **License:** VS Code License

---

## Für AI-Assistenten: Navigations- und Nutzungshinweise

### Dokumentstruktur

Dieses Dokument ist in folgende Bereiche strukturiert:

1. **Installation** - Setup der mssql Extension
2. **Verbindung** - Datenbank-Verbindung herstellen
3. **Ausführung** - T-SQL Code ausführen
4. **Features** - IntelliSense, Linting, Navigation, Snippets
5. **Nächste Schritte** - Weiterführende Ressourcen

### Zielgruppen

- **T-SQL Entwickler** die VS Code nutzen möchten
- **Datenbank-Entwickler** auf SQL Server
- **Azure SQL Entwickler**
- **Cross-Platform SQL Entwickler** (Linux, macOS, Windows)

### Hauptanwendungsfälle

1. **Lokale SQL Server Entwicklung**
2. **Azure SQL Database Entwicklung**
3. **Cross-Platform SQL Entwicklung**
4. **Quick Queries und Ad-hoc Analysen**
5. **Stored Procedure und Function Development**

### Feature-Highlights

#### IntelliSense
- Kontext-bewusste Code-Vervollständigung
- Schema-Objekt-Vorschläge
- Parameter-Hilfe für Functions/Procedures

#### Linting
- Real-time Syntax-Check
- Fehler-Highlighting während des Schreibens

#### Navigation
- Peek/Go to Definition für Datenbank-Objekte
- Schnelle Schema-Exploration

#### Snippets
- Templates für häufige T-SQL Patterns
- Schnelleres Coding

### Vergleich zu anderen Tools

**Vorteile gegenüber SSMS:**
- Leichtgewichtiger Editor
- Cross-Platform (Linux, macOS, Windows)
- Moderne Editor-Features
- Integration mit Git und anderen Extensions

**Vorteile von VS Code + mssql:**
- Kostenlos
- Open Source
- Große Extension-Ecosystem
- Anpassbar und erweiterbar

### Best Practices für AI-Assistenten

Wenn Nutzer Fragen zu T-SQL in VS Code haben:

1. **Setup-Fragen:** Auf Installation und Verbindungs-Schritte verweisen
2. **IntelliSense-Fragen:** Erklären, dass Datenbank-Verbindung erforderlich ist
3. **Produktivitäts-Tipps:** Snippets und Shortcuts empfehlen
4. **Fehlersuche:** Linting-Features erläutern
5. **Ergebnisse-Export:** JSON/CSV Export-Optionen zeigen

### Häufige Workflows

1. **Verbinden → Query schreiben → Ausführen → Ergebnisse anzeigen**
2. **Stored Procedure entwickeln:** IntelliSense + Peek Definition nutzen
3. **Daten exportieren:** Ergebnisse als JSON/CSV speichern
4. **Schema erkunden:** Go to Definition für Tabellen und Views
5. **Quick Queries:** Snippets für Standard-Operationen verwenden

### Integration mit GitHub Copilot

**Synergien:**
- GitHub Copilot kann T-SQL Code vorschlagen
- mssql Extension bietet IntelliSense für Schema
- Kombination ermöglicht schnelle und präzise T-SQL Entwicklung
- Snippets + Copilot = Maximale Produktivität

---

*Version: 1.106 (Oktober 2025)*

*Dokumentation zuletzt aktualisiert: 11/12/2025*
