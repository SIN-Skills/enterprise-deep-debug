#!/usr/bin/env python3
"""
GitLab LogCenter (DEPRECATED) - Use Box Storage instead.

This module is deprecated. All functionality has been moved to box_storage.py.
Importing this module will emit a deprecation warning and delegate to box_storage.

Migration: Replace `from gitlab_logcenter import get_logcenter` with
`from box_storage import get_logcenter`.
"""

import warnings

warnings.warn(
    "gitlab_logcenter is deprecated. Use box_storage module instead. "
    "All logs now go to Box.com via A2A-SIN-Box-Storage.",
    DeprecationWarning,
    stacklevel=2,
)

# Re-export from the new module
from .box_storage import get_logcenter, BoxStorageClient  # noqa: F401
