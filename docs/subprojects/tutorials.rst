Tutorials Subproject
===================

This is a template for a Tutorials subproject. This subproject provides step-by-step tutorials and examples.

Tutorial 1: Basic Data Processing
----------------------------------

In this tutorial, you'll learn how to process data using the basic API.

Prerequisites
~~~~~~~~~~~~~

Before starting this tutorial, make sure you have:

* Completed the :doc:`getting-started` guide
* Basic understanding of Python
* Sample data file (we'll show you how to create one)

Step 1: Setup
~~~~~~~~~~~~~

First, let's set up our environment:

.. code-block:: python

   import your_package
   from your_package import MainClass, ConfigManager
   
   # Initialize the main class
   processor = MainClass()

Step 2: Prepare Sample Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create some sample data to work with:

.. code-block:: python

   sample_data = {
       'items': [
           {'id': 1, 'name': 'Item 1', 'value': 100},
           {'id': 2, 'name': 'Item 2', 'value': 200},
           {'id': 3, 'name': 'Item 3', 'value': 300}
       ],
       'metadata': {
           'source': 'tutorial',
           'version': '1.0'
       }
   }

Step 3: Process the Data
~~~~~~~~~~~~~~~~~~~~~~~~

Now let's process our sample data:

.. code-block:: python

   # Process the data
   result = processor.process_data(sample_data)
   
   # Display results
   print("Processing completed!")
   print(f"Processed {len(result['processed_items'])} items")
   
   for item in result['processed_items']:
       print(f"- {item['name']}: {item['processed_value']}")

Step 4: Save Results
~~~~~~~~~~~~~~~~~~~~

Save the processed results to a file:

.. code-block:: python

   import json
   
   # Save to JSON file
   with open('processed_results.json', 'w') as f:
       json.dump(result, f, indent=2)
   
   print("Results saved to processed_results.json")

Tutorial 2: Advanced Configuration
-----------------------------------

Learn how to use advanced configuration options for complex workflows.

Configuration File Setup
~~~~~~~~~~~~~~~~~~~~~~~~~

Create a configuration file `advanced_config.json`:

.. code-block:: json

   {
       "processing": {
           "mode": "advanced",
           "batch_size": 50,
           "parallel": true
       },
       "output": {
           "format": "detailed",
           "include_metadata": true
       },
       "logging": {
           "level": "INFO",
           "file": "processing.log"
       }
   }

Loading and Using Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Load configuration
   config_manager = ConfigManager()
   config = config_manager.load_config('advanced_config.json')
   
   # Initialize with configuration
   processor = MainClass(config)
   
   # Process with advanced settings
   large_dataset = generate_large_dataset()  # Your data source
   result = processor.process_data(large_dataset)

Tutorial 3: Error Handling and Debugging
-----------------------------------------

Learn best practices for handling errors and debugging issues.

Common Error Patterns
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from your_package import ValidationError, ConfigurationError
   
   try:
       # Attempt processing
       result = processor.process_data(data)
       
   except ValidationError as e:
       print(f"Data validation failed: {e.message}")
       # Handle validation errors
       
   except ConfigurationError as e:
       print(f"Configuration error: {e}")
       # Handle configuration errors
       
   except Exception as e:
       print(f"Unexpected error: {e}")
       # Handle unexpected errors

Debugging Tips
~~~~~~~~~~~~~~

1. **Enable verbose logging**:

   .. code-block:: python
   
      import logging
      logging.basicConfig(level=logging.DEBUG)

2. **Validate input data**:

   .. code-block:: python
   
      from your_package import validate_input
      
      if not validate_input(your_data):
          print("Input data is invalid")
          return

3. **Check configuration**:

   .. code-block:: python
   
      print("Current configuration:")
      print(json.dumps(config, indent=2))

Tutorial 4: Integration Examples
---------------------------------

Examples of integrating with popular libraries and frameworks.

Integration with Pandas
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pandas as pd
   from your_package import MainClass
   
   # Load data from CSV
   df = pd.read_csv('data.csv')
   
   # Convert to format expected by the package
   data = df.to_dict('records')
   
   # Process
   processor = MainClass()
   result = processor.process_data(data)
   
   # Convert back to DataFrame
   result_df = pd.DataFrame(result['processed_items'])

Integration with Flask Web App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from flask import Flask, request, jsonify
   from your_package import MainClass
   
   app = Flask(__name__)
   processor = MainClass()
   
   @app.route('/process', methods=['POST'])
   def process_endpoint():
       try:
           data = request.json
           result = processor.process_data(data)
           return jsonify(result)
       except Exception as e:
           return jsonify({'error': str(e)}), 400
   
   if __name__ == '__main__':
       app.run(debug=True)

Next Steps
----------

After completing these tutorials:

* Review the :doc:`api-reference` for detailed API documentation
* Check out advanced topics in the main documentation
* Explore community examples and contributions

Additional Resources
--------------------

* GitHub repository with example code
* Community forum for questions and discussions
* Video tutorials (if available)
* Webinar recordings
