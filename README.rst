==============
sshdefaultscan
==============

**Scan networks for SSH servers with default username and password.**

Use **sshdefaultscan** to scan networks or hosts for SSH servers, try to connect
using some default username and password. It uses `Nmap`_ to provide easy and
powerfull target selection and `Paramiko`_ to test credentials.


Documentation
-------------

.. contents::
    :local:
    :depth: 2
    :backlinks: none

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

All the stuff:

.. code-block:: bash

    usage: sshdefaultscan.py [-h] [--username USERNAME] [--password PASSWORD]
                             [--port PORT] [--fast] [--batch]
                             [--batch-template BATCH_TEMPLATE]
                             hosts

    Scan networks for SSH servers with default username and password.

    positional arguments:
      hosts                 An IP address for a hostname or network, ex:
                            192.168.1.1 for single host or 192.168.1.1-254 for
                            network.

    optional arguments:
      -h, --help            show this help message and exit

      --username USERNAME   Set username, default is "root".

      --password PASSWORD   Set password, default is "root".

      --port PORT           Set port, default is 22.

      --fast                Change timeout settings for the scanner in order to
                            scan faster (T5).

      --batch               Batch mode will only output hosts, handy to use with
                            unix pipes.

      --batch-template BATCH_TEMPLATE
                            Change batch mode output template, default is
                            "{host}". Available context variables: host, username,
                            password. Ex: "{username}@{host}" will return
                            "root@192.168.0.1" as output when running in batch
                            mode.


Install
-------

You will need to have `Nmap`_ installed. If you are on Debian/Ubuntu, this should
do all the work:

.. code-block:: bash

    $ sudo apt-get install nmap

On OSX you can install with Homebrew or macports:

.. code-block:: bash

    $ brew install nmap

or

.. code-block:: bash

    $ port install nmap

Once you have `Nmap`_ installed, install dependencies from the ``requirements.txt``
file using ``pip``:

.. code-block:: bash

    $ pip install -r requirements.txt

If the project get some stars, I will upload it to the `The Python Package Index`_.


Other features
--------------

Logging
^^^^^^^

All important information is stored in ``sshdefaultscan.log``:

.. code-block:: bash

    2015-06-05 22:07:09,432 - sshdefaultscan - INFO - 192.168.166.177 Logged in with root:root in 14.25s
    2015-06-05 22:08:13,660 - sshdefaultscan - INFO - 192.100.100.166 Logged in with root:root in 13.99s
    2015-06-08 21:19:46,295 - sshdefaultscan - INFO - 10.0.1.170 Logged in with root:root in 14.26s

Batch mode
^^^^^^^^^^

If you want to combine ``sshdefaultscan`` with other tools or make reports, you
can use the ``--batch`` option. When running in batch mode, ``sshdefaultscan``
will print results to stdout and will suppress logging in the terminal (logging
into file will not be disabled by this option).

Basic
"""""

.. code-block:: bash

    $ python sshdefaultscan.py --batch 10.0.1-254.1-254
    10.0.3.2
    10.0.3.9
    10.0.100.24
    10.0.211.19

Use it with other tools, let's see the latency with this hosts using ``ping``:

.. code-block:: bash

    $ python sshdefaultscan.py --batch 10.0.3.1-254 | xargs -n 1 ping -c 1 | grep icmp_
    64 bytes from 10.0.3.2: icmp_seq=1 ttl=50 time=24 ms
    64 bytes from 10.0.3.9: icmp_seq=1 ttl=50 time=26 ms

Get hostname from an IP address using ``host``:

.. code-block:: bash

    $ python sshdefaultscan.py --batch 192.168.1.1-254 | xargs -n 1 host
    1.1.168.192.in-addr.arpa domain name pointer ROUTER.
    11.1.168.192.in-addr.arpa domain name pointer hostA.
    16.1.168.192.in-addr.arpa domain name pointer android-67d82275b133e285

Advanced
""""""""

Sometime having only the hostname is not enough and a custom output is needed.
When using ``--batch-template`` option a custom template can be set. For example,
let's export the scan results to a CSV file:

.. code-block:: bash

    $ python sshdefaultscan.py --batch-template "{host},{username},{password}" 192.168.1.1-254 > scan.csv

The template uses `Python's string.format() <https://docs.python.org/2/library/string.html#formatstrings>`_ with
this parameters:

* host
* username
* password

There is no need to use ``--batch`` when ``--batch-template`` is used, **sshdefaultscan** will assume that
you want to run in batch mode.


Disclaimer
----------

This software is provided for educational purposes and testing only: use it in
your own network or with permission from the network owner. I'm not responsible
of what actions people decide to take using this software. I'm not not responsible
if someone do something against the law using this software. Please be good and
don't do anything harmful :)


Changelog
---------

``0.3.0`` - 2015-09-17
    * Added ``--port`` parameter to set custom SSH port.
    * Handle socket error when making SSH connection.

``0.2.1`` - 2015-07-03
    * Batch mode custom output with ``--batch-template``.
    * Improved scan speed (in both normal and ``--fast``) by disabling reverse DNS resolution.

``0.2.0`` - 2015-06-30
    * Batch mode can be used with the ``--batch`` option.

``0.1.3`` - 2015-06-19
    * Fixed logger: was using default username and password, now is using the ones sent by the user.

``0.1.2`` - 2015-06-13
    * Added ``--fast`` parameter to allow faster scans reducing timeouts (`T5 Nmap template <http://nmap.org/book/man-performance.html>`_).

``0.1.1`` - 2015-06-08
    * Added ``--username`` and ``--password`` parameters to set default username and password.

``0.1.0`` - 2015-06-07
    * Initial release.


Author
------

Andres Tarantini (atarantini@gmail.com)


License
-------

Released under GNU GPLv3, see `COPYING <https://github.com/atarantini/sshdefaultscan/blob/master/COPYING>`_ file for more details.

.. _Nmap: http://nmap.org/
.. _Paramiko: http://www.paramiko.org/
.. _`The Python Package Index`: https://pypi.python.org/pypi
