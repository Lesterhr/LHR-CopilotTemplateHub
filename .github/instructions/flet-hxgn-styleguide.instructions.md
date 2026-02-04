# Flet UI Style Guide - Intergraph Hexagon Design System

**Name:** flet_hxgn_styleguide  
**Description:** Visual design patterns and styling conventions for Flet applications following the Intergraph Hexagon aesthetic

## Overview

This guide defines the visual design language for Flet applications based on the Intergraph Hexagon color scheme. It covers colors, transparency effects, component styling, animations, and layout patterns to create modern, professional desktop applications matching the Hexagon/Intergraph brand identity.

## Design Philosophy

### Core Principles
- **Modern & Professional**: Clean, minimalist design with purposeful visual hierarchy
- **Semi-Transparent Layers**: Use Windows API transparency for a glass-like, modern appearance
- **Smooth Animations**: Fluid transitions and micro-interactions for polished UX
- **Dark Theme First**: Optimized for dark mode with high contrast elements
- **Consistent Spacing**: Uniform padding, margins, and spacing throughout

---

## Color Palette

### Primary Colors

#### Background Colors
```python
# Main app background - Cool white (Hexagon software)
page.bgcolor = "#F5F5F5"                # Cool white background

# Secondary surface backgrounds
surface_bg = "#FFFFFF"                  # Pure white - Content areas, cards
surface_dark = "#3A3A3A"                # Dark gray - Sidebar, navigation
surface_medium = "#E6E6E6"              # Light gray - Secondary surfaces
surface_accent = "#505050"              # Medium gray - Hover states
```

#### Accent Colors
```python
# Primary accent - Hexagon Corporate Blue
primary_blue = "#005B8E"                # Hexagon corporate blue (header, primary actions)
primary_blue_light = "#0091DA"          # Lighter blue variant (hover, active states)
primary_blue_dark = "#00405F"           # Darker blue variant (pressed states)

# Status colors
success = "#8CC63F"                     # Hexagon green - Success states
success_bg = "#6BA02F"                  # Darker green - Success buttons/backgrounds
warning = "#FFA500"                     # Orange - Warning states  
warning_bg = "#CC8400"                  # Darker orange - Warning backgrounds
error = "#E31E24"                       # Hexagon red - Error states
error_bg = "#B71C1C"                    # Darker red - Error backgrounds
info = "#0091DA"                        # Hexagon light blue - Info states
info_bg = "#005B8E"                     # Hexagon corporate blue - Info backgrounds
```

#### Text Colors
```python
# Text hierarchy
text_primary = ft.Colors.WHITE          # Headings, important text
text_secondary = ft.Colors.WHITE70      # Subtitles, descriptions
text_tertiary = "#999999"               # Helper text, disabled
```

### Color Usage Guidelines

**Headers & Titles**: Use `ft.Colors.WHITE` with bold font weights on Hexagon blue (#005B8E)  
**Descriptions**: Use `ft.Colors.WHITE70` for subtitle text  
**Status Messages**: Match color to context (GREEN (#8CC63F) for success, ORANGE (#FFA500) for warnings, RED (#E31E24) for errors)  
**Helper Text**: Use `#7F7F7F` (medium gray) with italic styling  
**Primary Actions**: Use Hexagon corporate blue (#005B8E) for buttons and key interactions  
**Secondary Actions**: Use light gray (#E6E6E6) or medium gray (#505050) for secondary buttons

---

## Typography

### Font Weights
```python
# Headings and emphasis
ft.FontWeight.BOLD              # Main headings (size 20-32)
ft.FontWeight.W_500             # Buttons, badges, section titles

# Body text - use default weight
```

### Text Sizes
```python
# Hierarchy
page_title = 32                 # Main app title
section_heading = 20            # Major sections
subsection_heading = 18         # Subsections
label = 16                      # Standard labels
body = 14                       # Body text, buttons
caption = 13                    # Step indicators
helper = 12                     # Helper text, metadata
```

### Example Typography
```python
# Main header
ft.Text("AI-Promptbook", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)

# Subtitle
ft.Text("GitHub Repository Creator", size=14, color=ft.Colors.WHITE70)

# Section heading
ft.Text("Repository Details", size=20, weight=ft.FontWeight.BOLD)

# Helper text
ft.Text("Token erstellen: GitHub -> Settings...", 
        size=12, color="#999999", italic=True)
```

---

## Component Styling

### Containers & Cards

#### Standard Container
```python
ft.Container(
    content=...,
    padding=15,                        # Standard padding
    bgcolor="#005B8E",                 # Hexagon corporate blue
    border_radius=10,                  # Rounded corners
)
```

#### Status Card (Info/Warning/Success)
```python
# Success variant
ft.Container(
    content=ft.Row([
        ft.Icon(ft.Icons.CHECK_CIRCLE, color="#8CC63F"),
        ft.Text("Authentifiziert als user", color="#8CC63F", size=16),
    ]),
    padding=15,
    bgcolor="#6BA02F",                 # Hexagon green background (darker)
    border_radius=10,
)

# Warning variant  
ft.Container(
    content=ft.Row([
        ft.Icon(ft.Icons.INFO_OUTLINE, color="#FFA500"),
        ft.Text("Bitte wählen Sie...", color="#FFA500", size=14),
    ]),
    padding=15,
    bgcolor="#CC8400",                 # Darker orange background
    border_radius=10,
)
```

### Buttons

#### Primary Button (Call-to-Action)
```python
ft.Container(
    content=ft.Row([
        ft.Text("Weiter", size=14, weight=ft.FontWeight.W_500),
        ft.Icon(ft.Icons.ARROW_FORWARD, size=18),
    ], spacing=8, tight=True),
    padding=ft.padding.symmetric(horizontal=24, vertical=12),
    bgcolor="#005B8E",                 # Hexagon corporate blue for primary actions
    border_radius=8,
    on_click=callback,
    ink=True,                          # Ripple effect
    animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_CUBIC),
)
```

#### Secondary Button (Back/Cancel)
```python
ft.Container(
    content=ft.Row([
        ft.Icon(ft.Icons.ARROW_BACK, size=18),
        ft.Text("Zurück", size=14, weight=ft.FontWeight.W_500),
    ], spacing=8, tight=True),
    padding=ft.padding.symmetric(horizontal=24, vertical=12),
    bgcolor="#0091DA",                 # Hexagon light blue for secondary
    border_radius=8,
    on_click=callback,
    ink=True,
    animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_CUBIC),
)
```

#### Success Button
```python
ft.ElevatedButton(
    "Repository erstellen",
    icon=ft.Icons.ROCKET_LAUNCH,
    on_click=callback,
    bgcolor="#8CC63F",                 # Hexagon green for positive actions
    height=50,
)
```

#### Standard Button (Less Emphasis)
```python
ft.ElevatedButton(
    "Token laden",
    icon=ft.Icons.LOGIN,
    on_click=callback,
    # Uses default styling
)
```

### Headers

#### Gradient Header (Hero Element)
```python
ft.Container(
    content=ft.Column([
        ft.Text(
            "AI-Promptbook",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE
        ),
        ft.Text(
            "GitHub Repository Creator & Project Manager",
            size=14,
            color=ft.Colors.WHITE70
        ),
    ], spacing=5),
    padding=25,
    gradient=ft.LinearGradient(
        begin=ft.alignment.center_left,
        end=ft.alignment.center_right,
        colors=["#00405F", "#005B8E"],  # Hexagon corporate blue gradient
    ),
    border_radius=ft.border_radius.only(bottom_left=15, bottom_right=15),
)
```

### Navigation Footer

#### Bottom Navigation Bar
```python
ft.Container(
    content=ft.Row(
        controls=[btn_back, btn_next],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    ),
    padding=ft.padding.symmetric(horizontal=30, vertical=20),
    bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),  # Subtle overlay
    border=ft.border.only(top=ft.BorderSide(1, "#505050")),
)
```

### Step Indicators

#### Wizard Progress Indicator
```python
# Completed step
ft.Container(
    content=ft.Row([
        ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.WHITE, size=18),
        ft.Text("1. Token", color=ft.Colors.WHITE, size=13, weight=ft.FontWeight.W_500),
    ], spacing=8, tight=True),
    padding=ft.padding.symmetric(horizontal=16, vertical=10),
    bgcolor="#8CC63F",                 # Hexagon green for completed
    border_radius=20,                  # Pill shape
    animate=ft.Animation(400, ft.AnimationCurve.EASE_OUT_CUBIC),
)

# Current step
ft.Container(
    content=ft.Row([
        ft.Icon(ft.Icons.FOLDER_SPECIAL, color=ft.Colors.WHITE, size=18),
        ft.Text("2. Repository", color=ft.Colors.WHITE, size=13, weight=ft.FontWeight.W_500),
    ], spacing=8, tight=True),
    padding=ft.padding.symmetric(horizontal=16, vertical=10),
    bgcolor="#005B8E",                 # Hexagon corporate blue for current
    border_radius=20,
    animate=ft.Animation(400, ft.AnimationCurve.EASE_OUT_CUBIC),
)

# Future step
ft.Container(
    content=ft.Row([
        ft.Icon(ft.Icons.SETTINGS_APPLICATIONS, color="#FFFFFF", size=18),
        ft.Text("3. Projekt Setup", color="#FFFFFF", size=13, weight=ft.FontWeight.W_500),
    ], spacing=8, tight=True),
    padding=ft.padding.symmetric(horizontal=16, vertical=10),
    bgcolor="#B0BEC5",                 # Light gray-blue for future
    border_radius=20,
    animate=ft.Animation(400, ft.AnimationCurve.EASE_OUT_CUBIC),
)

# Connector between steps
ft.Container(
    width=40,
    height=2,
    bgcolor="#8CC63F",                 # Match step state
    margin=ft.margin.symmetric(horizontal=5),
    animate=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
)
```

### Input Fields

#### Text Field
```python
ft.TextField(
    label="Repository Name *",
    hint_text="mein-projekt",
    width=500,                         # Consistent widths
)

# Multiline variant
ft.TextField(
    label="Beschreibung",
    hint_text="Eine kurze Beschreibung...",
    width=500,
    multiline=True,
    min_lines=3,
    max_lines=5,
)

# Password field with reveal
ft.TextField(
    label="GitHub Personal Access Token",
    password=True,
    can_reveal_password=True,
    width=500,
    hint_text="ghp_xxxxxxxxxxxxxxxxxxxx",
)
```

#### Dropdown
```python
ft.Dropdown(
    label="Projekt-Sprache",
    width=300,
    value="python",
    options=[
        ft.dropdown.Option("python", "Python"),
        ft.dropdown.Option("javascript", "JavaScript/Node.js"),
        ft.dropdown.Option("general", "Allgemein/Andere"),
    ],
)
```

#### Checkbox
```python
ft.Checkbox(
    label="Privates Repository",
    value=False,
)
```

### Dialogs

#### Alert Dialog
```python
ft.AlertDialog(
    title=ft.Text("Gespeicherte Tokens verwalten"),
    content=ft.Container(
        content=...,
        width=400,
        height=300,
    ),
    actions=[
        ft.TextButton("Schließen", on_click=close_callback),
    ],
)
```

### Notifications

#### SnackBar
```python
# Success notification
ft.SnackBar(
    content=ft.Text("Authentifizierung erfolgreich!", color=ft.Colors.WHITE),
    bgcolor="#8CC63F",                 # Hexagon green
)

# Warning notification
ft.SnackBar(
    content=ft.Text("Bitte wählen Sie einen Token aus", color=ft.Colors.WHITE),
    bgcolor="#FFA500",                 # Orange
)

# Error notification
ft.SnackBar(
    content=ft.Text("Token konnte nicht geladen werden", color=ft.Colors.WHITE),
    bgcolor="#E31E24",                 # Hexagon red
)

# Info notification
ft.SnackBar(
    content=ft.Text("Information", color=ft.Colors.WHITE),
    bgcolor="#0091DA",                 # Hexagon light blue
)
```

---

## Animations

### Animation Curves & Durations

```python
# Standard transitions
ft.Animation(300, ft.AnimationCurve.EASE_OUT_CUBIC)   # Buttons, simple elements

# Smooth, emphasized transitions  
ft.Animation(400, ft.AnimationCurve.EASE_OUT_CUBIC)   # Step indicators

# Complex transitions
ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT_CUBIC) # Page slides
```

### Page Transitions (Wizard Steps)

#### Slide-Out → Slide-In Pattern
```python
# Step 1: Slide current content OUT to left
animated_container.offset = ft.Offset(-1, 0)
page.update()
time.sleep(0.75)

# Step 2: Disable animation, jump to right
animated_container.animate_offset = None
animated_container.offset = ft.Offset(1, 0)

# Step 3: Update content while off-screen
content_area.controls.clear()
# ... add new content ...
page.update()
time.sleep(0.1)

# Step 4: Re-enable animation, slide IN from right
animated_container.animate_offset = ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT_CUBIC)
page.update()
time.sleep(0.02)
animated_container.offset = ft.Offset(0, 0)
```

---

## Layout Patterns

### Page Structure

```python
ft.Column([
    header,                   # Gradient header (no spacing)
    step_indicator,           # Step progress
    main_content,             # Scrollable content (expand=True)
    navigation,               # Bottom button bar
], spacing=0, expand=True)
```

### Spacing Guidelines

```python
# Container padding
tight_padding = 10           # Compact elements
standard_padding = 15        # Cards, info boxes
generous_padding = 25        # Headers, major sections
section_padding = 30         # Main content area

# Margins and spacing
element_spacing = 5          # Tight grouping (e.g., title + subtitle)
standard_spacing = 20        # Between form sections
divider_height = 30          # Visual separation

# Symmetrical padding helper
ft.padding.symmetric(horizontal=24, vertical=12)
```

### Widths

```python
# Standard component widths
text_field_width = 500       # Primary input fields
dropdown_width = 300         # Dropdowns, secondary inputs
dialog_width = 400           # Modal dialogs
```

---

## Windows-Specific Features

### Transparency Effect

```python
def apply_windows_transparency(self):
    """Apply 95% opacity via Windows API for glass effect"""
    try:
        hwnd = ctypes.windll.user32.FindWindowW(None, self.page.title)
        if hwnd:
            GWL_EXSTYLE = -20
            WS_EX_LAYERED = 0x80000
            LWA_ALPHA = 0x2
            
            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_LAYERED)
            
            alpha = int(0.95 * 255)  # 95% opacity
            ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, alpha, LWA_ALPHA)
    except Exception as e:
        print(f"Could not apply Windows transparency: {e}")
```

**Usage**: Call after page content is added and window is created:
```python
self.page.update()
time.sleep(0.1)  # Ensure window is created
self.apply_windows_transparency()
```

### Window Configuration

```python
page.window_width = 1200
page.window_height = 800
page.window_resizable = True
page.window.maximized = True        # Start maximized
page.scroll = ft.ScrollMode.HIDDEN  # Disable page-level scroll
```

---

## Theme Configuration

### Page-Level Settings

```python
page.title = "AI-Promptbook - GitHub Repo Creator"
page.theme_mode = ft.ThemeMode.LIGHT
page.bgcolor = "#F5F5F5"             # Hexagon cool white background
page.padding = 0                     # Full-bleed layout
```

---

## Common Patterns

### Status Feedback Pattern

```python
# During operation
progress_ring.visible = True
status_text.value = "Erstelle Repository..."
status_text.color = "#0091DA"        # Hexagon light blue
page.update()

# Success
status_text.value = "Fertig!"
status_text.color = "#8CC63F"        # Hexagon green
progress_ring.visible = False
page.update()

# Error
status_text.value = f"Fehler: {message}"
status_text.color = "#E31E24"        # Hexagon red
progress_ring.visible = False
page.update()
```

### Form Validation Pattern

```python
def validate_and_proceed(self, e):
    if not self.required_field.value:
        self.show_snackbar(
            "Bitte füllen Sie alle Pflichtfelder aus!", 
            "#FFA500"                  # Orange warning
        )
        return
    
    # Proceed with valid data
    self.next_step()
```

### Conditional UI Updates

```python
def toggle_options(self, e):
    """Enable/disable related controls"""
    enabled = self.checkbox.value
    self.related_input.disabled = not enabled
    self.page.update()
```

---

## Accessibility Considerations

### Visual Hierarchy
- Use bold weights for headings
- Maintain consistent spacing between sections
- Use color + icons for status (not color alone)

### Interactive Elements
- Include ripple effects (`ink=True`) for tactile feedback
- Use descriptive labels for all inputs
- Add icons to buttons for visual clarity

### Status Communication
- Always pair status colors with icons
- Provide text descriptions, not just color changes
- Use SnackBar for important notifications

---

## Icon Usage

### Common Icons

```python
# Navigation
ft.Icons.ARROW_FORWARD       # Next/Proceed
ft.Icons.ARROW_BACK          # Back/Cancel

# Status
ft.Icons.CHECK_CIRCLE        # Success/Completed
ft.Icons.INFO_OUTLINE        # Information/Warning
ft.Icons.ERROR_OUTLINE       # Error

# Actions
ft.Icons.LOGIN               # Authentication
ft.Icons.VPN_KEY             # Tokens/Keys
ft.Icons.FOLDER_OPEN         # Browse files
ft.Icons.ROCKET_LAUNCH       # Create/Deploy
ft.Icons.SETTINGS            # Configuration
ft.Icons.DELETE              # Remove

# Content
ft.Icons.FOLDER_SPECIAL      # Repository
ft.Icons.SETTINGS_APPLICATIONS # Project setup
ft.Icons.ACCOUNT_CIRCLE      # User profile
```

### Icon Sizing
```python
small_icon = 16              # List items, inline
standard_icon = 18           # Buttons, badges
large_icon = 24              # Headers, emphasis
```

---

## Complete Example

### Full Step Implementation

```python
def show_example_step(self):
    """Example step with complete styling"""
    
    # Status card
    status_card = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.CHECK_CIRCLE, color="#8CC63F"),
            ft.Text("Ready to proceed", color="#8CC63F", size=16),
        ]),
        padding=15,
        bgcolor="#6BA02F",
        border_radius=10,
    )
    
    # Section heading
    heading = ft.Text("Configuration", size=20, weight=ft.FontWeight.BOLD)
    
    # Input field
    name_input = ft.TextField(
        label="Project Name *",
        hint_text="my-project",
        width=500,
    )
    
    # Checkbox with description
    option_checkbox = ft.Checkbox(
        label="Enable advanced features",
        value=True,
    )
    
    # Action button
    submit_button = ft.ElevatedButton(
        "Continue",
        icon=ft.Icons.ARROW_FORWARD,
        on_click=self.handle_submit,
        bgcolor="#005B8E",             # Hexagon corporate blue
        height=50,
    )
    
    # Progress indicator (initially hidden)
    progress = ft.ProgressRing(visible=False)
    status = ft.Text("")
    
    # Add to content area
    self.content_area.controls.extend([
        status_card,
        ft.Container(height=10),
        heading,
        name_input,
        option_checkbox,
        ft.Divider(height=30),
        ft.Row([submit_button, progress]),
        status,
    ])
```

---

## Summary Checklist

✅ **Colors**: Use Hexagon cool white background (#F5F5F5) with corporate blue gradient headers (#005B8E)  
✅ **Transparency**: Apply 95% opacity via Windows API  
✅ **Buttons**: Hexagon corporate blue (#005B8E) for primary, light blue (#0091DA) for secondary, Hexagon green (#8CC63F) for success  
✅ **Animations**: 300-800ms with EASE_OUT_CUBIC curves  
✅ **Typography**: Bold headers (32/20/18px), regular body (14px)  
✅ **Status**: GREEN (#8CC63F)=success, ORANGE (#FFA500)=warning, RED (#E31E24)=error, BLUE (#0091DA)=info  
✅ **Spacing**: 15-25px padding, 20-30px spacing between sections  
✅ **Borders**: 8-10px border radius for cards/buttons, use #E6E6E6 borders on white backgrounds  
✅ **Icons**: Pair with buttons and status messages  
✅ **Layout**: Header → Progress → Content → Navigation

This style guide ensures consistency across all Flet UI implementations following the Intergraph Hexagon design language.
