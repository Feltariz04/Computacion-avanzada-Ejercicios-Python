
import pytest
from myvector import Vector


@pytest.mark.parametrize("a, b", [
    ([1, 2], [3, 4]),
    ([1, 2, 3], [4, 5, 6]),
    ([-1, 0], [2, 3])
])
def test_commutativity(a, b):
    v1 = Vector(a)
    v2 = Vector(b)

    assert v1 + v2 == v2 + v1


@pytest.mark.parametrize("a, b, c", [
    ([1, 2], [3, 4], [5, 6]),
    ([1, 0, 2], [2, 3, 1], [4, 1, 5])
])
def test_associativity(a, b, c):
    v1 = Vector(a)
    v2 = Vector(b)
    v3 = Vector(c)

    assert (v1 + v2) + v3 == v1 + (v2 + v3)


@pytest.mark.parametrize("a", [
    [1, 2],
    [3, 4, 5],
    [-1, 0, 2]
])
def test_zero_vector(a):
    v = Vector(a)
    zero = Vector([0] * len(a))

    assert v + zero == v


@pytest.mark.parametrize("a, b, scalar", [
    ([1, 2], [3, 4], 2),
    ([1, 2, 3], [4, 5, 6], -3)
])
def test_distributivity(a, b, scalar):
    v1 = Vector(a)
    v2 = Vector(b)

    assert scalar * (v1 + v2) == scalar * v1 + scalar * v2


@pytest.mark.parametrize("a, b", [
    ([1, 0], [0, 1]),
    ([1, 2], [2, -1]),
    ([3, 0, 0], [0, 1, 2])
])
def test_orthogonal_vectors(a, b):
    v1 = Vector(a)
    v2 = Vector(b)

    assert v1.dot(v2) == 0


def test_different_dimensions():
    v1 = Vector([1, 2])
    v2 = Vector([1, 2, 3])

    with pytest.raises(ValueError):
        v1 + v2

    with pytest.raises(ValueError):
        v1 - v2