# LHR-CopilotTemplateHub AI Agent Guide

This repository manages reusable AI instruction templates for GitHub Copilot and other AI coding assistants. It includes a Flet GUI application for organizing templates between active and archived states.

## Architecture Overview

### Repository Structure
```
.github/
├── copilot-instructions.md              # This file - repository-wide guidance
└── instructions/                        # Path-specific templates
    ├── *.instructions.md                # Active templates (18 files)
    └── archived/                        # Inactive templates
```

**Key concept**: Templates in `instructions/` are **active** and loaded by GitHub Copilot. Templates in `archived/` are **inactive** for version control only.

### Core Components

1. **Template Repository** (`.github/instructions/`)
   - 18+ instruction templates covering Flet, SmartSketch, S3D, VS Code, SQL, etc.
   - Each template follows kebab-case: `topic-name.instructions.md`
   - Templates include YAML frontmatter with version, type, priority metadata

2. **GUI Application** (`instructions_organizer.py`)
   - Flet-based drag-and-drop interface for moving templates between active/archived
   - Follows `flet-styleguide.instructions.md` design system
   - Dark theme (#1a1d23 background, blue accents #3b82f6)
   - Two-column layout: Available Instructions | Archived Instructions

3. **Documentation**
   - `README.md`: User-facing overview with download instructions
   - `INDEX.md`: Template index with usage rules and priority resolution
   - `GUI_README.md`: German language GUI documentation

## Development Workflows

### Running the GUI Application
```powershell
# Desktop mode (default)
python instructions_organizer.py

# Web browser mode
python instructions_organizer.py --view web --port 8550

# Install dependencies first
pip install -r requirements.txt  # Only requires flet>=0.28.3
```

### Testing
```powershell
python test_organizer.py  # Unit tests for file operations
```

### Creating New Templates

1. **File naming**: Use `topic-name.instructions.md` in `.github/instructions/`
2. **Metadata format** (YAML frontmatter):
   ```yaml
   ---
   version: 1.0.0
   type: gui-framework | domain-specific | project-context | integration-guide
   priority: 1-5  # Lower = higher priority
   tags: [tag1, tag2, tag3]
   ---
   ```
3. **Required sections**:
   - "How AI Agents Should Use This Template"
   - Detailed patterns with code examples
   - Tags and applicability rules

4. **Synchronize documentation**:
   - Update `README.md` "Available Templates" section
   - Update `INDEX.md` with new template entry
   - Increment repository version if significant

### Template Priority System

When multiple templates apply to a file:
1. Repository-wide (this file) provides base context
2. Higher priority (lower number) path-specific templates take precedence
3. Domain-specific templates override general templates
4. Integration guides complement (not replace) base templates

Example: For Flet + SmartSketch project:
- Apply `flet-agent.instructions.md` (priority 1) for GUI
- Apply `smartsketch-integration-guide.instructions.md` (priority 2) for CAD logic
- Keep concerns separated in different modules

## Project-Specific Conventions

### Flet Application Patterns

**Style consistency**: All Flet apps in this repo follow `flet-styleguide.instructions.md`:

```python
# Dark theme setup
page.bgcolor = "#1a1d23"
page.theme_mode = ft.ThemeMode.DARK

# Component styling
container.bgcolor = ft.Colors.GREY_800
container.border_radius = 10
container.animate = ft.Animation(300, ft.AnimationCurve.EASE_OUT_CUBIC)

# Blue gradient headers
gradient=ft.LinearGradient(
    begin=ft.alignment.center_left,
    end=ft.alignment.center_right,
    colors=["#1e3a8a", "#3b82f6"]
)
```

**Class structure**: Follow OOP patterns in `instructions_organizer.py`:
- Custom component classes inherit from `ft.Container`
- Store callbacks in class init: `self.on_move_callback`
- Separate UI creation (`create_ui`) from data loading (`load_files`)

### File Safety Patterns

See `instructions_organizer.py` lines 315-325 for path sanitization:

```python
# ALWAYS validate filenames to prevent path traversal
safe_filename = Path(filename).name
if safe_filename != filename:
    # Reject files with directory components
    return

# Validate file extensions
if not safe_filename.endswith(".instructions.md"):
    return
```

### Drag-and-Drop Implementation

Key pattern from `InstructionFileCard` and `DropZone`:

```python
# Draggable component with data payload
ft.Draggable(
    group="instructions",  # Match drag/drop groups
    content=...,
    data={"filename": filename, "is_archived": is_archived}
)

# Drop target accepts data
ft.DragTarget(
    group="instructions",
    on_accept=self.handle_drop
)
```

## Integration Points

### GitHub Copilot Integration
- GitHub Copilot automatically loads `.github/copilot-instructions.md` (this file)
- Path-specific templates in `.github/instructions/` apply based on file context
- See [GitHub Copilot Documentation](https://aka.ms/vscode-instructions-docs)

### External Dependencies
- **Flet** (`flet>=0.28.3`): Only production dependency for GUI
- **Python 3.8+**: Standard library only (pathlib, shutil, argparse)

## Template Management via GUI

The `instructions_organizer.py` GUI enables:
- **Drag files** from Available → Archived to deactivate templates
- **Drag files** from Archived → Available to reactivate templates
- **Physical file movement**: Files are moved in the filesystem, not just UI state
- **Conflict detection**: Prevents overwriting files with same name
- **Path validation**: Security checks prevent directory traversal attacks

## Version Management

- **Repository Version**: Tracked in `README.md`
- **Template Versions**: Individual versions in each template's metadata
- **Semantic Versioning**: MAJOR.MINOR.PATCH
  - MAJOR: Breaking changes in template structure
  - MINOR: New templates or significant additions
  - PATCH: Fixes and minor improvements

## Key Files Reference

| File | Purpose | Lines |
|------|---------|-------|
| `instructions_organizer.py` | Main GUI application | 412 |
| `test_organizer.py` | Unit tests for file operations | 152 |
| `README.md` | User-facing documentation | 203 |
| `INDEX.md` | Template index and rules | 147 |
| `GUI_README.md` | German GUI documentation | 201 |
| `.github/instructions/` | Active template directory | 18 files |
