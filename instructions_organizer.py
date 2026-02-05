#!/usr/bin/env python3
"""
Instruction Files Organizer - GUI Application
Manage instruction files between Available and Archived sections with drag and drop.

Following the Flet Style Guide from .github/instructions/flet-styleguide.instructions.md
"""

import flet
import flet as ft
import shutil
import sys
from pathlib import Path


class InstructionFileCard(ft.Container):
    """A draggable card representing an instruction file"""
    
    def __init__(self, filename, is_archived, on_move_callback):
        super().__init__()
        self.filename = filename
        self.is_archived = is_archived
        self.on_move_callback = on_move_callback
        
        # Styling following flet-styleguide
        self.bgcolor = ft.Colors.GREY_800
        self.border_radius = 10
        self.padding = 15
        self.margin = 5
        self.ink = True
        self.animate = ft.Animation(300, ft.AnimationCurve.EASE_OUT_CUBIC)
        
        # Make card draggable
        self.content = ft.Draggable(
            group="instructions",
            content=ft.Row([
                ft.Icon(
                    ft.Icons.DESCRIPTION,
                    color=ft.Colors.BLUE_400,
                    size=24
                ),
                ft.Column([
                    ft.Text(
                        self.get_display_name(),
                        size=14,
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "Archived" if is_archived else "Available",
                        size=12,
                        color=ft.Colors.WHITE70,
                        italic=True,
                    ),
                ], spacing=2, tight=True),
            ], spacing=10),
            content_feedback=ft.Container(
                content=ft.Text(
                    self.get_display_name(),
                    size=14,
                    color=ft.Colors.WHITE,
                ),
                bgcolor=ft.Colors.BLUE_600,
                padding=10,
                border_radius=8,
            ),
            data={"filename": filename, "is_archived": is_archived},
        )
        
    def get_display_name(self):
        """Get a display-friendly name from the filename"""
        # Remove .instructions.md suffix
        name = self.filename.replace('.instructions.md', '')
        # Replace hyphens with spaces and title case
        return name.replace('-', ' ').title()


class DropZone(ft.Container):
    """A drop zone that can accept dragged instruction files"""
    
    def __init__(self, title, is_archived, on_drop_callback):
        super().__init__()
        self.title = title
        self.is_archived = is_archived
        self.on_drop_callback = on_drop_callback
        
        # Styling following flet-styleguide
        self.bgcolor = ft.Colors.with_opacity(0.05, ft.Colors.WHITE)
        self.border_radius = 15
        self.padding = 20
        self.expand = True
        self.border = ft.Border.all(2, ft.Colors.GREY_700)
        
        self.files_column = ft.Column(
            spacing=5,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
        
        # Header with gradient
        header = ft.Container(
            content=ft.Row([
                ft.Icon(
                    ft.Icons.FOLDER_SPECIAL if not is_archived else ft.Icons.ARCHIVE,
                    color=ft.Colors.WHITE,
                    size=24,
                ),
                ft.Text(
                    title,
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
            ], spacing=10),
            padding=15,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, 0),
                end=ft.Alignment(1, 0),
                colors=["#1e3a8a", "#3b82f6"],
            ),
            border_radius=ft.BorderRadius.only(top_left=10, top_right=10),
        )
        
        # Drop target
        self.drop_target = ft.DragTarget(
            group="instructions",
            content=self.files_column,
            on_accept=self.handle_drop,
        )
        
        self.content = ft.Column([
            header,
            ft.Container(height=10),
            self.drop_target,
        ], spacing=0, expand=True)
        
    def handle_drop(self, e):
        """Handle when an instruction file is dropped"""
        # The data is stored in the Draggable's data attribute
        if hasattr(e.control, 'content') and hasattr(e.control.content, 'data'):
            data = e.control.content.data
        else:
            # Extract from the drag event
            data = e.data
            
        if data:
            self.on_drop_callback(data, self.is_archived)
    
    def add_file(self, filename, is_archived, on_move_callback):
        """Add a file card to this drop zone"""
        card = InstructionFileCard(filename, is_archived, on_move_callback)
        self.files_column.controls.append(card)
    
    def clear_files(self):
        """Clear all file cards"""
        self.files_column.controls.clear()


class InstructionsOrganizerApp:
    """Main application for organizing instruction files"""
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.setup_page()
        
        # Paths
        self.instructions_dir = Path(".github/instructions")
        self.archived_dir = self.instructions_dir / "archived"
        
        # Ensure archived directory exists
        self.archived_dir.mkdir(parents=True, exist_ok=True)
        
        # Create UI
        self.create_ui()
        self.load_files()
        
    def setup_page(self):
        """Configure page settings following flet-styleguide"""
        self.page.title = "Instruction Files Organizer"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = "#1a1d23"
        self.page.padding = 0
        self.page.window_width = 1200
        self.page.window_height = 800
        self.page.window_resizable = True
        
    def create_ui(self):
        """Create the main user interface"""
        # Header with gradient
        header = ft.Container(
            content=ft.Column([
                ft.Text(
                    "Instruction Files Organizer",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),
                ft.Text(
                    "Organize instruction files with drag and drop",
                    size=14,
                    color=ft.Colors.WHITE70
                ),
            ], spacing=5),
            padding=25,
            gradient=ft.LinearGradient(
                begin=ft.alignment.center_left,
                end=ft.alignment.center_right,
                colors=["#1e3a8a", "#3b82f6"],
            ),
            border_radius=ft.BorderRadius.only(bottom_left=15, bottom_right=15),
        )
        
        # Create drop zones
        self.available_zone = DropZone(
            "Available Instructions",
            is_archived=False,
            on_drop_callback=self.handle_file_move
        )
        
        self.archived_zone = DropZone(
            "Archived Instructions",
            is_archived=True,
            on_drop_callback=self.handle_file_move
        )
        
        # Main content area
        content = ft.Container(
            content=ft.Row([
                self.available_zone,
                ft.VerticalDivider(width=1, color=ft.Colors.GREY_700),
                self.archived_zone,
            ], spacing=0, expand=True),
            padding=20,
            expand=True,
        )
        
        # Refresh button
        refresh_button = ft.Container(
            content=ft.Row([
                ft.Icon(ft.Icons.REFRESH, size=18),
                ft.Text("Refresh", size=14, weight=ft.FontWeight.W_500),
            ], spacing=8, tight=True),
            padding=ft.Padding.symmetric(horizontal=24, vertical=12),
            bgcolor=ft.Colors.GREY_800,
            border_radius=8,
            ink=True,
            on_click=lambda e: self.refresh_files(),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_CUBIC),
        )
        
        # Footer with refresh button
        footer = ft.Container(
            content=ft.Row([
                ft.Container(expand=True),
                refresh_button,
            ], alignment=ft.MainAxisAlignment.END),
            padding=20,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            border=ft.Border.only(top=ft.BorderSide(1, ft.Colors.GREY_800)),
        )
        
        # Main layout
        self.page.add(
            ft.Column([
                header,
                content,
                footer,
            ], spacing=0, expand=True)
        )
        
    def load_files(self):
        """Load instruction files from directories"""
        # Clear existing files
        self.available_zone.clear_files()
        self.archived_zone.clear_files()
        
        # Load available files
        if self.instructions_dir.exists():
            for file in sorted(self.instructions_dir.glob("*.instructions.md")):
                self.available_zone.add_file(
                    file.name,
                    is_archived=False,
                    on_move_callback=self.handle_file_move
                )
        
        # Load archived files
        if self.archived_dir.exists():
            for file in sorted(self.archived_dir.glob("*.instructions.md")):
                self.archived_zone.add_file(
                    file.name,
                    is_archived=True,
                    on_move_callback=self.handle_file_move
                )
        
        self.page.update()
        
    def handle_file_move(self, data, target_is_archived):
        """Handle moving a file between available and archived"""
        if isinstance(data, dict):
            filename = data.get("filename")
            source_is_archived = data.get("is_archived")
        else:
            # Fallback if data format is different
            return
        
        if not filename:
            return
        
        # Validate and sanitize the filename to prevent path traversal
        safe_filename = Path(filename).name
        
        # Reject if the sanitized name differs (indicating directory components)
        if safe_filename != filename:
            self.show_snackbar("Invalid file name.", ft.Colors.RED_400)
            return
        
        # Ensure it's an instruction file
        if not safe_filename.endswith(".instructions.md"):
            self.show_snackbar("Unsupported file type.", ft.Colors.RED_400)
            return
            
        if source_is_archived != target_is_archived:
            # Determine source and destination paths
            if source_is_archived:
                source_path = self.archived_dir / safe_filename
                dest_path = self.instructions_dir / safe_filename
            else:
                source_path = self.instructions_dir / safe_filename
                dest_path = self.archived_dir / safe_filename
            
            # Move the file
            try:
                if not source_path.exists():
                    self.show_snackbar(
                        f"File not found: {safe_filename}",
                        ft.Colors.ORANGE_400
                    )
                    return
                
                # Check if destination file already exists
                if dest_path.exists():
                    self.show_snackbar(
                        f"Cannot move {safe_filename}: a file with the same name already exists in the destination.",
                        ft.Colors.ORANGE_400
                    )
                    return
                
                # Move the file
                shutil.move(str(source_path), str(dest_path))
                
                # Show success message
                self.show_snackbar(
                    f"Moved {safe_filename} to {'Archived' if target_is_archived else 'Available'}",
                    ft.Colors.GREEN_400
                )
                
                # Reload files
                self.load_files()
                    
            except Exception as ex:
                self.show_snackbar(
                    f"Error moving file: {str(ex)}",
                    ft.Colors.RED_400
                )
    
    def refresh_files(self):
        """Refresh the file list"""
        self.load_files()
        self.show_snackbar("Files refreshed", ft.Colors.BLUE_400)
    
    def show_snackbar(self, message, color):
        """Show a snackbar notification"""
        snackbar = ft.SnackBar(
            content=ft.Text(message, color=ft.Colors.WHITE),
            bgcolor=color,
            duration=3000,
        )
        self.page.overlay.append(snackbar)
        snackbar.open = True
        self.page.update()


def main(page: ft.Page):
    """Main entry point"""
    InstructionsOrganizerApp(page)


if __name__ == "__main__":
    # Parse command-line arguments
    import argparse
    
    parser = argparse.ArgumentParser(description="Instruction Files Organizer GUI")
    parser.add_argument(
        "--view",
        choices=["desktop", "web"],
        default="desktop",
        help="View mode: desktop (default) or web browser"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8550,
        help="Port for web browser mode (default: 8550)"
    )
    
    args = parser.parse_args()
    
    # Determine view mode
    if args.view == "web":
        ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=args.port)
    else:
        ft.app(target=main)
