from __future__ import annotations

from hypothesis import given, strategies as st
from rpncalc.rpn_v2 import RPNCalculator, Config


@given(st.integers(), st.integers())
def test_operators(n1: int, n2: int):
    rpn = RPNCalculator(Config())
    rpn.evaluate(str(n1))
    rpn.evaluate(str(n2))
    rpn.evaluate("+")
    assert rpn.stack == [n1 + n2]


@given(
    st.lists(
        st.one_of(
            st.integers().map(str),
            st.floats().map(str),
            st.just("+"), st.just("-"),
            st.just("*"), st.just("/"),
        )
    )
)
def test_usage(inputs: list[str]):
    rpn = RPNCalculator(Config())
    for inp in inputs:
        rpn.evaluate(inp)