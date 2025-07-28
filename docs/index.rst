RFmx Instr Python API Documentation
===================================

About
=====

The **nirfmx-python** repository generates Python bindings (Application Programming Interface)
for interacting with the NI-RFmx drivers.

**nirfmx-python** follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_
support policy for different versions.

Operating System Support
========================

**nirfmxinstr** supports Windows systems where the supported drivers are
installed. Refer to `NI Hardware and Operating System Compatibility <https://www.ni.com/r/hw-support>`_ for
which versions of the driver support your hardware on a given operating system.

Installation
============

You can use `pip <http://pypi.python.org/pypi/pip>`_ to download
`nirfmxinstr <https://pypi.org/project/nirfmxinstr/>`_ and install it.

.. code-block:: shell

    $ python -m pip install nirfmxinstr

Support and Feedback
====================

For support with Python API, hardware, the driver runtime or any other questions,
please visit `NI Community Forums <https://forums.ni.com/>`_.

Documentation:
==============

.. toctree::
  :maxdepth: 1

  attributes
  enums
  errors
  session

Additional Documentation
========================

Refer to the `NI-RFmx User Manual <https://www.ni.com/docs/en-US/bundle/rfmx/page/user-manual-welcome.html>`_
for an overview of NI-RFmx, system requirements, troubleshooting, key concepts, etc.

License
=======

This project is licensed under the MIT License. While the source code is not publicly released,
the license permits binary distribution with attribution.

**Note:** This Python driver depends on several third-party components that are subject to separate
commercial licenses. Users are responsible for ensuring they have the appropriate rights and licenses
to use those dependencies in their environments.

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
