# Instruction Files Organizer - UI Mockup

## Main Application View

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                                                                                │
│  ╔══════════════════════════════════════════════════════════════════════════╗ │
│  ║  📋 Instruction Files Organizer                                          ║ │
│  ║  Organize instruction files with drag and drop                           ║ │
│  ╚══════════════════════════════════════════════════════════════════════════╝ │
│                                                                                │
├────────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│  ┌─────────────────────────────────────┬─────────────────────────────────────┐│
│  │ 📁 Available Instructions            │ 📦 Archived Instructions            ││
│  ├─────────────────────────────────────┼─────────────────────────────────────┤│
│  │                                      │                                     ││
│  │  ┌─────────────────────────────┐    │  ┌─────────────────────────────┐   ││
│  │  │ 📄 Flet Agent               │    │  │ 📄 Old Template             │   ││
│  │  │ Available                   │    │  │ Archived                    │   ││
│  │  └─────────────────────────────┘    │  └─────────────────────────────┘   ││
│  │                                      │                                     ││
│  │  ┌─────────────────────────────┐    │  ┌─────────────────────────────┐   ││
│  │  │ 📄 Flet Styleguide          │    │  │ 📄 Deprecated Guide         │   ││
│  │  │ Available                   │    │  │ Archived                    │   ││
│  │  └─────────────────────────────┘    │  └─────────────────────────────┘   ││
│  │                                      │                                     ││
│  │  ┌─────────────────────────────┐    │                                     ││
│  │  │ 📄 Smartsketch Readme       │    │                                     ││
│  │  │ Available                   │    │                                     ││
│  │  └─────────────────────────────┘    │                                     ││
│  │                                      │                                     ││
│  │  ┌─────────────────────────────┐    │                                     ││
│  │  │ 📄 DB Integration Agent     │    │                                     ││
│  │  │ Available                   │    │                                     ││
│  │  └─────────────────────────────┘    │                                     ││
│  │                                      │                                     ││
│  │  [... 14 more files ...]            │                                     ││
│  │                                      │                                     ││
│  └─────────────────────────────────────┴─────────────────────────────────────┘│
│                                                                                │
├────────────────────────────────────────────────────────────────────────────────┤
│                                                              ┌──────────────┐  │
│                                                              │  🔄 Refresh  │  │
│                                                              └──────────────┘  │
└────────────────────────────────────────────────────────────────────────────────┘
```

## Color Scheme (Following flet-styleguide)

- **Background**: Dark anthracite (#1a1d23)
- **Header**: Blue gradient (#1e3a8a → #3b82f6)
- **Cards**: Grey (#4A5568)
- **Text**: White / White70
- **Icons**: Blue (#3b82f6)
- **Success**: Green (#8CC63F)

## Drag and Drop Behavior

### Moving from Available to Archived:
```
1. User clicks on "Flet Agent" card in Available section
2. User drags the card ──────────────────────>
3. Card shows blue highlight during drag
4. User drops card in Archived section
5. File is moved: .github/instructions/ → .github/instructions/archived/
6. Success message: "Moved flet-agent.instructions.md to Archived" (green)
7. UI updates to show file in Archived section
```

### Moving from Archived to Available:
```
1. User clicks on "Old Template" card in Archived section
2. User drags the card <──────────────────────
3. Card shows blue highlight during drag
4. User drops card in Available section
5. File is moved: .github/instructions/archived/ → .github/instructions/
6. Success message: "Moved old-template.instructions.md to Available" (green)
7. UI updates to show file in Available section
```

## Features Demonstrated

✅ **Two-panel layout**: Separate sections for Available and Archived files
✅ **File cards**: Each instruction file shown as a draggable card
✅ **Visual feedback**: Blue highlight during drag, smooth animations
✅ **Status indicators**: "Available" or "Archived" label on each card
✅ **Icons**: File icon (📄) for each instruction file
✅ **Refresh button**: Reload file list without restarting app
✅ **Notifications**: Success, error, and info messages via snackbars
✅ **Scrollable**: Both panels scroll independently when content overflows
✅ **Dark theme**: Modern dark UI following flet-styleguide

## Real Application Screenshot

Due to network restrictions in the test environment, a live screenshot couldn't be captured.
However, when running locally, the application will look similar to the mockup above with:
- Smooth gradient header
- Card-based file display
- Drag-and-drop animations
- Real-time file system integration

## To See the Real UI

Run the application locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python instructions_organizer.py
```

The desktop window will open with the full interactive UI.
