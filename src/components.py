import itertools as it


class InputNumberError(Exception):

    def __init__(self, comp, required_inputs):
        self.message = 'The {} component should receive {}.'.format(comp, required_inputs)
        super().__init__(self.message)


class Comps:
    """
    This is a base class for the some of the available components that initializes
    the object with a name and the self.out value of 0.
    """

    def __init__(self, name):
        self.comp_name = name
        self.out = 0
        self.current_state = 'None'
    def __repr__(self):
        return self.comp_name


class Gate:

    def __init__(self, name, gate_type):
        self.gate_type = gate_type
        self.comp_name = name
        self.out = 0

    def output(self, input_list):
        self.out = int({'and': all(input_list),
                        'nand': not all(input_list),
                        'or': any(input_list),
                        'nor': not any(input_list),
                        'xor': input_list.count(1) % 2 != 0
                        }[self.gate_type])


class AndGate(Comps):
    """
    This class defines objects with the output method that simulates the behavior of
    the AND Gate. If all the input values are (1) the output will be a (1). Otherwise,
    if there is at least one zero as an input, the output will be a (0).

    The two input truth table for the AND Gate is:

    S1 S0 │ output
    ──────┼───────
     0  0 │   0
     0  1 │   0
     1  0 │   0
     1  1 │   1
    """

    def output(self, *input_list):

        if len(input_list) < 2:
            raise InputNumberError(self.comp_name, '2 or more inputs')

        if all(input_list):
            self.out = 1

        else:
            self.out = 0


class NandGate(Comps):
    """
    This class defines objects with the output method that simulates the behavior of
    the NAND Gate. If the at least of the input values is (0), the output will be (1).
    Otherwise, if all inputs are (1), the output will be (0).

    The two input truth table for the NAND Gate is:

    S1 S0 │ output
    ──────┼───────
     0  0 │   1
     0  1 │   1
     1  0 │   1
     1  1 │   0
    """

    def output(self, *input_list):

        if len(input_list) != 2:
            raise InputNumberError(self.comp_name, 'only 2 inputs')

        if input_list.count(0) >= 1:
            self.out = 1

        else:
            self.out = 0


class OrGate(Comps):
    """
    This class defines objects with the output method that simulates the behavior of
    the OR Gate. If at least one of the inputs in a (1), the output will be a (1).
    Otherwise, if all the inputs are (0), the output will be (0).

    The two input truth table for the OR Gate is:

    S1 S0 │ output
    ──────┼───────
     0  0 │   0
     0  1 │   1
     1  0 │   1
     1  1 │   1
    """

    def output(self, *input_list):

        if len(input_list) < 2:
            raise InputNumberError(self.comp_name, '2 or more inputs')

        if input_list.count(1) >= 1:
            self.out = 1

        else:
            self.out = 0


class NorGate(Comps):
    """
    This class defines objects with the output method that simulates the behavior of
    the NOR Gate. If all the input values are (0), the output will be (1). Otherwise,
    at least one of the inputs is (1), the output will be (0).

    The two input truth table for the NOR Gate is:

    S1 S0 │ output
    ──────┼───────
     0  0 │   1
     0  1 │   0
     1  0 │   0
     1  1 │   0
    """

    def output(self, *input_list):

        if len(input_list) != 2:
            raise InputNumberError(self.comp_name, 'only 2 inputs')

        if input_list.count(1) == 0:
            self.out = 1

        else:
            self.out = 0


class XorGate(Comps):
    """
    This class defines objects with the output method that simulates the behavior
    of the XOR Gate. If the number of inputs that are (1) is odd, the output will
    be (1). Otherwise, if the number of inputs that are (1) is even, the output
    will be (0).

    The two input truth table for the XOR Gate is:

    S1 S0 │ output
    ──────┼───────
     0  0 │   0
     0  1 │   1
     1  0 │   1
     1  1 │   0
    """

    def output(self, *input_list):

        if len(input_list) < 2:
            raise InputNumberError(self.comp_name, '2 or more inputs')

        if input_list.count(1) % 2 != 0:
            self.out = 1

        else:
            self.out = 0


class NotGate(Comps):
    """
    This class defines objects with the output method that simulates the
    behavior of the NOT Gate. If the input is a (0) the output is will be a
    (1) or if the input is a (1) the output will be a (0).

    The truth table for the NOT Gate is:

     S │ output
    ───┼───────
     0 │   1
     1 │   0
    """

    def output(self, *input_list):

        if len(input_list) != 1:
            raise InputNumberError(self.comp_name, 'only 1 input')

        self.out = int(not input_list[0])


class ConstOut(Comps):
    """
    This class defines objects that will provide a fixed output, either
    a (0) or a (1), throughout the simulation.
    """

    def __init__(self, name, output):
        super().__init__(name)
        self.out = output

    def output(self, *input_list):
        if len(input_list) != 0:
            raise InputNumberError(self.comp_name, '0 inputs')

        pass


class Clock(Comps):
    """
    This class defines objects with an output method that will change
    the output value from (1) to (0) or from (0) to (1) on all simulation
    runs.
    """

    def output(self, *input_list):
        if len(input_list) != 0:
            raise InputNumberError(self.comp_name, '0 inputs')

        self.out = int(not self.out)


class Mux(Comps):
    """
    This class defines objects with an output method that simulates the
    behavior of the MUX component. This component will accept 6 inputs:
    2 for mode selection and 4 input values. The mode selection inputs
    determine which of the 4 input values goes to the output.

    This is the mode selection table:

    mode_1 mode_0 │ output
    ──────────────┼────────
      0      0    │ Input 0
      0      1    │ Input 1
      1      0    │ Input 2
      1      1    │ Input 3
    """

    def output(self, input_0, input_1, input_2, input_3, mode_0, mode_1):

        if mode_1 == 0 and mode_0 == 0:

            self.out = input_0

        elif mode_1 == 0 and mode_0 == 1:

            self.out = input_1

        elif mode_1 == 1 and mode_0 == 0:

            self.out = input_2

        else:

            self.out = input_3


class Switch(Comps):
    """
    This class defines objects with an output method that simulates the
    behavior of the Switch component. When the component receives two inputs,
    it behaves like a switch where a mode input of (1) passes the input value
    directly to the output. A mode input of (0) blocks the pass and keeps the
    last output value saved.

     S mode │ output
    ────────┼───────
     0   1  │   0
     1   1  │   1
     0   0  │   1
     0   1  │   0


    When the component receives three inputs, the mode selection input selects
    one of the two available input values. If the mode is (0) the input_0 goes
    to the output. Otherwise if the mode is (1), the input_1 goes to the output.

     S1 S0  mode │ output
    ─────────────┼───────
     1   0   0   │   0
     1   0   1   │   1

    """

    def output(self, input_0, mode, input_1=None):

        if input_1:
            if mode:
                self.out = input_1
            else:
                self.out = input_0

        elif mode:
            self.out = input_0


class USR(Comps):
    """
    This class defines objects with the output method that simulates the
    behavior of a 4-Bit Universal Shift Register (USR). Like the real USR,
    this component has 4 register operating modes determined by two mode
    selection inputs.

    USR Operating Modes:

     mode_1 mode_0 │ Register Operations
    ───────────────┼────────────────────
       0      0    │  No Change
       0      1    │  Shift Right
       1      0    │  Shift Left
       1      1    │  Parallel Load
    """

    def __init__(self, name, initial_state):
        super().__init__(name)
        self.current_state = initial_state

    def output(self, mode_1, mode_0, clock, data_in=None, *parallel_inputs):

        if clock == 1:

            if mode_1 == 1 and mode_0 == 1:
                self.out = self.current_state
                self.current_state = list(parallel_inputs)

            elif mode_1 == 1 and mode_0 == 0:
                self.out = self.current_state[0]
                self.current_state = [self.current_state[1],self.current_state[2], self.current_state[3], data_in]

            elif mode_1 == 0 and mode_0 == 1:
                self.out = self.current_state[3]
                self.current_state = [data_in, self.current_state[0], self.current_state[1], self.current_state[2]]

        if not bool(self.out):
            self.out = 0
