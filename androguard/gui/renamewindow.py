from PyQt5 import QtWidgets


class RenameDialog(QtWidgets.QDialog):
    """
        parent: SourceWindow that started the new XrefDialog
    """

    def __init__(self, parent=None, win=None, element="", info=()):
        super().__init__(parent)

        self.sourceWin = parent
        self.info = info
        self.element = element
        title = "Rename: " + element
        self.setWindowTitle(title)

        layout = QtWidgets.QGridLayout()
        question = QtWidgets.QLabel("Please enter new name:")
        layout.addWidget(question, 0, 0)
        self.lineEdit = QtWidgets.QLineEdit()
        layout.addWidget(self.lineEdit, 0, 1)
        self.buttonOK = QtWidgets.QPushButton("OK", self)
        layout.addWidget(self.buttonOK, 1, 1)
        self.buttonCancel = QtWidgets.QPushButton("Cancel", self)
        layout.addWidget(self.buttonCancel, 1, 0)

        self.lineEdit.setText(self.element)

        self.setLayout(layout)

        self.buttonCancel.clicked.connect(self.cancelClicked)
        self.buttonOK.clicked.connect(self.okClicked)

    def cancelClicked(self):
        self.close()

    def okClicked(self):
        self.sourceWin.renameElement(self.element, self.lineEdit.text(),
                                     self.info)
        self.close()
