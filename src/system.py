import itertools as it
from src.components import *


class LogicSystem:

    def __create_layer(self, connections, current_layers):
        mapped_comps = list(it.chain.from_iterable(current_layers))

        layer = []

        for comp, input_comps in connections.items():

            if comp not in layer \
                    and comp not in mapped_comps \
                    and all(input_comp in mapped_comps for input_comp in input_comps):
                layer.append(comp)

        return layer

    def organize_comps(self, connections):
        layers = [[comp for comp in connections if connections[comp] == []]]

        comp_count = len(layers[0])

        num_of_comps = len(connections)

        while comp_count != num_of_comps:
            new_layer = self.__create_layer(connections, layers)

            layers.append(new_layer)

            comp_count += len(new_layer)

        return layers

    def __init__(self, connections, sys_runs, file_name):

        self.connections = connections
        self.sys_runs = sys_runs
        self.text_file = open('{}.txt'.format(file_name), 'w+')
        self.layers = self.organize_comps(self.connections)
        self.mapped_comps = list(it.chain.from_iterable(self.layers))

    def run_system(self):

        run = 0
        # stop = 0
        while run < self.sys_runs:

            for comp in self.mapped_comps:

                input_comps = self.connections[comp]
                input_values = []
                for in_comp in input_comps:
                    input_values.append(in_comp.out)

                # if isinstance(comp, USR):
                #     if comp.current_state == [None, None, None, None]:
                #         stop += 1
                #
                #     if stop == 2:
                #         run = self.sys_runs
                #
                #     comp.output(input_values)

                if not isinstance(comp, ConstOut):
                    comp.output(*input_values)

                else:
                    pass

            run += 1

        self.text_file.close()


