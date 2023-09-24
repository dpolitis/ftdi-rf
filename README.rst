ftdi-rf
======

Introduction
------------

Python module for sending and receiving 433/315MHz LPD/SRD signals with generic low-cost GPIO RF modules on a Generic PC.

Protocol and base logic ported ported from `rc-switch`_.

Supported hardware
------------------

Most generic 433/315MHz capable modules (cost: ~2€) connected via ftdi serial compatible hardware to a Generic PC.

.. figure:: http://i.imgur.com/vG89UP9.jpg
   :alt: 433modules

Compatibility
-------------

Generic RF outlets and most 433/315MHz switches (cost: ~15€/3pcs).

.. figure:: http://i.imgur.com/WVRxvWe.jpg
   :alt: rfoutlet


Chipsets:

* SC5262 / SC5272
* HX2262 / HX2272
* PT2262 / PT2272
* EV1527 / RT1527 / FP1527 / HS1527

For a full list of compatible devices and chipsets see the `rc-switch Wiki`_

Dependencies
------------

::

    pyftdi

Installation
------------

On your PC, install the *ftdi_rf* module via pip.

Python 3::

    # apt-get install python3-pip
    # pip3 install ftdi-rf

Wiring diagram (example)
------------------------

FT232RL or other supported ftdi serial hardware::

    TX:
       GND > (GND)
       VCC > (5V)
      DATA > RX (GPIO1), Or other pin of your liking)

    RX:
       VCC > (5V)
      DATA > TX (GPIO0), Or other pin of your liking
       GND > (GND)

Usage
-----

See `scripts`_ (`ftdi-rf_send`_, `ftdi-rf_receive`_) which are also shipped as cmdline tools.

Open Source
-----------

* The code is licensed under the `BSD Licence`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues

.. _rc-switch: https://github.com/sui77/rc-switch
.. _rc-switch Wiki: https://github.com/sui77/rc-switch/wiki
.. _BSD Licence: http://www.linfo.org/bsdlicense.html
.. _GitHub: https://github.com/dpolitis/ftdi-rf
.. _GitHub issues: https://github.com/dpolitis/ftdi-rf/issues
.. _scripts: https://github.com/dpolitis/ftdi-rf/blob/master/scripts
.. _ftdi-rf_send: https://github.com/dpolitis/ftdi-rf/blob/master/scripts/ftdi-rf_send
.. _ftdi-rf_receive: https://github.com/dpolitis/ftdi-rf/blob/master/scripts/ftdi-rf_receive
