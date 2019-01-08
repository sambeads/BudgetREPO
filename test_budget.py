import skeleton
import pytest
from hypothesis import given
import hypothesis.strategies as st

# I want to check to make sure that there aren't any rows with negative returns
@pytest.mark.xfail
def test_no_negative_rows():
    df = skeleton.read_from_excel()
    has_rows_less_than_zero = df['Amount'][df.Amount < 0].any()
    assert not has_rows_less_than_zero
