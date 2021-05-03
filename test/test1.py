# import LogicSimulator.src as comps
from src.components import *
from src.system import *
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

j = Mux('mux1')

k = Switch('swt1')

l = USR('usr1', [0, 1, 0, 1])

m = Gate('and2', 'and')

connection_dict = {a: [], b: [], c: [], g: [d, c], d: [a, b, c], e: [b, c], f: [d, e], h: [], i: [a]}

gate_outputs = {'and': [0, 0, 0, 1], 'or': [0, 1, 1, 1], 'nand': [1, 1, 1, 0], 'nor': [1, 0, 0, 0], 'xor': [0, 1, 1, 0]}


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

    gate = m

    for input_list in [[0, 0], [0, 1], [1, 0], [1, 1]]:

        gate.output(input_list)

        outputs.append(gate.out)

    assert outputs == [0, 0, 0, 1]


def test_organizer():

    layers = organize_comps(connection_dict)

    assert layers == [[a, b, c, h], [d, e, i], [g, f]]


def test_gates():

    outputs = []
    comp = e
    gate_type = 'and'

    for inputs in [[0, 0], [0, 1], [1, 0], [1, 1]]:
        comp.output(*inputs)
        outputs.append(comp.out)

    assert outputs == gate_outputs[gate_type]


def test_mux():

    outputs = []
    comp = j

    for inputs in [[1, 2, 3, 4, 0, 0], [1, 2, 3, 4, 1, 0], [1, 2, 3, 4, 0, 1], [1, 2, 3, 4, 1, 1]]:
        comp.output(*inputs)
        outputs.append(comp.out)

    assert outputs == [1, 2, 3, 4]


def test_switch():

    outputs = []
    comp = k

    for inputs in [[1, 0], [1, 1], [0, 0, 1], [0, 1, 1]]:
        comp.output(*inputs)
        outputs.append(comp.out)

    assert outputs == [0, 1, 0, 1]


def test_usr():

    outputs = []
    states = []
    comp = l
    for inputs in [[0, 0, 1, 2], [0, 1, 1, 2], [1, 0, 1, 3], [1, 1, 1, None, 1, 1, 1, 1],
                   [1, 1, 0, None, 1, 1, 1, 1]]:

        comp.output(*inputs)
        outputs.append(comp.out)
        states.append(comp.current_state)

    assert outputs == [0, 1, 2, [0, 1, 0, 3], [0, 1, 0, 3]]
    assert states == [[0, 1, 0, 1], [2, 0, 1, 0], [0, 1, 0, 3], [1, 1, 1, 1], [1, 1, 1, 1]]


