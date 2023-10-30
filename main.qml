import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

Window {
    visible: true
    width: 600
    height: 500
    title: "HelloApp"
    opacity: 0.7
    color : "black"
    // borderless
    // flags: Qt.Window | Qt.FramelessWindowHint

    TextArea {
        anchors.fill: parent
        anchors.leftMargin: 15
        selectByMouse: true
        color: "ghostwhite"
        text: "Hello World"
        font.pixelSize: 36
    }
}
