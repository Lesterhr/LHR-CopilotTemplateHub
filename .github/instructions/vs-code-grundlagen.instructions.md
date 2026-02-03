# VS Code Grundlagen - Guide to Success on VSCode

> **Navigation für KI-Assistenten:**
> - Abschnitt 1: Was ist VSCode - Einführung und Überblick
> - Abschnitt 2: Setup auf Unix-Computern
> - Abschnitt 3: Setup auf eigenem Computer (Download, SFTP, C0 Extension)
> - Abschnitt 4: Troubleshooting - Fehlerbehandlung
> - Abschnitt 5: Verwendung von VSCode für C0-Programme
>
> **Hauptthemen:** VSCode Installation, SFTP-Konfiguration, Remote-Entwicklung, C0-Extension, Syntax Highlighting, Auto-Completion

---

## Inhaltsverzeichnis

1. [Was ist VSCode](#1-was-ist-vscode)
2. [VSCode auf unix.andrew.cmu.edu Computern einrichten](#2-vscode-auf-unixandrewcmuedu-computern-einrichten)
3. [VSCode auf eigenem Computer einrichten](#3-vscode-auf-eigenem-computer-einrichten)
   - 3.1 [VSCode herunterladen](#31-vscode-herunterladen)
   - 3.2 [SFTP Extension einrichten](#32-sftp-extension-einrichten)
   - 3.3 [C0 Extension einrichten](#33-c0-extension-einrichten)
4. [Troubleshooting](#4-troubleshooting)
   - 4.1 [Erste Schritte](#41-erste-schritte)
   - 4.2 [Unix Server wechseln](#42-unix-server-wechseln)
   - 4.3 [Sync-Fehler](#43-sync-fehler)
5. [VSCode zur Bearbeitung von C0-Programmen verwenden](#5-vscode-zur-bearbeitung-von-c0-programmen-verwenden)

---

## 1. Was ist VSCode

**Visual Studio Code (VSCode)** ist ein moderner Editor, der entwickelt wurde, um Code schnell und effizient zu schreiben.

### Hauptfunktionen:

- **Standard Syntax Highlighting**: Farbliche Hervorhebung von Code-Elementen
- **Auto-Completion**: Automatische Vorschläge für Variablen- und Funktionsnamen
- **Typ-Überprüfung**: Code wird während des Schreibens typgeprüft
- **Funktions-Prototypen**: Anzeige von Prototypen und Dokumentation von aufgerufenen Funktionen
- **Remote-Entwicklung**: Code auf eigenem Computer schreiben und auf unix.andrew.cmu.edu speichern

---

## 2. VSCode auf unix.andrew.cmu.edu Computern einrichten

Die Einrichtung wird automatisch als Teil des ersten 15-122 Labs durchgeführt.

> **Hinweis für Assistenten:** Dieser Abschnitt ist relevant für Nutzer, die VSCode direkt auf CMU-Unix-Computern verwenden.

---

## 3. VSCode auf eigenem Computer einrichten

Sie können Ihre 15-122 Programmieraufgaben (oder anderen 15-122 Code) auf Ihrem eigenen Computer bearbeiten und auf unix.andrew.cmu.edu speichern lassen.

### Erforderliche Schritte:

1. VSCode herunterladen (siehe 3.1)
2. SFTP Extension installieren (siehe 3.2)
3. C0 Extension installieren (siehe 3.3)

### 3.1 VSCode herunterladen

**Download-Quelle:** https://code.visualstudio.com/download

Der erste Schritt zur lokalen Einrichtung von VSCode für 15-122 ist das Herunterladen von VSCode von der offiziellen Website.

---

### 3.2 SFTP Extension einrichten

#### Was ist SFTP?

**SFTP (Secure File Transfer Protocol)** ermöglicht es Ihnen, Dateien auf Ihrem lokalen Computer zu bearbeiten und sie nach dem Speichern mit AFS zu synchronisieren.

#### Vorteile:

- Keine kontinuierliche Verbindung zu CMU Unix-Servern erforderlich
- Computer verbindet sich nur bei Bedarf zum Hochladen von Änderungen
- Effizientere Arbeitsweise als ständige SSH-Verbindung

#### Wichtiger Hinweis zu Extensions:

VSCode bietet mehrere Extensions an (SSH, ältere liximomo SFTP Extension). **Die Natizyskunk SFTP Extension ist die zuverlässigste** für die Arbeit mit AFS.

#### Schritt-für-Schritt Anleitung:

**Schritt 1: SFTP Extension installieren**

1. Klicken Sie auf die "Extensions"-Tab in der linken Sidebar
2. Suchen Sie nach "SFTP"
3. Wählen Sie die Extension von **Natizyskunk**
4. Klicken Sie auf den blauen "Install"-Button

> **⚠️ WICHTIG:** Wenn Sie die SFTP Extension von liximomo installiert haben, müssen Sie diese deinstallieren, damit die Natizyskunk-Version funktioniert.

**Schritt 2: Arbeitsordner erstellen und öffnen**

1. Erstellen Sie einen 15-122 Ordner irgendwo auf Ihrem Computer
2. Öffnen Sie ihn in VSCode mit "File → Open"

**Schritt 3: SFTP Konfiguration erstellen**

1. Öffnen Sie die Command Palette:
   - **Windows:** `Ctrl + Shift + P`
   - **Mac:** `Cmd + Shift + P`
2. Tippen Sie "SFTP: Config" und drücken Sie Enter
3. Eine Datei namens "sftp.json" wird erstellt

**Schritt 4: Konfiguration anpassen**

Ersetzen Sie den Text in der Config-Datei mit folgendem (fügen Sie Ihre Andrew ID ein):

```json
{
  "name": "15122",
  "host": "unix.andrew.cmu.edu",
  "protocol": "sftp",
  "port": 22,
  "username": "REPLACE THIS WITH YOUR ANDREW ID IN LOWER CASE",
  "remotePath": "private/15122",
  "uploadOnSave": true,
  "downloadOnOpen": true,
  "ignore": [
    ".vscode",
    ".git",
    ".DS_Store",
    "admin"
  ]
}
```

**Konfigurationsparameter erklärt:**

- `name`: Name der Verbindung
- `host`: Server-Adresse (unix.andrew.cmu.edu)
- `protocol`: Übertragungsprotokoll (sftp)
- `port`: Verbindungsport (22 für SFTP)
- `username`: Ihre Andrew ID (in Kleinbuchstaben!)
- `remotePath`: Pfad zum 15122-Ordner auf AFS
- `uploadOnSave`: Automatischer Upload beim Speichern
- `downloadOnOpen`: Automatischer Download beim Öffnen
- `ignore`: Dateien/Ordner, die nicht synchronisiert werden sollen

> **Hinweis:** Wenn Sie Ihren 15122-Ordner an einem anderen Ort in AFS erstellt haben, müssen Sie "private/15122" durch den Pfad zu Ihrem 15122-Ordner ersetzen.

**Vergessen Sie nicht, die Datei zu speichern!**

**Schritt 5: Erste Synchronisation durchführen**

1. Rechtsklick auf einen leeren Bereich in der Explorer-Sidebar
2. Klicken Sie auf "Sync Remote → Local"
3. Sie werden nach Ihrem Passwort gefragt
4. Nach Eingabe sollten Sie Ihre 122-Dateien sehen!

#### Wann welche Sync-Operation verwenden:

- **Sync Remote → Local**: Wenn neue Dateien zum AFS-Ordner hinzugefügt wurden (z.B. Labs kopieren oder Starter-Code von Autolab herunterladen)
- **Sync Local → Remote**: Wenn neue Dateien auf Ihrem lokalen Computer hinzugefügt wurden
- **Automatische Synchronisation**: Bearbeitete Dateien werden beim Speichern automatisch zu AFS übertragen

> **Troubleshooting:** Wenn Sie einen Authentifizierungsfehler erhalten, überprüfen Sie Ihren Benutzernamen in sftp.json und Ihr Passwort.

---

### 3.3 C0 Extension einrichten

Ohne Syntax Highlighting sieht der Code sehr einfach aus. Das 122-Team hat eine C0 Extension vorbereitet!

#### Installation:

1. Gehen Sie zurück zur Extensions-Tab
2. Suchen Sie nach "C0 VSCode Language Support"
3. Installieren Sie durch Klicken auf den blauen Install-Button

> **⚠️ WICHTIG:** Installieren Sie NICHT "C0 Syntax Highlighter"! Dies würde mit der richtigen Extension interferieren.

> **Hinweis zur AFS-Speicherung:** Seien Sie vorsichtig, dass Extensions, die Sie remote mit der SSH Extension installieren, Ihren AFS-Speicher belegen! Wenn Ihr AFS fast voll ist, siehe Troubleshooting-Schritte für Alternativen.

#### Color Theme auswählen:

Nach der Installation werden Sie aufgefordert, ein Farbthema zu wählen:

- **c0-light**: Helles Theme (für helle Editor-Themes)
- **c0-dark**: Dunkles Theme (für dunkle Editor-Themes)

**Empfehlung:** Wählen Sie das Theme, das zu Ihrem Editor passt (dunkler Editor → c0-dark, heller Editor → c0-light).

#### Nächste Schritte (Setup Lab):

Wenn Sie dem Setup Lab folgen:

1. Bearbeiten Sie die Dateien `factorial.c0` und `favorite_number.c0` wie im Handout beschrieben
2. Speichern Sie Ihre Änderungen mit `Ctrl+S` (Windows) oder `Cmd+S` (Mac)
3. Fahren Sie nach Abschluss der Bearbeitungen mit dem Abschnitt "Running a C0 Program" fort

---

## 4. Troubleshooting

### 4.1 Erste Schritte

Wenn Ihre SFTP Extension Probleme beim Verbinden hat, versuchen Sie Folgendes:

1. **VSCode neu starten**
2. **SFTP Extension neu installieren**
3. **Internetverbindung überprüfen** (Stabilität)

### 4.2 Unix Server wechseln

Wenn die obigen Schritte das Problem nicht beheben:

1. Versuchen Sie, sich über andere Mittel zu verbinden (Terminal, MobaXTerm)
2. Wenn das Problem hier weiterhin besteht, gibt es wahrscheinlich ein größeres Problem mit den Unix-Servern
3. Dies kann oft durch SSH-Verbindung zu einem anderen Unix-Server umgangen werden:

```bash
ssh [ANDREW_ID]@unix1.andrew.cmu.edu
ssh [ANDREW_ID]@unix2.andrew.cmu.edu
# ... weitere Server
```

**Wenn ein Server funktioniert:**

1. Ändern Sie den SFTP-Host in der "sftp.json"-Datei auf den funktionierenden Server
2. Beispiel: `"host": "unix1.andrew.cmu.edu"`

**Wenn weiterhin Probleme auftreten:** Kontaktieren Sie Computing Services.

### 4.3 Sync-Fehler

Wenn Ihre SFTP Extension Sync-Fehler anzeigt:

**Diagnoseschritte:**

1. SSH in AFS über andere Mittel
2. Überprüfen Sie, ob Ihr neuester Fortschritt dort ist
3. Machen Sie eine Änderung in Ihrer lokalen Datei
4. Prüfen Sie, ob der Fortschritt in AFS widergespiegelt wird

**Wenn es korrekt zu funktionieren scheint:**

- Sie können die Fehler ignorieren und weiterarbeiten

**Wenn Ihr Fortschritt nicht gespeichert wird:**

1. Erstellen Sie einen neuen Ordner auf Ihrem lokalen Computer
2. Befolgen Sie die obigen Schritte erneut

---

## 5. VSCode zur Bearbeitung von C0-Programmen verwenden

### Syntax Highlighting und Color Themes

**Syntax Highlighting** ist die einfachste Möglichkeit, Änderungen zu sehen.

- Die bereitgestellten Color Themes sind auf C0-spezifische Syntax angepasst
- Sie können auch andere Color Themes verwenden, die Ihren Präferenzen entsprechen
- Themes können in der Datei `settings.json` bearbeitet werden

**Vorteile:**

- Bessere Lesbarkeit des Codes
- Schnellere Identifikation von Code-Elementen
- Fehler werden leichter erkannt

---

### Auto-Completion

Beim Tippen von Code erhalten Sie automatisch generierte Auto-Completion-Vorschläge.

**Features:**

- Angepasst mit C0-Bibliotheksfunktionen
- Berücksichtigt benutzerdefinierte Funktionen und Variablen
- Kontextbewusste Vorschläge

**Verwendung:**

- **`Ctrl + Space`**: Zeigt eine Liste vorgeschlagener Variablen und Funktionen, die aktuell im Scope sind

**Vorteile:**

- Schnelleres Codieren
- Weniger Tippfehler
- Entdeckung verfügbarer Funktionen

---

### Hovering (Schwebende Informationen)

Hovern über Elementen zeigt detaillierte Informationen.

**Funktions-Hovering:**

- Zeigt die Funktionsspezifikation
- Anzeige von Parametern und Rückgabewerten
- Dokumentation der Funktion

**Variablen-Hovering:**

- Zeigt den Typ der Variable
- Informationen über Deklaration
- Scope-Informationen

**Vorteile:**

- Schneller Zugriff auf Dokumentation
- Keine Notwendigkeit, zu Deklarationen zu navigieren
- Besseres Verständnis des Codes

---

### Go-To (Navigation zu Deklarationen)

Sie können mehr Informationen über eine Funktion oder Variable erhalten und zu ihrer Deklaration springen.

**Verwendung:**

1. Halten Sie **`Ctrl`** (Windows) oder **`Cmd`** (Mac) gedrückt, während Sie hovern
2. Klicken Sie auf die Funktion/Variable
3. Sie werden zur Stelle gebracht, wo die Funktion/Variable deklariert wurde

**Vorteile:**

- Schnelle Navigation im Code
- Verständnis von Funktionsimplementierungen
- Effizientes Code-Review

---

### Signature Hints (Signatur-Hinweise)

Signature Hints zeigen Namen und Typen einer Funktion sowie den aktiven Parameter.

**Features:**

- Anzeige aller Funktionsparameter
- Hervorhebung des aktuellen Parameters
- Typ-Informationen für jeden Parameter
- Rückgabetyp der Funktion

**Wann erscheinen sie:**

- Beim Tippen von Funktionsaufrufen
- Beim Navigieren durch Parameter mit der Tastatur
- Beim Bearbeiten von Funktionsargumenten

**Vorteile:**

- Reduziert Fehler bei Funktionsaufrufen
- Keine Notwendigkeit, Dokumentation nachzuschlagen
- Klarheit über erwartete Parameter-Typen

---

## Zusammenfassung für KI-Assistenten

### Kernkonzepte:

1. **VSCode Setup**: Download und Installation von code.visualstudio.com
2. **SFTP-Workflow**: Remote-Entwicklung mit automatischer Synchronisation
3. **C0 Extension**: Spezielle Language Support für C0-Programmierung
4. **Auto-Completion**: Intelligente Code-Vorschläge
5. **Hovering & Navigation**: Schneller Zugriff auf Informationen und Deklarationen

### Wichtige Befehle:

- **Command Palette öffnen:** `Ctrl+Shift+P` (Windows) / `Cmd+Shift+P` (Mac)
- **Auto-Completion:** `Ctrl+Space`
- **Speichern:** `Ctrl+S` (Windows) / `Cmd+S` (Mac)
- **Go-To:** `Ctrl+Click` (Windows) / `Cmd+Click` (Mac)

### Troubleshooting-Reihenfolge:

1. VSCode neu starten
2. Extension neu installieren
3. Internetverbindung prüfen
4. Unix-Server wechseln
5. Computing Services kontaktieren

### SFTP Sync-Operationen:

- **Remote → Local**: Neue Dateien von Server holen
- **Local → Remote**: Lokale Dateien zum Server hochladen
- **Auto-Sync**: Beim Speichern automatisch synchronisieren

---

**Quelle:** CMU 15-122 Course Guide
**Copyright:** © Carnegie Mellon University 2025
**Dokumenttyp:** Setup- und Benutzerhandbuch für VSCode mit C0-Programmierung
