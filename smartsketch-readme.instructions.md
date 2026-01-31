---
template-type: project-context
applies-to: ["smartsketch", "intergraph", "cad", "com-automation"]
priority: 1
version: 1.0.0
last-updated: 2025-11-14
---

# SmartSketch Entwickler-Dokumentation

## 📋 How AI Agents Should Use This Template

**When to apply**: Working on SmartSketch-related projects or COM automation

**Apply to files**:
- SmartSketch Add-In projects
- COM/ActiveX integration code
- C# projects referencing `RadNetAutomation.dll`
- VB6/VB.NET SmartSketch automation

**Ignore for**:
- Generic CAD operations not specific to SmartSketch
- Pure .NET projects without COM interop
- Web-based CAD viewers

**Key patterns to follow**:
1. SmartSketch uses COM/ActiveX technology stack
2. Reference libraries in `SmartSketch\Program\Rad2d\bin\`
3. Use RAD2D object model hierarchy
4. Handle COM interop properly (Marshal.ReleaseComObject)

---

## Übersicht

Dieses Repository enthält die Programmierressourcen für Intergraph SmartSketch, einschließlich Beispiele, Bibliotheken und Dokumentation zur Entwicklung von Add-Ins und Tools, die mit SmartSketch interagieren.

## Voraussetzungen

### Software-Anforderungen

- **SmartSketch Installation**: Eine vollständige Installation von Intergraph SmartSketch
- **Intergraph Smart Licensing**: Lizenzierungssystem muss installiert und konfiguriert sein
- **Entwicklungsumgebung**:
  - Für C#: Visual Studio 2012 oder höher
  - Für VB: Visual Basic 6.0 oder Visual Studio mit VB.NET
  - .NET Framework 4.8 oder höher (für C# Projekte)

### Erforderliche Bibliotheken

Die SmartSketch API basiert auf COM/ActiveX-Technologie. Folgende Hauptbibliotheken werden benötigt:

- **smartsketch.tlb** - Type Library für SmartSketch Objektmodell
- **RadNetAutomation.dll** - RAD2D Automatisierungs-API
- **RadNetCmdCtrl.dll** - Command Control API
- **RadNetMouseCtrl.dll** - Mouse Control API
- **RadNetMenuCtrl.dll** - Menu Control API

Diese befinden sich im Verzeichnis: `SmartSketch\Program\Rad2d\bin\`

## Projekt-Struktur

```
SmartSketch/
├── C# Examples/              # C# Beispielprojekte
│   ├── Centerlines_Matchlines/  # Beispiel für Linien-Befehle
│   ├── DialogBar/            # DialogBar Beispiele
│   └── Dialogs/              # Dialog Beispiele
├── VB Examples/              # Visual Basic Beispiele
│   ├── ActXCom/              # ActiveX COM Beispiele
│   ├── ActXDLL/              # ActiveX DLL Beispiele
│   └── FUNCTIONS.bas         # Hilfsfunktionen
├── Program/
│   └── Rad2d/bin/            # API-Bibliotheken (.dll, .ocx)
├── Programming Help/         # Dokumentationsdateien (.chm, .cab)
├── Schema Files/             # XML Schema Definitionen
├── Symbols/                  # Symbol-Bibliotheken
└── Template/                 # Vorlagen (.igr Dateien)
```

## Erste Schritte

### 1. Projekt-Setup für C#

1. **Neues C# Projekt erstellen**:
   - Visual Studio starten
   - Neues Projekt: Class Library (.NET Framework)
   - Target Framework: .NET Framework 4.8

2. **Referenzen hinzufügen**:
   ```xml
   <Reference Include="RadNetAutomation">
       <HintPath>..\..\Program\Rad2d\bin\RadNetAutomation.dll</HintPath>
       <Private>False</Private>
   </Reference>
   <Reference Include="RadNetCmdCtrl">
       <HintPath>..\..\Program\Rad2d\bin\RadNetCmdCtrl.dll</HintPath>
       <Private>False</Private>
   </Reference>
   <Reference Include="RadNetMouseCtrl">
       <HintPath>..\..\Program\Rad2d\bin\RadNetMouseCtrl.dll</HintPath>
       <Private>False</Private>
   </Reference>
   ```

3. **Command-Klasse implementieren**:
   ```csharp
   using Ingr.RAD2D.MacroControls.CmdCtrl;
   
   public class MeinCommand
   {
       public void igCommand_Initialize(object basicCommand)
       {
           // Initialisierungslogik
       }
   }
   ```

### 2. Projekt-Setup für VB6

1. **Neues ActiveX DLL/OCX Projekt erstellen**
2. **Referenzen hinzufügen**:
   - SmartSketch.tlb
   - I2DCmCtl.ocx
   - I2DMsCtl.ocx

3. **Type Library referenzieren**:
   ```vb
   Reference=*\G{F2DB9A50-A696-11CE-B3A0-08003601C4D7}#1.0#0#SmartSketch.tlb
   ```

### 3. Build und Deployment

#### C# Projekt:
```
1. Projekt kompilieren → DLL wird erstellt
2. DLL in SmartSketch\Addins\ Ordner kopieren
3. SmartSketch neu starten
```

#### VB6 Projekt:
```
1. Projekt kompilieren → OCX/DLL wird erstellt
2. OCX/DLL registrieren: regsvr32 MeinCommand.ocx
3. Datei in SmartSketch\Addins\ kopieren
4. SmartSketch neu starten
```

## SmartSketch Objektmodell

### Haupt-Objekte

- **Application**: Einstiegspunkt zur Applikation
- **Document**: Repräsentiert ein SmartSketch-Dokument
- **Sheet**: Einzelnes Zeichnungsblatt
- **DrawingObjects**: Sammlung von Zeichnungsobjekten (Linien, Kreise, etc.)
- **LinearStyles**: Linienformate und -stile
- **Layers**: Ebenen-Management

### Wichtige Objekthierarchie

```
Application
└── RADApplication
    └── ActiveDocument (Document)
        └── ActiveSheet (Sheet)
            ├── Lines2d
            ├── Circles2d
            ├── Arcs2d
            ├── SmartSymbols2d
            └── Layers
```

## Beispiel: Einfacher Command

### C# Beispiel

```csharp
using System;
using Ingr.RAD2D.MacroControls.CmdCtrl;

namespace MeinAddin
{
    public class BeispielCommand
    {
        private IgCommand commandControl;
        
        public void igCommand_Initialize(object basicCommand)
        {
            commandControl = new IgCommand();
            commandControl.Command = basicCommand;
            
            // Zugriff auf die Applikation
            var application = commandControl.Application;
            var radApp = application.RADApplication;
            var document = radApp.ActiveDocument;
            var sheet = document.ActiveSheet;
            
            // Interaktivität aktivieren
            radApp.Interactive = true;
            
            // Hier eigene Logik implementieren
            
            // Command beenden
            commandControl.Done = true;
        }
    }
}
```

### VB6 Beispiel

```vb
Option Explicit

Public Sub Main()
    ' Entry point für VB6 DLL
End Sub

Public Function igCommand_Initialize(basicCommand As Object)
    Dim app As Application
    Dim doc As Document
    Dim sheet As Sheet
    
    Set app = basicCommand.Application
    Set doc = app.RADApplication.ActiveDocument
    Set sheet = doc.ActiveSheet
    
    app.RADApplication.Interactive = True
    
    ' Eigene Logik hier
    
    basicCommand.Done = True
End Function
```

## Ressourcen

### Dokumentation

- **Programming Help Ordner**: Enthält CHM-Hilfedateien
  - `SktchPrg.chm` - SmartSketch Programmier-Guide
  - `ICmndCtl.chm` - Command Control Dokumentation
  - `IMseCtl.chm` - Mouse Control Dokumentation
  - `IPMnuCtl.chm` - Menu Control Dokumentation

### Beispiel-Projekte

1. **Centerlines_Matchlines** (C#): Demonstriert Linienstile und Custom Commands
2. **MouseCmd** (VB): Zeigt Mouse Event Handling
3. **EventSpy** (VB): Event-Monitoring Tool
4. **DialogBar** (VB/C#): Custom Dialog Bars erstellen

## Häufige Aufgaben

### Zugriff auf aktives Dokument
```csharp
var doc = application.RADApplication.ActiveDocument;
```

### Linie erstellen
```csharp
var sheet = doc.ActiveSheet;
var line = sheet.Lines2d.AddByCoordinates(x1, y1, x2, y2);
```

### Layer wechseln
```csharp
sheet.Layers.ActiveLayer = sheet.Layers["MeinLayer"];
```

### Linien-Stil ändern
```csharp
var style = doc.LinearStyles["Centerline"];
line.LinearStyle = style;
```

## Troubleshooting

### Problem: DLL wird nicht geladen
- Prüfen Sie, ob alle Abhängigkeiten verfügbar sind
- Bei VB6: Mit `regsvr32` registrieren
- Bei C#: .NET Framework Version prüfen

### Problem: COM-Fehler beim Debugging
- Visual Studio als Administrator ausführen
- COM-Interop Exceptions aktivieren

### Problem: Type Library nicht gefunden
- Pfad zur smartsketch.tlb überprüfen
- Referenzen im Projekt aktualisieren

## Lizenzierung

Die SmartSketch API unterliegt den Intergraph/Hexagon Lizenzbestimmungen. Stellen Sie sicher, dass die Intergraph Smart Licensing Komponente korrekt konfiguriert ist.

## Support und weitere Informationen

- Dokumentation im `Programming Help` Ordner
- Beispielcode im `C# Examples` und `VB Examples` Ordner
- Schema-Definitionen im `Schema Files` Ordner

---

**Copyright**: Intergraph Corporation / Hexagon AB und Tochtergesellschaften
**Version**: SmartSketch 11.x
