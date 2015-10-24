====================
sshdefaultscan 0.4.0
====================

**Scan networks for SSH servers with default username and password.**

Use **sshdefaultscan** to scan networks or hosts for SSH servers, try to connect
using some default username and password. It uses `Nmap`_ to provide easy and
powerfull target selection and `Paramiko`_ to test credentials.

**Full documentation at** http://sshdefaultscan.readthedocs.org/

.. image:: https://readthedocs.org/projects/sshdefaultscan/badge/?version=latest


Usage
-----

Scan your own machine:

.. code-block:: bash

    $ python sshdefaultscan.py 127.0.0.1

    2015-06-08 21:16:57,711 - sshdefaultscan - DEBUG - Scanning...
    2015-06-08 21:17:03,892 - sshdefaultscan - DEBUG - 1 hosts up, 1 total in 0.28s
    2015-06-08 21:17:03,892 - sshdefaultscan - DEBUG - 127.0.0.1 Seems to have SSH open
    2015-06-08 21:17:06,001 - sshdefaultscan - INFO - 127.0.0.1 Logged in with root:root in 2.11s

Your local network, with ``--fast`` to improve speed:

.. code-block:: bash

    $ python sshdefaultscan.py --fast 192.168.1.1-254

    2015-06-08 21:21:59,408 - sshdefaultscan - DEBUG - Scanning...
    2015-06-08 21:22:08,807 - sshdefaultscan - DEBUG - 1 hosts up, 254 total in 3.38s
    2015-06-08 21:22:08,808 - sshdefaultscan - DEBUG - 192.168.1.42 Seems to have SSH open
    2015-06-08 21:22:11,463 - sshdefaultscan - DEBUG - 192.168.1.42 Authentication failed. (2.65s)

Different username or password:

.. code-block:: bash

    $ python sshdefaultscan.py --username admin --password 1234 192.168.1.1-254

    2015-06-08 21:21:59,408 - sshdefaultscan - DEBUG - Scanning...
    2015-06-08 21:22:08,807 - sshdefaultscan - DEBUG - 3 hosts up, 254 total in 3.11s
    2015-06-08 21:22:08,808 - sshdefaultscan - DEBUG - 192.168.1.42 Seems to have SSH open
    2015-06-08 21:22:11,463 - sshdefaultscan - INFO - 192.168.1.42  Logged in with admin:1234 in 0.98s

Or a much bigger network segment:

.. code-block:: bash

    $ python sshdefaultscan.py 192.168.99-110.1-254

    2015-06-08 21:24:47,177 - sshdefaultscan - DEBUG - Scanning...
    2015-06-08 21:25:16,035 - sshdefaultscan - DEBUG - 127 hosts up, 3048 total in 28.75s
    2015-06-08 21:25:16,035 - sshdefaultscan - DEBUG - 192.168.109.60 Seems to have SSH open
    2015-06-08 21:25:16,035 - sshdefaultscan - DEBUG - 192.168.110.182 Seems to have SSH open
    2015-06-08 21:25:16,035 - sshdefaultscan - DEBUG - 192.168.110.184 Seems to have SSH open
    2015-06-08 21:25:19,047 - sshdefaultscan - DEBUG - 192.168.109.60 Authentication failed. (3.01s)
    2015-06-08 21:25:20,436 - sshdefaultscan - DEBUG - 192.168.110.182 Authentication failed. (1.39s)
    ...

See full documentation at http://sshdefaultscan.readthedocs.org/


Disclaimer
----------

This software is provided for educational purposes and testing only: use it in
your own network or with permission from the network owner. I'm not responsible
of what actions people decide to take using this software. I'm not responsible
if someone do something against the law using this software. Please be good and
don't do anything harmful :)


Author
------

Andres Tarantini (atarantini@gmail.com)


License
-------

Released under GNU GPLv3, see `COPYING <https://github.com/atarantini/sshdefaultscan/blob/master/COPYING>`_ file for more details.

.. _Nmap: http://nmap.org/
.. _Paramiko: http://www.paramiko.org/
.. _`The Python Package Index`: https://pypi.python.org/pypi
