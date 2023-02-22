from watchFaceParser.elements.gts2mini.dateElements.yearMonthAndDay import YearMonthAndDay
from watchFaceParser.elements.gts2mini.dateElements.oneLineMonthAndDay import OneLineMonthAndDay
from watchFaceParser.elements.gts2mini.dateElements.oneLineYearMonthAndDay import OneLineYearMonthAndDay
from watchFaceParser.elements.gts2mini.dateElements.monthAndDayAlt import MonthAndDayAlt

class Date:
    definitions = {
        1: { 'Name': 'MonthAndDayAlt', 'Type': MonthAndDayAlt}, # alternate date
        2: { 'Name': 'OneLineMonthAndDay', 'Type': OneLineMonthAndDay},
        3: { 'Name': 'OneLineYearMonthAndDay', 'Type': OneLineYearMonthAndDay},
        9: { 'Name': 'YearMonthAndDay', 'Type': YearMonthAndDay},  
        4: { 'Name': 'PaddingZeroMonth', 'Type': 'bool'},
        5: { 'Name': 'PaddingZeroDay', 'Type': 'bool'},
        6: { 'Name': 'UnknownBoolean6', 'Type': 'bool'}, #always false!
    }

