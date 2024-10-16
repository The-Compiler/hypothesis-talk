from __future__ import annotations

import sys

from rpncalc.utils import calc

class RPNCalculator:
    def __init__(self, config):
        self.config = config
        self.stack = []

    def run(self) -> None:
        while True:
            inp = input("> ")
            if inp == "q":
                return
            elif inp == "p":
                print(self.stack)
            else:
                self.evaluate(inp)

    def err(self, msg: str) -> None:
        print(msg, file=sys.stderr)

    def evaluate(self, inp: str) -> None:
        try:
            self.stack.append(float(inp))
            return
        except ValueError:
            pass

        if inp not in ["+", "-", "*", "/"]:
            self.err(
                f"Invalid input: {inp}")
            return

        if len(self.stack) < 2:
            self.err("Not enough operands")
            return

        b = self.stack.pop()
        a = self.stack.pop()

        try:
            res = calc(a, b, inp)
        except ZeroDivisionError:
            self.err("Division by zero")
            return

        self.stack.append(res)
        print(res)


if __name__ == "__main__":
    rpn = RPNCalculator()
    rpn.run()