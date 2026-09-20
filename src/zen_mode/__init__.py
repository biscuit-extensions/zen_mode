from __future__ import annotations

import typing

from .extension import ZenMode

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


def setup(api: "ExtensionsAPI") -> None:
    """Entrypoint for Biscuit to load the extension."""
    api.register("zen_mode", ZenMode(api))
