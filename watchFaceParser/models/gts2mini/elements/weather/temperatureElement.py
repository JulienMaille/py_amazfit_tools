import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int


class TemperatureElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._current = None
        self._oneline = None
        self._lowest = None
        self._highes = None
        super(TemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        if self._current:
            self._current.draw4(drawer, resources, state.getCurrentTemperature())
        if self._oneline:
            self._oneline.draw3(drawer, resources, state)
        if self._lowest:
            self._lowest.draw4(drawer, resources, state.getCurrentTemperature()-10)
        if self._highes:
            self._highes.draw4(drawer, resources, state.getCurrentTemperature()+10)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.weather.weatherTextElement import WeatherTextElement
            self._current = WeatherTextElement(parameter, self, 'Current')
            return self._current
        elif parameterId == 2: # OneLine
            from watchFaceParser.models.gts2mini.elements.weather.oneLineTemperatureElement import OneLineTemperatureElement
            self._oneline = OneLineTemperatureElement(parameter, self, 'OneLine')
            return self._current
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.weather.weatherTextElement import WeatherTextElement
            self._highes = WeatherTextElement(parameter, self, 'Highest')
            return self._highes
        if parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.weather.weatherTextElement import WeatherTextElement
            self._lowest = WeatherTextElement(parameter, self, 'Lowest')
            return self._lowest
        else:
            print ("Unknown TemperatureElement",parameterId)
            super(TemperatureElement, self).createChildForParameter(parameter)
