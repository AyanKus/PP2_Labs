class ConsoleIO:

    def getString(self):
        return input("Please, write something here: ")
    
    def printString(self, line: str):
        return print(line.upper())
    

consoleIO = ConsoleIO()

line = consoleIO.getString()
consoleIO.printString(line)    