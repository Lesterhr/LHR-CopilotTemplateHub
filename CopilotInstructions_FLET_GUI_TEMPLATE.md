---
template-type: gui-framework
applies-to: ["flet", "python", "desktop-app"]
priority: 1
version: 1.0.0
last-updated: 2025-11-14
---

# Standard Flet GUI Template

## 📋 How AI Agents Should Use This Template

**When to apply**: Building or modifying Flet-based desktop applications

**Apply to files**:
- `*_app.py` - Main application files
- `source/gui/**/*.py` - GUI components and views
- Files importing `flet as ft`

**Ignore for**:
- Backend logic, data processing
- API clients, database models
- Non-GUI utility functions

**Key patterns to follow**:
1. Use the App class structure with `_build_ui()` methods
2. Apply the standard color scheme (`#4A9FD8` primary blue)
3. Use threading for long-running operations to prevent UI blocking
4. Follow the view-based navigation pattern for multi-page apps

---

## Framework
- **GUI Framework**: Flet >= 0.24.0
- **Python Version**: 3.10+
- **Architektur**: Single-Page Application mit Multi-View Navigation

## Projektstruktur

```
project/
├── source/
│   └── gui/
│       ├── main_app.py          # Haupt-App-Klasse
│       ├── simple_app.py        # Vereinfachte App-Variante
│       └── views/               # Modulare View-Komponenten
│           ├── __init__.py
│           ├── import_view.py
│           ├── mapping_view.py
│           └── settings_view.py
├── requirements.txt
└── main.py                      # Entry Point
```

## App-Klasse Struktur

```python
import flet as ft
from loguru import logger

class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "App Title"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 20
        self.page.window_width = 1200
        self.page.window_height = 800
        
        # Application State
        self.current_view = None
        
        logger.info("App initialized")
        self._build_ui()
    
    def _build_ui(self):
        """Baut die Haupt-UI auf"""
        header = self._build_header()
        content = self._build_content()
        status = self._build_status_bar()
        
        self.page.add(
            ft.Column([
                header,
                ft.Divider(height=1),
                content,
                ft.Container(height=10),
                status,
            ], scroll=ft.ScrollMode.AUTO, expand=True)
        )
```

## Farbschema

### Primärfarben
- **Primary Blue**: `#4A9FD8` (Header, Buttons, Highlights)
- **Dark Blue**: `#2A7AB8` (Überschriften, Akzente)
- **Light Blue**: `#E3F2FD` (Hintergründe)

### Neutrale Farben
- **White**: `ft.Colors.WHITE` (Text auf Buttons, Icons)
- **Grey 600**: `ft.Colors.GREY_600` (Sekundärer Text)
- **Grey 300**: `ft.Colors.GREY_300` (Borders)
- **Blue Grey 100**: `ft.Colors.BLUE_GREY_100` (AppBar Background)

### Verwendungsbeispiele
```python
# Header/AppBar
bgcolor="#4A9FD8"

# Buttons (Primary Action)
ft.ElevatedButton(
    "Action",
    bgcolor="#4A9FD8",
    color=ft.Colors.WHITE,
)

# Section Headers
ft.Text("Titel", size=18, weight=ft.FontWeight.BOLD, color="#2A7AB8")

# Status/Info Text
ft.Text("Info", size=12, color=ft.Colors.GREY_600)
```

## Standard-Komponenten

### Header
```python
header = ft.Container(
    content=ft.Row([
        ft.Icon(ft.Icons.APP_ICON, size=40, color=ft.Colors.WHITE),
        ft.Column([
            ft.Text("App Name", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Text("Subtitle", size=14, color=ft.Colors.WHITE70),
        ], spacing=0),
    ]),
    padding=15,
    bgcolor="#4A9FD8",
    border_radius=10,
    margin=ft.margin.only(bottom=10),
)
```

### Status Bar
```python
self.status_text = ft.Text("Bereit", size=12, color=ft.Colors.WHITE)
status_bar = ft.Container(
    content=self.status_text,
    padding=10,
    bgcolor="#4A9FD8",
    border_radius=5,
)
```

### Section Container
```python
section = ft.Container(
    content=ft.Column([
        ft.Row([
            ft.Icon(ft.Icons.SECTION_ICON, color="#4A9FD8"),
            ft.Text("Section Title", size=18, weight=ft.FontWeight.BOLD, color="#2A7AB8"),
        ]),
        ft.Container(height=10),
        # Section content here
    ]),
    padding=15,
    border=ft.border.all(1, ft.Colors.GREY_300),
    border_radius=10,
)
```

### Navigation Rail (Optional - für Multi-View Apps)
```python
nav_rail = ft.NavigationRail(
    selected_index=0,
    label_type=ft.NavigationRailLabelType.ALL,
    min_width=100,
    destinations=[
        ft.NavigationRailDestination(
            icon=ft.Icons.HOME_OUTLINED,
            selected_icon=ft.Icons.HOME,
            label="Home",
        ),
        ft.NavigationRailDestination(
            icon=ft.Icons.SETTINGS_OUTLINED,
            selected_icon=ft.Icons.SETTINGS,
            label="Settings",
        ),
    ],
    on_change=self._on_nav_change,
)
```

## Layout-Pattern

### Workflow-basiert (Step by Step)
Für sequentielle Workflows mit mehreren Schritten:

```python
def _build_ui(self):
    self.page.add(
        ft.Column([
            header,
            ft.Divider(height=1),
            self.step1_section,  # Schritt 1: Input
            ft.Divider(height=15),
            self.step2_section,  # Schritt 2: Processing
            ft.Divider(height=15),
            self.step3_section,  # Schritt 3: Output
            ft.Container(height=10),
            status_bar,
        ], scroll=ft.ScrollMode.AUTO, expand=True)
    )
```

### Navigation-basiert
Für Apps mit verschiedenen unabhängigen Bereichen:

```python
def _build_ui(self):
    self.page.add(
        ft.Row([
            nav_rail,
            ft.VerticalDivider(width=1),
            ft.Column([
                self.current_view,
            ], expand=True, scroll=ft.ScrollMode.AUTO),
        ], expand=True)
    )
```

## Best Practices

### State Management
```python
# Zentraler State in App-Klasse
self.data: List[Dict[str, Any]] = []
self.selected_item: Optional[int] = None
self.processing: bool = False
```

### UI Updates
```python
# Nach Änderungen immer UI aktualisieren
self.status_text.value = "Processing..."
self.page.update()

# Bei File Dialogs
await self.page.update_async()
```

### Error Handling
```python
try:
    # Operation
    self._set_status("Success", is_error=False)
except Exception as e:
    logger.error(f"Error: {e}")
    self._set_status(f"Error: {e}", is_error=True)
```

### Logging
```python
from loguru import logger

logger.info("Operation started")
logger.error(f"Error occurred: {e}")
logger.debug(f"Debug info: {data}")
```

## Entry Point Pattern

```python
# main.py
import flet as ft
from source.gui.main_app import MyApp

def main(page: ft.Page):
    app = MyApp(page)

if __name__ == "__main__":
    ft.app(target=main)
```

## Abhängigkeiten (requirements.txt)

```
# GUI Framework
flet>=0.24.0

# Logging
loguru>=0.7.0

# Data Processing (optional)
pandas>=2.1.0
openpyxl>=3.1.0

# Configuration (optional)
pyyaml>=6.0.0
python-dotenv>=1.0.0
```

## Icon-Empfehlungen

- **Import/Upload**: `ft.Icons.UPLOAD_FILE`
- **Export/Download**: `ft.Icons.DOWNLOAD`, `ft.Icons.SAVE`
- **Settings**: `ft.Icons.SETTINGS`
- **Help**: `ft.Icons.HELP_OUTLINE`
- **Transform/Process**: `ft.Icons.TRANSFORM`
- **AI/Smart**: `ft.Icons.AUTO_AWESOME`
- **Cloud/Integration**: `ft.Icons.CLOUD_UPLOAD`
- **Mapping**: `ft.Icons.COMPARE_ARROWS`
- **Draw**: `ft.Icons.DRAW`
- **Table/List**: `ft.Icons.TABLE_CHART`

## Responsive Design

```python
# Viewport Einstellungen
self.page.window_width = 1200
self.page.window_height = 800
self.page.window_resizable = True

# Scrollbare Layouts
ft.Column([...], scroll=ft.ScrollMode.AUTO, expand=True)
ft.ListView(spacing=5, height=200)  # Fixed height mit scroll
```
