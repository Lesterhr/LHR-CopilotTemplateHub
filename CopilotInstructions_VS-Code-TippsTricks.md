# VS Code Tipps & Tricks Vol. 1

> **Navigation für KI-Assistenten:**
> - 31 praktische Tipps für effizientes Arbeiten mit VS Code
> - Kategorien: Updates, Bearbeitung, Navigation, Git, Extensions, Konfiguration, Tastenkombinationen
> - Schwierigkeitsgrad: Anfänger bis Fortgeschritten
> - Version: März 2016 (1. Aktualisierung April 2016)
>
> **Hauptthemen:** Produktivitäts-Tipps, Editor-Features, Git-Integration, Extensions, Workspace-Konfiguration, Tastenkürzel, Best Practices

---

## Inhaltsverzeichnis

1. [Was ist Visual Studio Code?](#was-ist-visual-studio-code)
2. [Die 31 Tipps & Tricks](#die-31-tipps--tricks)
   - [Updates & Insiders](#updates--insiders)
   - [Editor-Bearbeitung](#editor-bearbeitung)
   - [Navigation & Suche](#navigation--suche)
   - [Git-Integration](#git-integration)
   - [Extensions & Anpassungen](#extensions--anpassungen)
   - [Spezialisierte Features](#spezialisierte-features)
   - [Konfiguration & Einstellungen](#konfiguration--einstellungen)
   - [Tastenkombinationen](#tastenkombinationen)
3. [Lieblings-Tastenkombinationen der Autoren](#lieblings-tastenkombinationen-der-autoren)
4. [Über die Autoren](#über-die-autoren)

---

## Was ist Visual Studio Code?

**Visual Studio Code (VS Code)** ist ein Open Source Code Editor zum Entwickeln und Debuggen moderner Cloud- und Webanwendungen, der kostenlos für Linux, OS X sowie Windows verfügbar ist.

### Hauptmerkmale:

- **Über 30 Programmiersprachen** unterstützt (JavaScript, C#, C++, PHP, Java, HTML, R, CSS, SQL, Markdown, TypeScript, Less, Sass, JSON, XML, Python, etc.)
- **Blitzschneller Editor** mit integriertem Debugging
- **Git-Unterstützung** auf Knopfdruck
- **IntelliSense-Vervollständigung** für intelligentes Coding
- **Arbeitet auf Datei- und Ordner-Ebene** (keine Projektdateien erforderlich)
- **Erweiterbar durch Extensions** für alle Plattformen
- **Monatliche Updates** für kontinuierliche Verbesserung

### Architektur:

- **GitHub Electron Shell** für plattformübergreifende Entwicklung
- **Monaco Editor** als HTML-basierter Editor-Kern
- **Roslyn** für .NET-Unterstützung
- **TypeScript** für JavaScript-Entwicklung
- **Visual Studio Debugging Engine** für Debugging-Features

---

## Die 31 Tipps & Tricks

### Updates & Insiders

#### **Tipp 1: Updates vor allen anderen erhalten als VS Code Insider**

Visual Studio Code ist Open Source und wird ständig weiterentwickelt. Änderungen sind sofort im öffentlichen Repository sichtbar: https://github.com/Microsoft/vscode

**VS Code Insiders** ist eine Vorabversion, die parallel zur normalen Version installiert werden kann:

- **Eigenständiges Programm** mit eigenen Einstellungen und Erweiterungen
- **Parallel installierbar** neben der stabilen Version
- **Neueste Features** vor allen anderen testen
- **Fallback zur stabilen Version** bei Problemen möglich

**Download:** https://code.visualstudio.com/insiders

> **Workflow-Tipp:** Nutzen Sie Insiders zum Testen neuer Features, während die stabile Version für produktive Arbeit bereitsteht.

---

### Editor-Bearbeitung

#### **Tipp 2: Mehrere Eingabemarken (Multi-Cursor)**

Bearbeiten Sie mehrere Stellen in einer Datei parallel - ideal für identische Änderungen an verschiedenen Positionen.

**Verwendung:**

- **`Alt + Klick`**: Zusätzliche Eingabemarke an Klickposition einfügen
- **Jede Tastatureingabe** wird an allen Eingabemarken ausgeführt
- **Verschiedene Stellen markieren** gleichzeitig möglich

**Anwendungsfall:** Mehrere Variablennamen gleichzeitig umbenennen oder formatieren.

> **Produktivitäts-Boost:** Multi-Cursor ist eines der mächtigsten Features für repetitive Änderungen.

---

#### **Tipp 9: Emmet Snippets**

HTML und XML schneller schreiben mit CSS-ähnlichen Ausdrücken, die mit der Tab-Taste expandiert werden.

**Einfache Beispiele:**

- `html` + Tab → `<html></html>`
- `li*5` + Tab → 5x `<li></li>` eingefügt
- Eingabemarke wird automatisch zwischen Tags platziert

**Unterstützte Formate:**

- HTML, XML, Razor
- CSS, Less, SCSS
- XSL, Jade, Handlebars, HBS
- JSX, TSX

**Emmet Cheat Sheet:** http://docs.emmet.io/cheat-sheet/

> **Hinweis für Assistenten:** Emmet ist besonders effizient für Frontend-Entwicklung - komplexe HTML-Strukturen können mit kurzen Ausdrücken generiert werden.

---

#### **Tipp 31: Zeilenumbruch im Editor**

Verhindern Sie, dass Text über den Rand des Editorfensters hinausgeht.

**Schnelle Umschaltung:**

- **`Alt + Z`**: Zeilenumbruch umschalten (Toggle Word Wrap)
- Auch über View-Menü: "Toggle Word Wrap"

**Dauerhafte Konfiguration:**

```json
"editor.wrappingColumn": 0
```

- **Wert 0**: Automatischer Umbruch am Fensterrand
- **Wert 300** (Standard): Umbruch nach 300 Zeichen
- Änderung wird sofort nach Speichern wirksam

---

### Navigation & Suche

#### **Tipp 3: Visual Studio Code mit der Kommandopalette steuern**

Die **Command Palette** ist der zentrale Zugriffspunkt für alle VS Code-Befehle.

**Öffnen:**

- **`F1`**: Command Palette mit ">" (Kommando-Modus)
- **`Ctrl + P`**: Leere Eingabe (Navigations-Modus)

**Modi der Eingabe:**

Das erste Zeichen bestimmt den Modus:

| Präfix | Modus | Funktion |
|--------|-------|----------|
| `>` | Kommando | Alle VS Code-Befehle |
| (leer) | Navigation | Zuletzt geöffnete Dateien, schnelle Dateisuche |
| `?` | Hilfe | Liste aller verfügbaren Modi |
| `@` | Symbol-Suche | Symbole in aktueller Datei |
| `#` | Workspace-Symbol | Symbole im gesamten Workspace |
| `:` | Zeile | Zur Zeile springen |

**Navigation-Modus Features:**

- Liste der zuletzt geöffneten Dateien
- Filtert geöffnete und Workspace-Dateien
- Bei IntelliSense-Unterstützung: auch Symbole

> **Best Practice:** `Ctrl + P` ist einer der meistgenutzten Shortcuts - prägen Sie ihn sich ein!

---

#### **Tipp 7: Suchergebnisse ausblenden**

Bei der Suche über alle Dateien können bereits untersuchte Treffer ausgeblendet werden.

**Verwendung:**

1. Suche durchführen über alle Dateien
2. Mauszeiger über Trefferzahl bei Datei bewegen
3. **Kreuz** erscheint - Klick blendet Datei aus
4. Erneute Suche zeigt alle Dateien wieder an

**Vorteil:** Behält Überblick über bereits bearbeitete Fundstellen bei umfangreichen Änderungen.

---

#### **Tipp 8: RegEx-Treffer beim Ersetzen wieder einsetzen**

Kombinieren Sie reguläre Ausdrücke mit der Ersetzen-Funktion für mächtige Transformationen.

**Gruppen definieren:**

- Mit **Klammern** `()` Gruppen in RegEx definieren
- Referenzierung im Ersetzungs-Text: `$1`, `$2`, `$3`, ...
- `$$` für wörtliches Dollarzeichen

**Beispiel - Hochkommata durch Anführungszeichen ersetzen:**

- **Suche:** `'([^']*)'`
- **Ersetzen:** `"$1"`
- **Ergebnis:** `'text'` → `"text"`

**Erklärung:**

- `'([^']*)'` findet Text mit Hochkommata
- `([^']*)` definiert Gruppe 1 (Text zwischen Hochkommata)
- `"$1"` ersetzt durch Anführungszeichen und Inhalt von Gruppe 1

> **Power-User-Tipp:** Reguläre Ausdrücke mit Gruppen ermöglichen komplexe Code-Transformationen in Sekunden.

---

#### **Tipp 26: Navigieren zwischen verwendeten Dateien**

Schnell zwischen zuletzt verwendeten Dateien wechseln.

**Tastenkombinationen:**

- **`Ctrl + E`**: Liste zuletzt verwendeter Dateien (synonym zu `Ctrl + Tab`)
- **`Ctrl + Tab`**: Vorwärts durch Liste
- **`Ctrl + Shift + Tab`**: Rückwärts durch Liste
- **`Ctrl + Pfeiltasten`**: Alternative Navigation bei gedrückter Ctrl-Taste

**Workflow:**

1. `Ctrl + E` oder `Ctrl + Tab` drücken
2. Tab-Taste bei gedrückter Ctrl wiederholt drücken
3. Enter oder Ctrl loslassen zum Öffnen

> **Kommandopalette:** `Ctrl + Shift + P` zeigt Shortcuts neben Befehlen an - ideal zum Lernen.

---

#### **Tipp 27: Dateien in eigenem Editor-Fenster öffnen**

Dateien "an der Seite" öffnen für Split-Screen-Entwicklung.

**Methoden:**

1. **`Ctrl + Klick`** auf Datei im Explorer
2. **Icon am rechten Rand** der Dateiliste nutzen
3. **`Ctrl + K, F12`**: Definition in eigenem Fenster öffnen

**Fensterverwaltung:**

- **`Ctrl + 1/2/3`**: Wechsel zwischen bis zu 3 Editor-Fenstern
- **`Ctrl + W`**: Aktuelles Fenster schließen
- **`Ctrl + B`**: Fokus auf Editorfenster (aus Explorer/Suche)

---

### Git-Integration

#### **Tipp 14: Git Quick Change Info**

Änderungen zur vorherigen Version direkt im Editor sichtbar.

**Markierungen (links neben Zeilennummern):**

- **Grüne Linie**: Neue Zeilen hinzugefügt
- **Blaue Linie**: Zeilen wurden verändert
- **Roter Pfeil**: Zeilen wurden gelöscht

**Voraussetzung:** Datei muss unter Git Source-Verwaltung stehen.

**Vorteil:** Live-Feedback während der Bearbeitung - kein Wechsel zur Git-Ansicht nötig.

---

#### **Tipp 15: Git-Ansicht aktualisieren**

VS Code nutzt das externe Git-Programm. Die Ansicht kann manchmal nicht aktuell sein.

**Aktualisierung:**

- **Refresh-Button** oben in der Git-Ansicht
- **Refresh-Button** unten in der Statusbar

**Wann nötig:** Bei Änderungen außerhalb von VS Code oder wenn Ansicht durcheinandergerät.

---

#### **Tipp 16: Git-Inline-Vergleich**

Alternative zur Side-by-Side-Vergleichsansicht.

**Standard:** Änderungen werden nebeneinander gezeigt (Split View)

**Inline View aktivieren:**

1. Reiter-Untermenü öffnen
2. "Switch to Inline View" auswählen
3. Änderungen werden in einem Code-Fenster gezeigt

**Zurück zur Side-by-Side View:**

- Dasselbe Menü erneut verwenden

**Vorteil Inline:** Bessere Übersicht bei kleinen Änderungen, weniger Bildschirmplatz benötigt.

---

#### **Tipp 17: Dateien vergleichen**

VS Code kann beliebige Dateien miteinander vergleichen, nicht nur Git-Versionen.

**Methode 1 - Command Palette:**

1. `Files: Compare Active File With...` aufrufen
2. Datei aus Menü auswählen
3. Vergleichsansicht öffnet sich

**Methode 2 - Kontextmenü:**

1. Rechtsklick auf erste Datei im Explorer
2. "Select for Compare" wählen
3. Rechtsklick auf zweite Datei
4. "Compare with '<Erste Datei>'" wählen

**Anwendungsfall:** Unterschiede zwischen Konfigurationsdateien, Code-Versionen oder Backups analysieren.

---

### Extensions & Anpassungen

#### **Tipp 18: Extensions**

VS Code kann durch Extensions von Drittanbietern erweitert werden.

**Features:**

- Mit **TypeScript oder JavaScript** entwickelt
- Veröffentlicht im **Visual Studio Code Marketplace**
- Installation mit wenigen Klicks
- Plattformübergreifend verfügbar

**Marketplace:** https://marketplace.visualstudio.com/#VSCode

**Installation:**

- Befehl: `Extension: Install Extension`
- Extensions durchsuchen und auswählen
- Automatische Installation

**Entwicklung eigener Extensions:**

- Dokumentation verfügbar unter Visual Studio Code: Extensions entwickeln
- Eigene Funktionalität teilen mit der Community
- Open-Source-Ökosystem

> **Hinweis:** Extensions können VS Code-Funktionalität erheblich erweitern - von Sprach-Support bis zu kompletten Workflows.

---

#### **Tipp 23: Einstellungen und Extensions synchronisieren**

VS Code bietet keine native Synchronisierung - aber Workarounds existieren.

**Manuelle Synchronisierung:**

1. Cloud-Dienste nutzen (OneDrive, Dropbox)
2. Einstellungsordner durch symbolische Links ersetzen
3. Links zu synchronisierten Ordnern erstellen

**Ordner-Verknüpfungen erstellen:**

- **Windows:** `mklink /d <VSCode-Ordner> <Synchronisierter-Ordner>`
- **Mac & Linux:** `ln -s <Synchronisierter-Ordner> <VSCode-Ordner>`

**Automatische Lösung - Extension:**

**"Visual Studio Code Settings Sync"** aus dem Marketplace:

- Nutzt GitHub GIST
- Sehr einfache Einrichtung
- Automatische Synchronisation über mehrere Rechner

> **Best Practice:** Settings Sync Extension für problemlose Synchronisation über mehrere Geräte.

---

#### **Tipp 28: Tastenkombinationen anpassen**

Eigene Tastenkombinationen für maximale Produktivität definieren.

**Ressourcen:**

- **Offizielle Übersicht:** Key Bindings for Visual Studio Code
- Aktuelle Shortcuts für jedes Betriebssystem

**Wichtig - Internationale Tastaturen:**

- VS Code zeigt Shortcuts für Ihre Tastatur an
- Intern wird immer **US-amerikanisches Layout** verwendet
- Dies gilt auch für `keybindings.json`
- Unterschiede durch **blauen Kreis mit "i"** markiert

**Eigene Tastenkombination anlegen:**

1. **`Ctrl + K, Ctrl + K`** drücken
2. Ziel-Tastenkombination eingeben
3. Enter drücken
4. Vorgefertigter Eintrag in `keybindings.json` wird angelegt
5. `command` und `when` Werte definieren

**Verfügbare Befehle:** Am Ende der Standard-Tastaturkurzbefehle (File | Preferences | Keyboard Shortcuts) finden sich nicht zugewiesene Befehle.

---

#### **Tipp 30: Änderung der Oberflächensprache**

VS Code richtet sich nach System-Ländereinstellungen, kann aber angepasst werden.

**Sprache ändern:**

1. **`F1`** drücken
2. "Configure Language" (oder "Sprache konfigurieren") wählen
3. In `locale.json` den `locale`-Eintrag ändern:
   - `"de-de"` für Deutsch
   - `"en-us"` für Englisch (US)
4. VS Code neu starten

**Anwendungsfall:** Entwickler bevorzugen oft englischsprachige IDEs trotz deutschsprachigem System.

---

### Spezialisierte Features

#### **Tipp 4: Sprache für eine Datei auswählen**

VS Code erkennt Sprachen meist automatisch, aber manchmal muss manuell nachgeholfen werden.

**Wann nötig:**

- Neue Datei ohne Speicherung
- Datei ohne Dateiendung
- Falsche automatische Erkennung

**Sprache ändern:**

**Methode 1:** Befehl `Change Language Mode` ausführen

**Methode 2:** Unten rechts in Statusleiste auf aktuelle Sprache klicken

**Resultat:** Liste mit unterstützten Sprachen öffnet sich

**Dateinamens-Suffix zuordnen:**

Falls VS Code einen Suffix nicht erkennt, kann im Auswahlfenster eine permanente Verknüpfung vorgenommen werden.

> **Tipp:** VS Code unterstützt Syntax-Highlighting für sehr viele Sprachen - nutzen Sie es!

---

#### **Tipp 5: AutoSave**

Automatisches Speichern nach jeder Änderung - besonders praktisch für Web-Entwicklung.

**Aktivierung in Einstellungen:**

```json
"files.autoSave": "afterDelay",
"files.autoSaveDelay": 1000
```

**Optionen für `files.autoSave`:**

- `"off"`: Deaktiviert (Standard)
- `"afterDelay"`: Nach definiertem Zeitintervall
- `"onFocusChange"`: Bei Fokuswechsel
- `"onWindowChange"`: Bei Fensterwechsel

**Vorteile:**

- Kein ständiges Drücken von Speichern
- Dateien immer aktuell beim Browser-Refresh
- Ideal für iterative Entwicklung

**Vorsicht bei:**

- Automatischen Tasks bei Dateiänderungen (z.B. TypeScript-Transpilierung)
- Kann CPU stark belasten
- Möglicherweise unerwünschte Build-Trigger

---

#### **Tipp 6: Unwichtige Ordner verstecken**

Ordner und Dateien, die nie editiert werden, können aus der Explorer-Ansicht ausgeblendet werden.

**Verwendung:**

In `settings.json` (global oder Workspace) die Option `files.exclude` verwenden:

```json
"files.exclude": {
  "node_modules/": true,
  ".git/": true
}
```

**Pattern-Beispiel - TypeScript generierte JavaScript-Dateien ausblenden:**

```json
"files.exclude": {
  "**/*.js": { "when": "$(basename).ts" }
}
```

**Workspace-Einstellungen öffnen:**

- Befehl: `Preferences: Open Workspace Settings`
- Datei wird automatisch erstellt, falls nicht vorhanden

**Anwendungsfall:** `node_modules`, Build-Output, temporäre Dateien ausblenden.

---

#### **Tipp 10: Tastenkürzel-Akkorde**

Wie Visual Studio unterstützt VS Code **Chord-Shortcuts** - zwei Tastenkombinationen nacheinander.

**Beispiel:**

Lokale Suche auf `Ctrl + F, Ctrl + F` legen:

```json
{ "key": "ctrl+f ctrl+f", "command": "actions.find" }
```

Globale Suche auf `Ctrl + F, Ctrl + G` legen:

```json
{ "key": "ctrl+f ctrl+g", "command": "workbench.action.findInFiles" }
```

**Syntax in `keybindings.json`:**

- Akkord-Bestandteile durch **Leerzeichen** trennen
- Beispiel: `"ctrl+k ctrl+s"`

**Visual Feedback:**

Nach erstem Tastenkürzel zeigt Statusbar: `"(Ctrl+F) was pressed. Waiting for second key of chord..."`

**Vorteil:** Gruppierung ähnlicher Befehle, mehr Shortcuts ohne Konflikte.

---

#### **Tipp 11: Markdown-Vorschau**

Markdown-Dateien mit formatierter Vorschau anzeigen.

**Vorschau-Befehle:**

- **`Ctrl + Shift + V`**: Zwischen Markdown und Vorschau umschalten
- **`Ctrl + K, V`**: Vorschau seitlich öffnen

**Format:** GitHub Flavored Markdown

- Zusätzliche Funktionen zum normalen Markdown
- Ideal für GitHub-README-Dateien

**Kombination mit Zeilenumbruch:**

- **`Alt + Z`**: Toggle Word Wrap
- Besonders nützlich bei langen Zeilen in Markdown

> **Hinweis:** Perfekt für Dokumentation und README-Dateien in Echtzeit testen.

---

#### **Tipp 12: CSS-Selektoren visualisieren**

VS Code hilft bei komplexen CSS-Selektoren mit visueller Vorschau.

**Funktion:**

- Mauszeiger über CSS-Selektor bewegen
- Vorschau zeigt, wie HTML-Elemente aussehen müssen
- Erklärt, wann der Selektor angewendet wird

**Anwendungsfall:** Komplizierte Selektoren verstehen, die man nicht häufig verwendet.

**Vorteil:** Visuelles Lernen und schnelles Verständnis von Selektor-Logik.

---

#### **Tipp 13: "Latest Version" von Abhängigkeiten in package.json**

Für Node.js-Projekte zeigt VS Code Informationen zu Modulen in `package.json`.

**Hover-Information:**

- Mauszeiger über Abhängigkeit bewegen
- **Name** des Moduls
- **Kurze Beschreibung**
- **Neueste Version** wird angezeigt

**Auto-Completion:**

- **`Ctrl + Space`**: Neue Abhängigkeit eingeben
- Liste verfügbarer Module wird angezeigt
- Automatische Vervollständigung

**Vorteil:** Schnelle Überprüfung auf Updates, keine manuelle NPM-Suche nötig.

---

#### **Tipp 19: Automatische Taskerkennung für Gulp, Grunt und Jake**

VS Code erkennt automatisch Tasks in Node.js Build-Tools.

**Unterstützte Build-Tools:**

- **Gulp**
- **Grunt**
- **Jake**

**Verwendung:**

1. Befehl `Tasks: Run Task` ausführen
2. Liste mit automatisch erkannten Tasks öffnet sich
3. Task auswählen und ausführen

**Vorteil:** Keine manuelle `tasks.json` erforderlich - VS Code liest Build-Dateien direkt.

> **Hinweis für Assistenten:** Funktioniert nur bei Node.js-Projekten mit entsprechenden Build-Dateien.

---

#### **Tipp 20: PHP-Konfiguration in Visual Studio Code**

VS Code unterstützt PHP mit Syntax-Highlighting, aber für Live-Fehlerüberprüfung ist Konfiguration nötig.

**Schritt 1 - PHP installieren:**

- Download: http://php.net/downloads.php
- Lokal installieren oder Archiv entpacken

**Schritt 2 - Pfad konfigurieren:**

In `settings.json`:

```json
"php.validate.executablePath": "C:/path/to/php.exe"
```

**Benachrichtigung bei fehlender Konfiguration:**

"Cannot validate the php file. The php program was not found. Use the 'php.validate.executablePath' setting to configure the location of 'php'."

**Zusätzliche Extension:**

**"PHP Debug adapter for Visual Studio Code"** im Marketplace für Debugging-Unterstützung.

---

### Konfiguration & Einstellungen

#### **Tipp 21: Kommandozeilenparameter von Visual Studio Code**

VS Code kann über die Kommandozeile mit dem Befehl `code` gestartet werden.

**Grundlegende Verwendung:**

```bash
code [Optionen] [Pfade]
```

**Wichtigste Optionen:**

| Option | Funktion |
|--------|----------|
| `-r, --reuse-window` | In bestehendem Fenster öffnen oder neues erstellen |
| `-n, --new-window` | Immer neues Fenster öffnen |
| `-g, --goto` | Format: `Dateipfad:Zeile:Spalte` - Cursor positionieren |
| `--disable-extensions` | VS Code ohne Extensions starten |
| `--verbose` | Debug-Informationen ausgeben |
| `--diff <file1> <file2>` | Diff-Editor mit zwei Dateien öffnen |

**Beispiele:**

```bash
code .                          # Aktuellen Ordner öffnen
code file.txt                   # Datei öffnen
code file.txt:10:5 -g          # Datei an Zeile 10, Spalte 5 öffnen
code --diff file1.txt file2.txt # Dateien vergleichen
```

**Linux-Konfiguration:**

Symbolischen Link erstellen:

```bash
sudo ln -s /path/to/vscode/Code /usr/local/bin/code
```

---

#### **Tipp 22: Speicherorte in Visual Studio Code**

VS Code speichert verschiedene Dateien an unterschiedlichen Orten.

**Einstellungen, Tastenkombinationen und Code-Snippets:**

| Betriebssystem | Pfad |
|----------------|------|
| **Windows** | `%APPDATA%\Code\User\` |
| **Mac** | `$HOME/Library/Application Support/Code/User/` |
| **Linux** | `$HOME/.config/Code/User/` |

**Dateien in diesem Ordner:**

- `settings.json` - Benutzereinstellungen
- `keybindings.json` - Tastenkombinationen
- `snippets/` - Benutzer-Snippets für verschiedene Sprachen

**Extensions:**

| Betriebssystem | Pfad |
|----------------|------|
| **Windows** | `%USERPROFILE%\.vscode\extensions\` |
| **Mac** | `$HOME/.vscode/extensions` |
| **Linux** | `$HOME/.vscode/extensions` |

**Extension-Struktur:**

- Jede Extension hat eigenen Unterordner
- Format: `autor.extension-name`
- Keine zentrale Installations-Datei
- Installation = Ordner in Extensions-Verzeichnis verschieben

**Insiders-Version:**

Nutzt `Code Insiders` bzw. `.vscode-insiders` statt `Code` bzw. `.vscode`

---

#### **Tipp 24: Crash-Berichte ausschalten**

Bei Abstürzen werden Crash-Berichte an Microsoft gesendet.

**Deaktivierung:**

```json
"telemetry.enableCrashReporter": false
```

**Wirksamkeit:** Neustart erforderlich

---

#### **Tipp 25: Übermittlung von Telemetrie-Daten abschalten**

VS Code sammelt anonymisierte Nutzungsdaten zur Verbesserung.

**Deaktivierung:**

1. Datei-Menü → Einstellungen → Benutzereinstellungen
2. In Standardeinstellungen suchen: `"telemetry.enableTelemetry": true`
3. In eigener `settings.json` überschreiben:

```json
"telemetry.enableTelemetry": false
```

**Zweck der Telemetrie:**

- Anonymisierte Nutzungsdaten
- Verwendung zur Verbesserung von VS Code
- Opt-out jederzeit möglich

---

## Lieblings-Tastenkombinationen der Autoren

Die am häufigsten verwendeten Shortcuts der E-Book-Autoren Tobias Kahlert und Kay Giza:

### Top-Produktivitäts-Shortcuts:

| Tastenkombination | Funktion |
|-------------------|----------|
| `Alt + Z` | **Zeilenumbruch umschalten** |
| `Ctrl + P` | **Schnell Dateien öffnen** |
| `Ctrl + Tab` | **Zwischen zuletzt verwendeten Dateien navigieren** |
| `Ctrl + 1/2/3` | **Geöffnete Editor-Fenster anspringen** |
| `Ctrl + W` | **Aktiven Editor schließen** |
| `Ctrl + #` | **Zeile(n) ein- oder auskommentieren** |
| `Ctrl + Shift + K` | **Zeile(n) löschen** |
| `Ctrl + Klick` | **Datei aus Explorer an der Seite öffnen** |

### Suche-Optimierung:

| Tastenkombination | Funktion |
|-------------------|----------|
| `Alt + C` | **Suche nach exakter Schreibweise ein/aus** (case-sensitive) |
| `Alt + W` | **Suche nach ganzen Wörtern ein/aus** |
| `Ctrl + D` | **Auswahl auf nächsten Suchtreffer positionieren** |
| `Ctrl + K, Ctrl + D` | **Letzte Auswahl auf nächsten Suchtreffer positionieren** |

### Navigation & Code:

| Tastenkombination | Funktion |
|-------------------|----------|
| `Ctrl + K, F12` | **Definition des markierten Terms an der Seite öffnen** |
| `Alt + Pfeil oben` | **Zeile komplett nach oben verschieben** |
| `Alt + Pfeil unten` | **Zeile komplett nach unten verschieben** |

---

## Hinweise zum E-Book

### Über dieses Dokument

- **Erstellt:** März 2016 (1. Aktualisierung April 2016)
- **Basis:** Englischsprachige Vorabversionen
- **Plattform:** Windows (Tastenbefehle für Windows)
- **Updates:** Monatliche VS Code-Releases entwickeln sich schnell weiter

### Wichtige Hinweise:

**Für Mac/Linux-Nutzer:**

- E-Book basiert auf Windows
- Tastenzuordnungen für andere Betriebssysteme: code.visualstudio.com

**Community & Feedback:**

- Deutschsprachiges Forum zu Visual Studio Code
- Mögliche Überführung auf GitHub für Community-Beiträge
- Feedback erwünscht!

**Weitere Ressourcen:**

- **Neue Tipp-Sammlung:** Vom VS Code Team
- **Code-Pakete:** Wachsendes Repository mit Ressourcen für VS Code

### Aktuelle Version

Dokument immer aktuell unter: **http://aka.ms/VSCodeTippsTricks**

---

## Über die Autoren

### Kay Giza

- **Position:** Audience Evangelism Manager bei Microsoft Deutschland
- **Blog:** http://www.giza-blog.de
- **Twitter:** http://twitter.com/KayGiza
- **XING:** Kay Giza
- **LinkedIn:** Kay Giza

### Tobias Kahlert

- **Position (2016):** Werkstudent im Visual Studio Audience Marketing-Team bei Microsoft Deutschland
- **Twitter:** https://twitter.com/CubeCode
- **Microsoft TechWiese.de Profil:** Tobias Kahlert
- **XING:** Tobias Kahlert

---

## Über Dr. Erich Gamma (Vorwort)

**Position:** Microsoft Distinguished Engineer, Development Lead Visual Studio Code

### Hintergrund:

- Leitet VS Code-Projekt von Zürich aus
- Verantwortlich für Monaco Online-Editor (in vielen Microsoft-Produkten)
- **Vorher IBM:** Einer der Väter von Eclipse und dessen Java-Entwicklungswerkzeuge
- **"Gang of Four"-Mitglied:** Buch-Klassiker "Entwurfsmuster. Elemente wiederverwendbarer objektorientierter Software"
- **JUnit:** Entwickelt zusammen mit Kent Beck - de-facto Standard-Testwerkzeug für Java

### Entwicklungsphilosophie:

> "Uns war von Anfang an bewusst; wenn wir ein Werkzeug für Entwickler bauen, dann müssen wir es auch selbst nutzen. [...] Dank diesem 'eat your own dog food' haben wir das Werkzeug immer weiter verfeinert und verbessert."

**Entwicklungsbeginn:** Vor über 5 Jahren
**Beta-Release:** Mai 2015
**Community:** Sehr aktiv mit Feedback über Bug-Reports, Tweets, Stack Overflow

---

## Zusammenfassung für KI-Assistenten

### Kategorisierung der Tipps:

**Editor-Produktivität:**

- Multi-Cursor (Tipp 2)
- Emmet Snippets (Tipp 9)
- Zeilenumbruch (Tipp 31)
- AutoSave (Tipp 5)

**Navigation & Workflow:**

- Command Palette (Tipp 3)
- Datei-Navigation (Tipp 26, 27)
- Workspace-Organisation (Tipp 6)

**Suche & Ersetzen:**

- Suchergebnisse managen (Tipp 7)
- RegEx-Gruppen (Tipp 8)

**Git-Integration:**

- Quick Change Info (Tipp 14)
- Inline-Vergleich (Tipp 16)
- Dateien vergleichen (Tipp 17)

**Spezialisierte Features:**

- Markdown-Vorschau (Tipp 11)
- CSS-Visualisierung (Tipp 12)
- PHP-Konfiguration (Tipp 20)

**Extensions & Anpassung:**

- Extensions (Tipp 18)
- Settings Sync (Tipp 23)
- Tastenkombinationen (Tipp 28)

### Best Practices:

1. **Command Palette beherrschen** (`Ctrl + P`, `F1`)
2. **Multi-Cursor nutzen** für repetitive Änderungen
3. **Emmet Snippets** für HTML/CSS-Entwicklung
4. **Git-Integration** für Versionskontrolle nutzen
5. **Extensions** für spezifische Workflows installieren
6. **Settings Sync** für Multi-Device-Entwicklung
7. **Tastenkombinationen lernen** für maximale Effizienz

### Workflow-Optimierung:

- **Datei-Navigation:** `Ctrl + P` > `Ctrl + Tab` > Explorer
- **Code-Bearbeitung:** Multi-Cursor > Emmet > Manual
- **Git-Workflow:** Quick Info > Inline Compare > Full Diff
- **Suche:** Local (`Ctrl + F`) > Workspace > RegEx

### Wichtigste Tastenkombinationen:

1. `Ctrl + P` - Quick Open
2. `Ctrl + Shift + P` / `F1` - Command Palette
3. `Ctrl + D` - Nächstes Vorkommen auswählen
4. `Alt + Z` - Zeilenumbruch umschalten
5. `Ctrl + K, F12` - Definition seitlich öffnen

---

**Quelle:** Visual Studio Code - Tipps & Tricks Vol. 1
**Copyright:** © Microsoft Deutschland GmbH 2016
**Autoren:** Tobias Kahlert und Kay Giza
**Dokumenttyp:** Produktivitäts-Guide und Best Practices
**Version:** März 2016, 1. Aktualisierung April 2016
**Download:** http://aka.ms/VSCodeTippsTricks
