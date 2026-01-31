# BASF SmartPlant P&ID Functions - AI Coding Agent Instructions

## Project Overview

This is a **VB.NET COM/extension library** for Intergraph SmartPlant P&ID (SPPID), providing custom validation, macros, and VD Explorer integration for BASF process engineering workflows. The codebase extends SPPID 2019 with PSI data management, pressure equipment directive (PED) calculations, and drawing revision control.

## Architecture

### Component Structure
- **COM Components** (`COM_BASF*`): COM-visible wrappers exposing functionality to SPPID
  - `COM_BASFValidation`: Validation rules and locking mechanisms
  - `COM_BASFMacro`: Custom drawing macros
  - `COM_BASFImportImpl`: Data import implementations
  - `COM_BASFCopyTransformation`: Copy/transformation utilities
  
- **Extension Components** (`ExtBASF*`): Internal implementation libraries
  - `ExtBASFValidation`, `ExtBASFMacro`, etc.: Core logic referenced by COM wrappers
  
- **Standalone Tools**:
  - `VDExplorerMain`: VD Explorer data transfer application
  - `IGRConfigurator`/`VDEConfigurator`: Configuration utilities
  - `GlobalRDB`: Reference database management
  - `MB_PID_Tool`: Pipeline designation tooling

### Key Dependencies
- **SmartPlant P&ID API**: Located in `libs/SPPID/` - includes `RadNetAutomation.dll`, `llama.dll`, `plaice.dll`, `sp2dopensite412.dll`
- **External Libraries**: `libs/External/` contains COM interop assemblies
- **Target Platform**: x86 only (SPPID is 32-bit)
- **Framework**: .NET Framework 4.6.2

## Critical Build Workflow

### Initial Setup (First Time)
1. Compile `CustomService` in **Release** → outputs to `Deliveries/SetupFiles/Libraries/SDCService.dll`
2. Compile `BuildSetupCollection` (Debug or Release)
3. Run `BuildSetupCollection.exe`, select `Sources.net/AdditionalCompileFiles/CollectionAddLibs.xml`
   - This copies required COM interop DLLs to debug/release bin folders
   - Note: Double backslash `\\` in XML target path means "use this path exactly, don't append collection name"
4. Rebuild `SPMHierarchy` project (dependency for many projects)

### Debug Build
1. Set configuration to **Debug|x86**
2. Open `Sources.net/With Shared Code/BASFTotal.sln`
3. Rebuild solution (19 projects)

### Release Build & Packaging
1. Compile complete **Debug** build first (to populate all dependencies)
2. Set to **Release|x86**
3. Rebuild `BASFTotal.sln` → 19 succeeded, 2 skipped (BuildSetupCollection, ImportAspen2PID)
4. Run `BuildSetupCollection.exe`, select `Deliveries/CollectionBASF_Basic.xml` → creates 7 collections
5. Open `Deliveries/SetupAllBASF.sln`
6. Rebuild all setup projects (8 MSI installers)

**Critical**: PostBuildEvents copy DLLs to `Deliveries/CollectionBASF_Basic/P&ID Workstation/bin/` subdirectories

## Configuration System

### Layered XML Configuration
Configuration files in `Deliveries/SetupFiles/` follow a hierarchical override pattern:
- `ConfigurationMaster.xml`: Base configuration (540 lines of parameters)
- Project-specific XMLs can override base values
- Config parameters control: locking behavior, validation rules, VD export settings, equipment table generation

Key config sections: `<General>`, `<Drawing>`, `<Export>`, `<VDTransfer>`, `<Attributes>`, `<Locking>`, `<Tables>`

### Installation Variants
- **Admin Setup**: Full installation with all tools + configurators
- **User Setup**: Runtime only (Macros + Validations, no configurators)

## Code Conventions

### VB.NET Patterns
- **Option Strict Off**: Legacy compatibility mode (avoid introducing strict typing)
- **COM Visibility**: Use `<ComVisible(True)>` and `<ClassInterface(ClassInterfaceType.AutoDual)>` for COM wrappers
- **Platform Constants**: `DefineConstants` includes `SPPIDVersion = 4200 : NEWFunc = 40 : UseReg = 0 : Win32=True`
- **Error Handling**: Extensive `On Error Resume Next` + explicit `Err.Raise` patterns

### File Organization
- Shared code in `Sources.net/With Shared Code/` - referenced by multiple projects via relative paths
- Each project has `IF_BASF/` folder containing interface definitions (`MasterClass.vb`, `modDCMain.vb`)
- PostBuildEvent scripts use `xcopy` with `/Y` flag to copy outputs to delivery folders

### SPPID API Integration
- Access SPPID objects via `Llama.*` namespace (LMConnector, LMSymbol, LMPipeRun, etc.)
- Use `plaice.dll` for validation framework
- RadNet APIs handle drawing manipulation (`RadNetAutomation`, `RadNetCmdCtrl`)
- Always check for `Nothing` before accessing SPPID object properties

## Common Tasks

### Adding a New Validation Rule
1. Extend class in `ExtBASFValidation/Classes/` (e.g., `BASFValA.vb`)
2. Expose via COM wrapper in `COM_BASFValidation/Classes/`
3. Register in `ConfigurationMaster.xml` if configuration-driven
4. Rebuild solution → Run BuildSetupCollection for test deployment

### Modifying XML Configuration
- Edit `Deliveries/SetupFiles/ConfigurationMaster.xml`
- DTD schema defined inline at file top (lines 4-59)
- Parameters have `name`, `value`, `comment`, `used`, `show` attributes
- Test changes by copying to SPPID's `Template Files\Config\SpecFunctions\` directory

### Debugging with SPPID
- SPPID loads DLLs from `C:\Program Files (x86)\SmartPlant\P&ID Workstation\bin\`
- For debug: Use CollectionAddLibs.xml to populate debug bin, then manually copy to SPPID install
- Set breakpoints in Visual Studio, attach to `smartplantpid.exe` process

## File Path Conventions
- **Absolute paths in code**: Hardcoded to `C:\Program Files (x86)\SmartPlant\P&ID Workstation\`
- **Reference Data**: SPPID RDB located via PlantSetting 711 (Drawing Path)
- **Template Files**: SPPID OptionSetting 682 (Template Files Directory)
- **Logs**: View with XSL stylesheet `ViewLogBASF.xsl` configured in ConfigurationMaster.xml

## Testing Notes
- SPPID 2019 (version 4200) is target platform
- Required BASF P&ID Reference Data V 2.3
- Test drawings must have valid plant/revision context
- VD Explorer tests require VDEConfig.xml in RDB Config folder

## User-Facing Functionality

### Function Rights Management (3-Level Security)
The system implements a hierarchical function rights structure (since v5.0.0.27):
1. **Level 1**: RDB level - `P&ID Reference Data\Template Files\Config\SpecFunctions\FunctionRights.dat`
2. **Level 2**: Project level - `<projectpath>\Config_BFU\FunctionRights.dat`
3. **Level 3**: User level - `%AppData%\Intergraph_GmbH\FunctionRights.dat`

Configuration controlled by `WithIndividualFunctionRights` and `FunctionRightStructure` parameters in Configuration.xml:
- `FunctionRightStructure` format: `3mom` (number of levels + m/o/i for must/optional/ignore per level)
- Encrypted `.dat` files control available functionality per level
- User visibility settings stored in `%AppData%\BASF_ExtPrograms\FunctionRights.xml`

**Admin Modes** (password-protected):
- **Admin mode**: Create-only via environment variable `FunctionRights=adm` or file `%TEMP%\.FunctionRights.adm`
- **Edit mode**: Create and edit once via `FunctionRights=edi` or `.FunctionRights.edi`
- **Auto mode**: Always prompt for edit via `FunctionRights=aut` or `.FunctionRights.aut`

### Activation & UI
- Toolbar activation: Add `BFuncToolbar.dll` from SPPID bin to toolbar, click "B" button
- BASFMain toolbar trigger: Enter "BASFValidation" in any SPPID object's Description property
- Individual function visibility managed per user via checkbox dialog (saved per plant/project)

### Key User Functions

#### PSI (Pipe Service Index) & PED (Pressure Equipment Directive)
- **Revision Management**: View all transferred PSI revisions and active revision
- **Clear Dwg Marian Data**: Delete Marian data from active drawing (requires Settings enablement)
- **Check All Drawings**: Update entire project against active Marian revision
- **Check Active Drawing**: Update single drawing against Marian revision
- Settings control clearing of PSI/PED data on copy/paste and for Delivered Units

#### Equipment Table Generation
- Auto-generates equipment table at left bottom of P&ID
- Table variants configured in Configuration.xml
- Position controlled by "Use actual starting point" (smallest x/y of existing labels)
- Max width setting: `max. EqTbl Width` for space-constrained layouts
- Option: "Create Entries For Items With Empty ItemTag"
- "for all users" option (password-protected) saves position project-wide

#### OPC (Off Page Connector) Functions
- **Check OPC Targets**: Validates To/From entries match partner OPC's target equipment/piperuns
- Lists non-matching OPCs with coordinates
- Optional batch reset of invalid To/From entries
- Controlled by `OPCTargetsAll` and `OPCTargetsNotForEmptyTag` config parameters

#### Drawing Management
- **Set Discipline Into Filename**: Auto-inserts discipline code/number into filename format `<plant_section>_<dc><dn>_<sheet>`
  - Uses properties: `TB Discipline Code` and `TB Discipline No`
  - Triggered on first modification after opening
  - Clearable via "Clear Discipline from Filename" button (default: approved drawings only)
- **Check Titleblock**: Updates entire titleblock from drawing properties
- **Check Line Label Flag**: Updates `Line Label Flag` for all piperuns in project
  - `True`: Piperun has "Main" line label (defined in `Main_Linelabels.ini`)
  - `False`: No piperun of same ItemTag has Main label
  - `Null`: Other piperun segment with same ItemTag has Main label
  - Uses direct SQL for performance, requires exclusive project access
  - Critical for Line List Reports

#### M/A (Measuring/Adjusting) Location Management
**Check/Complete M/A** (manual or auto-triggered on Approve):
- Auto-sets `Measuring/Adjusting Location` on ConnectToProcess (CTP) lines
- Bubble validation: Sets `Uncomplete` flag if multiple CTPs lack M/A values or have duplicates
- CTP auto-setting rules (priority order):
  1. `M1` if direct connection to inline instrument
  2. `S1` if bubble's `Instr Type Modifier` starts with "V"
  3. `S1` if modifier has "C" in 1st/2nd position and inline instrument attached
  4. `EV1` if `Measured Variable Code` starts with "N" and symbol is motor (per VDMotorFilter.xml)
  5. `M1` otherwise
- Sets `M/A Automatic` to True
- Inline instrument: Sets `Instr Func Type` to "Control" based on bubble/loop/signal conditions

**Valid CTP criteria**:
- Connected (not dangling)
- Not to another bubble
- Not to Gap or Break
- Not to own branch point

#### Other Functions
- **Pipeline Designation Management**: Create/edit/delete pipeline shortcuts and comments
- **Pipeline Designation Report**: Generate report for active drawing
- **View Logfile**: Open last action log or validation log
- **Drawing Locked checkbox**: Controls VDExplorer transfer exclusion
- **Approve Active Dwg**: Triggers transfer via VDExplorer Transfer Main

### File Paths for User Configurations
- Function visibility: `%AppData%\BASF_ExtPrograms\FunctionRights.xml`
- User-level rights: `%AppData%\Intergraph_GmbH\FunctionRights.dat`
- Main line labels config: `<RDB>\Template Files\Config\SpecFunctions\Main_Linelabels.ini`
- VD Motor filter: `<RDB>\Config\VDExplorer\VDMotorFilter.xml`

### Validation Trigger Points
- On object creation/modification
- On drawing approval (M/A check, equipment table, OPC check, pipeline report)
- On first modification after opening (discipline in filename)
- Manual via toolbar buttons
- Controlled by `ApproveActionStatus`, `ApproveActionConfirm`, `ApproveActionConsequence` in Configuration.xml
