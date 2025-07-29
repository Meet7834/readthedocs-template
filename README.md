# Read the Docs Template with Subprojects

This is a comprehensive template for setting up a main documentation project with subprojects on Read the Docs.

## Structure

```
├── docs/                           # Main documentation
│   ├── conf.py                    # Sphinx configuration
│   ├── index.rst                  # Main documentation index
│   ├── subprojects.rst            # Subprojects overview
│   ├── subprojects/               # Internal subproject docs
│   │   ├── getting-started.rst
│   │   ├── api-reference.rst
│   │   └── tutorials.rst
│   └── requirements.txt
├── subproject-templates/          # Templates for external subprojects
│   └── basic-subproject/         # Complete subproject template
│       ├── docs/
│       ├── .readthedocs.yml
│       └── README.md
├── .readthedocs.yml              # Read the Docs configuration
├── READTHEDOCS_SETUP.md          # Detailed setup guide
└── README.md                     # This file
```

## Quick Start

### For Main Project

1. **Clone this repository**
2. **Customize** the documentation content in `docs/`
3. **Update** `docs/conf.py` with your project information
4. **Import** to Read the Docs and build

### For Subprojects

1. **Copy** the template from `subproject-templates/basic-subproject/`
2. **Customize** the content for your specific subproject
3. **Set up** as a separate Read the Docs project
4. **Link** to main project through Read the Docs dashboard

## Features

- ✅ **Main project setup** with Sphinx and Read the Docs configuration
- ✅ **Subproject templates** ready to use
- ✅ **Cross-project linking** with intersphinx
- ✅ **Consistent theming** across all projects
- ✅ **Complete documentation** examples
- ✅ **Setup guides** and best practices

## Documentation Types Included

### Main Project
- Project overview and general information
- Links to all subprojects
- High-level architecture documentation

### Subproject Templates
- **Getting Started**: Installation and quick start guides
- **API Reference**: Complete API documentation
- **Tutorials**: Step-by-step tutorials and examples
- **Contributing**: Development and contribution guidelines

## Customization

1. **Update project information** in `docs/conf.py`
2. **Modify content** in RST files to match your project
3. **Add or remove subprojects** as needed
4. **Customize styling** and theme options
5. **Configure cross-linking** between projects

## Read the Docs Setup

See `READTHEDOCS_SETUP.md` for detailed instructions on:
- Setting up the main project on Read the Docs
- Creating and linking subprojects
- Configuring cross-project navigation
- Best practices for maintenance

## Benefits of This Approach

- **Modular documentation** that scales with your project
- **Independent versioning** for different components
- **Organized content** for different audiences
- **Professional appearance** with consistent styling
- **Easy maintenance** with templates and automation

## Getting Help

- Check the `READTHEDOCS_SETUP.md` for detailed setup instructions
- Review the example content in `docs/subprojects/`
- Use the subproject template as a starting point
- Refer to Read the Docs and Sphinx documentation for advanced features