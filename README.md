# Copilot Templates Repository

Centralized, versioned templates for AI-assisted development across multiple tools and projects.

## 📚 Available Templates

### 🎨 **Flet GUI Template** (v1.0.0)
Desktop GUI patterns using Flet framework
- **File**: `flet-gui-template.instructions.md`
- **Use for**: Python desktop applications with Flet
- **Tags**: `flet`, `gui`, `python`, `desktop-app`

### 🏭 **S3D Symbol Instructions** (v1.0.0)
SmartPlant 3D symbol discovery and template parsing
- **File**: `s3d-symbol-navigation-guide.instructions.md`
- **Use for**: S3D symbol discovery, piping instrumentation
- **Tags**: `s3d`, `smartplant-3d`, `symbols`, `piping`

### 📐 **SmartSketch README** (v1.0.0)
SmartSketch project context and COM automation
- **File**: `smartsketch-readme.instructions.md`
- **Use for**: SmartSketch Add-In development
- **Tags**: `smartsketch`, `intergraph`, `cad`, `com-automation`

### 🔌 **SmartSketch Integration Guide** (v1.0.0)
SmartSketch API integration patterns
- **File**: `smartsketch-integration-guide.instructions.md`
- **Use for**: SmartSketch API automation and commands
- **Tags**: `smartsketch`, `api-integration`, `com-automation`

## 🚀 Usage

### For AI-Promptbook
Templates are automatically available in the repository creation wizard.

### Direct Download (Latest Version)
```bash
# Download manifest
curl -O https://raw.githubusercontent.com/Lesterhr/copilot-templates/main/manifest.json

# Download specific template
curl -O https://raw.githubusercontent.com/Lesterhr/copilot-templates/main/flet-gui-template.instructions.md
```

### Download Specific Version
```bash
# Replace v1.0.0 with desired version tag
curl -O https://raw.githubusercontent.com/Lesterhr/copilot-templates/v1.0.0/flet-gui-template.instructions.md
```

## 📋 Template Structure

Each template includes:
- **Metadata Header**: YAML frontmatter with version, type, priority
- **AI Usage Section**: Clear instructions for when and how AI agents should apply the template
- **Content**: Detailed patterns, examples, and best practices

## 🔄 Versioning

- **Template versions**: Individual version per template (e.g., v1.0.0)
- **Repository versions**: Tagged releases (e.g., v1.0.0)
- **Semantic versioning**: MAJOR.MINOR.PATCH
  - MAJOR: Breaking changes in template structure
  - MINOR: New templates or significant additions
  - PATCH: Fixes and minor improvements

## 📦 File Structure

```
copilot-templates/
├── manifest.json                                      # Template registry
├── INDEX.md                                           # Human-readable index
├── README.md                                          # This file
├── flet-gui-template.instructions.md
├── s3d-symbol-navigation-guide.instructions.md
├── smartsketch-readme.instructions.md
└── smartsketch-integration-guide.instructions.md
```

## 🛠️ For Tool Developers

### Reading Templates Programmatically

```python
import requests
import json

# Fetch manifest
manifest_url = "https://raw.githubusercontent.com/Lesterhr/copilot-templates/main/manifest.json"
manifest = requests.get(manifest_url).json()

# List available templates
for template_name, info in manifest['templates'].items():
    print(f"{template_name} v{info['version']} - {info['description']}")

# Download a template
template_url = f"https://raw.githubusercontent.com/Lesterhr/copilot-templates/main/{template_name}"
template_content = requests.get(template_url).text
```

### Checking for Updates

```python
def check_updates(local_manifest, remote_manifest):
    updates = {}
    for name, remote_info in remote_manifest['templates'].items():
        local_version = local_manifest['templates'].get(name, {}).get('version', '0.0.0')
        remote_version = remote_info['version']
        
        if remote_version > local_version:
            updates[name] = {
                'current': local_version,
                'available': remote_version
            }
    
    return updates
```

## 📝 Contributing

### Adding New Templates

1. Create template with `.instructions.md` suffix (kebab-case naming)
2. Add YAML metadata header
3. Include "How AI Agents Should Use This Template" section
4. Update `manifest.json` with template metadata
5. Update `INDEX.md` with template description
6. Increment repository version
7. Create git tag for new version

### Updating Existing Templates

1. Edit template file
2. Increment version in metadata header
3. Update version in `manifest.json`
4. Add entry to `changelog` in `manifest.json`
5. Update `last_updated` date
6. Create git tag if needed

## 🏷️ Template Naming Convention

All templates must follow this pattern:
```
<descriptive-name>.instructions.md
```

Use kebab-case for multi-word names.

Examples:
- `flet-gui-template.instructions.md`
- `django-rest-api.instructions.md`
- `react-components.instructions.md`

## 📜 License

MIT License - See LICENSE file for details

## 🔗 Related Tools

- **AI-Promptbook**: GitHub repository creator with template integration
- More tools coming soon...

---

**Repository Version**: 1.0.0  
**Last Updated**: 2025-11-14  
**Maintained by**: Lesterhr
