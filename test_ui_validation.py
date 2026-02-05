#!/usr/bin/env python3
"""
Validate UI components can be created without errors
"""
import sys
from pathlib import Path
import flet as ft

def validate_ui():
    """Test that all UI components can be instantiated"""
    print("Testing UI component creation...")
    
    # Test gradient with new alignment API
    try:
        gradient = ft.LinearGradient(
            begin=ft.alignment.Alignment.CENTER_LEFT,
            end=ft.alignment.Alignment.CENTER_RIGHT,
            colors=["#1e3a8a", "#3b82f6"],
        )
        print("✓ Gradient with new alignment API works")
    except Exception as e:
        print(f"✗ Gradient failed: {e}")
        return False
    
    # Test that ft.run exists
    if not hasattr(ft, 'run'):
        print("✗ ft.run() not available")
        return False
    print("✓ ft.run() is available")
    
    # Test basic controls
    try:
        text = ft.Text("Test", color=ft.Colors.WHITE)
        container = ft.Container(content=text, bgcolor=ft.Colors.BLUE_900)
        row = ft.Row([container])
        column = ft.Column([row])
        print("✓ Basic controls work")
    except Exception as e:
        print(f"✗ Basic controls failed: {e}")
        return False
    
    print("\n" + "="*50)
    print("✓ All UI validation tests passed!")
    print("="*50)
    return True

if __name__ == "__main__":
    success = validate_ui()
    sys.exit(0 if success else 1)
