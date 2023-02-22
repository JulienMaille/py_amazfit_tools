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

        def getIndex(childs, id):
            for index, x in enumerate(childs):
                if x._id == id:
                    return index
            return -1

        def order(childs, id1, id2):
            idx1 = getIndex(childs, id1)
            idx2 = getIndex(childs, id2)
            if idx2 > idx1 >= 0 and idx2 >= 0:
                childs[idx1], childs[idx2] = childs[idx2], childs[idx1]

        # make sure Activity(4) is after Progress elements (7, 9, 15)
        order(t, 4, 7)
        order(t, 4, 9)
        order(t, 4, 15)
        # make sure DateBlock(5) is after Progress elements (7, 9, 15)
        # make sure AnalogDial(20) is after Digital Dial (21)
        order(t, 20, 21)
        # make sure TimeExtended(3), DateBlock(5), Weather(6), Steps(7) and Battery(9) is after Status (8)
        order(t, 3, 8)
        order(t, 5, 8)
        order(t, 6, 8)
        order(t, 7, 8)
        order(t, 9, 8)
        # make sure AoD TimeExtended(29:1) is after AoD Weekday(29:3)
        aod_idx = getIndex(t, 29)
        if aod_idx >= 0: order(t[aod_idx]._child, 1, 3)

        return t
