# Basic Subproject Template

This is a template for creating a basic subproject that can be linked to your main Read the Docs project.

## Setup Instructions

1. **Copy this template** to a new repository or directory
2. **Update the configuration** in `docs/conf.py` with your project details
3. **Modify the content** in `docs/index.rst` and other RST files
4. **Set up Read the Docs** for this subproject
5. **Link it to your main project** through Read the Docs dashboard

## Structure

```
basic-subproject/
├── docs/
│   ├── conf.py          # Sphinx configuration
│   ├── index.rst        # Main documentation file
│   ├── requirements.txt # Python dependencies
│   └── content/         # Additional content files
├── .readthedocs.yml     # Read the Docs configuration
└── README.md            # This file
```

## Connecting to Main Project

1. In your main Read the Docs project dashboard, go to "Admin" → "Subprojects"
2. Add this subproject by entering its Read the Docs URL
3. Configure the alias and canonical URL as needed
4. Update your main documentation to link to this subproject

## Customization

- Update `project`, `author`, and other metadata in `docs/conf.py`
- Customize the theme and extensions as needed
- Add your content in RST format
- Update dependencies in `docs/requirements.txt`
