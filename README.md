# Copilot Templates Repository

Centralized, versioned templates for AI-assisted development across multiple tools and projects.

## 📚 Available Templates

### 🎨 **Flet GUI Template** (v1.0.0)
Desktop GUI patterns using Flet framework
- **File**: `.github/instructions/flet-agent.instructions.md`
- **Use for**: Python desktop applications with Flet
- **Tags**: `flet`, `gui`, `python`, `desktop-app`

### 🏭 **S3D Symbol Instructions** (v1.0.0)
SmartPlant 3D symbol discovery and template parsing
- **File**: `.github/instructions/s3d-symbol-navigation-guide.instructions.md`
- **Use for**: S3D symbol discovery, piping instrumentation
- **Tags**: `s3d`, `smartplant-3d`, `symbols`, `piping`

### 📐 **SmartSketch README** (v1.0.0)
SmartSketch project context and COM automation
- **File**: `.github/instructions/smartsketch-readme.instructions.md`
- **Use for**: SmartSketch Add-In development
- **Tags**: `smartsketch`, `intergraph`, `cad`, `com-automation`

### 🔌 **SmartSketch Integration Guide** (v1.0.0)
SmartSketch API integration patterns
- **File**: `.github/instructions/smartsketch-integration-guide.instructions.md`
- **Use for**: SmartSketch API automation and commands
- **Tags**: `smartsketch`, `api-integration`, `com-automation`

## 🚀 Usage

### For AI-Promptbook
Templates are automatically available in the repository creation wizard.

### Direct Download (Latest Version)
```bash
# Download repository-wide instructions
curl -O https://raw.githubusercontent.com/Lesterhr/LHR-CopilotTemplateHub/main/.github/copilot-instructions.md

# Download specific template
curl -O https://raw.githubusercontent.com/Lesterhr/LHR-CopilotTemplateHub/main/.github/instructions/flet-agent.instructions.md
```

### Download Specific Version
```bash
# Replace v1.0.0 with desired version tag
curl -O https://raw.githubusercontent.com/Lesterhr/LHR-CopilotTemplateHub/v1.0.0/.github/instructions/flet-agent.instructions.md
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
LHR-CopilotTemplateHub/
├── .github/
│   ├── copilot-instructions.md                     # Repository-wide custom instructions
│   └── instructions/                               # Path-specific custom instructions
│       ├── flet-agent.instructions.md
│       ├── s3d-symbol-navigation-guide.instructions.md
│       ├── smartsketch-readme.instructions.md
│       ├── smartsketch-integration-guide.instructions.md
│       ├── github-copilot-tutorial.instructions.md
│       ├── github-copilot-lernleitfaden.instructions.md
│       ├── github-copilot-offizieller-leitfaden.instructions.md
│       └── ... (other instruction files)
├── INDEX.md                                        # Human-readable index
└── README.md                                       # This file
```

### GitHub Copilot Custom Instructions Structure

This repository follows GitHub Copilot best practices:

1. **Repository-wide custom instructions**: `.github/copilot-instructions.md`
   - Applies to all requests made in the context of this repository
   - Provides general guidance for working with templates

2. **Path-specific custom instructions**: `.github/instructions/NAME.instructions.md`
   - Apply to requests made in the context of files that match specified patterns
   - Each template provides specialized guidance for specific frameworks or tools

3. **Combined usage**: When both types of instructions apply, they are used together
   - Repository-wide instructions provide general context
   - Path-specific instructions provide specialized guidance

## 🛠️ For Tool Developers

### Reading Templates Programmatically

```python
import requests
import json

# Base URL for GitHub raw content
base_url = "https://raw.githubusercontent.com/Lesterhr/LHR-CopilotTemplateHub/main"

# Fetch repository-wide instructions
repo_instructions_url = f"{base_url}/.github/copilot-instructions.md"
repo_instructions = requests.get(repo_instructions_url).text

# Fetch a specific template
template_name = "flet-agent.instructions.md"
template_url = f"{base_url}/.github/instructions/{template_name}"
template_content = requests.get(template_url).text
```

### Checking for Updates

```python
import requests
from packaging import version

def check_template_updates(local_templates):
    """
    Check for updates to instruction templates.
    
    Args:
        local_templates: dict with template names and current versions
    
    Returns:
        dict with available updates
    """
    base_url = "https://api.github.com/repos/Lesterhr/LHR-CopilotTemplateHub/contents/.github/instructions"
    
    response = requests.get(base_url)
    remote_files = response.json()
    
    updates = {}
    for file_info in remote_files:
        if file_info['name'].endswith('.instructions.md'):
            # Fetch file to check version in metadata
            content_response = requests.get(file_info['download_url'])
            # Parse version from content metadata
            # ... (version parsing logic)
            pass
    
    return updates
```

## 📝 Contributing

### Adding New Templates

1. Create template in `.github/instructions/` with `.instructions.md` suffix (kebab-case naming)
2. Add YAML metadata header with version, type, priority
3. Include "How AI Agents Should Use This Template" section
4. Update `INDEX.md` with template description
5. Increment repository version in README.md
6. Create git tag for new version

### Updating Existing Templates

1. Edit template file in `.github/instructions/`
2. Increment version in metadata header
3. Update `last_updated` date in file
4. Update INDEX.md if description changed
5. Create git tag if needed

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
