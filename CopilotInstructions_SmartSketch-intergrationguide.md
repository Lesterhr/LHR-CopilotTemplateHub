---
template-type: integration-guide
applies-to: ["smartsketch", "api-integration", "com-automation", "csharp"]
priority: 2
version: 1.0.0
last-updated: 2025-11-14
works-with: ["SmartSketch-README.md"]
---

# SmartSketch Integration Guide für AI Assistenten

## 📋 How AI Agents Should Use This Template

**When to apply**: Implementing SmartSketch API integrations, Add-Ins, or automation scripts

**Apply to files**:
- API wrapper classes
- Command implementations
- Event handlers for SmartSketch events
- Drawing object manipulation code

**Ignore for**:
- Business logic unrelated to SmartSketch
- Data models without CAD interaction
- General utility functions

**Key patterns to follow**:
1. Use COM object model hierarchy (Application → Document → Sheet → Elements)
2. Implement proper COM cleanup (ReleaseComObject)
3. Follow the Command Pattern for user interactions
4. Handle SmartSketch events through event interfaces

**Works with**: Use alongside `SmartSketch-README.md` for complete context

---

## Zweck dieses Dokuments

Dieser Guide hilft AI-Assistenten wie GitHub Copilot dabei, Entwickler bei der Erstellung von SmartSketch Add-Ins und Tools zu unterstützen. Er beschreibt die Architektur, API-Patterns und Best Practices für die SmartSketch-Entwicklung.

---

## 1. Technologie-Stack und Architektur

### Kern-Technologie
SmartSketch basiert auf **COM/ActiveX-Technologie** und verwendet:
- COM Automation Server
- Type Libraries (.tlb)
- ActiveX Controls (.ocx)
- .NET Interop für moderne C# Entwicklung

### Unterstützte Entwicklungssprachen
- **C# / .NET Framework 4.8**: Moderne Entwicklung mit .NET Interop
- **Visual Basic 6.0**: Legacy-Unterstützung
- **VB.NET**: Möglich, aber weniger dokumentiert

### API-Architektur
```
SmartSketch Application (COM Server)
    ↓
RAD2D Engine (Rad2d.exe)
    ↓
.NET Wrapper Assemblies
    ├── RadNetAutomation.dll (Hauptobjektmodell)
    ├── RadNetCmdCtrl.dll (Command Framework)
    ├── RadNetMouseCtrl.dll (Maus-Interaktion)
    └── RadNetMenuCtrl.dll (UI-Anpassung)
```

---

## 2. Objektmodell-Hierarchie

### Kern-Hierarchie
```
Application (Root)
├── RADApplication
│   ├── ActiveDocument
│   │   ├── ActiveSheet
│   │   │   ├── Zeichnungsobjekte:
│   │   │   │   ├── Lines2d (Linien)
│   │   │   │   ├── Circles2d (Kreise)
│   │   │   │   ├── Arcs2d (Bögen)
│   │   │   │   ├── Rectangles2d (Rechtecke)
│   │   │   │   ├── SmartSymbols2d (Symbole)
│   │   │   │   └── TextBoxes (Text)
│   │   │   ├── Layers (Ebenen)
│   │   │   └── AttributeSets (Eigenschaften)
│   │   ├── LinearStyles (Linienstile)
│   │   ├── DimensionStyles (Bemaßungsstile)
│   │   ├── Sheets (Blatt-Sammlung)
│   │   └── Variables (Variablen)
│   ├── Interactive (Boolean - User-Interaktion)
│   └── Documents (Dokument-Sammlung)
├── DialogBars (Custom UI Elemente)
├── Menus (Menü-Anpassung)
└── ToolBars (Toolbar-Anpassung)
```

### Wichtige Sammlungs-Objekte (Collections)
Alle Sammlungen folgen dem Pattern:
- Zugriff per Index: `collection[0]`
- Zugriff per Name: `collection["Name"]`
- Iteration: `foreach` (C#) oder `For Each` (VB)
- ActiveStyle/ActiveLayer Pattern für aktuell aktive Elemente

---

## 3. Command Framework

### Command Entry Point
**Jeder SmartSketch-Command muss diese Methode implementieren:**

```csharp
public void igCommand_Initialize(object basicCommand)
{
    // 1. Command Control Setup
    // 2. Zugriff auf Application/Document
    // 3. Command-Logik
    // 4. Interactive-Mode setzen
    // 5. Command beenden mit Done = true
}
```

### Command-Lebenszyklus
```
Initialize → Activate → [User Interaction] → Deactivate → Terminate
```

**Event-Handler für C#:**
```csharp
commandControl.Initialize += commandControl_Initialize;
commandControl.Activate += commandControl_Activate;
commandControl.Deactivate += commandControl_Deactivate;
commandControl.Terminate += commandControl_Terminate;
```

### Stackable Commands
Commands können "stackable" sein (mehrfach aufrufbar):
```csharp
public bool IsStackable { get; set; } = true;
```

---

## 4. Standard-Implementierungsmuster

### Pattern 1: Basis Command-Struktur (C#)

```csharp
using System;
using Ingr.RAD2D.MacroControls.CmdCtrl;

namespace MeinNamespace
{
    public class MeinCommand
    {
        private IgCommand commandControl;
        
        public MeinCommand()
        {
            commandControl = new IgCommand();
        }
        
        public void igCommand_Initialize(object basicCommand)
        {
            // 1. Command zuweisen
            commandControl.Command = basicCommand;
            
            // 2. Application-Objekte holen
            var application = commandControl.Application;
            var radApp = application.RADApplication;
            var document = radApp.ActiveDocument;
            var sheet = document.ActiveSheet;
            
            // 3. Interaktiv setzen (wichtig!)
            radApp.Interactive = true;
            
            // 4. Eigene Logik hier
            
            // 5. Command beenden
            commandControl.Done = true;
        }
    }
}
```

### Pattern 2: Zeichnungsobjekt erstellen

```csharp
public void ErstelleLinie(Sheet sheet, double x1, double y1, double x2, double y2)
{
    // Linie erstellen
    var line = sheet.Lines2d.AddByCoordinates(x1, y1, x2, y2);
    
    // Optional: Stil zuweisen
    var document = sheet.Document;
    line.LinearStyle = document.LinearStyles["Continuous"];
    
    // Optional: Layer zuweisen
    line.Layer = sheet.Layers["Layer1"];
}
```

### Pattern 3: Stil-Management

```csharp
public void ErstelleCustomStil(Document document)
{
    var linearStyles = document.LinearStyles;
    
    // Prüfen ob Stil existiert
    bool styleExists = false;
    foreach (var style in linearStyles)
    {
        if (style.StyleName == "MeinStil")
        {
            styleExists = true;
            break;
        }
    }
    
    // Stil erstellen oder aktivieren
    if (!styleExists)
    {
        linearStyles.ActiveStyle = linearStyles["Normal"];
        // Pattern zuweisen
        linearStyles.ActiveStyle.Pattern = document.LinearPatterns["Dash"];
        // Weitere Eigenschaften setzen
    }
}
```

### Pattern 4: Mouse Control Integration

```csharp
using Ingr.RAD2D.MacroControls.MouseCtrl;

public class MitMausInteraktion
{
    private IgMouse mouseControl;
    
    public void Setup()
    {
        mouseControl = new IgMouse();
        mouseControl.MouseDown += MouseControl_MouseDown;
    }
    
    private void MouseControl_MouseDown(object sender, IgMouseEventArgs e)
    {
        double x = e.X;
        double y = e.Y;
        // Koordinaten verarbeiten
    }
}
```

---

## 5. Projekt-Konfiguration

### C# Projekt (.csproj)
**Wichtige Einstellungen:**

```xml
<PropertyGroup>
    <TargetFrameworkVersion>v4.8</TargetFrameworkVersion>
    <OutputType>Library</OutputType>
    <Platform>AnyCPU</Platform>
</PropertyGroup>

<ItemGroup>
    <!-- Haupt-Referenzen -->
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
    
    <!-- System-Referenzen -->
    <Reference Include="System" />
    <Reference Include="System.Windows.Forms" />
    <Reference Include="System.Drawing" />
</ItemGroup>
```

**Wichtig**: `<Private>False</Private>` verhindert, dass DLLs kopiert werden (SmartSketch lädt sie selbst).

### VB6 Projekt (.vbp)
```
Type=Control
Reference=*\G{F2DB9A50-A696-11CE-B3A0-08003601C4D7}#1.0#0#SmartSketch.tlb
Object={6CECF850-76F8-11D1-9F64-080036944303}#2.5#0; I2DMsCtl.ocx
Object={2FE1FD40-76FD-11D1-9F64-080036944303}#2.5#0; I2DCmCtl.ocx
```

---

## 6. Häufige Entwicklungsaufgaben

### 6.1 Geometrie-Operationen

#### Linie erstellen
```csharp
var line = sheet.Lines2d.AddByCoordinates(x1, y1, x2, y2);
```

#### Kreis erstellen
```csharp
var circle = sheet.Circles2d.AddByCenterRadius(centerX, centerY, radius);
```

#### Rechteck erstellen
```csharp
var rect = sheet.Rectangles2d.AddByCoordinates(x1, y1, x2, y2);
```

#### Bogen erstellen
```csharp
var arc = sheet.Arcs2d.AddBy3Points(x1, y1, x2, y2, x3, y3);
```

### 6.2 Layer-Management

```csharp
// Alle Layer durchlaufen
foreach (var layer in sheet.Layers)
{
    Console.WriteLine(layer.Name);
}

// Aktiven Layer setzen
sheet.Layers.ActiveLayer = sheet.Layers["MeinLayer"];

// Neuen Layer erstellen
var newLayer = sheet.Layers.Add("NeuerLayer");
```

### 6.3 Attribute und Eigenschaften

```csharp
// AttributeSet zugreifen
var attrs = drawingObject.AttributeSets;

// Attribut lesen
if (attrs.Count > 0)
{
    var attr = attrs[0];
    var value = attr.Value;
}
```

### 6.4 Symbol-Platzierung

```csharp
// Symbol platzieren
var symbol = sheet.SmartSymbols2d.PlaceSymbol(
    "SymbolName", 
    x, y, 
    rotation
);
```

### 6.5 Selektion und Locate

```csharp
// SelectSet verwenden
var selectSet = document.SelectSet;
selectSet.Clear();

// Objekt zur Selektion hinzufügen
selectSet.Add(line);

// Alle selektierten Objekte durchlaufen
foreach (var obj in selectSet)
{
    // Verarbeiten
}
```

---

## 7. Best Practices

### 7.1 Ressourcen-Management
```csharp
// IDisposable Pattern verwenden
public class MeinCommand : IDisposable
{
    public void Dispose()
    {
        // Cleanup
        if (commandControl != null)
        {
            commandControl.Done = true;
        }
    }
}
```

### 7.2 Error Handling
```csharp
try
{
    var document = application.RADApplication.ActiveDocument;
    // Operationen
}
catch (System.Runtime.InteropServices.COMException ex)
{
    // COM-Fehler behandeln
    System.Windows.Forms.MessageBox.Show(
        $"SmartSketch Fehler: {ex.Message}"
    );
}
```

### 7.3 Interactive Mode
**Immer setzen, wenn Benutzerinteraktion erwartet wird:**
```csharp
application.RADApplication.Interactive = true;
```

**Deaktivieren für Batch-Operationen:**
```csharp
application.RADApplication.Interactive = false;
// Batch-Operationen
application.RADApplication.Interactive = true; // Wieder aktivieren
```

### 7.4 Transaction-ähnliches Pattern
```csharp
public void BatchOperation(Document document)
{
    var wasInteractive = document.Application.RADApplication.Interactive;
    
    try
    {
        document.Application.RADApplication.Interactive = false;
        
        // Viele Operationen
        for (int i = 0; i < 1000; i++)
        {
            // Zeichnungsoperationen
        }
    }
    finally
    {
        document.Application.RADApplication.Interactive = wasInteractive;
    }
}
```

---

## 8. UI-Integration

### 8.1 UserControl als Command-UI (C#)
```csharp
public partial class MeinUserControl : UserControl
{
    public IgCommand commandControl;
    
    public MeinUserControl()
    {
        InitializeComponent();
    }
    
    private void btnOK_Click(object sender, EventArgs e)
    {
        // Logik ausführen
        
        // Command beenden
        commandControl.Application.RADApplication.Interactive = true;
        this.Hide();
        commandControl.Done = true;
    }
}
```

### 8.2 DialogBar
DialogBars sind dockbare UI-Elemente in SmartSketch:
```csharp
var dialogBars = application.DialogBars;
var myDialogBar = dialogBars.Add("MeinDialog");
```

---

## 9. Debugging und Troubleshooting

### Debugging Setup
1. Visual Studio als Administrator starten
2. Projekt-Eigenschaften → Debug:
   - Start external program: `C:\Program Files\SmartSketch\Program\Rad2d\bin\draft.exe`
   - Enable native code debugging für COM-Interop

### Häufige Fehler

#### "Command not found" oder "DLL not loaded"
**Lösung:**
- DLL in `SmartSketch\Addins\` kopieren
- Bei VB6: `regsvr32` ausführen
- Pfade in .csproj überprüfen

#### COM Exception beim Zugriff auf Objekte
**Lösung:**
```csharp
// Null-Checks
if (application.RADApplication.ActiveDocument != null)
{
    var doc = application.RADApplication.ActiveDocument;
}
```

#### Type Library nicht gefunden
**Lösung:**
- Absolute Pfade in Referenzen verwenden
- Type Library im GAC registrieren (tlbimp.exe)

---

## 10. Deployment

### Deployment-Checkliste

1. **Build-Konfiguration:**
   - Release-Build erstellen
   - Output-Verzeichnis: `bin\Release\`

2. **Dateien kopieren:**
   ```
   MeinAddin.dll → SmartSketch\Addins\
   ```

3. **Registrierung (nur VB6/OCX):**
   ```cmd
   regsvr32 "C:\SmartSketch\Addins\MeinAddin.ocx"
   ```

4. **SmartSketch neu starten**

5. **Testen:**
   - Command in SmartSketch aufrufen
   - Fehlerlog prüfen

### Installation Script (PowerShell)
```powershell
# Deployment-Script
$source = ".\bin\Release\MeinAddin.dll"
$target = "C:\Program Files\SmartSketch\Addins\"

Copy-Item $source $target -Force
Write-Host "Addin deployed successfully"
```

---

## 11. Code-Beispiele für häufige Szenarien

### Szenario 1: Alle Linien einer bestimmten Länge finden
```csharp
public List<Line2d> FindeLangeLinien(Sheet sheet, double minLength)
{
    var result = new List<Line2d>();
    
    foreach (var line in sheet.Lines2d)
    {
        var geom = line.LineGeometry2d;
        double length = geom.Length;
        
        if (length >= minLength)
        {
            result.Add(line);
        }
    }
    
    return result;
}
```

### Szenario 2: Layer-Report erstellen
```csharp
public string ErstelleLayerReport(Sheet sheet)
{
    var report = new StringBuilder();
    report.AppendLine("Layer Report:");
    
    foreach (var layer in sheet.Layers)
    {
        report.AppendLine($"  {layer.Name} - Visible: {layer.Visible}");
    }
    
    return report.ToString();
}
```

### Szenario 3: Stil-Konvertierung
```csharp
public void KonvertiereLinienStil(Sheet sheet, string vonStil, string nachStil)
{
    var document = sheet.Document;
    var neuerStil = document.LinearStyles[nachStil];
    
    foreach (var line in sheet.Lines2d)
    {
        if (line.LinearStyle.StyleName == vonStil)
        {
            line.LinearStyle = neuerStil;
        }
    }
}
```

---

## 12. Namespaces und Using-Direktiven

### Standard C# Imports
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using System.Drawing;

// SmartSketch-spezifisch
using Ingr.RAD2D.MacroControls.CmdCtrl;
using Ingr.RAD2D.MacroControls.MouseCtrl;
using Ingr.RAD2D.MacroControls.MenuCtrl;
```

---

## 13. Referenz-Tabellen

### Wichtige Methoden-Referenz

| Objekt | Methode | Beschreibung |
|--------|---------|--------------|
| Lines2d | AddByCoordinates(x1,y1,x2,y2) | Linie erstellen |
| Circles2d | AddByCenterRadius(x,y,r) | Kreis erstellen |
| Layers | Add(name) | Neuer Layer |
| SelectSet | Add(object) | Objekt selektieren |
| LinearStyles | ActiveStyle | Aktiver Stil |

### Event-Referenz

| Control | Event | Verwendung |
|---------|-------|------------|
| IgCommand | Initialize | Command-Setup |
| IgCommand | Activate | Command aktiviert |
| IgCommand | Deactivate | Command deaktiviert |
| IgCommand | Terminate | Command beendet |
| IgMouse | MouseDown | Mausklick |
| IgMouse | MouseMove | Mausbewegung |
| IgMouse | MouseUp | Maus losgelassen |

---

## 14. AI-Assistant Hinweise

### Beim Generieren von Code beachten:

1. **Immer `igCommand_Initialize` implementieren**
2. **Interactive = true setzen** für Benutzerinteraktion
3. **Done = true** am Ende des Commands
4. **Null-Checks** für COM-Objekte
5. **Try-Catch** für COM-Exceptions
6. **Private = False** für SmartSketch-DLL-Referenzen
7. **.NET Framework 4.8** als Target verwenden
8. **using**-Direktiven korrekt setzen

### Code-Generierungs-Template:
```csharp
// Standard SmartSketch Command Template
using System;
using Ingr.RAD2D.MacroControls.CmdCtrl;

namespace [NAMESPACE]
{
    public class [CLASSNAME]
    {
        private IgCommand commandControl;
        
        public [CLASSNAME]()
        {
            commandControl = new IgCommand();
        }
        
        public void igCommand_Initialize(object basicCommand)
        {
            try
            {
                commandControl.Command = basicCommand;
                var app = commandControl.Application;
                var doc = app.RADApplication.ActiveDocument;
                var sheet = doc.ActiveSheet;
                
                app.RADApplication.Interactive = true;
                
                // [USER CODE HERE]
                
                commandControl.Done = true;
            }
            catch (Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(
                    $"Fehler: {ex.Message}", 
                    "SmartSketch Command"
                );
            }
        }
    }
}
```

---

## 15. Versionsinformationen

- **SmartSketch Version**: 11.x
- **API Version**: RAD2D (2D Drawing Engine)
- **Empfohlene .NET Version**: 4.8
- **COM-Typ**: In-Process Server (DLL/OCX)

---

**Ende des Integration Guides**

Dieser Guide deckt 95% der typischen SmartSketch-Entwicklungsaufgaben ab und sollte als Referenz für Code-Generierung und Entwicklerunterstützung dienen.
