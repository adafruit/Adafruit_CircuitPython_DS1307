""" MicroPython library to support DS1307 Real Time Clock (RTC).

This library supports the use of the DS1307-based RTC in MicroPython. It
contains a base RTC class used by all Adafruit RTC libraries (except where
the chip itself requires modifications). This base class is inherited by the
chip-specific subclasses.

Functions are included for reading and writing registers and manipulating
datetime objects.

* Author(s): Philip R. Moyer and Radomir Dopieralski for Adafruit Industries.
* Date: November 2016
* Affiliation: Adafruit Industries

Implementation Notes
--------------------

**Hardware:**

* Adafruit Feather HUZZAH ESP8266 (Product ID: 2821)
* Adafruit Feather M0 Adalogger (Product ID: 2796)
* Adafruit Arduino Zero (Product ID: 2843)
* Pycom LoPy
* Adafruit DS1307 RTC breakout (Product ID: 3296)

**Software and Dependencies:**

* MicroPython firmware for the ESP8266, which can be obtained from

https://micropython.org/download/#esp8266

* MicroPython firmware for the M0-based boards, which can be obtained from:

https://github.com/adafruit/micropython/releases

* ucollections library
* utime library

**Notes:**

#.  Milliseconds are not supported by this RTC.
#.  Alarms and timers are not supported by this RTC.
#.  The data sheet for the DS1307 can be obtained from.
#.  mpy files automatically generated.

https://datasheets.maximintegrated.com/en/ds/DS1307.pdf

"""

##############################################################################
# Credits and Acknowledgements:
#        Original code written by Radomir Dopieralski. See LICENSE file.
##############################################################################


##############################################################################
# Imports
##############################################################################

try:
	import os
except ImportError:
	import uos as os

osName = os.uname()[0]
bootMicro = False
if 'samd21' == osName:
	bootMicro = True
if 'esp8266' == osName:
	bootMicro = True
if 'LoPy' == osName:
	bootMicro = True
if 'WiPy' == osName:
	bootMicro = True
if 'pyboard' == osName:
	bootMicro = True

if bootMicro:
	import ucollections
	import utime
else:
	import collections as ucollections
	import time as utime


##############################################################################
# Globals and constants
##############################################################################

DateTimeTuple = ucollections.namedtuple("DateTimeTuple", ["year", "month",
    "day", "weekday", "hour", "minute", "second", "millisecond"])


##############################################################################
# Functions
##############################################################################

def datetime_tuple(year, month, day, weekday=0, hour=0, minute=0,
                    second=0, millisecond=0):
    """Return individual values converted into a data structure (a tuple).

    **Arguments:**

    * year - The year (four digits, required, no default).
    * month - The month (two digits, required, no default).
    * day - The day (two digits, required, no default).
    * weekday - The day of the week (one digit, not required, default zero).
    * hour - The hour (two digits, 24-hour format, not required, default zero).
    * minute - The minute (two digits, not required, default zero).
    * second - The second (two digits, not required, default zero).
    * millisecond - Milliseconds (not supported, default zero).

    """
    return DateTimeTuple(year, month, day, weekday, hour, minute,second,
        millisecond)


def _bcd2bin(value):
    """Convert binary coded decimal to Binary

    **Arguments:**

    * value - the BCD value to convert to binary (required, no default)

    """
    return value - 6 * (value >> 4)


def _bin2bcd(value):
    """Convert a binary value to binary coded decimal.

    **Arguments:**

    * value - the binary value to convert to BCD. (required, no default)

    """
    return value + 6 * (value // 10)


def tuple2seconds(datetime):
    """Convert a datetime tuple to seconds since the epoch.

    **Arguments:**

    * datetime - a datetime tuple containing the date and time to convert.
      (required, no default)

    """
    return utime.mktime((datetime.year, datetime.month, datetime.day,
        datetime.hour, datetime.minute, datetime.second, datetime.weekday, 0))


def seconds2tuple(seconds):
    """Convert seconds since the epoch into a datetime structure.

    **Arguments:**

    * seconds - the value to convert. (required, no default)

    """
    year, month, day, hour, minute, second, weekday, _yday = utime.localtime()
    return DateTimeTuple(year, month, day, weekday, hour, minute, second, 0)


##############################################################################
# Classes and methods
##############################################################################

class _BaseRTC:
    """ Provide RTC functionality common across all Adafruit RTC products.

    This is the parent class inherited by the chip-specific subclasses.

    **Methods:**

    * __init__ - constructor
    * _register - read and write registers
    * _flag - return or set flag bits in registers
    * datetime - return or set the RTC clock
    * alarm_time - return or set the time-of-day alarm

    """
    def __init__(self, i2c, address=0x68):
        """Base RTC class constructor.

        **Arguments:**

        * i2c - an existing I2C interface object (required, no default)
        * address - the hex i2c address for the DS1307 chip (default 0x68).

        """
        self.i2c = i2c                # An existing I2C interface object
        self.address = address        # The I2C address for the device

    def _register(self, register, buffer=None):
        """Base RTC class register method to set or read a register value.

        **Arguments:**

        * register - Hex address of the register to be manipulated. (required)
        * buffer - Data to be written to the register location, or None
          if the register is to be read.

        """
        if buffer is None:
            # Read the register byte and return it.
            return self.i2c.readfrom_mem(self.address, register, 1)[0]
        # Write the buffer contents into the register location.
        self.i2c.writeto_mem(self.address, register, buffer)

    def _flag(self, register, mask, value=None):
        """Set or return a bitwise flag setting.

        **Arguments:**

        * register - Hex address of the register to be used. (required)
        * mask - Binary bitmask to extract or write specific bits. (required)
        * value - Data to write into the flag register. If None, the method
          returns the flag(s). If set, it is written to the register (using the
          mask parameter).

        """
        data = self._register(register)
        if value is None:
            return bool(data & mask)
        if value:
            data |= mask
        else:
            data &= ~mask
        self._register(register, bytearray((data,)))


class DS1307(_BaseRTC):
    """DS1307 RTC subclass.

    Supports DS1307-based real time clocks and inherits the _BaseRTC parent
	class.

    **Methods:**

    * stop - Stops the DS1307 from transmitting data on I2C.
    * memory - Reads or writes bytes in specified memory locations.
    * alarm-time - Raises an exception since the DS1307 doesn't have alarms.

    """
    _NVRAM_REGISTER = 0x08
    _DATETIME_REGISTER = 0x00
    _SQUARE_WAVE_REGISTER = 0x07

	def datetime(self, datetime=None):
	    """Read or set the RTC clock.

	    **Arguments:**

	    * datetime - a datetime structure to write to the RTC, i.e., sets the
	      clock.

	    """
	    buffer = bytearray(7)
	    if datetime is None:
	        # Read and return the date and time.
	        self.i2c.readfrom_mem_into(self.address, self._DATETIME_REGISTER,
	                                       buffer)
	        return datetime_tuple(
	            year=_bcd2bin(buffer[6]) + 2000,
	            month=_bcd2bin(buffer[5]),
	            day=_bcd2bin(buffer[4]),
	            weekday=_bcd2bin(buffer[3]),
	            hour=_bcd2bin(buffer[2]),
	            minute=_bcd2bin(buffer[1]),
	            second=_bcd2bin(buffer[0] & 0x3F),
	        )
	    # Set the time.
	    datetime = datetime_tuple(*datetime)    # convert argument to struct
	    buffer[0] = _bin2bcd(datetime.second)   # format conversions
	    buffer[1] = _bin2bcd(datetime.minute)
	    buffer[2] = _bin2bcd(datetime.hour)
	    buffer[3] = _bin2bcd(datetime.weekday)
	    buffer[4] = _bin2bcd(datetime.day)
	    buffer[5] = _bin2bcd(datetime.month)
	    buffer[6] = _bin2bcd(datetime.year - 2000)
	    self._register(self._DATETIME_REGISTER, buffer) # Write the register


    def stop(self, value=None):
        """Stops the DS1307 data transmission, or returns current value.

        **Arguments:**

        * value - The value (True or False) to set in the stop register. If None,
          return the current value. (Optional, default None)

        """
        return self._flag(0x00, 0b10000000, value)

    def memory(self, address, buffer=None):
        """Reads or writes memory locations in the DS1307 chip.

        **Arguments:**

        * address - The memory address to read or write. (required, no default)
        * buffer - The data to write or None to read. (not required, default None)

        """
        if buffer is not None and address + len(buffer) > 56:
            raise ValueError("address out of range")
        return self._register(self._NVRAM_REGISTER + address, buffer)

    def alarm_time(self, datetime=None):
        """Raise an exception - alarms are not supported by DS1307."""
        raise NotImplementedError("alarms not available")
