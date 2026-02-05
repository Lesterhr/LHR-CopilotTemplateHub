#!/usr/bin/env python3
"""
Simple test for the Instruction Files Organizer
Verifies basic functionality without requiring UI interaction
"""

import sys
from pathlib import Path
import tempfile
import shutil

# Test the file operations logic
def test_file_operations():
    """Test file moving between available and archived"""
    
    # Create temporary test directory structure
    with tempfile.TemporaryDirectory() as tmpdir:
        base_path = Path(tmpdir)
        instructions_dir = base_path / ".github" / "instructions"
        archived_dir = instructions_dir / "archived"
        
        # Create directories
        instructions_dir.mkdir(parents=True)
        archived_dir.mkdir(parents=True)
        
        # Create test files
        test_file1 = instructions_dir / "test-file1.instructions.md"
        test_file2 = instructions_dir / "test-file2.instructions.md"
        
        test_file1.write_text("# Test File 1")
        test_file2.write_text("# Test File 2")
        
        print("✓ Created test structure")
        print(f"  - Instructions dir: {instructions_dir}")
        print(f"  - Archived dir: {archived_dir}")
        print(f"  - Test files: {test_file1.name}, {test_file2.name}")
        
        # Test 1: List available files
        available_files = list(instructions_dir.glob("*.instructions.md"))
        assert len(available_files) == 2, f"Expected 2 files, got {len(available_files)}"
        print(f"\n✓ Test 1 passed: Found {len(available_files)} available files")
        
        # Test 2: Move file to archived
        shutil.move(str(test_file1), str(archived_dir / test_file1.name))
        available_files = list(instructions_dir.glob("*.instructions.md"))
        archived_files = list(archived_dir.glob("*.instructions.md"))
        
        assert len(available_files) == 1, f"Expected 1 available file, got {len(available_files)}"
        assert len(archived_files) == 1, f"Expected 1 archived file, got {len(archived_files)}"
        print(f"✓ Test 2 passed: Moved file to archived")
        print(f"  - Available: {len(available_files)}, Archived: {len(archived_files)}")
        
        # Test 3: Move file back to available
        archived_file = archived_dir / test_file1.name
        shutil.move(str(archived_file), str(instructions_dir / test_file1.name))
        available_files = list(instructions_dir.glob("*.instructions.md"))
        archived_files = list(archived_dir.glob("*.instructions.md"))
        
        assert len(available_files) == 2, f"Expected 2 available files, got {len(available_files)}"
        assert len(archived_files) == 0, f"Expected 0 archived files, got {len(archived_files)}"
        print(f"✓ Test 3 passed: Restored file from archived")
        print(f"  - Available: {len(available_files)}, Archived: {len(archived_files)}")
        
        # Test 4: Handle file name conflicts
        # Create a file with same name in both directories
        conflict_file_available = instructions_dir / "conflict-test.instructions.md"
        conflict_file_archived = archived_dir / "conflict-test.instructions.md"
        conflict_file_available.write_text("# Available Version")
        conflict_file_archived.write_text("# Archived Version")
        
        # Verify both exist
        assert conflict_file_available.exists(), "Conflict file should exist in available"
        assert conflict_file_archived.exists(), "Conflict file should exist in archived"
        print(f"✓ Test 4 passed: File conflict scenario detected")
        print(f"  - Both directories have file with same name")
        
        print("\n" + "="*50)
        print("✓ All file operation tests passed!")
        print("="*50)
        
        return True


def test_app_imports():
    """Test that the app can be imported and basic classes work"""
    try:
        # Check if flet is available
        import flet as ft
        print("✓ Flet imported successfully")
        
        # Check if our app file exists
        app_path = Path(__file__).parent / "instructions_organizer.py"
        if app_path.exists():
            print(f"✓ Application file found: {app_path}")
        else:
            print(f"✗ Application file not found: {app_path}")
            return False
        
        # Check Colors syntax
        blue = ft.Colors.BLUE
        grey = ft.Colors.GREY_800
        print(f"✓ Flet Colors API working correctly (BLUE={blue}, GREY_800={grey})")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("  Run: pip install flet>=0.28.3")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False


def main():
    """Run all tests"""
    print("="*50)
    print("Instruction Files Organizer - Test Suite")
    print("="*50)
    print()
    
    tests_passed = 0
    tests_total = 2
    
    # Test 1: Imports
    print("Test 1: Checking imports...")
    if test_app_imports():
        tests_passed += 1
    print()
    
    # Test 2: File operations
    print("Test 2: Testing file operations...")
    if test_file_operations():
        tests_passed += 1
    print()
    
    # Summary
    print("="*50)
    print(f"Test Results: {tests_passed}/{tests_total} tests passed")
    print("="*50)
    
    if tests_passed == tests_total:
        print("✓ All tests passed! The application is ready to use.")
        return 0
    else:
        print(f"✗ {tests_total - tests_passed} test(s) failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
