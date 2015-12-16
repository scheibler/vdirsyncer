# -*- coding: utf-8 -*-
'''
vdirsyncer is a synchronization tool for vdir. See the README for more details.
'''

from __future__ import print_function

try:
    from .version import version as __version__  # noqa
except ImportError:
    raise ImportError(
        'Failed to find (autogenerated) version.py. '
        'This might be because you are installing from GitHub\'s tarballs, '
        'use the PyPI ones.'
    )


def _detect_faulty_requests():
    import requests
    if 'dist-packages' not in requests.__file__:
        return

    text = (
        '{e}\n\n'
        'This most likely means you are running into a bug specific to '
        'Debian-based distributions.\n\n'
        'Consult {d}/problems.html#requests-related-importerrors-on-debian'
        '-based-distributions on how to deal with this, or use a different '
        'operating system.'
    )

    try:
        from requests_toolbelt.auth.guess import GuessAuth  # noqa
    except ImportError as e:
        import sys
        print(text.format(e=str(e), d=DOCS_HOME), file=sys.stderr)
        sys.exit(1)


_detect_faulty_requests()


PROJECT_HOME = 'https://github.com/untitaker/vdirsyncer'
DOCS_HOME = 'https://vdirsyncer.readthedocs.org/en/stable'
