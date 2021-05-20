import itertools as it


class LogicSystem:

    @staticmethod
    def __create_layer(connections, current_layers):
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
        self.sys_name = file_name
        self.text_file = open('{}.txt'.format(file_name), 'w+')
        self.layers = self.organize_comps(self.connections)
        self.mapped_comps = list(it.chain.from_iterable(self.layers))

    def starting_text(self):
        text = 'This text file is a simulation of the system {}\n\n' \
               'The following is the network layout for the system.'.format(self.sys_name)

        for layer in range(len(self.layers)):
            text += '\n\nLayer {}:\n\n'.format(layer+1)
            for comp in self.layers[layer]:
                text += '     {}'.format(comp)
        text += '\n\n' + '-'*65 + '\n\nInitial state for all components:\n\n\n'

        for comp in self.mapped_comps:
            text += '{} output: {} current state: {}\n\n'.format(comp.comp_name, comp.out, comp.current_state)

        self.text_file.write(text)

    def run_system(self):
        self.starting_text()
        self.text_file.write('-'*65 + '\n\nSimulation Start\n\n')
        run = 1
        while run <= self.sys_runs:

            self.text_file.write("-"*65+'\n\nRun{}:\n\n'.format(run))

            for comp in self.mapped_comps:

                input_comps = self.connections[comp]
                input_values = [in_comp.out for in_comp in input_comps]

                comp.output(*input_values)
                self.text_file.write('{} output: {} current state:{}\n\n'.format(comp.comp_name,
                                                                                 comp.out,
                                                                                 comp.current_state))
            run += 1

        self.text_file.close()
