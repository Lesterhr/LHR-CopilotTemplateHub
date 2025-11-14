---
template-type: domain-specific
applies-to: ["s3d", "smartplant-3d", "symbol-discovery", "piping"]
priority: 2
version: 1.0.0
last-updated: 2025-11-14
---

# S3D Symbol & Template Discovery Guide

## 📋 How AI Agents Should Use This Template

**When to apply**: Working with SmartPlant 3D (S3D) symbol discovery, template parsing, or piping instrumentation

**Apply to files**:
- Symbol discovery/scanning modules
- Template folder traversal code
- Partsheet Excel parsing
- DLL loading and symbol registration

**Ignore for**:
- Generic file I/O operations
- UI components unrelated to S3D
- Non-S3D CAD integrations

**Key patterns to follow**:
1. Always use recursive directory traversal (`os.walk()`) for symbol discovery
2. Understand 3-4 level hierarchy: Format → Category → Subcategory → Symbol
3. Symbol folders contain: DLL (required) + GIFs (multiple) + docs (optional)
4. Follow the semantic organization (by function, not file type)

---

## Template Folder Structure (Critical for Symbol/Partsheet Discovery)

### Hierarchy Understanding Principles

**General Rule**: S3D template folders organize symbols by **functional category** with 2-4 levels of depth:
- **Level 0**: Format type (VB vs dotNET)
- **Level 1**: Major category (Valves, Instruments, Fittings, etc.)
- **Level 2**: Subcategory (2-way valves, Angle valves, etc.)
- **Level 3**: Individual symbol folder containing DLL + GIFs + docs

**Key Insight**: The hierarchy is **semantic, not technical** - organized by how engineers think about components (function, configuration, mounting style), not by file type.

**Discovery Strategy**: Always use recursive directory traversal (`os.walk()`) because:
1. Category depth varies (some symbols at Level 2, others at Level 3+)
2. Customer templates may have custom category names
3. No guaranteed flat structure exists

### Standard S3D Template Organization
```
Ressources/
├── VB/                                    # Visual Basic symbols (legacy format)
│   ├── SymbolGIF/                         # GIF visual catalog (flat structure)
│   ├── Sample Data/                       # Example partsheet Excel files (flat)
│   └── VB-Symbols Data Mapping - Piping and Instrumentation.xlsx
│
└── dotNET/                                # .NET symbols (modern format)
    ├── SymbolGIF/                         # GIF visual catalog (optional flat copy)
    ├── Sample Data/                       # Example partsheet Excel files (flat)
    ├── Symbol Data Mapping/               # Central mapping file
    │   └── Symbols Data Mapping - Piping and Instrumentation - DotNet.xlsx
    │
    └── [Category Folders]/                # ★ Hierarchical symbol organization ★
        ├── Valves/                        # ← Level 1: Component type
        │   ├── 2-way valves/              # ← Level 2: Configuration
        │   │   └── 2-way Divert Sterile Access Valve/  # ← Level 3: Specific symbol
        │   │       ├── 2WayDiverterSterileValve.dll    # ← Symbol DLL (always here)
        │   │       ├── 2WayDiverterValvePDB9173.gif    # ← Symbol variants (PDB)
        │   │       ├── 2WayDiverterValvePDB9174.gif    # ← One GIF per PartDataBasis
        │   │       ├── Instruction Document.doc        # ← Optional documentation
        │   │       └── Symbols Test Plan.doc           # ← Optional test specs
        │   ├── 3-way Valves/
        │   │   ├── 3-way Globe Valve/
        │   │   └── 3-way Ball Valve/
        │   ├── Angle valves 90o/
        │   └── Axial flow valves/
        │
        ├── In-Line Fittings/              # ← Level 1: Different component type
        │   ├── Caps/
        │   ├── Couplings/
        │   └── Reducers/
        │
        ├── Branch Fittings/
        │   ├── Tees/
        │   ├── Crosses/
        │   └── Laterals/
        │
        ├── Offline Instruments/           # ← Instruments: mounting style categorization
        │   ├── Flow Instruments/
        │   ├── Pressure Instruments/
        │   └── Temperature Instruments/
        │
        └── On-the-fly Instruments/        # ← vs "Offline" (different mounting)
            ├── Flow Transmitters/
            └── Analyzers/
```

### Folder Hierarchy Variations (Customer-Specific)

Different customers/projects may organize symbols differently:

```
# Example 1: Piping-focused template
Ressources/dotNET/
├── Valves/
├── Fittings/
└── Piping Specialties/

# Example 2: Instrumentation-focused template
Ressources/dotNET/
├── Control Valves/
├── Measurement Devices/
├── Actuators/
└── Accessories/

# Example 3: Industry-specific (Pharmaceutical)
Ressources/dotNET/
├── Sanitary Components/
├── Sterile Valves/
└── CIP/SIP Equipment/
```

**Adaptation Rule**: Never hardcode category names. Always discover structure programmatically by walking directories and identifying folders containing `.dll` files.

### Key Discovery Patterns

#### 1. Symbol DLL Location Algorithm
```python
# Pattern: Navigate hierarchical folders by category
base_path = "Ressources/dotNET/{Category}/{Subcategory}/{Symbol Name}/"
dll_file = f"{SymbolName}.dll"

# Example categories in dotNET/:
# - Valves/ (2-way, 3-way, Angle, Axial flow, etc.)
# - In-Line Fittings/
# - Branch Fittings/
# - Offline Instruments/
# - On-the-fly Instruments/
# - Fire and Safety/
# - Parametric Assemblies/
```

#### 2. Partsheet/Bulkload Discovery
```python
# VB partsheets: Flat structure in Sample Data/
vb_partsheets = "Ressources/VB/Sample Data/*.xlsx"

# .NET partsheets: Also in Sample Data/ OR embedded in category folders
dotnet_partsheets = "Ressources/dotNET/Sample Data/*.xlsx"

# Alternative: Search category folders for Excel files
for category_folder in walk("Ressources/dotNET/"):
    partsheets = glob(f"{category_folder}/**/*.xlsx")
```

#### 3. Symbol-to-Template Mapping File (Source of Truth)
```python
# Central mapping database for VB→.NET conversion
mapping_file = "Ressources/dotNET/Symbol Data Mapping/Symbols Data Mapping - Piping and Instrumentation - DotNet.xlsx"

# Contains:
# - Symbol names (ProgID)
# - PartDataBasis (PDB) variations
# - DLL references
# - Property mappings
# - Template partsheet references
```

## Essential File Relationships

### Symbol Identification Pattern
```python
# VB Format: "text.text"
vb_symbol = "SP3DBallValve.CBallValve"

# .NET Format: "text,text.text.text.text" (contains comma)
net_symbol = "BallValve,Ingr.SP3D.Content.Piping.BallValve"

# Detection regex:
vb_pattern = r'^[A-Za-z0-9_]+\.[A-Za-z0-9_]+$'
net_pattern = r'^[^,]+,[^,\.]+\.[^,\.]+'
```

### GIF Catalog Navigation
```python
# Symbol GIFs are named: {SymbolName}PDB{Number}.gif
# Example: "2WayDiverterValvePDB9173.gif"
# Indicates: Symbol="2WayDiverterValve", PartDataBasis=9173

gif_pattern = r'(?P<symbol>.+?)PDB(?P<pdb>\d+)\.gif'
```

### Partsheet Header Detection (Never Assume Row 1!)
```python
def find_partsheet_header(worksheet):
    """Search rows 1-10 for partsheet header pattern"""
    # Required headers (case-insensitive):
    # - Definition
    # - PartClassType
    # - SymbolDefinition
    # - SymbolIcon (optional)
    # - UserClassName / OccClassName (optional)
    
    # Excel cell B4: PartClassType
    # Excel cell C4: SymbolDefinition
    # Excel cell D4: SymbolIcon
```

## Critical Workflows

### Finding All Templates for a Symbol
```python
# 1. Start with symbol name (e.g., "BallValve")
symbol_name = "BallValve"

# 2. Find category folder by searching directory structure
for root, dirs, files in os.walk("Ressources/dotNET/"):
    if f"{symbol_name}.dll" in files:
        symbol_folder = root  # Found it!
        
# 3. Collect all related files:
dll_file = os.path.join(symbol_folder, f"{symbol_name}.dll")
gif_files = glob(os.path.join(symbol_folder, "*.gif"))
doc_files = glob(os.path.join(symbol_folder, "*.doc"))

# 4. Find template partsheet in Sample Data/:
sample_data = "Ressources/dotNET/Sample Data/"
partsheet_candidates = [f for f in os.listdir(sample_data) 
                        if symbol_name.lower() in f.lower()]
```

### Symbol Mapping Priority Hierarchy
```python
# Priority 1: ReplaceSymbol.xlsx (3,317 mapping rows)
replace_symbol = "source/ReplaceSymbol.xlsx"
# Column mapping: VBSymbolDefinition → SymbolDefinition

# Priority 2: Symbols Data Mapping files
vb_mapping = "Ressources/VB/VB-Symbols Data Mapping - Piping and Instrumentation.xlsx"
net_mapping = "Ressources/dotNET/Symbols Data Mapping - Piping and Instrumentation - DotNet.xlsx"

# Priority 3: Similarity matching (30% threshold fallback)
```

### Template Structure for Bulkload Generation
```python
# Master template file (used by Bulkloadsheet Generator)
template_file = "source/Bulkloadsheet generator konzept/BTS_Instruments_Template_LHR.xlsx"

# Template contains:
# - CustomInterface sheets (per symbol type)
# - Property definitions
# - Validation rules (R1-R8)
# - Pre-formatted commodity sheets
```

## Project-Specific Conventions

### Directory Traversal for Symbol Discovery
```python
# Always use os.walk() for hierarchical search
def find_symbol_dll(symbol_name, base_path="Ressources/dotNET/"):
    """Recursively search all subdirectories"""
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.lower() == f"{symbol_name.lower()}.dll":
                return os.path.join(root, file)
    return None
```

### Partsheet Identification Logic
```python
# A valid partsheet MUST have these columns (case-insensitive):
required_columns = {'definition', 'partclasstype', 'symboldefinition'}

# Check rows 1-10 for header (flexible detection):
def is_valid_partsheet(excel_file):
    wb = load_workbook(excel_file)
    for sheet in wb.worksheets:
        header_info = find_partsheet_header(sheet)  # Searches rows 1-10
        if header_info and 'header_row' in header_info:
            return True
    return False
```

### Symbol Category Mapping (Common Patterns)
```
VB Category → .NET Category:
- Valves/* → Valves/{Type}/
- Instruments → Offline Instruments/ OR On-the-fly Instruments/
- Fittings → In-Line Fittings/ OR Branch Fittings/ OR Direction Change Fittings/
- Specialties → On-the-fly Piping Specialties/
- Safety → Fire and Safety/
```

## Tool Integration Points

### Lazy Loading Strategy (optimized_symbol_loader.py)
```python
# Stage 1: Load symbol types only (fast)
symbol_types = get_symbol_types()  # VB vs .NET

# Stage 2: Load GIF catalog for gallery (medium)
gif_catalog = get_gif_catalog(symbol_type)  # File names only

# Stage 3: Load properties AFTER selection (slow, on-demand)
properties = get_symbol_properties(selected_symbol)  # Excel parsing
```

### Symbol Translator Mapping Flow
```python
# Input: VB partsheet
# 1. Detect VB symbol format (text.text)
# 2. Lookup in ReplaceSymbol.xlsx (Symbol + PartDataBasis)
# 3. Find .NET template in Sample Data/
# 4. Transfer commodity data with property formulas
# 5. Output: .NET partsheet with color-coded status tabs
```

## Common Pitfalls

1. **Assuming flat directory structure**: .NET symbols use 2-4 level deep hierarchical folders. Always use `os.walk()` for recursive search, never `os.listdir()` on a single level.

2. **Hardcoding category names**: Customer templates vary significantly. Don't assume "Valves/" exists - discover structure by finding folders containing `.dll` files.

3. **Hardcoding header row**: Partsheet headers can be in rows 1-10. Always search with `find_partsheet_header()`, never assume row 1.

4. **Ignoring PDB variants**: Same symbol can have 10+ PartDataBasis variations (different GIFs like `SymbolPDB9173.gif`, `SymbolPDB9174.gif`). Each PDB is a distinct symbol configuration.

5. **DLL naming inconsistencies**: Folder names use spaces/special chars, DLL filenames use CamelCase:
   - Folder: `"2-way Divert Sterile Access Valve"`
   - DLL: `"2WayDiverterSterileValve.dll"`
   - Always search by `.dll` extension, not folder name matching.

6. **Mixing VB and .NET structures**: VB uses flat `SymbolGIF/` folder with all GIFs. .NET distributes GIFs into symbol-specific folders within category hierarchies.

7. **Missing symbolic links**: Some templates use shortcuts/junctions pointing to shared symbol libraries. Use `os.path.realpath()` to resolve actual paths.

8. **Excel vs DLL mismatch**: Not all symbols have partsheet templates. Some exist only as GIF+DLL (graphics-only), some only in Excel (retired symbols). Always handle missing files gracefully.

## Complete End-to-End Workflow

### Customer Template Reception → Bulkload Sheet Generation

```python
# PHASE 1: Customer provides S3D template folder structure
customer_templates = "path/to/Piping and Instrumentation - DotNet/"
# Contains: Symbol DLLs, GIFs, documentation in hierarchical folders

# PHASE 2: Analyze customer's existing VB partsheets (if migrating)
vb_partsheets = upload_excel_files()  # Via Sheet Analyzer
analysis_result = analyze_partsheets(vb_partsheets)
# Output: S3D_Analysis_Results_{timestamp}.xlsx
# Contains: Symbol definitions, VB vs .NET classification

# PHASE 3: Map VB symbols to .NET equivalents
mapping_input = (analysis_result, symbol_analysis)
mapping_result = map_symbols(mapping_input)  # Via Symbol Mapper
# Output: Symbol_Mapping_Results_{timestamp}.xlsx
# Contains: VB→.NET recommendations with alternatives

# PHASE 4A: Manual transfer (human-assisted)
transfer_report = create_transfer_report(mapping_result, vb_partsheets)
# Output: Symbol_Transfer_Report_{timestamp}.xlsx
# Format: Side-by-side VB sheet | .NET template for copy-paste
# User manually transfers data cell-by-cell

# PHASE 4B: Automated conversion (preferred)
translated_sheets = translate_symbols(transfer_report)  # Via Symbol Translator
# Output: translated-{filename}_{timestamp}.xlsx
# Fully automated VB→.NET conversion with property formulas
# Status tabs: Green (success), Red (failed), Orange (warnings), Blue (summary)

# PHASE 5: Consolidate multiple partsheets (if needed)
merged_output = merge_partsheets(multiple_excel_files)  # Via Partsheet Merger
# Output: Merged_Partsheets_{timestamp}.xlsx
# Features: MD5 deduplication, yellow-highlighted differences

# PHASE 6: Generate new bulkload sheets from scratch
# Via Bulkloadsheet Generator (interactive web UI)
# 1. Browse GIF catalog → Select symbol
# 2. Fill dynamic form (based on symbol's CustomInterface)
# 3. Validate rules (R1-R8)
# 4. Download: Bulkloadsheet_{symbol}_{timestamp}.xlsx
```

### Detailed Workflow Steps

#### Step 1: Extract Symbol Information from Customer Templates
```python
def extract_customer_symbols(template_folder):
    """
    Navigate customer's S3D template folder to catalog available symbols
    """
    symbols_catalog = {}
    
    # Walk entire directory structure
    for root, dirs, files in os.walk(template_folder):
        for file in files:
            if file.endswith('.dll'):
                # Found a symbol DLL
                symbol_name = file.replace('.dll', '')
                symbol_folder = root
                
                # Collect related files
                gif_files = glob(os.path.join(root, '*.gif'))
                doc_files = glob(os.path.join(root, '*.doc*'))
                
                # Determine category from folder path
                category_path = root.replace(template_folder, '')
                category = category_path.split(os.sep)[1] if os.sep in category_path else 'Unknown'
                
                symbols_catalog[symbol_name] = {
                    'dll_path': os.path.join(root, file),
                    'category': category,
                    'gif_variants': [os.path.basename(g) for g in gif_files],
                    'documentation': doc_files,
                    'folder': symbol_folder
                }
    
    return symbols_catalog
```

#### Step 2: Locate Partsheet Templates
```python
def find_partsheet_for_symbol(symbol_name, template_folder):
    """
    Search for Excel partsheet templates matching a symbol
    """
    # Strategy 1: Check Sample Data folder
    sample_data = os.path.join(template_folder, 'Sample Data')
    if os.path.exists(sample_data):
        for excel_file in glob(os.path.join(sample_data, '*.xlsx')):
            # Check if Excel contains this symbol's partsheet
            if has_symbol_partsheet(excel_file, symbol_name):
                return excel_file
    
    # Strategy 2: Check symbol's own folder
    symbol_info = symbols_catalog.get(symbol_name)
    if symbol_info:
        symbol_folder = symbol_info['folder']
        excel_files = glob(os.path.join(symbol_folder, '*.xlsx'))
        if excel_files:
            return excel_files[0]
    
    # Strategy 3: Check Symbols Data Mapping file
    mapping_file = os.path.join(template_folder, 
                               'Symbol Data Mapping',
                               'Symbols Data Mapping*.xlsx')
    return mapping_file

def has_symbol_partsheet(excel_file, symbol_name):
    """Check if Excel file contains partsheet for this symbol"""
    wb = load_workbook(excel_file, read_only=True)
    for sheet in wb.worksheets:
        header_info = find_partsheet_header(sheet)  # Rows 1-10 search
        if header_info:
            # Check if SymbolDefinition matches
            symbol_col = header_info['column_mapping'].get('symboldefinition')
            if symbol_col:
                cell_value = sheet.cell(header_info['header_row'] + 1, symbol_col).value
                if symbol_name.lower() in str(cell_value).lower():
                    return True
    return False
```

#### Step 3: Build Symbol→Template Cross-Reference
```python
def build_symbol_template_index(template_folder):
    """
    Create master index of all symbols and their associated files
    """
    index = {}
    
    # 1. Extract all symbols from directory structure
    symbols = extract_customer_symbols(template_folder)
    
    # 2. For each symbol, find its partsheet template
    for symbol_name, symbol_info in symbols.items():
        partsheet = find_partsheet_for_symbol(symbol_name, template_folder)
        
        # 3. Parse GIF variants to extract PartDataBasis values
        pdb_variants = []
        for gif_file in symbol_info['gif_variants']:
            match = re.match(r'.+PDB(\d+)\.gif', gif_file)
            if match:
                pdb_variants.append(match.group(1))
        
        index[symbol_name] = {
            'dll': symbol_info['dll_path'],
            'category': symbol_info['category'],
            'partsheet_template': partsheet,
            'gif_variants': symbol_info['gif_variants'],
            'pdb_values': pdb_variants,
            'documentation': symbol_info['documentation']
        }
    
    return index
```

## Quick Reference Commands

```powershell
# Find all DLLs in template folder
Get-ChildItem -Path "Ressources\dotNET" -Filter "*.dll" -Recurse | Select-Object FullName

# List all category folders (depth 1)
Get-ChildItem -Path "Ressources\dotNET" -Directory | Select-Object Name

# Search for symbol by name in Excel files
Get-ChildItem -Path "Ressources\dotNET" -Filter "*.xlsx" -Recurse | Select-String -Pattern "BallValve"

# Count available symbols
(Get-ChildItem -Path "Ressources\dotNET" -Filter "*.dll" -Recurse).Count

# List all symbols with their categories
Get-ChildItem -Path "Ressources\dotNET" -Filter "*.dll" -Recurse | ForEach-Object { 
    [PSCustomObject]@{
        Symbol = $_.BaseName
        Category = $_.Directory.Parent.Name
        Path = $_.FullName
    }
}
```

## Key Files for Symbol Discovery

### Critical Symbol Mapping Files (Look for These Patterns)

**In Customer Template Folders** (adjust paths to actual customer structure):

1. **Symbols Data Mapping Files** - Master symbol catalogs per S3D version
   ```
   # VB/Legacy format (2014 and earlier)
   [Template Root]/Piping and Instrumentation/Piping and Instrumentation 2014/Symbol Data Mapping/
       └── Symbols Data Mapping - Piping and Instrumentation.xlsx
   
   # .NET format (2016+)
   [Template Root]/Piping and Instrumentation - DotNet/Symbol Data Mapping/
       └── Symbols Data Mapping - Piping and Instrumentation - DotNet.xlsx
   ```
   **Purpose**: Complete inventory of all symbols with metadata (ProgID, Class, Properties, PDB values)
   **Usage**: Reference source for symbol properties, partsheet column mappings, and available PDB variants

2. **SKEY Map Files** - Symbol key mappings for catalog integration
   ```
   # VB format
   [Template Root]/Piping and Instrumentation/Piping and Instrumentation 2014/SKEY/
       └── SKEY Map for Piping Symbols.xls
   
   # .NET format  
   [Template Root]/Piping and Instrumentation - DotNet/SKEY/
       └── SKEY Map for Piping Symbols.xls
   ```
   **Purpose**: Maps symbol names to catalog keys for S3D's internal referencing system
   **Usage**: Cross-reference between symbol display names and database identifiers

**Discovery Pattern**:
```python
def find_symbol_mapping_files(template_root):
    """Locate critical mapping files in customer template structure"""
    mapping_files = {}
    
    # Pattern 1: Look for "Symbol Data Mapping" folders recursively
    for root, dirs, files in os.walk(template_root):
        if 'Symbol Data Mapping' in root:
            for file in files:
                if 'Symbols Data Mapping' in file and file.endswith(('.xlsx', '.xls')):
                    format_type = 'dotNET' if 'DotNet' in file else 'VB'
                    mapping_files[f'{format_type}_symbols'] = os.path.join(root, file)
    
    # Pattern 2: Look for "SKEY" folders
    for root, dirs, files in os.walk(template_root):
        if 'SKEY' in root:
            for file in files:
                if 'SKEY Map' in file and file.endswith(('.xlsx', '.xls')):
                    format_type = 'dotNET' if 'DotNet' in root else 'VB'
                    mapping_files[f'{format_type}_skey'] = os.path.join(root, file)
    
    return mapping_files
```

**Important Notes**:
- These files are customer/project-specific with varying folder names
- Version numbers vary: "2014", "2016", "2019", "SP3D v12", etc.
- Always search by filename pattern ("Symbols Data Mapping", "SKEY Map"), not fixed paths
- .NET templates often include both formats for migration support

### Project-Specific Files (S3D-Partsheetanalyzer Internal)

- `source/ReplaceSymbol.xlsx`: Master VB→.NET mapping (3,317 rows) - consolidated from multiple customers
- `source/VB-all-sample-symbols.xlsx`: Aggregated VB symbol catalog for testing
- `source/dotNET-all-sample-symbols.xlsx`: Aggregated .NET symbol catalog for testing

**Note**: The following analysis tools (`symbol_mapping_analyzer.py`, `symbol_translator.py`, `template_analyzer.py`) are project-specific and won't exist in new customer projects. See next section for recreating navigation logic.

## Creating Navigation Tools for New Projects

When starting a new customer project, you'll need to recreate symbol discovery and navigation capabilities. Here's how to build the essential tools from scratch:

### 1. Symbol Catalog Generator

Create a tool to scan customer template folders and build a searchable symbol index:

```python
"""
symbol_catalog_generator.py
Scans Piping and Instrumentation folders to create symbol index
"""
import os
import glob
import pandas as pd
from openpyxl import load_workbook
import json
import re

class SymbolCatalogGenerator:
    def __init__(self, project_root):
        """
        project_root: Path containing "Piping and Instrumentation" folders
        """
        self.project_root = project_root
        self.vb_folder = os.path.join(project_root, "Piping and Instrumentation")
        self.dotnet_folder = os.path.join(project_root, "Piping and Instrumentation - DotNet")
        
        self.symbol_index = {
            'vb': {},
            'dotnet': {}
        }
    
    def scan_all_symbols(self):
        """Main entry point: scan both VB and .NET folders"""
        print("🔍 Scanning VB symbols...")
        if os.path.exists(self.vb_folder):
            self.symbol_index['vb'] = self._scan_format_folder(self.vb_folder, 'VB')
        
        print("🔍 Scanning .NET symbols...")
        if os.path.exists(self.dotnet_folder):
            self.symbol_index['dotnet'] = self._scan_format_folder(self.dotnet_folder, 'dotNET')
        
        return self.symbol_index
    
    def _scan_format_folder(self, base_path, format_type):
        """Recursively scan a template folder for all symbols"""
        symbols = {}
        
        # Find all DLL files (each represents a symbol)
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.endswith('.dll'):
                    symbol_name = file.replace('.dll', '')
                    
                    # Extract category from path
                    rel_path = root.replace(base_path, '').strip(os.sep)
                    category_parts = rel_path.split(os.sep)
                    
                    # Find associated files
                    gif_files = glob.glob(os.path.join(root, '*.gif'))
                    doc_files = glob.glob(os.path.join(root, '*.doc*'))
                    excel_files = glob.glob(os.path.join(root, '*.xls*'))
                    
                    # Extract PDB variants from GIF filenames
                    pdb_variants = []
                    for gif in gif_files:
                        match = re.search(r'PDB(\d+)', os.path.basename(gif))
                        if match:
                            pdb_variants.append(match.group(1))
                    
                    symbols[symbol_name] = {
                        'dll_path': os.path.join(root, file),
                        'folder': root,
                        'category_hierarchy': category_parts,
                        'primary_category': category_parts[0] if category_parts else 'Unknown',
                        'subcategory': category_parts[1] if len(category_parts) > 1 else None,
                        'gif_files': [os.path.basename(g) for g in gif_files],
                        'pdb_variants': pdb_variants,
                        'documentation': [os.path.basename(d) for d in doc_files],
                        'local_excel': [os.path.basename(e) for e in excel_files],
                        'format': format_type
                    }
        
        print(f"   ✅ Found {len(symbols)} {format_type} symbols")
        return symbols
    
    def find_symbol_partsheets(self, symbol_name):
        """Locate all partsheet templates for a specific symbol"""
        results = {
            'sample_data': [],
            'mapping_file': [],
            'local': []
        }
        
        # Strategy 1: Check in symbol's own folder
        for format_type in ['vb', 'dotnet']:
            if symbol_name in self.symbol_index[format_type]:
                symbol_info = self.symbol_index[format_type][symbol_name]
                if symbol_info['local_excel']:
                    results['local'] = [
                        os.path.join(symbol_info['folder'], excel)
                        for excel in symbol_info['local_excel']
                    ]
        
        # Strategy 2: Check Sample Data folders
        for format_type, base_path in [('vb', self.vb_folder), ('dotnet', self.dotnet_folder)]:
            sample_data = os.path.join(base_path, 'Sample Data')
            if os.path.exists(sample_data):
                for excel_file in glob.glob(os.path.join(sample_data, '*.xls*')):
                    if self._excel_contains_symbol(excel_file, symbol_name):
                        results['sample_data'].append(excel_file)
        
        # Strategy 3: Check Symbols Data Mapping files
        for format_type, base_path in [('vb', self.vb_folder), ('dotnet', self.dotnet_folder)]:
            mapping_pattern = os.path.join(base_path, '**', 'Symbol Data Mapping', 'Symbols Data Mapping*.xls*')
            for mapping_file in glob.glob(mapping_pattern, recursive=True):
                if self._excel_contains_symbol(mapping_file, symbol_name):
                    results['mapping_file'].append(mapping_file)
        
        return results
    
    def _excel_contains_symbol(self, excel_path, symbol_name):
        """Check if Excel file contains data for this symbol"""
        try:
            wb = load_workbook(excel_path, read_only=True, data_only=True)
            for sheet in wb.worksheets:
                # Search first 20 rows for symbol name
                for row in range(1, min(21, sheet.max_row + 1)):
                    for col in range(1, min(20, sheet.max_column + 1)):
                        cell_value = str(sheet.cell(row, col).value or '')
                        if symbol_name.lower() in cell_value.lower():
                            return True
            wb.close()
        except Exception as e:
            pass
        return False
    
    def export_catalog(self, output_file='symbol_catalog.json'):
        """Save catalog to JSON for fast loading"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.symbol_index, f, indent=2)
        print(f"✅ Catalog exported to {output_file}")
    
    def export_excel_summary(self, output_file='symbol_catalog.xlsx'):
        """Create Excel summary for human review"""
        rows = []
        for format_type in ['vb', 'dotnet']:
            for symbol_name, info in self.symbol_index[format_type].items():
                rows.append({
                    'Symbol': symbol_name,
                    'Format': format_type,
                    'Primary Category': info['primary_category'],
                    'Subcategory': info['subcategory'] or '',
                    'Full Path': info['folder'],
                    'DLL': os.path.basename(info['dll_path']),
                    'GIF Count': len(info['gif_files']),
                    'PDB Variants': ', '.join(info['pdb_variants']),
                    'Has Docs': 'Yes' if info['documentation'] else 'No',
                    'Local Excel': ', '.join(info['local_excel'])
                })
        
        df = pd.DataFrame(rows)
        df.to_excel(output_file, index=False)
        print(f"✅ Excel summary exported to {output_file}")

# Usage in new project:
if __name__ == '__main__':
    # Point to customer's template root
    project_root = r"C:\CustomerProject"  # Contains "Piping and Instrumentation" folders
    
    generator = SymbolCatalogGenerator(project_root)
    catalog = generator.scan_all_symbols()
    
    # Export for later use
    generator.export_catalog('symbol_catalog.json')
    generator.export_excel_summary('symbol_catalog.xlsx')
    
    # Example: Find partsheets for specific symbol
    partsheets = generator.find_symbol_partsheets('BallValve')
    print(f"\nPartsheets for BallValve: {partsheets}")
```

### 2. Partsheet Finder Utility

Specialized tool for locating partsheet templates by various criteria:

```python
"""
partsheet_finder.py
Find partsheet templates using multiple search strategies
"""
import os
import glob
from openpyxl import load_workbook

class PartsheetFinder:
    def __init__(self, piping_instrumentation_root):
        self.vb_folder = os.path.join(piping_instrumentation_root, "Piping and Instrumentation")
        self.dotnet_folder = os.path.join(piping_instrumentation_root, "Piping and Instrumentation - DotNet")
    
    def find_by_symbol_name(self, symbol_name, format_type='dotnet'):
        """Find partsheets containing a specific symbol"""
        base_folder = self.dotnet_folder if format_type == 'dotnet' else self.vb_folder
        results = []
        
        # Search all Excel files
        for excel_file in glob.glob(os.path.join(base_folder, '**', '*.xls*'), recursive=True):
            try:
                if self._check_partsheet_for_symbol(excel_file, symbol_name):
                    results.append(excel_file)
            except Exception as e:
                continue
        
        return results
    
    def find_by_category(self, category, format_type='dotnet'):
        """Find all partsheets in a category folder"""
        base_folder = self.dotnet_folder if format_type == 'dotnet' else self.vb_folder
        category_path = os.path.join(base_folder, category)
        
        if not os.path.exists(category_path):
            return []
        
        # Find all Excel files in category
        return glob.glob(os.path.join(category_path, '**', '*.xls*'), recursive=True)
    
    def _check_partsheet_for_symbol(self, excel_path, symbol_name):
        """Check if Excel contains partsheet for symbol"""
        wb = load_workbook(excel_path, read_only=True, data_only=True)
        
        for sheet in wb.worksheets:
            # Search for partsheet header (rows 1-10)
            header_info = self._find_partsheet_header(sheet)
            if not header_info:
                continue
            
            # Check SymbolDefinition column
            symbol_col = header_info.get('symboldefinition_col')
            if symbol_col:
                for row in range(header_info['header_row'] + 1, min(sheet.max_row + 1, 100)):
                    cell_value = str(sheet.cell(row, symbol_col).value or '')
                    if symbol_name.lower() in cell_value.lower():
                        wb.close()
                        return True
        
        wb.close()
        return False
    
    def _find_partsheet_header(self, worksheet):
        """Search rows 1-10 for partsheet header pattern"""
        required = {'definition', 'partclasstype', 'symboldefinition'}
        
        for row in range(1, min(11, worksheet.max_row + 1)):
            headers = {}
            for col in range(1, min(50, worksheet.max_column + 1)):
                cell_value = str(worksheet.cell(row, col).value or '').strip().lower()
                if cell_value in required:
                    headers[cell_value] = col
            
            # Found valid header if all required columns present
            if len(headers) >= 3:
                return {
                    'header_row': row,
                    **{f'{k}_col': v for k, v in headers.items()}
                }
        
        return None
    
    def get_all_sample_data_partsheets(self, format_type='dotnet'):
        """List all partsheets in Sample Data folder"""
        base_folder = self.dotnet_folder if format_type == 'dotnet' else self.vb_folder
        sample_data = os.path.join(base_folder, 'Sample Data')
        
        if not os.path.exists(sample_data):
            return []
        
        return glob.glob(os.path.join(sample_data, '*.xls*'))

# Usage:
finder = PartsheetFinder(r"C:\CustomerProject")
ball_valve_sheets = finder.find_by_symbol_name('BallValve', 'dotnet')
valve_category_sheets = finder.find_by_category('Valves', 'dotnet')
```

### 3. Quick Start Script

Combine both tools into a single initialization script for new projects:

```python
"""
initialize_project.py
Run this first in any new customer project
"""
import os
import sys

def initialize_new_project(project_root):
    """
    Initialize symbol discovery for a new customer project
    
    Args:
        project_root: Path containing "Piping and Instrumentation" folders
    """
    print("=" * 60)
    print("S3D Project Initialization")
    print("=" * 60)
    
    # Validate folder structure
    vb_folder = os.path.join(project_root, "Piping and Instrumentation")
    dotnet_folder = os.path.join(project_root, "Piping and Instrumentation - DotNet")
    
    if not os.path.exists(vb_folder) and not os.path.exists(dotnet_folder):
        print("❌ ERROR: Could not find expected folders:")
        print(f"   - {vb_folder}")
        print(f"   - {dotnet_folder}")
        sys.exit(1)
    
    print(f"✅ VB Folder: {vb_folder}")
    print(f"✅ .NET Folder: {dotnet_folder}")
    
    # Generate symbol catalog
    print("\n📊 Generating symbol catalog...")
    from symbol_catalog_generator import SymbolCatalogGenerator
    generator = SymbolCatalogGenerator(project_root)
    catalog = generator.scan_all_symbols()
    generator.export_catalog('symbol_catalog.json')
    generator.export_excel_summary('symbol_catalog.xlsx')
    
    # Summary statistics
    vb_count = len(catalog['vb'])
    dotnet_count = len(catalog['dotnet'])
    
    print(f"\n📈 Summary:")
    print(f"   - VB Symbols: {vb_count}")
    print(f"   - .NET Symbols: {dotnet_count}")
    print(f"   - Total: {vb_count + dotnet_count}")
    
    print("\n✅ Initialization complete!")
    print("   Generated files:")
    print("   - symbol_catalog.json (for programmatic access)")
    print("   - symbol_catalog.xlsx (for human review)")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python initialize_project.py <project_root>")
        print("Example: python initialize_project.py C:\\CustomerProject")
        sys.exit(1)
    
    initialize_new_project(sys.argv[1])
```

### Essential Navigation Patterns

**Always follow these patterns when navigating customer folders:**

```python
# ✅ CORRECT: Recursive discovery
def find_all_symbols(base_path):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.dll'):
                yield os.path.join(root, file)

# ❌ WRONG: Hardcoded paths
symbols = glob.glob("Piping and Instrumentation - DotNet/Valves/2-way valves/*.dll")

# ✅ CORRECT: Pattern-based search
def find_mapping_files(base_path):
    return glob.glob(
        os.path.join(base_path, '**', 'Symbol Data Mapping', 'Symbols Data Mapping*.xls*'),
        recursive=True
    )

# ❌ WRONG: Fixed path
mapping_file = "Piping and Instrumentation - DotNet/Symbol Data Mapping/..."
```
