"""Random generation of (Main Sequence) stars."""

from __future__ import annotations

import random

from impunity import impunity

from ..model import Star

__all__ = ['generate_star']


@impunity
def generate_star(
    rng: random.Random,
    require_habitable: bool,
) -> Star:
    """Generate a star at random.

    Parameters
    ----------
    rng: random.Random
        random number generator used for parameters
    require_habitable: bool
        decide whether the star is required to allow for
        habitable planets

    Returns
    -------
    Star
        the generated object
    """
    if require_habitable:
        return Star(rng.random(), 5.0, 9.0)
    return Star(rng.random(), 5.0, 7.0)
