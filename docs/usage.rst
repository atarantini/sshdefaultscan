Usage
=====

Basic
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


Complete list of arguments
--------------------------

.. code-block:: bash

    $ python sshdefaultscan.py -h

    usage: sshdefaultscan.py [-h] [--username USERNAME] [--password PASSWORD]
                             [--port PORT] [--fast] [--batch]
                             [--batch-template BATCH_TEMPLATE]
                             hosts

    Scan networks for SSH servers with default username and password.

    positional arguments:
      hosts                 An IP address for a hostname or network, ex: 192.168.1.1
                            for single host or 192.168.1.1-254 for network.

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
                            "root@192.168.0.1" as output when running in batch mode.