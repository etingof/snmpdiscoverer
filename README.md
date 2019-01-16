
SNMP Agent Discoverer
---------------------

[![PyPI](https://img.shields.io/pypi/v/snmpdiscoverer.svg?maxAge=2592000)](https://pypi.org/project/snmpdiscoverer)
[![Python Versions](https://img.shields.io/pypi/pyversions/snmpdiscoverer.svg)](https://pypi.org/project/snmpdiscoverer/)
[![Status](https://img.shields.io/pypi/status/snmpdiscoverer.svg)](https://github.com/etingof/snmpdiscoverer/)
[![Build status](https://travis-ci.org/etingof/snmpdiscoverer.svg?branch=master)](https://travis-ci.org/etingof/snmpdiscoverer)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/etingof/snmpdiscoverer/master/LICENSE.txt)

The SNMP Discoverer tool pokes at the SNMP agents over the network
to learn as much as possible about the system being managed.

Features
--------

* SNMPv1/v2c/v3 operations
* SNMPv3 USM supports MD5/SHA/SHA224/SHA256/SHA384/SHA512 auth and
  DES/3DES/AES128/AES192/AES256 privacy crypto algorithms
* Supports all SNMP commands
* Runs over IPv4 and IPv6
* Supports massively parallel, asynchronous operation
* Offers Ansible integration
* Works on Linux, Windows and OS X

Download & Install
------------------

SNMP Discoverer software is freely available for download from
[PyPI](https://pypi.org/project/snmpdiscoverer).

Just run:

```bash
$ pip install snmpdiscoverer
```

Alternatively, you can get it from [GitHub](https://github.com/etingof/snmpdiscoverer/releases).

How to use SNMP Discoverer
--------------------------

Running `snmpdiscoverer` will make the tool scanning network for
responding SNMP agents, collect and reports everything it finds out.

```bash
$ snmpdiscoverer
```

Getting help
------------

If something does not work as expected or we are missing an interesting feature,
[open an issue](https://github.com/etingof/snmpdiscoverer/issues) at GitHub or
post your question [on Stack Overflow](https://stackoverflow.com/questions/ask).

Finally, your PRs are warmly welcome! ;-)

Copyright (c) 2019, [Ilya Etingof](mailto:etingof@gmail.com). All rights reserved.
