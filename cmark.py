import sys
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtGui import QGuiApplication

if __name__=="__main__":
    app=QGuiApplication(sys.argv)

    engine=QQmlApplicationEngine()
    engine.load("main.qml")
    
    sys.exit(app.exec())
