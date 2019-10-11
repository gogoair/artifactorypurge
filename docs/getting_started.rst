Getting Started
===============

Authentication
--------------

Lavatory looks for several environment variables in order to authenticate:

``ARTIFACTORY_URL`` - Base URL to use for Artifactory connections

``ARTIFACTORY_USERNAME`` - Username to Artifactory

``ARTIFACTORY_PASSWORD`` - Password for Artifactory

These will be loaded in at the beginning of a run and raise an exception
if these environment variables are missing.

In addition, Lavatory supports the ability to send Slack notifications with optional environment variables (both of which must be set):

``SLACK_API_TOKEN`` - Slack API Token

``SLACK_CHANNEL`` - Slack Channel to Post Notification to

Purging Artifacts
-----------------

Creating a Basic Policy
~~~~~~~~~~~~~~~~~~~~~~~

For this documentation lets assume a repository named ``yum-local``. In a new directory, outside of Lavatory, create
``yum_local.py``. This will be a retention policy that only impacts the ``yum-local`` repository.

In ``yum_local.py`` lets create a basic policy:

::

    def purgelist(artifactory):
        """Policy to purge all artifacts older than 120 days"""
        purgable = artifactory.time_based_retention(keep_days=120)
        return purgable

The layout of the policy will look similar to ::

    [root@localhost /]# tree path/
    path
    `-- to
        `-- policies
            `-- yum_local.py


Running Lavatory
~~~~~~~~~~~~~~~~

To test the policy you just created you can run ``lavatory purge --policies-path=/path/to/policies --repo yum-local``

Below are all the options for the ``purge`` command:

::

    $ lavatory purge --help
    Usage: lavatory purge [OPTIONS]

      Deletes artifacts based on retention policies

    Options:
      --policies-path TEXT      Path to extra policies directory
      --dryrun / --nodryrun     Dryrun does not delete any artifacts. On by
                                default
      --default / --no-default  If false, does not apply default policy
      --repo TEXT               Name of specific repository to run against. Can
                                use --repo multiple times. If not provided, uses
                                all repos.
      --help                    Show this message and exit.

If you want to run Lavatory against a specific repository, you can use ``--repo <repo_name>``.
You can specify ``--repo`` as multiple times to run against multiple repos. If ``--repo`` is not
provided, Lavatory will run against all repos in Artifactory.

By default, Lavatory runs in drymode. Must include ``--nodryrun`` in order to
actually delete Artifacts

Configure SSL
~~~~~~~~~~~~~

When HTTPS Artifactory URL is provided, Lavatory uses ``certifi`` to get the
list of trusted certificates.

If your server's certificate is not signed by any of certifi's authorities,
you can either update the certifi's list whose file system path can be retrieved
by the following command:

::

    python -c "import certifi; print(certifi.where())"

or you can instruct Lavatory to use your own CA bundle file path by setting
the environment variable ``LAVATORY_CERTBUNDLE_PATH``.

CLI Help
--------

You can run any Lavatory command with ``--help`` for assistance.

Verbosity
~~~~~~~~~

Adding ``lavatory -v $command`` will increase logging verbosity.
You can add up to 5 ``v`` like ``lavatory -vvvvv $command`` for maximum
verbosity.
