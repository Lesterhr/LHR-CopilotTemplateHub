# Copilot Instructions Index

> **Purpose**: This file guides AI agents on which templates to use and when. It's automatically generated when templates are copied to new repositories.

## Available Templates

### 🎨 **CopilotInstructions_FLET_GUI_TEMPLATE.md** (v1.0.0)
- **Type**: GUI Framework
- **When to use**: Building Flet-based desktop applications
- **Applies to**: Python GUI projects, desktop apps with Flet framework
- **Priority**: High (1)
- **Key features**: App structure, color scheme, threading patterns, view navigation

---

### 🏭 **CopilotInstructions_s3d-symbol-instructions.md** (v1.0.0)
- **Type**: Domain-Specific
- **When to use**: Working with SmartPlant 3D symbols, templates, or piping instrumentation
- **Applies to**: S3D symbol discovery, DLL parsing, template folder traversal
- **Priority**: Medium (2)
- **Key features**: Symbol hierarchy, recursive discovery patterns, partsheet handling

---

### 📐 **CopilotInstructions_SmartSketch-README.md** (v1.0.0)
- **Type**: Project Context
- **When to use**: SmartSketch development or COM automation projects
- **Applies to**: SmartSketch Add-Ins, COM/ActiveX integration
- **Priority**: High (1)
- **Key features**: Project structure, library references, COM technology stack

---

### 🔌 **CopilotInstructions_SmartSketch-INTEGRATION_GUIDE.md** (v1.0.0)
- **Type**: Integration Guide
- **When to use**: Implementing SmartSketch API integrations
- **Applies to**: API wrappers, command implementations, event handlers
- **Priority**: Medium (2)
- **Key features**: Object model, COM cleanup, command patterns, event handling
- **Works with**: Use alongside SmartSketch-README.md

---

## Template Combination Rules

### Multiple Template Scenarios

#### **Flet + SmartSketch Project**
```
Priority Order:
1. CopilotInstructions_FLET_GUI_TEMPLATE.md → UI structure and styling
2. CopilotInstructions_SmartSketch-INTEGRATION_GUIDE.md → CAD integration logic
3. CopilotInstructions_SmartSketch-README.md → Project setup and references

Rules:
- Use Flet patterns for all GUI components
- Use SmartSketch patterns for CAD automation
- Keep UI and CAD logic separated (different modules)
```

#### **SmartSketch + S3D Project**
```
Priority Order:
1. CopilotInstructions_SmartSketch-README.md → Base SmartSketch context
2. CopilotInstructions_SmartSketch-INTEGRATION_GUIDE.md → API patterns
3. CopilotInstructions_s3d-symbol-instructions.md → Symbol handling specifics

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
Look in this directory for all `CopilotInstructions_*.md` files present.

### 2. **Determine Context**
- Check current file path and imports
- Match against "Applies to" in template metadata
- Use priority to resolve conflicts

### 3. **Apply Patterns**
- Follow the template with highest priority for the current file type
- Reference secondary templates for cross-cutting concerns
- Ignore templates that don't apply to current context

### 4. **Conflict Resolution**
If multiple templates suggest different patterns:
1. **Project-specific** templates override **general** templates
2. **Higher priority** (lower number) takes precedence
3. **Integration guides** complement base templates (additive, not exclusive)
4. When unsure, preserve existing code style

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

Templates are sourced from: `github.com/Lesterhr/copilot-templates`

To get the latest versions:
1. Visit the template repository
2. Check for updates in `manifest.json`
3. Download updated templates manually or via AI-Promptbook
4. Replace files in this `Copilot-Instructions/` folder

**Last Updated**: 2025-11-14
**Template Source Version**: 1.0.0
