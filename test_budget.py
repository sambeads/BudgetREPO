import skeleton
import pytest
from hypothesis import given
import hypothesis.strategies as st


def test_incrementing():

    assert skeleton.increment(3) == 4

# what are some things I want to test?
# I'm still getting the right columns

# trying a thing that gives many


@pytest.mark.xfail
def test_broken_increment():
    assert skeleton.broken_increment(
        3) == 'Positive, greater than zero (wrong)'
    assert skeleton.broken_increment(1) == 'Positive, greater than zero'

# I want a parametrized one instead of one with copied:


@pytest.mark.parametrize("test_input,expected", [
    (7, 'Positive, greater than zero (wrong)'),
    (5, 'Positive, greater than zero (wrong)'),
    (41, 'Positive, greater than zero (wrong)'),
])
def test_broken_increment_parametrized(test_input, expected):
    assert skeleton.broken_increment(test_input) == expected


@given(st.integers(max_value=100, min_value=2))
def test_inc_with_given(high):
    assert skeleton.increment(high) == (high +1)


# @given(st.sampled_from(elements))
# def test_inc_with_given(high):
#     assert skeleton.increment(high) == (high +1)