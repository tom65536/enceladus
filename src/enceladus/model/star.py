"""Model of a star."""

from __future__ import annotations

import dataclasses
from typing import Annotated

from impunity import impunity

__all__ = ['Star']


@impunity
@dataclasses.dataclass
class Star:
    """A stellar object."""

    mass: Annotated[float, 'kg']
    radius: Annotated[float, 'm']
    surface_temperature: Annotated[float, 'K']
