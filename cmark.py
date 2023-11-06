import sys
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QObject

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load("main.qml")
    root = engine.rootObjects()[0]
    win = root.findChild(QObject, "textBrowser")
    win.setProperty("text", "Text Browser")
    win.append("Append")
    
    sys.exit(app.exec())
