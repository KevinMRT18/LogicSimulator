import itertools as it


class Comps:

    def __init__(self, name):
        self.comp_name = name
        self.out = None

    def __repr__(self):
        return self.comp_name

    class Gates:

        def __init__(self, name, gate_type):
            self.gate_type = gate_type
            self.comp_name = name
            self.out = None

        def output(self, input_list):

            if (self.gate_type == 'and' and all(input_list)) \
                    or (self.gate_type == 'nand' and input_list.count(0) >= 1) \
                    or (self.gate_type == 'or' and input_list.count(1) >= 1)  \
                    or (self.gate_type == 'nor' and input_list.count(1) == 0) \
                    or (self.gate_type == 'xor' and input_list.count(1) % 2 != 0) \
                    or (self.gate_type == 'not' and input_list == [0]):

                self.out = 1

            else:

                self.out = 0


class AndGate(Comps):

    def output(self, input_list):

        if all(input_list):

            self.out = 1

        else:

            self.out = 0


class NandGate(Comps):

    def output(self, input_list):

        if input_list.count(0) >= 1:

            self.out = 1

        else:

            self.out = 0


class OrGate(Comps):

    def output(self, input_list):

        if input_list.count(1) >= 1:

            self.out = 1

        else:

            self.out = 0


class NorGate(Comps):

    def output(self, input_list):

        if input_list.count(1) == 0:

            self.out = 1

        else:

            self.out = 0


class XorGate(Comps):

    def output(self, input_list):

        if input_list.count(1) % 2 != 0:

            self.out = 1

        else:
            self.out = 0


class NotGate(Comps):

    def output(self, input_list):

        if input_list == 0:

            self.out = 1

        else:

            self.out = 0


class ConstOut(Comps):

    def __init__(self, name, output):
        super().__init__(name)

        self.out = output


a = ConstOut('Cst1', 0)

b = ConstOut('Cst2', 1)

c = ConstOut('Cst3', 1)

d = OrGate('Or1')

e = AndGate('And1')

f = NandGate('Nand1')

g = NorGate('Nor1')

connection_dict = {a: [], b: [], c: [], g: [d, c], d: [a, b, c], e: [b, c], f: [d, e]}


def _create_layer(connections, current_layers):

    mapped_comps = list(it.chain.from_iterable(current_layers))

    layer = []

    for comp, input_comps in connections.items():

        if comp not in layer \
                and comp not in mapped_comps \
                and all(input_comp in mapped_comps for input_comp in input_comps):

            layer.append(comp)

    return layer


def organize_comps(connections):

    layers = [[comp for comp in connections if connections[comp] == []]]

    comp_count = len(layers[0])

    num_of_comps = len(connections)

    while comp_count != num_of_comps:
        new_layer = _create_layer(connections, layers)

        layers.append(new_layer)

        comp_count += len(new_layer)

    return layers
