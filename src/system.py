import itertools as it


class LogicSystem:

    def __init__(self, connections, sys_runs, file_name):

        self.connections = connections
        self.sys_runs = sys_runs
        self.text_file = '{}.txt'.format(file_name)
