# import LogicSimulator.src as comps
from src.components import *
import pytest

a = AndGate('and1')
b = XorGate('xor1')



def test_out():
    a.output([1, 1])
    assert a.out == 1, 'The result expected was 1'
    b.output([1, 1])
    assert b.out == 0, 'The result expected was 0'

