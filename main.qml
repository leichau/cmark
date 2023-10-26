import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

Window {
    visible: true
    width: 600
    height: 500
    title: "HelloApp"
    opacity: 0.5
    // borderless
    // flags: Qt.Window | Qt.FramelessWindowHint

    Text {
        anchors.centerIn: parent
        text: "Hello World"
        font.pixelSize: 24
    }
}
