Examples
========

This section provides practical examples of using this subproject.

Example 1: Basic Operations
---------------------------

.. code-block:: python

   import your_subproject
   
   # Create client instance
   client = your_subproject.Client()
   
   # Example operation
   data = {'key': 'value', 'number': 42}
   result = client.process(data)
   
   print(f"Processed result: {result}")

Example 2: Configuration Management
-----------------------------------

.. code-block:: python

   from your_subproject import Client, Config
   
   # Load configuration from file
   config = Config.from_file('config.json')
   
   # Or create programmatically
   config = Config({
       'timeout': 30,
       'retries': 3,
       'debug': True
   })
   
   client = Client(config)
   result = client.execute_with_config()

Example 3: Error Handling
--------------------------

.. code-block:: python

   from your_subproject import Client, SubprojectError
   
   client = Client()
   
   try:
       result = client.risky_operation()
       print(f"Success: {result}")
   except SubprojectError as e:
       print(f"Subproject error: {e}")
   except Exception as e:
       print(f"Unexpected error: {e}")

Example 4: Async Operations
---------------------------

If your subproject supports async operations:

.. code-block:: python

   import asyncio
   from your_subproject import AsyncClient
   
   async def main():
       client = AsyncClient()
       
       try:
           result = await client.async_operation()
           print(f"Async result: {result}")
       finally:
           await client.close()
   
   # Run the async function
   asyncio.run(main())

Example 5: Batch Processing
---------------------------

.. code-block:: python

   from your_subproject import BatchProcessor
   
   # Prepare batch data
   batch_data = [
       {'id': 1, 'data': 'first'},
       {'id': 2, 'data': 'second'},
       {'id': 3, 'data': 'third'}
   ]
   
   processor = BatchProcessor()
   results = processor.process_batch(batch_data)
   
   for result in results:
       print(f"ID {result['id']}: {result['processed_data']}")

Example 6: Integration with Other Libraries
--------------------------------------------

Working with pandas:

.. code-block:: python

   import pandas as pd
   from your_subproject import DataProcessor
   
   # Load data
   df = pd.read_csv('data.csv')
   
   # Process with subproject
   processor = DataProcessor()
   processed_data = processor.process_dataframe(df)
   
   # Convert back to DataFrame
   result_df = pd.DataFrame(processed_data)
   result_df.to_csv('processed_data.csv', index=False)

Complete Example Script
------------------------

Here's a complete script that demonstrates multiple features:

.. code-block:: python

   #!/usr/bin/env python3
   """
   Complete example demonstrating subproject features
   """
   
   import json
   import logging
   from your_subproject import Client, Config, SubprojectError
   
   # Setup logging
   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)
   
   def main():
       # Configuration
       config = Config({
           'timeout': 30,
           'max_workers': 4,
           'debug': False
       })
       
       # Initialize client
       client = Client(config)
       
       try:
           # Sample data
           sample_data = {
               'items': [
                   {'name': 'item1', 'value': 100},
                   {'name': 'item2', 'value': 200}
               ],
               'metadata': {
                   'source': 'example',
                   'timestamp': '2025-01-01T00:00:00Z'
               }
           }
           
           # Process data
           logger.info("Processing data...")
           result = client.process(sample_data)
           
           # Save results
           with open('results.json', 'w') as f:
               json.dump(result, f, indent=2)
           
           logger.info(f"Processing complete. Results saved.")
           return result
           
       except SubprojectError as e:
           logger.error(f"Subproject error: {e}")
           return None
       except Exception as e:
           logger.error(f"Unexpected error: {e}")
           return None
   
   if __name__ == "__main__":
       result = main()
       if result:
           print("Example completed successfully!")
       else:
           print("Example failed!")

Additional Resources
--------------------

* Check the :doc:`api` documentation for complete method references
* See the main documentation for more complex integration patterns
* Visit the GitHub repository for more example scripts
