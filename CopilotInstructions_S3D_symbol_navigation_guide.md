# Projekt-Verzeichnisstruktur: S3D Piping and Instrumentation 2014 - DotNet

**Dokumentiert am:** 21. November 2025
**Version:** 1.0
**Technologie-Stack:** .NET Framework, Intergraph Smart 3D (S3D), XML, Excel

## Inhaltsverzeichnis
- [Projekt-Verzeichnisstruktur: S3D Piping and Instrumentation 2014 - DotNet](#projekt-verzeichnisstruktur-s3d-piping-and-instrumentation-2014---dotnet)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Verzeichnisbaum-Übersicht](#verzeichnisbaum-übersicht)
  - [Detaillierte Beschreibung](#detaillierte-beschreibung)
    - [📁 / (Wurzelverzeichnis)](#--wurzelverzeichnis)
    - [📁 /Symbol Data Mapping](#-symbol-data-mapping)
    - [📁 /Xml](#-xml)
    - [📁 /Valves (und ähnliche Komponenten-Ordner)](#-valves-und-ähnliche-komponenten-ordner)
      - [Beispielstruktur einer Komponente](#beispielstruktur-einer-komponente)
    - [📁 /Sample Data](#-sample-data)
    - [📁 /Select Lists](#-select-lists)
    - [📁 /Common Symbol Functions](#-common-symbol-functions)
    - [📁 /Custom Command](#-custom-command)
    - [📁 /Parametric Assemblies](#-parametric-assemblies)

## Verzeichnisbaum-Übersicht

```
/
├── 📁 Accessories/
├── 📁 Branch Fittings/
├── 📁 Common Symbol Functions/
├── 📁 Custom Command/
├── 📁 Direction Change Fittings/
├── 📁 End Fittings/
├── 📁 Fire and Safety/
├── 📁 In-Line Fittings/
├── 📁 Migration Compatible Symbols Utility/
├── 📁 Offline Instruments/
├── 📁 Offline Instruments and Non-Wetted Instruments/
├── 📁 On-the-fly Instruments/
├── 📁 On-the-fly Piping Specialties/
├── 📁 Other specialty components/
├── 📁 Parametric Assemblies/
├── 📁 Port Graphics/
├── 📁 Sample Data/
├── 📁 Select Lists/
├── 📁 SKEY/
├── 📁 Straight sections/
├── 📁 Surface-mounted fittings/
├── 📁 Symbol Data Mapping/
│   └── ⚙️ Symbols Data Mapping - Piping and Instrumentation - DotNet.xlsx
├── 📁 Valves/
│   ├── 📁 2-way valves/
│   │   └── 📁 2-way Divert Sterile Access Valve/
│   │       ├── ⚙️ 2WayDiverterSterileValve.dll
│   │       ├── 🖼️ 2WayDiverterValvePDB9173.gif
│   │       └── 📄 Instruction Document.doc
│   └── ... (weitere Unterkategorien)
└── 📁 Xml/
    ├── ⚙️ DimensionalAttributesforValveSymbolGraphics.xml
    ├── ⚙️ NPDEquivalence.xml
    ├── ⚙️ OutsideDiameterforSymbolGraphics.xml
    ├── ⚙️ Port Graphics.xml
    ├── ⚙️ SPISymbolParameterToInterfaceMap.xml
    ├── ⚙️ SPItoSP3DPortMapping.xml
    └── ⚙️ ThresholdAngleForWeightCalculations.xml
```

## Detaillierte Beschreibung

### 📁 / (Wurzelverzeichnis)
**Zweck:** Hauptverzeichnis für die S3D Piping and Instrumentation Symbol-Bibliothek (.NET Version). Es enthält Kategorien von Rohrleitungskomponenten, Instrumenten, Konfigurationsdateien und Beispieldaten.

### 📁 /Symbol Data Mapping
**Zweck:** Zentraler Einstiegspunkt für die Zuordnung von Symbolen. Diese Excel-Datei ist der **INDEX**, der den Weg von einer PDB-Nummer zu den physischen Symbol-Dateien (DLLs und GIFs) zeigt.

#### ⚙️ Symbols Data Mapping - Piping and Instrumentation - DotNet.xlsx
- **Pfad:** `/Symbol Data Mapping/Symbols Data Mapping - Piping and Instrumentation - DotNet.xlsx`
- **Typ:** Excel Arbeitsmappe (Master-Index für alle Symbole)
- **Zweck:** Definiert die Zuordnung zwischen PDB-Nummern, Symbol-Beschreibungen und den implementierenden .NET-Symbolen.
- **Struktur:** 2471 Zeilen × 5 Spalten

##### Excel-Spaltenstruktur:
| Spalte | Name | Beschreibung |
|--------|------|--------------|
| 1 | **Symbol Folder Name** | Name des Ordners, der die DLL und GIFs enthält (z.B. `Gate Valve`, `Double Wye`) |
| 2 | **DotNet Symbol ProgID** | Programmierbare ID für COM-Interop (z.B. `GateValve,Ingr.SP3D.Content.Piping.GateValve`) |
| 3 | **PDB** | PDB-Nummer (Piping Data Block), eindeutige ID für jede Symbol-Variante (z.B. `2142`, `2431`) |
| 4 | **PDB Description** | Textuelle Beschreibung des Symbols (z.B. `Gate valve, PIV, Type 1, face-to-face`) |
| 5 | **DotNet Data Workbook** | Verweis auf die zugehörige Katalogdatei (PartClass Name) |

##### Wichtige Erkenntnisse für AI-Agents:

**1. Symbol Folder Name Logik:**
- Die Spalte "Symbol Folder Name" ist **NICHT in jeder Zeile gefüllt**
- Der Ordnername steht nur in der **ersten Zeile** einer Symbol-Gruppe
- Alle folgenden Zeilen mit leerer Spalte 1 gehören zum **letzten nicht-leeren** Ordnernamen
- **Algorithmus:** Suche rückwärts bis zur ersten nicht-leeren Zeile in Spalte 1

**2. Navigation von PDB zu physischen Dateien:**

**Beispiel 1: Gate Valve (PDB 2142)**
```
Excel-Eintrag:
  Zeile 2: Symbol Folder Name = "Gate Valve"
           ProgID = "GateValve,Ingr.SP3D.Content.Piping.GateValve"
           PDB = "2142"
           Description = "Gate valve, PIV, Type 1, face-to-face"

Physischer Pfad:
  \Valves\Linear Valves\Gate Valve\
    ├── GateValve.dll                    ← Die Symbol-Implementation
    ├── SP3DGateValvePDB2142.gif        ← Grafik für PDB 2142
    ├── SP3DGateValvePDB2157.gif        ← Weitere Varianten
    └── Gate Valves.xls                 ← Lokale Katalogdaten
```

**Beispiel 2: Double Wye (PDB 2431)**
```
Excel-Eintrag:
  Zeile 1922: Symbol Folder Name = "Double Wye"
              PDB = "525"
  Zeile 1932: Symbol Folder Name = ""    ← Leer! Gehört zu "Double Wye"
              PDB = "2431"
              Description = "Wye, double with side opening, Type 1"

Physischer Pfad:
  \Branch Fittings\Double Wyes\Double Wye\
    ├── DoubleWye.dll                    ← Eine DLL für alle Varianten
    ├── SP3DDoubleYPDB525.gif           ← Grafik für PDB 525
    ├── SP3DDoubleYPDB2431.gif          ← Grafik für PDB 2431
    └── SP3DDoubleYPDB3500.gif          ← Weitere Varianten
```

**Beispiel 3: Electromagnetic Flowmeter (PDB 2800)**
```
Excel-Eintrag:
  Symbol Folder Name = "Electromagnetic Flowmeters"
  PDB = "2800"
  Description = "Electromagnetic flowmeter, Type 8"

Physischer Pfad:
  \In-Line Fittings\In-line instruments flow measurement\Electromagnetic Flowmeters\
    ├── ElectroMagneticFlowMeter.dll
    ├── ElectroMagneticFM2800.gif       ← Namenskonvention: ElectroMagneticFM{PDB}.gif
    └── Electromagnetic Flowmeters.xls
```

**3. Namenskonventionen für Dateien:**

**DLL-Dateien:**
- **Pattern:** `{SymbolName}.dll` (CamelCase, keine Leerzeichen)
- **Beispiele:**
  - `GateValve.dll`
  - `DoubleWye.dll`
  - `ElectroMagneticFlowMeter.dll`
  - `DoubleBasketStrainer.dll`

**GIF-Dateien:**
- **Pattern:** `{Prefix}{SymbolName}PDB{PDBNumber}.gif`
- **Prefixes:**
  - `SP3D...` für die meisten Komponenten
  - `ElectroMagneticFM...` für Flowmeter
  - Kein Prefix bei manchen Spezialfällen
- **Beispiele:**
  - `SP3DGateValvePDB2142.gif`
  - `SP3DDoubleYPDB2431.gif`
  - `ElectroMagneticFM2800.gif`
  - `SP3DDoubleBasketStrainerPDB1000.gif`

**4. Suchstrategie für AI-Agents:**

```
SCHRITT 1: PDB-Nummer in Excel finden
  → Öffne "Symbols Data Mapping - Piping and Instrumentation - DotNet.xlsx"
  → Tabellenblatt "Piping and Instrumentation"
  → Suche in Spalte 3 (PDB) nach der Ziel-PDB

SCHRITT 2: Symbol Folder Name ermitteln
  → Prüfe Spalte 1 (Symbol Folder Name) in der gefundenen Zeile
  → Falls leer: Suche RÜCKWÄRTS bis zur ersten nicht-leeren Zeile
  → Dieser Wert ist der Ordnername

SCHRITT 3: Ordner im Dateisystem suchen
  → Suche rekursiv nach Ordnern mit diesem Namen
  → Pattern: **/{SymbolFolderName}/
  → Beispiel: **/Gate Valve/ findet \Valves\Linear Valves\Gate Valve\

SCHRITT 4: Dateien identifizieren
  → DLL: Meist nur eine DLL pro Ordner
  → GIF: Dateiname enthält "PDB{Nummer}"
  → Beispiel: Für PDB 2431 suche nach *PDB2431.gif
```

**5. Getestete Beispiele (verifiziert):**

| PDB | Symbol Folder Name | Pfad | DLL | GIF |
|-----|-------------------|------|-----|-----|
| 2142 | Gate Valve | `\Valves\Linear Valves\Gate Valve\` | `GateValve.dll` | `SP3DGateValvePDB2142.gif` |
| 2431 | Double Wye | `\Branch Fittings\Double Wyes\Double Wye\` | `DoubleWye.dll` | `SP3DDoubleYPDB2431.gif` |
| 2800 | Electromagnetic Flowmeters | `\In-Line Fittings\In-line instruments flow measurement\Electromagnetic Flowmeters\` | `ElectroMagneticFlowMeter.dll` | `ElectroMagneticFM2800.gif` |
| 1000 | Double Basket Strainer | `\Other specialty components\Strainers\Double Basket Strainer\` | `DoubleBasketStrainer.dll` | `SP3DDoubleBasketStrainerPDB1000.gif` |
| 3500 | Double Wye | `\Branch Fittings\Double Wyes\Double Wye\` | `DoubleWye.dll` | `SP3DDoubleYPDB3500.gif` |

**6. Weitere Tabellenblätter:**
- `On-the-fly Piping Specialities`
- `On-the-fly Instruments`
- `Legacy SPI DDPs`
- `Merged SPI DDPs`

---

#### Navigation von PDB zu Data Workbook und Partsheet

**Spalte 5 (DotNet Data Workbook) Struktur:**
- Enthält relative Pfade zu Excel-Workbooks mit Katalogdaten
- Format: `Pfad\Dateiname.xls - (PartSheetName1, PartSheetName2, ...)`
- Kann **mehrere Workbooks** für eine PDB enthalten (durch Komma getrennt)

**Zwei Speicherorte für Data Workbooks:**

**A) Zentral im `/Sample Data/` Ordner:**
- Sammelt Katalogdaten für mehrere Symbol-Typen
- Typische Dateien: `Sample Data for On-the-fly Instruments.xls`, `No-Hub and Hub-Spigot Fittings.xls`
- Vorteil: Konsolidierte Datenhaltung für verwandte Komponenten

**B) Lokal im Symbol-Ordner:**
- Liegt direkt neben der DLL und den GIF-Dateien
- Beispiel: `Electromagnetic Flowmeters.xls` im Ordner `\In-Line Fittings\In-line instruments flow measurement\Electromagnetic Flowmeters\`
- Vorteil: Alle Dateien eines Symbols an einem Ort

**Partsheet Namenskonvention:**
- **Pattern:** `{SymbolPrefix}PDB{PDBNumber}`
- **Präfixe:**
  - Standard: Name des Symbols in CamelCase (z.B. `EMagFlowMeterPDB2800`)
  - Mit Namespace: `CI` = Custom Instrument (z.B. `CIGateValvePDB2142`)
  - Verkürzt: `DoubleBStrainerPDB1000` (statt `DoubleBasketStrainer`)
  - Generisch: `GateValveOF1` (ohne PDB, für "On-the-fly" Varianten)

**Partsheet Struktur (standardisiert):**
```
Zeile 1:  ! Back to Index              ← Navigation zurück zum Index-Sheet
Zeile 2:  Definition | PartClassType | SymbolDefinition | UserClassName | OccClassName
Zeile 3:  [Leer]
Zeile 4:  Daten      | SpecialtyClass | DoubleBasketStrainer | Double Basket... | Double Basket...
Zeile 5:  [Leer]
Zeile 6:  CommodityPart                ← Beginn der Teildaten
Zeile 7:  Head | IndustryCommodityCode | CommodityType | GeometryType | GraphicalRepresentation
Zeile 8:  Start
Zeile 9+: [Teile-Daten]               ← Eigentliche Katalogeinträge
```

**Wichtige Felder im Partsheet:**
- **PartClassType:** `InstrumentsClass`, `SpecialtyClass`, etc.
- **SymbolDefinition:** Referenz zur DLL (z.B. `ElectroMagneticFlowMeter`)
- **IndustryCommodityCode:** Eindeutiger Code für das Teil (z.B. `IVPZZCNZZAASZZZZUS`)
- **CommodityType:** Numerischer Typ-Code (z.B. `1514`, `8420`)
- **GeometryType:** Grafik-Typ ID (z.B. `15`, `500`)

**Getestete Beispiele (verifiziert):**

| PDB | Symbol Folder | Data Workbook Speicherort | Workbook Datei | Partsheet Name | Sheets Total |
|-----|--------------|---------------------------|----------------|----------------|--------------|
| 2142 | Gate Valve | `/Sample Data/` (zentral) | `Sample Data for On-the-fly Instruments.xls` | `CIGateValvePDB2142` | 119 |
| 2431 | Double Wye | `/Sample Data/` (zentral) | `No-Hub and Hub-Spigot Fittings.xls` | `DoubleYPDB2431` | 86 |
| 2800 | Electromagnetic Flowmeters | Symbol-Ordner (lokal) | `Electromagnetic Flowmeters.xls` | `EMagFlowMeterPDB2800` | 73 |
| 1000 | Double Basket Strainer | Symbol-Ordner (lokal) | `Sample Data for Double Basket Strainers.xls` | `DoubleBStrainerPDB1000` | 15 |
| 3500 | Double Wye | `/Sample Data/` (zentral) | `Marine Drainage System fittings.xls` | `DoubleWyePDB3500` | 15+ |

**Spezialfall: Mehrere Workbooks für eine PDB:**
```
PDB 2142 (Gate Valve) erscheint in 3 Workbooks:
1. Sample Data for On-the-fly Instruments.xls
   → Partsheets: CIGateValvePDB2142, GateValveOF1
2. Sample Data for On-the-fly Specialties.xls
   → Partsheets: GateValveOFS1, GateValveOFS2, GateValveOFS3
3. Wellhead Piping Sample Data.xls
   → Partsheet: GateValvePDB2142

Grund: Verschiedene Anwendungskontexte (Instrumentation, Specialties, Wellhead)
```

**Suchstrategie für Data Workbook (erweitert):**

```
SCHRITT 1: Excel Mapping-Datei öffnen
  → Öffne "Symbols Data Mapping - Piping and Instrumentation - DotNet.xlsx"
  → Suche PDB in Spalte 3

SCHRITT 2: Data Workbook Pfad extrahieren
  → Lese Spalte 5 (DotNet Data Workbook)
  → Parse Format: "Pfad\Datei.xls - (SheetName1, SheetName2)"
  → Extrahiere Dateiname und Partsheet-Namen

SCHRITT 3: Workbook lokalisieren
  FALL A - Absoluter Pfad enthält "Sample Data\":
    → Suche in: {Wurzel}\Sample Data\{Dateiname}
    → Beispiel: "Piping and Instrumentation - DotNet\Sample Data\No-Hub..."
    → Voller Pfad: C:\...\Piping and Instrumentation 2014 - DotNet\Sample Data\No-Hub and Hub-Spigot Fittings.xls
  
  FALL B - Pfad enthält Symbol-Kategorie:
    → Suche in: {Wurzel}\{Kategorie}\{Unterkategorie}\{Symbol}\{Dateiname}
    → Beispiel: "...In-Line Fittings\...\Electromagnetic Flowmeters\Electromagnetic Flowmeters.xls"
    → Verwende rekursive Suche mit Dateinamen

SCHRITT 4: Partsheet öffnen
  → Öffne Workbook
  → Suche Sheet mit Namen aus Spalte 5 (in Klammern angegeben)
  → Falls mehrere Sheets: Wähle denjenigen mit PDB-Nummer im Namen
  → Pattern: *PDB{Nummer}* hat Vorrang vor generischen Namen
```

**Fehlerbehandlung für AI-Agents:**

1. **Workbook nicht gefunden:**
   - Prüfe beide Speicherorte (zentral + lokal)
   - Verwende Dateisuche: `**/{Dateiname}.xls`
   - Ignoriere Versionssuffixe in Dateinamen

2. **Partsheet nicht gefunden:**
   - Suche nach Sheet mit PDB-Nummer: `*{PDB}*`
   - Prüfe alternative Namensschreibweisen
   - Prüfe "Index" Sheet für Verweise

3. **Mehrere Workbooks:**
   - Spalte 5 enthält mehrere Einträge (durch Komma getrennt)
   - Alle Workbooks sind gültig für unterschiedliche Anwendungsfälle
   - Verwende das erste Workbook als Standard

**Zusammenfassung der vollständigen Navigationskette:**

```
PDB 2800 → Komplette Navigation:

1. Symbols Data Mapping Excel → PDB 2800 finden
2. Spalte 1 → "Electromagnetic Flowmeters" (Symbol Folder Name)
3. Spalte 5 → "...\Electromagnetic Flowmeters\Electromagnetic Flowmeters.xls - (EMagFlowMeterPDB2800)"
4. Dateisystem → \In-Line Fittings\In-line instruments flow measurement\Electromagnetic Flowmeters\
5. Dateien:
   ├── ElectroMagneticFlowMeter.dll        ← Symbol-Code
   ├── ElectroMagneticFM2800.gif           ← Grafik
   └── Electromagnetic Flowmeters.xls      ← Katalogdaten
       └── Sheet: EMagFlowMeterPDB2800     ← Partsheet mit Teildefinitionen
```

### 📁 /Xml
**Zweck:** Enthält XML-Konfigurationsdateien für globale Einstellungen, Grafiken und Mappings.

#### ⚙️ DimensionalAttributesforValveSymbolGraphics.xml
- **Pfad:** `/Xml/DimensionalAttributesforValveSymbolGraphics.xml`
- **Typ:** XML Konfiguration
- **Zweck:** Definition von Dimensionsattributen für die grafische Darstellung von Ventilen.

#### ⚙️ Port Graphics.xml
- **Pfad:** `/Xml/Port Graphics.xml`
- **Typ:** XML Konfiguration
- **Zweck:** Definition der grafischen Darstellung von Anschlüssen (Ports).

#### ⚙️ SPItoSP3DPortMapping.xml
- **Pfad:** `/Xml/SPItoSP3DPortMapping.xml`
- **Typ:** XML Konfiguration
- **Zweck:** Mapping von SmartPlant Instrumentation (SPI) Ports zu Smart 3D (SP3D) Ports.

### 📁 /Valves (und ähnliche Komponenten-Ordner)
**Zweck:** Enthält die eigentlichen Symbol-Implementierungen für Ventile. Andere Ordner wie `Accessories`, `In-Line Fittings` folgen demselben Muster.
**Struktur:** `Kategorie` -> `Unterkategorie` -> `Symbol-Ordner`

#### Beispielstruktur einer Komponente
**Pfad:** `/Valves/2-way valves/2-way Divert Sterile Access Valve/`

##### ⚙️ 2WayDiverterSterileValve.dll
- **Typ:** .NET Assembly (DLL)
- **Zweck:** Enthält den kompilierten Code (C# oder VB.NET) für das Symbol. Implementiert die Logik für die grafische Erstellung und das Verhalten des Bauteils in S3D.
- **Abhängigkeiten:** S3D Core Libraries.

##### 🖼️ *.gif (z.B. 2WayDiverterValvePDB9173.gif)
- **Typ:** Bilddatei (GIF)
- **Zweck:** Vorschaubild oder Icon für das Symbol im Katalog oder in der Auswahlmaske.

##### 📄 Instruction Document.doc
- **Typ:** Word Dokument
- **Zweck:** Dokumentation und Anleitung für das spezifische Symbol.

### 📁 /Sample Data
**Zweck:** Enthält Excel-Dateien (`.xls`, `.xlsx`), die als "Template Sheets" oder Katalogdaten dienen.
**Zusammenhang:** Diese Dateien werden oft verwendet, um die Datenbank (Catalog) mit Teilen zu befüllen, die dann die Symbole (aus den DLLs) verwenden.

#### 📄 *.xls / *.xlsx (z.B. Piping Catalog.xls)
- **Typ:** Excel Katalog-Daten
- **Zweck:** Definition von Teilen (Parts), Spezifikationen und deren Attributen.
- **Abhängigkeiten:** Verweisen auf Symbole (ProgIDs), die in den DLLs definiert sind.

### 📁 /Select Lists
**Zweck:** Enthält Auswahllisten (Codelists) für Attribute.

#### 📄 Sample Codelists.xls
- **Pfad:** `/Select Lists/Sample Codelists.xls`
- **Typ:** Excel Datei
- **Zweck:** Definiert gültige Werte für verschiedene Attribute in S3D.

### 📁 /Common Symbol Functions
**Zweck:** Enthält Hilfefunktionen und Dokumentation, die von mehreren Symbolen gemeinsam genutzt werden.
- **Dateien:** `.chm` (Hilfedateien).

### 📁 /Custom Command
**Zweck:** Enthält benutzerdefinierte Befehle oder Assemblies für spezielle Aufgaben (z.B. `Piping Assembly of a Butterfly Valve`).

### 📁 /Parametric Assemblies
**Zweck:** Enthält parametrische Baugruppen (Assemblies), die aus mehreren Symbolen oder Komponenten bestehen können.
