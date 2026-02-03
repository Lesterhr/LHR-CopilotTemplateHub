# LHR-CopilotTemplateHub Repository Instructions

This repository contains a collection of custom instruction templates for GitHub Copilot. These templates provide specialized guidance for various development scenarios, frameworks, and tools.

## Repository Purpose

This is a centralized, versioned repository of AI-assisted development templates designed to:
- Provide consistent coding patterns across multiple tools and projects
- Offer specialized guidance for specific frameworks (Flet, SmartSketch, etc.)
- Share best practices for development workflows
- Enable reusable templates for AI-assisted development

## How to Use This Repository

### For AI Agents
When working with code in this repository:
1. **Template Creation/Editing**: Follow the existing structure and naming conventions (`.instructions.md` suffix)
2. **Metadata**: Include YAML frontmatter with version, type, and priority information
3. **Documentation**: Keep README.md and INDEX.md synchronized with template changes
4. **Versioning**: Use semantic versioning (MAJOR.MINOR.PATCH) for templates

### Template Structure Requirements
Each template should include:
- Clear metadata header with version and type information
- "How AI Agents Should Use This Template" section
- Detailed patterns, examples, and best practices
- Proper categorization with tags and keywords

### Path-Specific Instructions
Path-specific custom instructions are located in `.github/instructions/` directory. These provide specialized guidance for particular development contexts, frameworks, or tools. When working on code that matches a template's domain:
- Check the relevant `.instructions.md` file in `.github/instructions/`
- Apply both repository-wide and path-specific guidance
- Follow priority rules when multiple templates apply

## Contributing Guidelines

When adding or updating templates:
1. Create or edit files in `.github/instructions/` directory
2. Use kebab-case naming: `descriptive-name.instructions.md`
3. Update version numbers in both file metadata and manifest.json
4. Keep INDEX.md synchronized with changes
5. Follow semantic versioning principles
6. Test templates in real-world scenarios before committing

## Template Naming Convention

All instruction files must follow:
```
<descriptive-name>.instructions.md
```

Examples:
- `flet-agent.instructions.md`
- `github-copilot-tutorial.instructions.md`
- `smartsketch-integration-guide.instructions.md`

## Quality Standards

Templates in this repository should:
- Be clear, concise, and actionable
- Include practical examples
- Follow consistent formatting
- Be regularly updated and maintained
- Avoid deprecated patterns or obsolete information

## Version Management

- **Repository Version**: Tracked in README.md
- **Template Versions**: Individual versions in each template's metadata
- **Semantic Versioning**: MAJOR.MINOR.PATCH
  - MAJOR: Breaking changes in template structure
  - MINOR: New templates or significant additions
  - PATCH: Fixes and minor improvements
