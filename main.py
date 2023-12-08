#Copyright (c) 2023 Nikolaus Luebbert
#All rights reserved. Although I will probably give you permission to use it for whatever you want to do with it if you ask me first.
from logic import *

def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()
    

if __name__ == '__main__':
    main()
