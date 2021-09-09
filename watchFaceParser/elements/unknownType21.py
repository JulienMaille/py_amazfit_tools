from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.unknownType21d8 import UnknownType21d8

class UnknownType21:
    definitions = {
        1: { 'Name': 'Unknown1', 'Type': Number}, #looks like this is a hours?
        3: { 'Name': 'Unknown3', 'Type': 'long'},
        6: { 'Name': 'Unknown6', 'Type': 'long'}, 
        8: { 'Name': 'Unknown8', 'Type': UnknownType21d8}, #looks like this is a minutes?
    }

