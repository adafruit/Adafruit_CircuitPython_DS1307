
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ds1307/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/ds1307/en/latest/
    :alt: Documentation Status

.. image :: https://badges.gitter.im/adafruit/circuitpython.svg
    :target: https://gitter.im/adafruit/circuitpython?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
    :alt: Gitter

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

.. image:: 3296-00.jpg

Dependencies
=============

This driver depends on the `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_
and `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
libraries. Please ensure they are also available on the CircuitPython filesystem.
This is easily achieved by downloading
`a library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Notes
===========

Of course, you must import the library to use it:

.. code:: python

    import nativeio
    import adafruit_ds1307
    import time

All the Adafruit RTC libraries take an instantiated and active I2C object
(from the `nativeio` library) as an argument to their constructor. The way to
create an I2C object depends on the board you are using. For boards with labeled
SCL and SDA pins, you can:

.. code:: python

    from board import *

You can also use pins defined by the onboard `microcontroller` through the
`microcontroller.pin` module.

Now, to initialize the I2C bus:

.. code:: python

    myI2C = nativeio.I2C(SCL, SDA)

Once you have created the I2C interface object, you can use it to instantiate
the RTC object:

.. code:: python

    rtc = adafruit_ds1307.DS1307(myI2C)

To set the time, you need to set ``datetime`` to a `time.struct_time` object:

.. code:: python

    rtc.datetime = time.struct_time((2017,1,9,15,6,0,0,9,-1))

After the RTC is set, you retrieve the time by reading the ``datetime``
attribute and access the standard attributes of a struct_time such as `tm_year`,
`tm_hour` and `tm_min`.

.. code:: python

    t = rtc.datetime
    print(t)
    print(t.tm_hour, t.tm_min)

API Reference
=============

.. toctree::
   :maxdepth: 2

   api
