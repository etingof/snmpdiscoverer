#!/usr/bin/env python
#
# This file is part of snmpdiscoverer software.
#
# Copyright (c) 2019, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/snmpdiscoverer/license.html
#
import sys
import argparse
import logging

log = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose',
                        action='count',
                        default=0,
                        help='Enable verbose operation (can repeat).')

    required = parser.add_argument_group("Required Options")
    required.add_argument('-A', '--icinganame',
                          required=True,
                          help='Specify Icinga name.')
    required.add_argument('-H', '--hostaddress',
                          required=True,
                          help='Specify Server Hostname or IP Address.')

    connection = parser.add_argument_group("Optional Connection Information.")
    connection.add_argument('-U', '--user',
                            help='Specify User Name.')
    connection.add_argument('-P', '--password',
                            help='Specify User Password.')

    snmp = parser.add_argument_group("SNMP Options")
    snmp.add_argument('--mib-objects',
                      metavar='MIB-Object[,MIB-Object,...]',
                      type=nagiosplugin.MultiArg,
                      required=True,
                      help='MIB object in form of MIB-NAME::MIB-Symbol.index[.index]')
    snmp.add_argument('--community',
                      help='SNMP v1/v2c Community Name',
                      default="public")
    snmp.add_argument('--mib-source',
                      action='append',
                      default=[],
                      help='MIB source URL (can repeat)')

    nagios = parser.add_argument_group("Nagios Plugin Information")
    nagios.add_argument('-w', '--warning',
                        metavar='RANGE[,RANGE,...]',
                        type=nagiosplugin.MultiArg,
                        help='Specify warning range')
    nagios.add_argument('-c', '--critical',
                        metavar='RANGE[,RANGE,...]',
                        type=nagiosplugin.MultiArg,
                        help='Specify critical range')

    args = parser.parse_args()


    # json config:
    #  snmp targets
    #     snmp config
    #       versions templates
    #       credentials templates
    #     transport templates
    #

    # download and cache iana private enterprise numbers

    # download and cache OID->MIB index

    # generate a sequence of transport endpoints from templates

    # run async snmp manager over chunks of agents, query

    #

if __name__ == '__main__':
    sys.exit(main())
