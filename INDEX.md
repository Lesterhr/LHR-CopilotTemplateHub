# Copilot Instructions Index

> **Purpose**: This file guides AI agents on which templates to use and when. Templates are organized following GitHub Copilot best practices.

## Repository Structure

This repository follows GitHub Copilot's official structure for custom instructions:

- **Repository-wide instructions**: `.github/copilot-instructions.md` - Applies to all requests in this repository
- **Path-specific instructions**: `.github/instructions/*.instructions.md` - Applies based on file context and patterns

## Available Templates

### 🎨 **flet-agent.instructions.md** (v1.0.0)
- **Type**: GUI Framework
- **Location**: `.github/instructions/flet-agent.instructions.md`
- **When to use**: Building Flet-based desktop applications
- **Applies to**: Python GUI projects, desktop apps with Flet framework
- **Priority**: High (1)
- **Key features**: App structure, color scheme, threading patterns, view navigation

---

### 🏭 **s3d-symbol-navigation-guide.instructions.md** (v1.0.0)
- **Type**: Domain-Specific
- **Location**: `.github/instructions/s3d-symbol-navigation-guide.instructions.md`
- **When to use**: Working with SmartPlant 3D symbols, templates, or piping instrumentation
- **Applies to**: S3D symbol discovery, DLL parsing, template folder traversal
- **Priority**: Medium (2)
- **Key features**: Symbol hierarchy, recursive discovery patterns, partsheet handling

---

### 📐 **smartsketch-readme.instructions.md** (v1.0.0)
- **Type**: Project Context
- **Location**: `.github/instructions/smartsketch-readme.instructions.md`
- **When to use**: SmartSketch development or COM automation projects
- **Applies to**: SmartSketch Add-Ins, COM/ActiveX integration
- **Priority**: High (1)
- **Key features**: Project structure, library references, COM technology stack

---

### 🔌 **smartsketch-integration-guide.instructions.md** (v1.0.0)
- **Type**: Integration Guide
- **Location**: `.github/instructions/smartsketch-integration-guide.instructions.md`
- **When to use**: Implementing SmartSketch API integrations
- **Applies to**: API wrappers, command implementations, event handlers
- **Priority**: Medium (2)
- **Key features**: Object model, COM cleanup, command patterns, event handling
- **Works with**: Use alongside smartsketch-readme.instructions.md

---

## Template Combination Rules

### Multiple Template Scenarios

#### **Flet + SmartSketch Project**
```
Priority Order:
1. flet-gui-template.instructions.md → UI structure and styling
2. smartsketch-integration-guide.instructions.md → CAD integration logic
3. smartsketch-readme.instructions.md → Project setup and references

Rules:
- Use Flet patterns for all GUI components
- Use SmartSketch patterns for CAD automation
- Keep UI and CAD logic separated (different modules)
```

#### **SmartSketch + S3D Project**
```
Priority Order:
1. smartsketch-readme.instructions.md → Base SmartSketch context
2. smartsketch-integration-guide.instructions.md → API patterns
3. s3d-symbol-navigation-guide.instructions.md → Symbol handling specifics

Rules:
- SmartSketch templates provide base COM automation patterns
- S3D template adds symbol discovery and template parsing
- Both use similar COM/ActiveX approaches
```

#### **Single Template Usage**
- If only one template is active, follow it exclusively
- No conflicts or priority resolution needed

---

## How AI Agents Should Read This

### 1. **Check Active Templates**
Look in `.github/instructions/` directory for all `*.instructions.md` files present.

### 2. **Read Repository-Wide Instructions**
Check `.github/copilot-instructions.md` for general guidance that applies to all work in this repository.

### 3. **Determine Context**
- Check current file path and imports
- Match against "Applies to" in template metadata
- Use priority to resolve conflicts

### 4. **Apply Patterns**
- Follow repository-wide instructions for general guidance
- Follow the template with highest priority for the current file type
- Reference secondary templates for cross-cutting concerns
- Ignore templates that don't apply to current context

### 4. **Conflict Resolution**
If multiple templates suggest different patterns:
1. **Repository-wide instructions** provide base context for all work
2. **Project-specific** templates override **general** templates
3. **Higher priority** (lower number) takes precedence
4. **Integration guides** complement base templates (additive, not exclusive)
5. When unsure, preserve existing code style

---

## Template Metadata Quick Reference

| Template | Type | Priority | Version | Tags |
|----------|------|----------|---------|------|
| FLET_GUI_TEMPLATE | gui-framework | 1 | 1.0.0 | flet, python, desktop |
| s3d-symbol-instructions | domain-specific | 2 | 1.0.0 | s3d, piping, symbols |
| SmartSketch-README | project-context | 1 | 1.0.0 | smartsketch, com, cad |
| SmartSketch-INTEGRATION_GUIDE | integration-guide | 2 | 1.0.0 | api, automation |

---

## Updating Templates

Templates are maintained in this repository: `github.com/Lesterhr/LHR-CopilotTemplateHub`

### To get the latest versions:
1. Visit the template repository
2. Check for updates in `.github/instructions/` directory
3. Download updated templates from `.github/instructions/` folder
4. Replace files in your local `.github/instructions/` directory

### Template locations:
- **Repository-wide**: `.github/copilot-instructions.md`
- **Path-specific**: `.github/instructions/*.instructions.md`

**Last Updated**: 2025-11-14  
**Template Source Version**: 1.0.0
