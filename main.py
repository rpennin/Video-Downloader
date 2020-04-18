
from PyQt5 import QtWidgets, QtGui, QtCore
from gui import Ui_MainWindow
from warning import Ui_WarningDialogue
import sys
import os

class warningDialogue(QtWidgets.QDialog, Ui_WarningDialogue):
    def __init__(self, parent=None):
        super(warningDialogue, self).__init__(parent)
        self.setupUi(self)

class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)

    def browseSaveSlot(self):
        tab = self.formTabWidget.currentIndex()
        directoryLocation = QtWidgets.QFileDialog.getExistingDirectory(self,"Choose Save Location","./", options=QtWidgets.QFileDialog.ShowDirsOnly)
        if directoryLocation:
            if tab == 0:
                self.singleVideoSaveLocationLineEdit.setText(directoryLocation)
            elif tab == 1:
                self.playlistSaveLocationLineEdit.setText(directoryLocation)
            elif tab == 2:
                self.saveURLDownloadBrowseLineEdit.setText(directoryLocation)
            else:
                pass
        else:
            pass
            
    def browseOpenSlot(self):
        options = QtWidgets.QFileDialog.Options()
        urlFile, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Select the URL File","./", "*.txt", options=options)
        if urlFile:
            self.URLFileLocationLineEdit.setText(urlFile)
        else:
            pass

    def downloadSingleVideoSlot(self):
        url = self.singleVideoURLLineEdit.text()

        if (url == ""):
            aDlg = warningDialogue()
            aDlg.warningLabel.setText("A URL is required")
            aDlg.exec_()
        else:
            saveLocation = self.singleVideoSaveLocationLineEdit.text()

            if (saveLocation == ""):
                saveLocation = "./downloads"

            command = 'youtube-dl -o ' + saveLocation + r'/%(title)s.%(ext)s --geo-bypass --no-mtime ' + url

            os.system(f'cmd /c {command}')

    def downloadPlaylistSlot(self):
        url = self.playlistURLLineEdit.text()

        if (url == ""):
            aDlg = warningDialogue()
            aDlg.warningLabel.setText("A URL is required")
            aDlg.exec_()
        else:
            saveLocation = self.playlistSaveLocationLineEdit.text()

            if (saveLocation == ""):
                saveLocation = "./downloads"

            command = 'youtube-dl -o ' + saveLocation + r'/%(title)s.%(ext)s --yes-playlist -i --geo-bypass --no-mtime ' + url

            os.system(f'cmd /c {command}')

    def downloadFromFileSlot(self):
        urlFile = self.URLFileLocationLineEdit.text()

        if (urlFile == ""):
            aDlg = warningDialogue()
            aDlg.warningLabel.setText("A file location is required")
            aDlg.exec_()
        else:
            saveLocation = self.saveURLDownloadBrowseLineEdit.text()

            if (saveLocation == ""):
                saveLocation = "./downloads"

            command = 'youtube-dl -o ' + saveLocation + r'/%(title)s.%(ext)s -i --geo-bypass --no-mtime --batch-file ' + urlFile

            os.system(f'cmd /c {command}')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    aDlgui = mainProgram()
    aDlgui.show()
    sys.exit(app.exec_())