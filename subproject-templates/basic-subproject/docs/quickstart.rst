Quick Start
===========

Get up and running with this subproject in just a few minutes.

Basic Usage
-----------

Here's the simplest way to get started:

.. code-block:: python

   import your_subproject
   
   # Initialize
   client = your_subproject.Client()
   
   # Basic operation
   result = client.do_something()
   print(result)

Configuration
-------------

Basic configuration example:

.. code-block:: python

   config = {
       'setting1': 'value1',
       'setting2': 'value2'
   }
   
   client = your_subproject.Client(config)

Your First Script
-----------------

Create a file called ``hello_subproject.py``:

.. code-block:: python

   #!/usr/bin/env python3
   """
   Hello World example for the subproject
   """
   
   import your_subproject
   
   def main():
       # Initialize the client
       client = your_subproject.Client()
       
       # Perform a basic operation
       try:
           result = client.hello_world()
           print(f"Success: {result}")
       except Exception as e:
           print(f"Error: {e}")
   
   if __name__ == "__main__":
       main()

Run the script:

.. code-block:: bash

   python hello_subproject.py

Next Steps
----------

Now that you have the basics working:

1. Check out the :doc:`examples` for more complex scenarios
2. Review the :doc:`api` documentation for all available features
3. Read about advanced configuration options
