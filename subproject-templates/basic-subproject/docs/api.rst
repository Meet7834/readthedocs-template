API Reference
=============

Complete API documentation for this subproject.

Core Classes
------------

Client
~~~~~~

.. py:class:: Client(config=None)

   Main client class for interacting with the subproject functionality.
   
   :param config: Optional configuration object
   :type config: dict or Config object

   .. py:method:: process(data)
   
      Process input data according to the configured settings.
      
      :param data: Input data to process
      :type data: dict
      :return: Processed results
      :rtype: dict
      :raises SubprojectError: When processing fails

   .. py:method:: connect()
   
      Establish connection to required resources.
      
      :return: Connection status
      :rtype: bool

   .. py:method:: disconnect()
   
      Close all connections and clean up resources.

Config
~~~~~~

.. py:class:: Config(settings=None)

   Configuration management class.
   
   :param settings: Dictionary of configuration settings
   :type settings: dict

   .. py:method:: from_file(filepath)
   
      Load configuration from a JSON file.
      
      :param filepath: Path to configuration file
      :type filepath: str
      :return: New Config instance
      :rtype: Config

   .. py:method:: to_dict()
   
      Convert configuration to dictionary.
      
      :return: Configuration as dictionary
      :rtype: dict

   .. py:method:: validate()
   
      Validate configuration settings.
      
      :return: True if valid, False otherwise
      :rtype: bool

Utility Classes
---------------

DataProcessor
~~~~~~~~~~~~~

.. py:class:: DataProcessor(options=None)

   Specialized data processing utilities.
   
   :param options: Processing options
   :type options: dict

   .. py:method:: process_batch(items)
   
      Process multiple items in batch.
      
      :param items: List of items to process
      :type items: list
      :return: List of processed results
      :rtype: list

   .. py:method:: process_dataframe(df)
   
      Process pandas DataFrame.
      
      :param df: Input DataFrame
      :type df: pandas.DataFrame
      :return: Processed data
      :rtype: list

BatchProcessor
~~~~~~~~~~~~~~

.. py:class:: BatchProcessor(batch_size=100)

   Handle batch processing operations.
   
   :param batch_size: Number of items per batch
   :type batch_size: int

   .. py:method:: add_item(item)
   
      Add item to processing queue.
      
      :param item: Item to add
      :type item: any

   .. py:method:: process_all()
   
      Process all queued items.
      
      :return: Processing results
      :rtype: list

Functions
---------

Utility Functions
~~~~~~~~~~~~~~~~~

.. py:function:: validate_input(data)

   Validate input data format and content.
   
   :param data: Data to validate
   :type data: any
   :return: True if valid, False otherwise
   :rtype: bool

.. py:function:: format_output(result, format_type='json')

   Format output in specified format.
   
   :param result: Result data to format
   :type result: dict
   :param format_type: Output format ('json', 'xml', 'csv')
   :type format_type: str
   :return: Formatted output
   :rtype: str

.. py:function:: get_version()

   Get the current version of the subproject.
   
   :return: Version string
   :rtype: str

Constants
---------

.. py:data:: DEFAULT_CONFIG

   Default configuration settings.
   
   .. code-block:: python
   
      DEFAULT_CONFIG = {
          'timeout': 30,
          'retries': 3,
          'debug': False
      }

.. py:data:: API_VERSION

   Current API version.
   
   :type: str
   :value: "1.0.0"

.. py:data:: SUPPORTED_FORMATS

   List of supported output formats.
   
   :type: list
   :value: ['json', 'xml', 'csv', 'yaml']

Exceptions
----------

.. py:exception:: SubprojectError

   Base exception for all subproject-related errors.
   
   .. py:attribute:: message
   
      Error message describing the issue.
      
      :type: str

   .. py:attribute:: error_code
   
      Numeric error code for programmatic handling.
      
      :type: int

.. py:exception:: ValidationError

   Raised when input validation fails.
   
   Inherits from :py:exc:`SubprojectError`.

.. py:exception:: ConfigurationError

   Raised when configuration is invalid or missing.
   
   Inherits from :py:exc:`SubprojectError`.

.. py:exception:: ConnectionError

   Raised when connection to external resources fails.
   
   Inherits from :py:exc:`SubprojectError`.

Data Models
-----------

ProcessingResult
~~~~~~~~~~~~~~~~

.. py:class:: ProcessingResult

   Result object returned by processing operations.
   
   .. py:attribute:: success
   
      Whether the processing was successful.
      
      :type: bool
   
   .. py:attribute:: data
   
      Processed data.
      
      :type: any
   
   .. py:attribute:: metadata
   
      Additional metadata about the processing.
      
      :type: dict
   
   .. py:attribute:: timestamp
   
      When the processing completed.
      
      :type: datetime

   .. py:method:: to_dict()
   
      Convert result to dictionary.
      
      :return: Dictionary representation
      :type: dict

Type Definitions
----------------

For type hinting support:

.. py:data:: ConfigDict

   Type definition for configuration dictionaries.
   
   .. code-block:: python
   
      from typing import Dict, Any
      ConfigDict = Dict[str, Any]

.. py:data:: ProcessingCallback

   Type definition for processing callback functions.
   
   .. code-block:: python
   
      from typing import Callable, Any
      ProcessingCallback = Callable[[Any], Any]

Usage Examples
--------------

Quick usage examples for each major component:

.. code-block:: python

   from your_subproject import Client, Config, DataProcessor
   
   # Basic client usage
   client = Client()
   result = client.process({'key': 'value'})
   
   # With configuration
   config = Config({'timeout': 60})
   client = Client(config)
   
   # Data processing
   processor = DataProcessor()
   batch_result = processor.process_batch([item1, item2, item3])

See Also
--------

* :doc:`quickstart` - For getting started quickly
* :doc:`examples` - For detailed usage examples
* Main documentation for integration patterns
