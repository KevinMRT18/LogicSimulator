class Comps:

    def __init__(self, name):
        self.comp_name = name

    def __repr__(self):
        return self.comp_name


class AndGate(Comps):

    def output(self, input_list):

        for i in input_list:

            if i == 1:

                self.out = 1

            else:

                self.out = 0

                break


class NandGate(Comps):

    def output(self, input_list):

        for i in input_list:

            if i == 1:

                self.out = 0

            else:

                self.out = 1

                break


class OrGate(Comps):

    def output(self, input_list):

        for i in input_list:

            if i == 1:

                self.out = 1

                break

            else:

                self.out = 0


class NorGate(Comps):

    def output(self, input_list):

        for i in input_list:

            if i == 1:

                self.out = 0

                break

            else:

                self.out = 1


class XorGate(Comps):

    def output(self, *inputs):

        self.variable = inputs.count(1)

        if (self.variable % 2) == 0:

            self.out = 0

        else:
            self.out = 1


class NotGate(Comps):

    def output(self, inputs):

        if inputs == 1:

            self.out = 0

        else:

            self.out = 1


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


def flat(input_list):
    flat_list = []

    for sub_list in input_list:

        for index in sub_list:
            flat_list.append(index)

    return flat_list


def order1(connection_dict):
    layer1 = []

    for key in connection_dict:

        if connection_dict[key] == []:
            layer1.append(repr(key))

    return layer1


def order2(connection_dict, layer_list, index):
    layer = []

    flat_list = flat(layer_list)

    for key in connection_dict:

        counter = 0

        for value in connection_dict[key]:

            if repr(value) in layer_list[index]:

                counter += 1

            elif repr(value) not in flat_list:

                counter = 0

                break

        if counter >= 1 and repr(key) not in layer:
            layer.append(repr(key))

    return layer


def layer_list(connection_dict):
    layers = []

    layers.append(order1(connection_dict))

    index = 0

    comps = 0

    while comps != len(connection_dict):

        layers.append(order2(connection_dict, layers, index))

        index += 1

        comps = 0

        for a in layers:
            comps += len(a)

    return layers