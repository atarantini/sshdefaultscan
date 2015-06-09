**************
sshdefaultscan
**************

**Scan networks for SSH servers with default username and password.**

Use **sshdefaultscan** to scan networks or hosts for SSH servers, try to connect
using some default username and password. It uses `Nmap`_ to provide easy and
powerfull target selection and `Paramiko`_ to test credentials.


Usage
-----

Scan your own machine:

.. code-block:: bash

    $ python sshdefaultscan.py 127.0.0.1

    2015-06-08 21:16:57,711 - sshdefaultscan - DEBUG - Scanning...
    2015-06-08 21:17:03,892 - sshdefaultscan - DEBUG - 1 Up + 0 Down = 1 in 6.16s
    2015-06-08 21:17:03,892 - sshdefaultscan - DEBUG - 127.0.0.1 Seems to have SSH open
    2015-06-08 21:17:06,001 - sshdefaultscan - INFO - 127.0.0.1 Logged in with root:root in 2.11s

You local network:

.. code-block:: bash

    $ python sshdefaultscan.py 192.168.1.1-254

    2015-06-08 21:21:59,408 - sshdefaultscan - DEBUG - Scanning...
    2015-06-08 21:22:08,807 - sshdefaultscan - DEBUG - 3 Up + 251 Down = 254 in 9.38s
    2015-06-08 21:22:08,808 - sshdefaultscan - DEBUG - 192.168.1.42 Seems to have SSH open
    2015-06-08 21:22:11,463 - sshdefaultscan - DEBUG - 192.168.1.42 Authentication failed. (2.65s)

Or a much bigger network block:

.. code-block:: bash

    $ python sshdefaultscan.py 192.168.99-110.1-254

    2015-06-08 21:24:47,177 - sshdefaultscan - DEBUG - Scanning...
    2015-06-08 21:25:16,035 - sshdefaultscan - DEBUG - 127 Up + 2921 Down = 3048 in 28.75s
    2015-06-08 21:25:16,035 - sshdefaultscan - DEBUG - 192.168.109.60 Seems to have SSH open
    2015-06-08 21:25:16,035 - sshdefaultscan - DEBUG - 192.168.110.182 Seems to have SSH open
    2015-06-08 21:25:16,035 - sshdefaultscan - DEBUG - 192.168.110.184 Seems to have SSH open
    2015-06-08 21:25:19,047 - sshdefaultscan - DEBUG - 192.168.109.60 Authentication failed. (3.01s)
    2015-06-08 21:25:20,436 - sshdefaultscan - DEBUG - 192.168.110.182 Authentication failed. (1.39s)
    ...


Install
-------

You will need to have `Nmap`_ installed. If you are on Debian/Ubuntu, probably
this should do all the work:

.. code-block:: bash

    $ sudo apt-get install nmap

On OSX you can try:

.. code-block:: bash

    $ brew install nmap

Once you have it installed, install dependencies from the `requirements.txt`
file using `pip`:

.. code-block:: bash

    $ pip install -r requirements.txt

If the project get some stars, I will upload it to the `The Python Package Index`_.


Logging
-------

All important information is stored in `sshdefaultscan.log`:

.. code-block:: bash

    2015-06-05 22:07:09,432 - sshdefaultscan - INFO - 192.168.166.177 Logged in with root:root in 14.25s
    2015-06-05 22:08:13,660 - sshdefaultscan - INFO - 192.100.100.166 Logged in with root:root in 13.99s
    2015-06-08 21:19:46,295 - sshdefaultscan - INFO - 10.0.1.170 Logged in with root:root in 14.26s


Disclamer
---------

This software is provided for educational purposes and testing only: use it in
your own network or with permission from the network owner. I'm not responsible
of what actions people decide to take using this software. I'm not not
responsible if someone do something against the law using this sofware. Please
be good and don't do anything harmful.


Author
------

Andres Tarantini (atarantini@gmail.com)


License
-------

Released under GNU GPLv3, see COPYING file for more details.

.. _Nmap: http://nmap.org/
.. _Paramiko: http://www.paramiko.org/
.. _`The Python Package Index`: https://pypi.python.org/pypi