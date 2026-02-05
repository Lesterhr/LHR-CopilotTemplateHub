# Instruction Files Organizer GUI

Eine grafische Benutzeroberfläche (GUI) zur Organisation von Instruction-Dateien mit Drag-and-Drop-Funktionalität.

## Überblick

Diese Anwendung ermöglicht es Ihnen, Instruction-Dateien zwischen "Verfügbar" und "Archiviert" Kategorien zu organisieren. Dateien können einfach per Drag-and-Drop zwischen den beiden Bereichen verschoben werden.

![Instruction Files Organizer](https://github.com/user-attachments/assets/bab572f4-d219-448f-a94f-c83429025d80)

## Features

- ✨ **Zwei-Spalten-Layout**: Trennung zwischen verfügbaren und archivierten Instruction-Dateien
- 🎯 **Drag-and-Drop**: Intuitive Verschiebung von Dateien zwischen Kategorien
- 🎨 **Modernes Design**: Dunkles Theme mit blauen Akzentfarben (basierend auf flet-styleguide)
- 🔄 **Automatische Dateiverwaltung**: Physisches Verschieben von Dateien zwischen Verzeichnissen
- 📱 **Responsive Layout**: Funktioniert sowohl als Desktop- als auch Web-Anwendung
- 💾 **Persistenz**: Änderungen werden sofort im Dateisystem gespeichert

## Verzeichnisstruktur

```
.github/
├── instructions/                   # Verfügbare Instruction-Dateien
│   ├── flet-agent.instructions.md
│   ├── smartsketch-readme.instructions.md
│   └── ...
└── instructions/archived/          # Archivierte Instruction-Dateien
    └── (archivierte Dateien)
```

## Installation

### Voraussetzungen

- Python 3.8 oder höher
- pip (Python Package Manager)

### Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

Dies installiert:
- `flet>=0.28.3` - GUI Framework

## Verwendung

### Desktop-Anwendung starten

```bash
python instructions_organizer.py
```

Die Anwendung öffnet sich als Desktop-Fenster.

### Web-Browser-Modus

```bash
# Mit spezifischem Port (Standard: 8550)
python instructions_organizer.py --port 8550
```

Dann öffnen Sie `http://localhost:8550` in Ihrem Browser.

## Bedienung

### Dateien verschieben

1. **Von Verfügbar nach Archiviert**:
   - Klicken und halten Sie eine Datei-Karte im "Available Instructions" Bereich
   - Ziehen Sie die Karte zum "Archived Instructions" Bereich
   - Lassen Sie die Maustaste los, um die Datei zu archivieren

2. **Von Archiviert nach Verfügbar**:
   - Klicken und halten Sie eine Datei-Karte im "Archived Instructions" Bereich
   - Ziehen Sie die Karte zum "Available Instructions" Bereich
   - Lassen Sie die Maustaste los, um die Datei wiederherzustellen

### Dateien aktualisieren

- Klicken Sie auf den **"Refresh"** Button unten rechts, um die Dateiliste neu zu laden
- Dies ist nützlich, wenn Dateien außerhalb der Anwendung geändert wurden

### Benachrichtigungen

Die Anwendung zeigt Benachrichtigungen für:
- ✅ Erfolgreiche Dateioperationen (grün)
- ℹ️ Informationen (blau)
- ⚠️ Warnungen (orange)
- ❌ Fehler (rot)

## Design

Die Anwendung folgt dem **Flet Style Guide** (`flet-styleguide.instructions.md`):

- **Farbschema**: Dunkles Theme mit blauen Akzenten
  - Hintergrund: `#1a1d23` (dunkles Anthrazit)
  - Primärfarbe: `#3b82f6` (Blau)
  - Akzente: Grün für Erfolg, Orange für Warnungen, Rot für Fehler

- **Typografie**:
  - Haupttitel: 32px, Fett
  - Abschnittsüberschriften: 20px, Fett
  - Kartentext: 14px

- **Animationen**: Sanfte Übergänge (300ms) für bessere UX

- **Layout**: Responsives zwei-Spalten-Layout mit Gradient-Header

## Dateioperationen

Die Anwendung führt folgende Operationen aus:

- **Archivieren**: Verschiebt Datei von `.github/instructions/` nach `.github/instructions/archived/`
- **Wiederherstellen**: Verschiebt Datei von `.github/instructions/archived/` zurück nach `.github/instructions/`
- **Scannen**: Liest alle `.instructions.md` Dateien aus beiden Verzeichnissen

**Wichtig**: Die Anwendung arbeitet direkt mit dem Dateisystem. Alle Änderungen sind permanent!

## Fehlerbehebung

### Fehler: "Datei nicht gefunden"

Stellen Sie sicher, dass:
- Die Anwendung im Repository-Hauptverzeichnis ausgeführt wird
- Das `.github/instructions/` Verzeichnis existiert
- Sie Leserechte für die Verzeichnisse haben

### Fehler: "Kann Datei nicht verschieben"

Mögliche Ursachen:
- Datei ist bereits geöffnet in einem anderen Programm
- Keine Schreibrechte für Zielverzeichnis
- Datei existiert bereits im Zielverzeichnis

### Anwendung startet nicht

```bash
# Prüfen Sie die Python-Version
python --version  # Sollte >= 3.8 sein

# Prüfen Sie, ob Flet installiert ist
pip list | grep flet

# Neuinstallation bei Bedarf
pip install --upgrade flet
```

## Entwicklung

### Code-Struktur

```python
InstructionFileCard         # Draggable Karte für eine Instruction-Datei
DropZone                    # Drop-Bereich (Available/Archived)
InstructionsOrganizerApp    # Hauptanwendung
```

### Flet Style Guide

Die Anwendung folgt dem Style Guide in:
`.github/instructions/flet-styleguide.instructions.md`

### Anpassungen

Um das Erscheinungsbild anzupassen, bearbeiten Sie die Farbkonstanten in `instructions_organizer.py`:

```python
# Beispiel: Andere Primärfarbe
bgcolor=ft.Colors.PURPLE_600  # Statt BLUE_600
```

## Technische Details

- **Framework**: Flet (Python GUI Framework basierend auf Flutter)
- **Version**: >= 0.28.3
- **Plattform**: Cross-platform (Windows, macOS, Linux, Web)
- **Abhängigkeiten**: Siehe `requirements.txt`

## Lizenz

Dieses Tool ist Teil des LHR-CopilotTemplateHub Repositories.

## Support

Bei Fragen oder Problemen:
1. Überprüfen Sie die Fehlerbehebung oben
2. Erstellen Sie ein Issue im Repository
3. Konsultieren Sie die Flet-Dokumentation: https://flet.dev

---

**Version**: 1.0.0  
**Erstellt**: 2026-02-05  
**Style Guide**: flet-styleguide.instructions.md
