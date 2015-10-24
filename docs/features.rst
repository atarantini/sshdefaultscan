Features
--------

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