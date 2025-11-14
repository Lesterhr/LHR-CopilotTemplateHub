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
2. Apply modern UI standards (2025): maximized windows, gradient headers, container-based buttons
3. Use threading for long-running operations to prevent UI blocking
4. Follow the view-based navigation pattern for multi-page apps
5. **ALWAYS prioritize professional, modern look**: Follow the "Modern UI Standards (2025)" section below for all new GUI development

**Quality Standard**:
> Every Flet application should have a professional, modern look with maximized windows, smooth animations, and high-quality navigation patterns that follow 2025 UI/UX standards. Use gradient headers, container-based buttons with ripple effects, badge-style progress indicators, and zero-padding layouts for precise control.

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
        self.page.theme_mode = ft.ThemeMode.DARK  # Modern apps use DARK theme
        self.page.padding = 0  # Use container padding instead
        self.page.window_width = 1200
        self.page.window_height = 800
        self.page.window_resizable = True
        self.page.window_maximized = True  # Start maximized for better UX
        self.page.scroll = ft.ScrollMode.HIDDEN  # Let containers handle scrolling
        
        # Set custom window icon (optional)
        # icon_path = os.path.join(os.path.dirname(__file__), "app-icon.ico")
        # if os.path.exists(icon_path):
        #     self.page.window.icon = icon_path
        
        # Application State
        self.current_view = None
        
        logger.info("App initialized")
        self._build_ui()
    
    def _build_ui(self):
        """Baut die Haupt-UI auf"""
        header = self._build_header()
        content = self._build_content()
        footer = self._build_footer()
        
        self.page.add(
            ft.Column([
                header,
                ft.Container(content=content, padding=30, expand=True),
                footer,
            ], spacing=0, expand=True)
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

## Animations & Transitions

### Container Offset Animation (Slide Effects)
```python
# Setup: Container mit animation
self.animated_container = ft.Container(
    content=ft.Column([...]),
    animate_offset=500,  # Duration in milliseconds
    offset=ft.Offset(0, 0),  # Initial position (x, y) - NOT ft.transform.Offset!
)

# Trigger animation: Update offset
self.animated_container.offset = ft.Offset(-1, 0)  # Slide left
self.animated_container.update()

# Common offset values:
# ft.Offset(0, 0)   - Center (default)
# ft.Offset(-1, 0)  - Slide out left
# ft.Offset(1, 0)   - Slide out right
# ft.Offset(0, -1)  - Slide out top
# ft.Offset(0, 1)   - Slide out bottom
```

### Available AnimatedSwitcher Transitions
```python
# IMPORTANT: Limited transition types available in Flet
self.switcher = ft.AnimatedSwitcher(
    content,
    transition=ft.AnimatedSwitcherTransition.FADE,  # ✅ Available
    # transition=ft.AnimatedSwitcherTransition.ROTATION,  # ✅ Available
    # transition=ft.AnimatedSwitcherTransition.SCALE,  # ✅ Available
    # transition=ft.AnimatedSwitcherTransition.SLIDE_LEFT,  # ❌ NOT available
    duration=500,
    reverse_duration=500,
)

# For slide animations, use Container with animate_offset (see above)
```

### Smooth Step Transitions (Multi-Step Wizards)

**⚠️ PREFERRED ANIMATION PATTERN FOR STEP NAVIGATION**

This is the recommended approach for transitioning between wizard steps or views. The animation creates a smooth left-to-right slide effect where the old content slides out left while new content slides in from the right.

```python
def show_step(self, step):
    """Show step with smooth left-to-right slide animation
    
    Animation Flow:
    1. Current content slides OUT to the left
    2. Container instantly repositions to right (off-screen)
    3. New content loads while off-screen
    4. New content slides IN from right to center
    
    This creates a natural left-to-right progression effect.
    """
    import time
    
    self.current_step = step
    self.update_step_indicator()
    
    # Step 1: Slide current content OUT to the left
    self.animated_container.offset = ft.Offset(-1, 0)
    self.page.update()
    
    # Wait for slide-out animation to complete (slightly shorter for fluidity)
    time.sleep(0.75)  # Slightly less than full animation duration (800ms)
    
    # Step 2: Disable animation temporarily to instantly jump to right side
    # CRITICAL: Without disabling animation, the container would animate from left to right
    self.animated_container.animate_offset = None
    self.animated_container.offset = ft.Offset(1, 0)
    
    # Step 3: Update content while off-screen RIGHT
    self.content_area.controls.clear()
    
    if step == 2:
        self.show_repository_step()
    elif step == 3:
        self.show_project_setup_step()
    
    self.page.update()
    
    # Minimal delay before sliding in from right
    time.sleep(0.1)
    
    # Step 4: Re-enable animation and slide new content IN from right to center
    self.animated_container.animate_offset = ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT_CUBIC)
    self.page.update()  # Update to apply animation settings first
    
    time.sleep(0.02)  # Minimal delay to ensure animation is active
    
    self.animated_container.offset = ft.Offset(0, 0)
    
    # Update navigation buttons
    self.btn_back.visible = step > 1
    self.btn_next.visible = step < 3
    
    self.page.update()
```

**Common Mistakes & Solutions:**

1. **❌ Problem**: Content slides from left, not right
   - **Cause**: Forgot to disable `animate_offset` before repositioning
   - **Solution**: Set `animate_offset = None`, then reposition, then re-enable

2. **❌ Problem**: Animation is jerky/stuttery
   - **Cause**: Not calling `page.update()` after re-enabling animation
   - **Solution**: Add `self.page.update()` after setting `animate_offset` and before changing offset

3. **❌ Problem**: Content appears instantly without slide-in animation
   - **Cause**: No delay between re-enabling animation and changing offset
   - **Solution**: Add small `time.sleep(0.02)` to ensure animation is active

4. **❌ Problem**: Animation feels sluggish/laggy
   - **Cause**: Waiting too long between slide-out and slide-in
   - **Solution**: Use 0.75s (slightly less than full 0.8s duration) for fluid overlap

5. **❌ Problem**: New content briefly visible during repositioning
   - **Cause**: Content loaded before repositioning to right
   - **Solution**: Disable animation FIRST, reposition SECOND, then load content

**Animation Timing Guide:**
- Container animation duration: **800ms** (`ft.Animation(800, ...)`)
- Slide-out wait time: **750ms** (allows smooth overlap)
- Reposition delay: **100ms** (content loading time)
- Re-enable animation delay: **20ms** (ensure animation is active)
- Total transition time: ~1.6 seconds (feels smooth, not rushed)

**Why This Pattern?**
- ✅ Creates clear directional flow (left = old, right = new)
- ✅ Prevents jarring instant transitions
- ✅ Gives visual feedback that content is changing
- ✅ Feels professional and polished
- ✅ Matches user expectations from modern UIs


### Simple Step Transitions (Alternative)

**⚠️ NOTE**: For multi-step wizards, prefer the "Smooth Step Transitions" pattern above for better UX.

```python
def show_step_simple(self, step):
    """Simple step transition without left-to-right animation"""
    # 1. Slide current content out
    self.animated_container.offset = ft.Offset(-1, 0)
    self.animated_container.update()
    
    # 2. Brief pause for animation
    import time
    time.sleep(0.05)
    
    # 3. Update content
    self.content_area.controls.clear()
    if step == 1:
        self.show_step_one()
    elif step == 2:
        self.show_step_two()
    
    # 4. Position content off-screen right
    self.animated_container.offset = ft.Offset(1, 0)
    self.page.update()
    
    # 5. Slide in to center
    self.animated_container.offset = ft.Offset(0, 0)
    self.page.update()
```

### Animation Property Reference
```python
# All animate_ properties accept milliseconds (int) or animation objects
container = ft.Container(
    animate_offset=500,          # Slide animations
    animate_opacity=300,         # Fade in/out
    animate_scale=400,           # Zoom effects
    animate_rotation=500,        # Rotation effects
    animate_size=300,            # Size changes
    animate_position=400,        # Position changes
)

# Note: Use simple int values for duration (milliseconds)
# Advanced: ft.animation.Animation() object NOT needed for basic animations
```

### Common Animation Pitfalls
- ❌ `ft.animation.Animation()` - AttributeError (module 'flet' has no attribute 'animation')
- ❌ `ft.AnimatedSwitcherTransition.SLIDE_LEFT` - Not available, use FADE/ROTATION/SCALE only
- ❌ `ft.transform.Offset(x, y)` - AttributeError (module 'flet' has no attribute 'transform')
- ✅ Use `ft.Offset(x, y)` directly (imported from flet.core.transform, but accessible as ft.Offset)
- ✅ Use `animate_offset` with integer milliseconds for slide animations
- ✅ Valid offset range: -1 to 1 (where 1 = full width/height of container)

### Import Note
```python
import flet as ft

# These are available directly from ft:
ft.Offset(0, 0)      # ✅ Correct
ft.Rotate(0)         # ✅ Correct
ft.Scale(1.0)        # ✅ Correct

# NOT ft.transform.Offset - this will fail!
ft.transform.Offset(0, 0)  # ❌ AttributeError
```

## Modern UI Standards (2025)

### Window Configuration Best Practices

**⚠️ IMPORTANT: Window Maximization in Flet 0.28+**

For Flet version 0.28.0 and newer, use the `page.window.maximized` property instead of `page.window_maximized`:

```python
class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        
        # Configure page BEFORE adding content
        self.page.title = "My App"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = "#1a1d23"
        self.page.padding = 0
        self.page.window_width = 1200       # Fallback size if maximized fails
        self.page.window_height = 800
        self.page.window_resizable = True
        self.page.scroll = ft.ScrollMode.HIDDEN
        
        # ✅ CORRECT: Set maximized BEFORE setup_ui (Flet 0.28+)
        self.page.window.maximized = True
        
        # Initialize UI
        self.setup_ui()
    
    def setup_ui(self):
        # Build your UI
        main_container = ft.Container(...)
        self.page.add(main_container)
        
        # ✅ CORRECT: Re-apply maximized AFTER content is added
        self.page.window.maximized = True
        self.page.update()
```

**Common Mistakes:**

1. **❌ Using old syntax**: `page.window_maximized = True` (deprecated in 0.28+)
   - **Solution**: Use `page.window.maximized = True`

2. **❌ Setting maximized too early**: Before any content exists
   - **Solution**: Set it in `__init__` AND again after `page.add()`

3. **❌ Forgetting page.update()**: After setting maximized property
   - **Solution**: Always call `self.page.update()` after changing window properties

**Recommended Pattern:**
```python
# Step 1: Set in __init__ (before content)
self.page.window.maximized = True

# Step 2: Add your content
self.page.add(main_container)

# Step 3: Re-apply after content (ensures it works)
self.page.window.maximized = True
self.page.update()
```

**Why set it twice?**
- First time: Prepares the window state
- Second time: Ensures it applies after content is loaded
- Some platforms need content to exist before maximizing works

### Legacy Window Configuration (Flet < 0.28)
```python
# For older Flet versions (< 0.28), use the old syntax:
self.page.window_maximized = True  # Old syntax
### Legacy Window Configuration (Flet < 0.28)
```python
# For older Flet versions (< 0.28), use the old syntax:
self.page.window_maximized = True  # Old syntax
self.page.window_width = 1200       # Fallback size
self.page.window_height = 800
self.page.window_resizable = True
self.page.bgcolor = "#1a1d23"      # Dark anthracite (modern dark background)
self.page.padding = 0              # Use container padding for precise control
self.page.scroll = ft.ScrollMode.HIDDEN  # Let containers handle scrolling
self.page.theme_mode = ft.ThemeMode.DARK  # Modern apps default to dark theme

# Note: page.window_opacity does NOT work on Windows!
# For Windows transparency, use Windows API (see below)
```

### Windows Transparency (Windows API Solution)
```python
# Flet's window_opacity doesn't work on Windows - use Win32 API instead
import ctypes
from ctypes import wintypes
import time

class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        # ... page configuration ...
        
        # Build UI first
        self._build_ui()
        
        # Apply Windows transparency after UI is built
        self.page.update()
        time.sleep(0.1)  # Short delay to ensure window is created
        self.apply_windows_transparency()
    
    def apply_windows_transparency(self):
        """Apply Windows API transparency (only works on Windows)"""
        try:
            # Get window handle by title
            hwnd = ctypes.windll.user32.FindWindowW(None, self.page.title)
            if hwnd:
                # Constants for layered window
                GWL_EXSTYLE = -20
                WS_EX_LAYERED = 0x80000
                LWA_ALPHA = 0x2
                
                # Set layered window attribute
                style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
                ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_LAYERED)
                
                # Set transparency (0-255, where 255 is opaque)
                alpha = int(0.92 * 255)  # 92% opacity (235/255)
                ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, alpha, LWA_ALPHA)
                print(f"Applied Windows transparency: {alpha}/255")
            else:
                print("Could not find window handle")
        except Exception as e:
            print(f"Could not apply Windows transparency: {e}")

# Recommended opacity values:
# 0.92-0.95 (235-242/255) - Subtle glass effect, professional
# 0.85-0.90 (217-230/255) - Moderate transparency
# 0.50-0.80 (128-204/255) - Strong transparency (testing only)
```

### Important Notes for Windows Transparency
- ✅ Works on Windows 7/8/10/11
- ✅ Uses native Win32 `SetLayeredWindowAttributes` API
- ✅ No additional dependencies (ctypes is built-in)
- ⚠️ Must be called AFTER `page.update()` and UI construction
- ⚠️ Window must have a unique title to find HWND
- ⚠️ Add small delay (`time.sleep(0.1)`) to ensure window exists
- ❌ Flet's `page.window_opacity` does NOT work on Windows
```

### Modern Gradient Headers
```python
# Replace solid color headers with gradients
header = ft.Container(
    content=ft.Column([
        ft.Text("App Name", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
        ft.Text("Description", size=14, color=ft.Colors.WHITE70),
    ], spacing=5),
    padding=25,
    gradient=ft.LinearGradient(
        begin=ft.alignment.center_left,
        end=ft.alignment.center_right,
        colors=["#1e3a8a", "#3b82f6"],  # Blue gradient
    ),
    border_radius=ft.border_radius.only(bottom_left=15, bottom_right=15),
)
```

### Container-Based Navigation (Better than ElevatedButton)
```python
# Primary action button
btn_primary = ft.Container(
    content=ft.Row([
        ft.Text("Continue", size=14, weight=ft.FontWeight.W_500),
        ft.Icon(ft.Icons.ARROW_FORWARD, size=18),
    ], spacing=8, tight=True),
    padding=ft.padding.symmetric(horizontal=24, vertical=12),
    bgcolor=ft.Colors.BLUE_600,
    border_radius=8,
    on_click=self.continue_action,
    ink=True,  # Ripple effect on click
    animate=200,  # ✅ Use integer milliseconds, NOT ft.animation.Animation()
)

# Secondary action button
btn_secondary = ft.Container(
    content=ft.Row([
        ft.Icon(ft.Icons.ARROW_BACK, size=18),
        ft.Text("Back", size=14, weight=ft.FontWeight.W_500),
    ], spacing=8, tight=True),
    padding=ft.padding.symmetric(horizontal=24, vertical=12),
    bgcolor=ft.Colors.GREY_800,
    border_radius=8,
    on_click=self.back_action,
    ink=True,
    animate=200,  # Simple integer for animation duration
)

# ❌ WRONG: animate=ft.animation.Animation(200, ft.AnimationCurve.EASE_OUT)
# ✅ CORRECT: animate=200
```

### Modern Progress Stepper
```python
def create_step_badge(self, step_num, step_text, step_icon, is_completed, is_current):
    """Create modern step badge with icon and text"""
    if is_completed:
        bg_color = ft.Colors.GREEN_700
        text_color = ft.Colors.WHITE
        icon = ft.Icons.CHECK_CIRCLE
    elif is_current:
        bg_color = ft.Colors.BLUE_600
        text_color = ft.Colors.WHITE
        icon = step_icon
    else:
        bg_color = ft.Colors.GREY_800
        text_color = ft.Colors.GREY_500
        icon = step_icon
    
    return ft.Container(
        content=ft.Row([
            ft.Icon(icon, color=text_color, size=18),
            ft.Text(f"{step_num}. {step_text}", 
                   color=text_color, size=13, weight=ft.FontWeight.W_500),
        ], spacing=8, tight=True),
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        bgcolor=bg_color,
        border_radius=20,
        animate=300,  # ✅ Integer milliseconds
    )

def create_step_connector(self, is_completed):
    """Create connector line between steps"""
    return ft.Container(
        width=40, height=2,
        bgcolor=ft.Colors.GREEN_700 if is_completed else ft.Colors.GREY_700,
        margin=ft.margin.symmetric(horizontal=5),
    )
```

### Footer Navigation Bar
```python
# Modern footer with navigation buttons
footer = ft.Container(
    content=ft.Row([
        btn_back,
        btn_next,
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
    padding=ft.padding.symmetric(horizontal=30, vertical=20),
    bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
    border=ft.border.only(top=ft.BorderSide(1, ft.Colors.GREY_800)),
)
```

### Zero-Padding Layout Structure
```python
# Modern approach: No page padding, use containers
self.page.padding = 0

# Precise layout control with containers
self.page.add(
    ft.Column([
        header,  # Gradient header (no padding)
        ft.Container(
            content=step_indicator,
            padding=ft.padding.symmetric(vertical=20),
        ),
        ft.Container(
            content=main_content,
            padding=30,
            expand=True,  # Takes remaining space
        ),
        footer,  # Navigation bar (no padding)
    ], spacing=0, expand=True)
)
```

### Modern Color Palette
```python
# 2025 Modern Colors
PRIMARY_BLUE = "#3b82f6"      # Bright accent color
DARK_BLUE = "#1e3a8a"         # Header gradients
SUCCESS_GREEN = "#16a34a"     # Completed states
GREY_800 = "#1f2937"          # Background elements
GREY_700 = "#374151"          # Borders and dividers

# Gradient combinations
BLUE_GRADIENT = ["#1e3a8a", "#3b82f6"]
DARK_GRADIENT = ["#1f2937", "#111827"]
```

### Design Principles
1. **Maximize by default**: Desktop apps should start maximized
2. **Zero page padding**: Use containers for precise spacing control
3. **Gradients over solid colors**: Modern headers use gradients
4. **Container buttons**: More flexible than ElevatedButton
5. **Badge-style steppers**: Pills with rounded corners and icons
6. **Ink ripple effects**: Add `ink=True` to interactive containers
7. **Smooth animations**: 200-500ms with EASE_OUT curves
8. **Dark theme first**: Modern standard is ThemeMode.DARK
9. **Footer navigation**: Fixed bottom bar for navigation buttons
10. **Icon + Text**: Always pair buttons with both icon and text

