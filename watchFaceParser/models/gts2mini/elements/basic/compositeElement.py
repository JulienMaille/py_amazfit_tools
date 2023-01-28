import logging

from watchFaceParser.models.gts2mini.elements.basic.element import Element

class CompositeElement(Element):
    def __init__(self, parameters, parameter, parent, name):
        self._child = []
        if parameters is not None:
            for parameterChild in parameters:
                self._child.append(self.createChildForParameter(parameterChild))
        else:
            super(CompositeElement, self).__init__(parameter = parameter, parent = parent, name = name)
            if parameter.getChildren():
                for parameterChild in parameter.getChildren():
                    self._child.append(self.createChildForParameter(parameterChild))


    def getChildren(self):
        return self._child


    def createChilds(self, parameters):
        assert(type(parameters) == list)
        for parameterChild in parameters:
            self._child.append(self.createChildForParameter(parameterChild))


    def createChildForParameter(self, parameter):
        if parameter.hasChildren():
            from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement
            return ContainerElement(parameters = None, parameter = parameter, parent = self, name = '')
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
        return ValueElement(parameter = parameter, parent = self, name = '')


    def getDrawableChildren(self):
        t = []
        for child in self._child:
            try:
                getattr(child, 'draw3')
                t.append(child)
            except AttributeError:
                pass

        def getIndex(id):
            for index, x in enumerate(t):
                if x._id == id:
                    return index
            return -1

        def order(id1, id2):
            idx1 = getIndex(id1)
            idx2 = getIndex(id2)
            if( idx1 < idx2 ):
                t[idx1], t[idx2] = t[idx2], t[idx1]
        # make sure Activity(4) is after Progress elements (7, 9, 15)
        order(4, 7)
        order(4, 9)
        order(4, 15)
        # make sure DateBlock(5) is after Progress elements (7, 9, 15)
        # make sure AnalogDial(20) is after Digital Dial (21)
        order(20, 21)
        # make sure TimeExtended(3), DateBlock(5), Weather(6), Steps(7) and Battery(9) is after Status (8)
        order(3, 8)
        order(5, 8)
        order(6, 8)
        order(7, 8)
        order(9, 8)

        return t
