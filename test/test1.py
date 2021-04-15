# import LogicSimulator.src as comps
from src.components import *
import pytest

a = ConstOut('Cst1', 0)

b = ConstOut('Cst2', 1)

c = ConstOut('Cst3', 1)

d = OrGate('Or1')

e = AndGate('And1')

f = NandGate('Nand1')

g = NorGate('Nor1')

h = Clock('Clk1')

i = NotGate('Not1')

connection_dict = {a: [], b: [], c: [], g: [d, c], d: [a, b, c], e: [b, c], f: [d, e], h: [], i: [a]}


def test_clock():

    output_list = []

    comp = h

    assert comp.out == 0        # This tests if the initial value of the clock is 0

    for run in range(5):
        comp.output()
        output_list.append(comp.out)

    assert output_list == [1, 0, 1, 0, 1]    # This tests if the out value of the clock changes with each output call.


def test_gate():

    outputs = []

    gate = g

    for input_list in [[0, 0], [0, 1], [1, 0], [1, 1]]:

        gate.output(input_list)

        outputs.append(gate.out)

    assert outputs == [1, 0, 0, 0]


def test_organizer():

    layers = organize_comps(connection_dict)

    assert layers == [[a, b, c, h], [d, e, i], [g, f]]
