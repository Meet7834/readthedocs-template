Contributing
============

Thank you for your interest in contributing to this subproject! This guide will help you get started.

Getting Started
---------------

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:

   .. code-block:: bash

      git clone https://github.com/your-username/your-subproject.git
      cd your-subproject

3. **Create a virtual environment**:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate

4. **Install development dependencies**:

   .. code-block:: bash

      pip install -e .[dev]

Development Setup
-----------------

Code Style
~~~~~~~~~~

We use several tools to maintain code quality:

* **Black** for code formatting
* **isort** for import sorting
* **flake8** for linting
* **mypy** for type checking

Run all checks:

.. code-block:: bash

   # Format code
   black .
   isort .
   
   # Check linting
   flake8 .
   
   # Type checking
   mypy .

Testing
~~~~~~~

We use **pytest** for testing. Run tests with:

.. code-block:: bash

   # Run all tests
   pytest
   
   # Run with coverage
   pytest --cov=your_subproject
   
   # Run specific test file
   pytest tests/test_specific.py

Documentation
~~~~~~~~~~~~~

Documentation is built with Sphinx. To build locally:

.. code-block:: bash

   cd docs
   make html
   
   # View in browser
   open _build/html/index.html

Types of Contributions
----------------------

Bug Reports
~~~~~~~~~~~

When reporting bugs, please include:

* Clear description of the issue
* Steps to reproduce
* Expected vs actual behavior
* Python version and environment details
* Relevant code snippets or error messages

Feature Requests
~~~~~~~~~~~~~~~~

For new features:

* Describe the feature and its use case
* Explain why it would be valuable
* Consider backwards compatibility
* Provide example usage if possible

Code Contributions
~~~~~~~~~~~~~~~~~~

Pull Request Process
~~~~~~~~~~~~~~~~~~~~

1. **Create a branch** for your feature/fix:

   .. code-block:: bash

      git checkout -b feature/your-feature-name

2. **Make your changes** following our coding standards

3. **Add tests** for new functionality

4. **Update documentation** as needed

5. **Run the test suite** to ensure everything passes

6. **Commit your changes** with descriptive messages:

   .. code-block:: bash

      git add .
      git commit -m "Add feature: your feature description"

7. **Push to your fork**:

   .. code-block:: bash

      git push origin feature/your-feature-name

8. **Create a Pull Request** on GitHub

Coding Standards
----------------

Python Code
~~~~~~~~~~~

* Follow PEP 8 style guidelines
* Use type hints where appropriate
* Write docstrings for all public functions and classes
* Keep functions focused and small
* Use meaningful variable names

Example:

.. code-block:: python

   def process_data(input_data: Dict[str, Any]) -> ProcessingResult:
       """
       Process input data and return results.
       
       Args:
           input_data: Dictionary containing data to process
           
       Returns:
           ProcessingResult object with processed data
           
       Raises:
           ValidationError: If input data is invalid
       """
       if not validate_input(input_data):
           raise ValidationError("Invalid input data format")
       
       # Processing logic here
       processed = transform_data(input_data)
       
       return ProcessingResult(
           success=True,
           data=processed,
           metadata={'timestamp': datetime.now()}
       )

Documentation
~~~~~~~~~~~~~

* Use reStructuredText format for documentation
* Include code examples in docstrings
* Update relevant documentation files when making changes
* Ensure all public APIs are documented

Testing Guidelines
------------------

* Write unit tests for all new functions and classes
* Use meaningful test names that describe what is being tested
* Include both positive and negative test cases
* Mock external dependencies in tests
* Aim for good test coverage (>80%)

Example test:

.. code-block:: python

   import pytest
   from your_subproject import Client, ValidationError

   def test_client_process_valid_data():
       """Test that client processes valid data correctly."""
       client = Client()
       test_data = {'key': 'value', 'number': 42}
       
       result = client.process(test_data)
       
       assert result.success is True
       assert 'processed_key' in result.data

   def test_client_process_invalid_data():
       """Test that client raises error for invalid data."""
       client = Client()
       invalid_data = {'invalid': None}
       
       with pytest.raises(ValidationError):
           client.process(invalid_data)

Release Process
---------------

For maintainers:

1. Update version number in ``__init__.py``
2. Update ``CHANGELOG.md`` with new features and fixes
3. Create and push a new tag:

   .. code-block:: bash

      git tag -a v1.0.1 -m "Release version 1.0.1"
      git push origin v1.0.1

4. GitHub Actions will automatically build and publish to PyPI

Community
---------

* Join our discussions on GitHub
* Follow the code of conduct
* Be respectful and constructive in all interactions
* Help other contributors when possible

Recognition
-----------

All contributors will be recognized in:

* ``CONTRIBUTORS.md`` file
* Release notes for their contributions
* Annual contributor highlights

Thank You!
----------

Your contributions help make this project better for everyone. We appreciate your time and effort!
