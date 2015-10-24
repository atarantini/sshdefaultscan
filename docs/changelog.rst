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