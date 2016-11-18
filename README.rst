
Introduction
============

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


Implementation Details
=======================

.. toctree::
   :maxdepth: 2

Background
----------

This page contains the details of the functions, classes, and methods
available in the DS1307 library.

.. automodule:: adafruit_ds1307
   :members:
