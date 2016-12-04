
SNMP agents discovery tool
--------------------------
[![Python Versions](https://img.shields.io/pypi/pyversions/snmpdiscoverer.svg)](https://pypi.python.org/pypi/snmpdiscoverer/)
[![Build status](https://travis-ci.org/etingof/snmpdiscoverer.svg?branch=master)](https://secure.travis-ci.org/etingof/snmpdiscoverer)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/etingof/snmpdiscoverer/master/LICENSE.txt)

The `snmpdiscoverer` tool floods your network with unicast and broadacst SNMP queries in search for SNMP
agents living there. Once an agent responds, this tool tries to figure out the details of the agent
being discovered.

Features
--------

* SNMPv1/v2c and SNMPv3 support
* Unicast and broadcast operations
* Agent vendor, type and implemented MIBs discovery
* 100% Python, works with Python 2.6 though 3.6

Examples
--------


Copyright (c) 2016, [Ilya Etingof](mailto://etingof@gmail.com). All rights reserved.
