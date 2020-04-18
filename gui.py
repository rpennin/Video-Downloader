# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dl-gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(743, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.formTabWidget.setToolTip("")
        self.formTabWidget.setToolTipDuration(-1)
        self.formTabWidget.setStyleSheet("")
        self.formTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.formTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.formTabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.formTabWidget.setUsesScrollButtons(True)
        self.formTabWidget.setDocumentMode(False)
        self.formTabWidget.setTabsClosable(False)
        self.formTabWidget.setObjectName("formTabWidget")
        self.downloadSingleVideoTab = QtWidgets.QWidget()
        self.downloadSingleVideoTab.setEnabled(True)
        self.downloadSingleVideoTab.setToolTip("")
        self.downloadSingleVideoTab.setStyleSheet("font: 10pt \"Microsoft YaHei\";")
        self.downloadSingleVideoTab.setObjectName("downloadSingleVideoTab")
        self.singleVideoDownloadLabel = QtWidgets.QLabel(self.downloadSingleVideoTab)
        self.singleVideoDownloadLabel.setGeometry(QtCore.QRect(0, 0, 721, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.singleVideoDownloadLabel.setFont(font)
        self.singleVideoDownloadLabel.setTextFormat(QtCore.Qt.AutoText)
        self.singleVideoDownloadLabel.setScaledContents(False)
        self.singleVideoDownloadLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.singleVideoDownloadLabel.setWordWrap(True)
        self.singleVideoDownloadLabel.setIndent(-1)
        self.singleVideoDownloadLabel.setObjectName("singleVideoDownloadLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.downloadSingleVideoTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 150, 491, 27))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.videoURLHLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.videoURLHLayout.setContentsMargins(0, 0, 0, 0)
        self.videoURLHLayout.setObjectName("videoURLHLayout")
        self.videoURLLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.videoURLLabel.setObjectName("videoURLLabel")
        self.videoURLHLayout.addWidget(self.videoURLLabel)
        self.singleVideoURLLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.singleVideoURLLineEdit.setObjectName("singleVideoURLLineEdit")
        self.videoURLHLayout.addWidget(self.singleVideoURLLineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.downloadSingleVideoTab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 220, 541, 29))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.saveVideoLocationHLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveVideoLocationHLayout.setContentsMargins(0, 0, 0, 0)
        self.saveVideoLocationHLayout.setObjectName("saveVideoLocationHLayout")
        self.singleVideoSaveLocationLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.singleVideoSaveLocationLabel.setObjectName("singleVideoSaveLocationLabel")
        self.saveVideoLocationHLayout.addWidget(self.singleVideoSaveLocationLabel)
        self.singleVideoSaveLocationLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.singleVideoSaveLocationLineEdit.setToolTip("")
        self.singleVideoSaveLocationLineEdit.setObjectName("singleVideoSaveLocationLineEdit")
        self.saveVideoLocationHLayout.addWidget(self.singleVideoSaveLocationLineEdit)
        self.singleVideoBrowsePushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.singleVideoBrowsePushButton.setObjectName("singleVideoBrowsePushButton")
        self.saveVideoLocationHLayout.addWidget(self.singleVideoBrowsePushButton)
        self.saveDefaultVideoLocationLabel = QtWidgets.QLabel(self.downloadSingleVideoTab)
        self.saveDefaultVideoLocationLabel.setGeometry(QtCore.QRect(90, 250, 541, 20))
        self.saveDefaultVideoLocationLabel.setStyleSheet("font: 25 9pt \"Microsoft YaHei\";")
        self.saveDefaultVideoLocationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.saveDefaultVideoLocationLabel.setObjectName("saveDefaultVideoLocationLabel")
        self.downloadSingleVideoButton = QtWidgets.QPushButton(self.downloadSingleVideoTab)
        self.downloadSingleVideoButton.setGeometry(QtCore.QRect(270, 310, 161, 41))
        self.downloadSingleVideoButton.setObjectName("downloadSingleVideoButton")
        self.formTabWidget.addTab(self.downloadSingleVideoTab, "")
        self.importPlaylistTab = QtWidgets.QWidget()
        self.importPlaylistTab.setToolTip("")
        self.importPlaylistTab.setAutoFillBackground(True)
        self.importPlaylistTab.setStyleSheet("font: 10pt \"Microsoft YaHei\";")
        self.importPlaylistTab.setObjectName("importPlaylistTab")
        self.playlistDownloadLabel = QtWidgets.QLabel(self.importPlaylistTab)
        self.playlistDownloadLabel.setGeometry(QtCore.QRect(0, 0, 721, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.playlistDownloadLabel.setFont(font)
        self.playlistDownloadLabel.setTextFormat(QtCore.Qt.AutoText)
        self.playlistDownloadLabel.setScaledContents(False)
        self.playlistDownloadLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.playlistDownloadLabel.setWordWrap(True)
        self.playlistDownloadLabel.setIndent(-1)
        self.playlistDownloadLabel.setObjectName("playlistDownloadLabel")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.importPlaylistTab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(90, 220, 541, 29))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.savePlaylistLocationHLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.savePlaylistLocationHLayout.setContentsMargins(0, 0, 0, 0)
        self.savePlaylistLocationHLayout.setObjectName("savePlaylistLocationHLayout")
        self.playlistSaveLocationLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.playlistSaveLocationLabel.setObjectName("playlistSaveLocationLabel")
        self.savePlaylistLocationHLayout.addWidget(self.playlistSaveLocationLabel)
        self.playlistSaveLocationLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.playlistSaveLocationLineEdit.setToolTip("")
        self.playlistSaveLocationLineEdit.setObjectName("playlistSaveLocationLineEdit")
        self.savePlaylistLocationHLayout.addWidget(self.playlistSaveLocationLineEdit)
        self.playlistBrowsePushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.playlistBrowsePushButton.setObjectName("playlistBrowsePushButton")
        self.savePlaylistLocationHLayout.addWidget(self.playlistBrowsePushButton)
        self.saveDefaultPlaylistLocationLabel = QtWidgets.QLabel(self.importPlaylistTab)
        self.saveDefaultPlaylistLocationLabel.setGeometry(QtCore.QRect(90, 250, 541, 20))
        self.saveDefaultPlaylistLocationLabel.setStyleSheet("font: 25 9pt \"Microsoft YaHei\";")
        self.saveDefaultPlaylistLocationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.saveDefaultPlaylistLocationLabel.setObjectName("saveDefaultPlaylistLocationLabel")
        self.downloadPlaylistButton = QtWidgets.QPushButton(self.importPlaylistTab)
        self.downloadPlaylistButton.setGeometry(QtCore.QRect(270, 310, 161, 41))
        self.downloadPlaylistButton.setObjectName("downloadPlaylistButton")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.importPlaylistTab)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(120, 150, 491, 27))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.playlistURLHLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.playlistURLHLayout.setContentsMargins(0, 0, 0, 0)
        self.playlistURLHLayout.setObjectName("playlistURLHLayout")
        self.playlistURLLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.playlistURLLabel.setObjectName("playlistURLLabel")
        self.playlistURLHLayout.addWidget(self.playlistURLLabel)
        self.playlistURLLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.playlistURLLineEdit.setObjectName("playlistURLLineEdit")
        self.playlistURLHLayout.addWidget(self.playlistURLLineEdit)
        self.formTabWidget.addTab(self.importPlaylistTab, "")
        self.importFromFileTab = QtWidgets.QWidget()
        self.importFromFileTab.setToolTip("")
        self.importFromFileTab.setStyleSheet("font: 10pt \"Microsoft YaHei\";")
        self.importFromFileTab.setObjectName("importFromFileTab")
        self.downloadFromFileButton = QtWidgets.QPushButton(self.importFromFileTab)
        self.downloadFromFileButton.setGeometry(QtCore.QRect(270, 310, 161, 41))
        self.downloadFromFileButton.setObjectName("downloadFromFileButton")
        self.saveDefaultPlaylistLocationLabel_2 = QtWidgets.QLabel(self.importFromFileTab)
        self.saveDefaultPlaylistLocationLabel_2.setGeometry(QtCore.QRect(90, 250, 541, 20))
        self.saveDefaultPlaylistLocationLabel_2.setStyleSheet("font: 25 9pt \"Microsoft YaHei\";")
        self.saveDefaultPlaylistLocationLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.saveDefaultPlaylistLocationLabel_2.setObjectName("saveDefaultPlaylistLocationLabel_2")
        self.fileVideosDownloadLabel = QtWidgets.QLabel(self.importFromFileTab)
        self.fileVideosDownloadLabel.setGeometry(QtCore.QRect(0, 0, 721, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.fileVideosDownloadLabel.setFont(font)
        self.fileVideosDownloadLabel.setTextFormat(QtCore.Qt.AutoText)
        self.fileVideosDownloadLabel.setScaledContents(False)
        self.fileVideosDownloadLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileVideosDownloadLabel.setWordWrap(True)
        self.fileVideosDownloadLabel.setIndent(-1)
        self.fileVideosDownloadLabel.setObjectName("fileVideosDownloadLabel")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.importFromFileTab)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(90, 220, 541, 29))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.saveURLDownloadLocationHLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.saveURLDownloadLocationHLayout.setContentsMargins(0, 0, 0, 0)
        self.saveURLDownloadLocationHLayout.setObjectName("saveURLDownloadLocationHLayout")
        self.saveURLDownloadBrowseLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.saveURLDownloadBrowseLabel.setObjectName("saveURLDownloadBrowseLabel")
        self.saveURLDownloadLocationHLayout.addWidget(self.saveURLDownloadBrowseLabel)
        self.saveURLDownloadBrowseLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.saveURLDownloadBrowseLineEdit.setToolTip("")
        self.saveURLDownloadBrowseLineEdit.setObjectName("saveURLDownloadBrowseLineEdit")
        self.saveURLDownloadLocationHLayout.addWidget(self.saveURLDownloadBrowseLineEdit)
        self.saveURLDownloadBrowsePushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.saveURLDownloadBrowsePushButton.setObjectName("saveURLDownloadBrowsePushButton")
        self.saveURLDownloadLocationHLayout.addWidget(self.saveURLDownloadBrowsePushButton)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.importFromFileTab)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(90, 150, 541, 29))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.URLFileLocationHLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.URLFileLocationHLayout.setContentsMargins(0, 0, 0, 0)
        self.URLFileLocationHLayout.setObjectName("URLFileLocationHLayout")
        self.URLFileLocationLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.URLFileLocationLabel.setObjectName("URLFileLocationLabel")
        self.URLFileLocationHLayout.addWidget(self.URLFileLocationLabel)
        self.URLFileLocationLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.URLFileLocationLineEdit.setToolTip("")
        self.URLFileLocationLineEdit.setObjectName("URLFileLocationLineEdit")
        self.URLFileLocationHLayout.addWidget(self.URLFileLocationLineEdit)
        self.URLFileBrowsePushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.URLFileBrowsePushButton.setObjectName("URLFileBrowsePushButton")
        self.URLFileLocationHLayout.addWidget(self.URLFileBrowsePushButton)
        self.formTabWidget.addTab(self.importFromFileTab, "")
        self.getURLsTab = QtWidgets.QWidget()
        self.getURLsTab.setToolTip("")
        self.getURLsTab.setStyleSheet("font: 10pt \"Microsoft YaHei\";")
        self.getURLsTab.setObjectName("getURLsTab")
        self.label = QtWidgets.QLabel(self.getURLsTab)
        self.label.setGeometry(QtCore.QRect(250, 120, 141, 111))
        self.label.setObjectName("label")
        self.formTabWidget.addTab(self.getURLsTab, "")
        self.grabMP4 = QtWidgets.QWidget()
        self.grabMP4.setStyleSheet("font: 10pt \"Microsoft YaHei\";")
        self.grabMP4.setObjectName("grabMP4")
        self.label_2 = QtWidgets.QLabel(self.grabMP4)
        self.label_2.setGeometry(QtCore.QRect(280, 130, 141, 111))
        self.label_2.setObjectName("label_2")
        self.formTabWidget.addTab(self.grabMP4, "")
        self.horizontalLayout.addWidget(self.formTabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.formTabWidget.setCurrentIndex(0)
        self.singleVideoBrowsePushButton.clicked.connect(MainWindow.browseSaveSlot)
        self.playlistBrowsePushButton.clicked.connect(MainWindow.browseSaveSlot)
        self.URLFileBrowsePushButton.clicked.connect(MainWindow.browseOpenSlot)
        self.saveURLDownloadBrowsePushButton.clicked.connect(MainWindow.browseSaveSlot)
        self.downloadSingleVideoButton.clicked.connect(MainWindow.downloadSingleVideoSlot)
        self.downloadPlaylistButton.clicked.connect(MainWindow.downloadPlaylistSlot)
        self.downloadFromFileButton.clicked.connect(MainWindow.downloadFromFileSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.singleVideoDownloadLabel.setText(_translate("MainWindow", "Instructions:\n"
"\n"
"Put the URL for the video you would like to download in the \"Video URL\" box.\n"
"\n"
"After entering the URL choose the save location and click the\"Download Video\" button."))
        self.videoURLLabel.setText(_translate("MainWindow", "Video URL:"))
        self.singleVideoSaveLocationLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.singleVideoSaveLocationLabel.setText(_translate("MainWindow", "Save Location:"))
        self.singleVideoBrowsePushButton.setText(_translate("MainWindow", "Browse"))
        self.saveDefaultVideoLocationLabel.setText(_translate("MainWindow", "**By default the video will save in the downloads folder within the Video Downloader folder**"))
        self.downloadSingleVideoButton.setText(_translate("MainWindow", "Download Video"))
        self.formTabWidget.setTabText(self.formTabWidget.indexOf(self.downloadSingleVideoTab), _translate("MainWindow", "Single Video"))
        self.formTabWidget.setTabToolTip(self.formTabWidget.indexOf(self.downloadSingleVideoTab), _translate("MainWindow", "Download a single video by inputting a URL"))
        self.playlistDownloadLabel.setText(_translate("MainWindow", "Instructions:\n"
"\n"
"Put the URL for the playlist you would like to download in the \"Video URL\" box.\n"
"\n"
"After entering the URL choose the save location and click the\"Download Playlist\" button."))
        self.playlistSaveLocationLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.playlistSaveLocationLabel.setText(_translate("MainWindow", "Save Location:"))
        self.playlistBrowsePushButton.setText(_translate("MainWindow", "Browse"))
        self.saveDefaultPlaylistLocationLabel.setText(_translate("MainWindow", "**By default the videos will save in the downloads folder within the Video Downloader folder**"))
        self.downloadPlaylistButton.setText(_translate("MainWindow", "Download Playlist"))
        self.playlistURLLabel.setText(_translate("MainWindow", "Video URL:"))
        self.formTabWidget.setTabText(self.formTabWidget.indexOf(self.importPlaylistTab), _translate("MainWindow", "Playlist"))
        self.formTabWidget.setTabToolTip(self.formTabWidget.indexOf(self.importPlaylistTab), _translate("MainWindow", "Download a playlist by inputting the URL"))
        self.downloadFromFileButton.setText(_translate("MainWindow", "Download Videos"))
        self.saveDefaultPlaylistLocationLabel_2.setText(_translate("MainWindow", "**By default the videos will save in the downloads folder within the Video Downloader folder**"))
        self.fileVideosDownloadLabel.setText(_translate("MainWindow", "Instructions:\n"
"\n"
"Navigate to the .TXT file storing all the URLs. Each URL needs to be on a separate line.\n"
"\n"
"After entering the URL file location choose the save location and click the\"Download Videos\" button."))
        self.saveURLDownloadBrowseLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.saveURLDownloadBrowseLabel.setText(_translate("MainWindow", "Save Location:"))
        self.saveURLDownloadBrowsePushButton.setText(_translate("MainWindow", "Browse"))
        self.URLFileLocationLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.URLFileLocationLabel.setText(_translate("MainWindow", "File Location:"))
        self.URLFileBrowsePushButton.setText(_translate("MainWindow", "Browse"))
        self.formTabWidget.setTabText(self.formTabWidget.indexOf(self.importFromFileTab), _translate("MainWindow", "From URL File"))
        self.formTabWidget.setTabToolTip(self.formTabWidget.indexOf(self.importFromFileTab), _translate("MainWindow", "Select a text file to download all the videos from the URL\'s in the file"))
        self.label.setText(_translate("MainWindow", "Under Development"))
        self.formTabWidget.setTabText(self.formTabWidget.indexOf(self.getURLsTab), _translate("MainWindow", "Get URLs"))
        self.formTabWidget.setTabToolTip(self.formTabWidget.indexOf(self.getURLsTab), _translate("MainWindow", "Get URLs from a webpage by entering in the HTML tag the URLs you want to grab are in"))
        self.label_2.setText(_translate("MainWindow", "Under Development"))
        self.formTabWidget.setTabText(self.formTabWidget.indexOf(self.grabMP4), _translate("MainWindow", "Grab MP4"))
        self.formTabWidget.setTabToolTip(self.formTabWidget.indexOf(self.grabMP4), _translate("MainWindow", "Grab MP4 files in a webpage\'s HTML"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
