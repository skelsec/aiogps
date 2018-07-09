# Make core client functions available without prefix.
#
# This file is Copyright (c) 2010 by the GPSD project
# BSD terms apply: see the file COPYING in the distribution root for details.

api_major_version = 5   # bumped on incompatible changes
api_minor_version = 0   # bumped on compatible changes

#Setup a logger that can be imported and used
import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


# The 'client' module exposes some C utility functions for Python clients.
# The 'packet' module exposes the packet getter via a Python interface.

