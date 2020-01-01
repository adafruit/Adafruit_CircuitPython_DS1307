
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ds1307/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/ds1307/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_DS1307/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_DS1307/actions/
    :alt: Build Status

This is a great battery-backed real time clock (RTC) that allows your
microcontroller project to keep track of time even if it is reprogrammed,
or if the power is lost. Perfect for datalogging, clock-building,
time stamping, timers and alarms, etc. The DS1307 is the most popular
RTC - but it requires 5V power to work.

The DS1307 is simple and inexpensive but not a high precision device. It may
lose or gain up to two seconds a day. For a high-precision, temperature
compensated alternative, please check out the
`DS3231 precision RTC <https://www.adafruit.com/products/3013/>`_.
If you do not need a DS1307, or you need a 3.3V-power/logic capable RTC
please check out our affordable
`PCF8523 RTC breakout <https://www.adafruit.com/products/3295>`_.

.. image:: ../docs/_static/3296-00.jpg
    :alt: DS1307

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
=====================
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-ds1307/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-ds1307

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-ds1307

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-ds1307

Usage Notes
===========

Of course, you must import the library to use it:

.. code:: python

    import busio
    import adafruit_ds1307
    import time

All the Adafruit RTC libraries take an instantiated and active I2C object
(from the ``busio`` library) as an argument to their constructor. The way to
create an I2C object depends on the board you are using. For boards with labeled
SCL and SDA pins, you can:

.. code:: python

    from board import *

You can also use pins defined by the onboard ``microcontroller`` through the
``microcontroller.pin`` module.

Now, to initialize the I2C bus:

.. code:: python

    myI2C = busio.I2C(SCL, SDA)

Once you have created the I2C interface object, you can use it to instantiate
the RTC object:

.. code:: python

    rtc = adafruit_ds1307.DS1307(myI2C)

To set the time, you need to set ``datetime`` to a `time.struct_time` object:

.. code:: python

    rtc.datetime = time.struct_time((2017,1,9,15,6,0,0,9,-1))

After the RTC is set, you retrieve the time by reading the ``datetime``
attribute and access the standard attributes of a struct_time such as ``tm_year``,
``tm_hour`` and ``tm_min``.

.. code:: python

    t = rtc.datetime
    print(t)
    print(t.tm_hour, t.tm_min)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_DS1307/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
