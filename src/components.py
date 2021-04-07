class AndGate:

    def __init__(self, name):

        self.comp_name = name

    def output(self, input_list):

        for i in input_list:

            if i == 1:

                self.out = 1

            else:

                self.out = 0

                break


class NandGate:

    def __init__(self, name):

        self.comp_name = name

    def output(self, input_list):

        for i in input_list:

            if i == 1:

                self.out = 0

            else:

                self.out = 1

                break


class OrGate:

    def __init__(self, name):

        self.comp_name = name

    def output(self, input_list):

        for i in input_list:

            if i == 1:

                self.out = 1

                break

            else:

                self.out = 0


class NorGate:

    def __init__(self, name):

        self.comp_name = name

    def output(self, input_list):

        for i in input_list:

            if i == 1:

                self.out = 0

                break

            else:

                self.out = 1


class XorGate:

    def __init__(self, name):

        self.comp_name = name

    def output(self, *inputs):

        self.variable = inputs.count(1)

        if (self.variable % 2) == 0:

            self.out = 0

        else:
            self.out = 1


class NotGate:

    def __init__(self, name):

        self.comp_name = name

    def output(self, inputs):

        if inputs == 1:

            self.out = 0

        else:

            self.out = 1


class ConstOut:

    def __init__(self, name, output):
        self.comp_name = name

        self.out = output


a = ConstOut('Cst1', 0)

b = ConstOut('Cst2', 1)

c = ConstOut('Cst3', 1)

d = AndGate('And1')

e = AndGate('And2')

f = AndGate('And3')

g = AndGate('And4')

connection_dict = {a: [], b: [], c: [], g: [d, c], d: [a, b, c], e: [b, c], f: [d, e]}


def order1(connection_dict):
    layer1 = []

    for key in connection_dict:

        if connection_dict[key] == []:
            layer1.append(key)

    return layer1


def order2(connection_dict, layer_list):
    layer = []

    for key in connection_dict:

        a = 0

        for value in connection_dict[key]:

            if value not in layer_list:

                break

            else:

                a += 1

        if a >= 1 and key not in layer:
            layer.append(key)

    return layer


def layer_list(connection_dict):
    layers = []

    layers.append(order1(connection_dict))

    index = 0

    comps = 0

    while comps != len(connection_dict):

        layers.append(order2(connection_dict, layers[index]))

        index += 1

        comps = 0

        for a in layers:
            comps += len(a)

    return layers