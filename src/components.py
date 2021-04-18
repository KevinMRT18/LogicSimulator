import itertools as it


class Comps:

    def __init__(self, name):
        self.comp_name = name
        self.out = 0

    def __repr__(self):
        return self.comp_name


class Gate:

    def __init__(self, name, gate_type):
        self.gate_type = gate_type
        self.comp_name = name
        self.out = 0

    def output(self, input_list):

        output_type = {'and': all(input_list), 'nand': input_list.count(0) >= 1,
                       'or': input_list.count(1) >= 1, 'nor': input_list.count(1) == 0,
                       'xor': input_list.count(1) % 2 != 0, 'not': input_list == [0]}.pop(self.gate_type)

        if output_type:

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


class Clock(Comps):

    def output(self):

        if self.out == 1:

            self.out = 0

        else:

            self.out = 1


class Mux(Comps):

    def output(self, input_list):

        [input_0, input_1, input_2, input_3, mode_0, mode_1] = input_list

        if mode_1 == 0 and mode_0 == 0:

            self.out = input_0

        elif mode_1 == 0 and mode_0 == 1:

            self.out = input_1

        elif mode_1 == 1 and mode_0 == 0:

            self.out = input_2

        else:

            self.out = input_3


class Switch(Comps):

    def output(self, input_list):

        if len(input_list) == 2:
            input_0 = input_list[0]
            mode = input_list[1]
            if mode == 1:
                self.out = input_0
            else:
                pass

        else:
            input_0 = input_list[0]
            input_1 = input_list[1]
            mode = input_list[2]
            if mode == 1:
                self.out = input_1
            else:
                self.out = input_0


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
