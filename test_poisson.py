import pytest
import numpy as np
from poisson import poisson


# Valores de mu para las pruebas
@pytest.mark.parametrize("mu", [1, 2, 5, 10])
def test_normalization(mu):
    total = sum(poisson(n, mu) for n in range(51))

    assert total == pytest.approx(1.0, abs=1e-6)


@pytest.mark.parametrize("mu", [1, 2, 5, 10])
def test_mean(mu):
    mean = sum(n * poisson(n, mu) for n in range(51))

    assert mean == pytest.approx(mu, abs=1e-6)


@pytest.mark.parametrize("mu", [1, 2, 5, 10])
def test_probability_zero(mu):
    probability = poisson(0, mu)

    assert probability == pytest.approx(
        __import__("math").exp(-mu), abs=1e-12
    )


