# Read the Docs Subproject Setup Guide

This guide explains how to set up a main documentation project with subprojects on Read the Docs.

## Overview

Read the Docs supports subprojects, which allow you to organize related documentation projects under a main project. This is useful for:

- Organizing documentation by component or module
- Maintaining separate versioning for different parts
- Managing documentation for different audiences
- Creating modular documentation architecture

## Main Project Setup

### 1. Set Up Your Main Project

Your current repository is already configured as the main project with:

- `.readthedocs.yml` configuration file
- `docs/` directory with Sphinx configuration
- `docs/subprojects.rst` that links to subprojects

### 2. Configure Read the Docs

1. **Import your project** to Read the Docs:
   - Go to https://readthedocs.org/
   - Click "Import a Project"
   - Connect your GitHub/GitLab account
   - Select your repository

2. **Configure build settings**:
   - The `.readthedocs.yml` file will be automatically detected
   - Builds will use the configuration specified in the file

## Subproject Setup

### Option 1: Internal Subprojects (Same Repository)

If you want to keep subprojects in the same repository:

1. **Structure your repository**:
   ```
   main-repo/
   ├── docs/                    # Main documentation
   │   ├── conf.py
   │   ├── index.rst
   │   └── subprojects.rst     # Links to subprojects
   ├── subproject1/
   │   └── docs/               # Subproject 1 docs
   │       ├── conf.py
   │       └── index.rst
   └── subproject2/
       └── docs/               # Subproject 2 docs
           ├── conf.py
           └── index.rst
   ```

2. **Create separate .readthedocs.yml files** for each subproject or use the main one with different configurations.

### Option 2: External Subprojects (Separate Repositories)

For separate repositories (recommended for larger projects):

1. **Create separate repositories** for each subproject
2. **Use the template** provided in `subproject-templates/basic-subproject/`
3. **Set up each subproject** on Read the Docs independently

## Linking Subprojects

### In Read the Docs Dashboard

1. **Go to your main project** dashboard on Read the Docs
2. **Navigate to Admin → Subprojects**
3. **Add subproject**:
   - Enter the subproject's Read the Docs URL
   - Set an alias (e.g., "api", "tutorials")
   - Configure canonical URL if needed

### In Documentation

Update your main documentation to link to subprojects:

```rst
Subprojects
===========

Our documentation is organized into several subprojects:

* `API Reference <https://main-project.readthedocs.io/projects/api/>`_
* `Tutorials <https://main-project.readthedocs.io/projects/tutorials/>`_
* `Getting Started <https://main-project.readthedocs.io/projects/getting-started/>`_
```

## Configuration Examples

### Main Project .readthedocs.yml

```yaml
version: 2

build:
  os: ubuntu-24.04
  tools:
    python: "3.13"

sphinx:
  configuration: docs/conf.py

python:
  install:
    - requirements: docs/requirements.txt

# Build subprojects if in same repo
submodules:
  include: all
```

### Subproject .readthedocs.yml

```yaml
version: 2

build:
  os: ubuntu-24.04
  tools:
    python: "3.13"

sphinx:
  configuration: docs/conf.py

python:
  install:
    - requirements: docs/requirements.txt

# Link back to main project
formats:
  - pdf
  - epub
```

## Advanced Configuration

### Cross-Project Linking

Configure intersphinx in your `conf.py` files to link between projects:

```python
# In main project conf.py
intersphinx_mapping = {
    'api': ('https://main-project.readthedocs.io/projects/api/', None),
    'tutorials': ('https://main-project.readthedocs.io/projects/tutorials/', None),
}

# In subproject conf.py
intersphinx_mapping = {
    'main': ('https://main-project.readthedocs.io/', None),
    'api': ('https://main-project.readthedocs.io/projects/api/', None),
}
```

### Shared Theme and Styling

Maintain consistent theming across projects:

```python
# Shared theme configuration
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'canonical_url': 'https://main-project.readthedocs.io/',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
}
```

### Custom Navigation

Add custom navigation to link between projects:

```python
# In conf.py
html_context = {
    'display_github': True,
    'github_user': 'your-username',
    'github_repo': 'your-repo',
    'github_version': 'main',
    'conf_py_path': '/docs/',
    # Custom navigation
    'nav_links': [
        ('Main Docs', 'https://main-project.readthedocs.io/'),
        ('API Reference', 'https://main-project.readthedocs.io/projects/api/'),
        ('Tutorials', 'https://main-project.readthedocs.io/projects/tutorials/'),
    ]
}
```

## Best Practices

### Organization

1. **Logical separation**: Organize subprojects by logical boundaries (API docs, tutorials, platform-specific docs)
2. **Independent versioning**: Each subproject can have its own versioning strategy
3. **Clear navigation**: Make it easy for users to move between main and subprojects

### Content Strategy

1. **Main project overview**: Keep high-level information in the main project
2. **Detailed content in subprojects**: Move detailed, specific content to appropriate subprojects
3. **Cross-linking**: Use intersphinx to link between related content

### Maintenance

1. **Consistent styling**: Use the same theme and configuration across all projects
2. **Regular updates**: Keep all projects updated and synchronized
3. **Centralized configuration**: Consider using shared configuration files where possible

## Troubleshooting

### Common Issues

**Subproject not appearing**:
- Check that the subproject is properly configured in Read the Docs dashboard
- Verify the alias is correct
- Ensure the subproject builds successfully

**Links not working**:
- Verify intersphinx configuration
- Check that URLs are correct and accessible
- Ensure projects are public if linking between them

**Build failures**:
- Check that all requirements are specified in requirements.txt
- Verify Python version compatibility
- Review build logs for specific errors

### Getting Help

- Read the Docs documentation: https://docs.readthedocs.io/
- Community support: https://github.com/readthedocs/readthedocs.org/issues
- Sphinx documentation: https://www.sphinx-doc.org/

## Example Workflow

1. **Set up main project** with basic documentation structure
2. **Create subproject repositories** using the provided templates
3. **Configure each subproject** on Read the Docs
4. **Link subprojects** to main project in dashboard
5. **Update navigation** in main documentation to include subproject links
6. **Test cross-linking** between projects
7. **Deploy and verify** all projects build correctly

This setup provides a scalable documentation architecture that can grow with your project needs.
