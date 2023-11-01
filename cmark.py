import sys
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QObject

if __name__=="__main__":
    app=QGuiApplication(sys.argv)

    engine=QQmlApplicationEngine()
    engine.load("main.qml")
    root = engine.rootObjects()[0].findChild(QObject, "textBrowser")
    root.setProperty("text", "Text Browser")
    
    sys.exit(app.exec())
