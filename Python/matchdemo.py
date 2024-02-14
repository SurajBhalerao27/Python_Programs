from enum import Enum
class Color(Enum):
    RED ='red'
    GREEN ='green'
    BLUE ='blue'

color = Color(input("Enter a color code you want: "))

match color:
    case Color.RED:
        print("I see red ")
    case Color.GREEN:
        print("Grass is green ")
    case Color.BLUE:
        print("Water is blue ")
