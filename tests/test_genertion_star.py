"""Test the generation of stars."""

from __future__ import annotations

import random

from enceladus.generation.star import generate_star


def test_generate_star() -> None:
    """Generate an ensemble of stars and check their properties."""
    rng = random.Random()

    result = generate_star(rng, True)

    assert result is not None
    assert result.mass > 0.0
    assert result.radius > 0.0
    assert result.surface_temperature > 0.0
