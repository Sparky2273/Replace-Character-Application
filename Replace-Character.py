import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QFileDialog,
    QLineEdit,
    QVBoxLayout,
    QMenuBar,
    QMenu,
    QAction,
    QMessageBox,
    QGroupBox,
    QMainWindow,
    QTextEdit,
    QDialog,
)


class ReplaceCharacter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.path = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Replace Character")
        self.setWindowIcon(QIcon("rc.ico"))
        self.setGeometry(250, 250, 300, 600)
        self.setFixedSize(300, 600)
        self.setWindowFlags(
            self.windowFlags()
            & ~(
                Qt.WindowMinimizeButtonHint
                | Qt.WindowMaximizeButtonHint
                | Qt.WindowCloseButtonHint
            )
        )

        self.menubar = QMenuBar()
        self.help_menu = QMenu("Help", self)
        self.menubar.addMenu(self.help_menu)

        self.about_action = QAction("About", self)
        self.about_action.triggered.connect(self.about)
        self.help_menu.addAction(self.about_action)

        self.manual_action = QAction("Manual", self)
        self.manual_action.triggered.connect(self.manual)
        self.help_menu.addAction(self.manual_action)

        self.select_file_button = QPushButton("Select File")
        self.select_file_button.clicked.connect(self.select_file)

        self.select_dir_button = QPushButton("Select Directory")
        self.select_dir_button.clicked.connect(self.select_directory)

        self.path_label = QLabel("")
        self.path_label.setWordWrap(True)

        self.old_char_label = QLabel("Enter character to replace:")
        self.old_char_input = QLineEdit()
        self.old_char_input.setMaxLength(1)

        self.new_char_label = QLabel("Enter new character:")
        self.new_char_input = QLineEdit()
        self.new_char_input.setMaxLength(1)

        self.remove_word_label = QLabel("Enter word to remove:")
        self.remove_word_input = QLineEdit()

        self.replace_button = QPushButton("Replace")
        self.replace_button.clicked.connect(self.replace_character)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear)

        self.close_button = QPushButton("Exit")
        self.close_button.clicked.connect(self.close)

        file_group_box = QGroupBox("File")
        file_layout = QVBoxLayout(file_group_box)
        file_layout.addWidget(self.select_file_button)
        file_layout.addWidget(self.select_dir_button)
        file_layout.addWidget(self.path_label)

        replace_group_box = QGroupBox("Replace Character")
        replace_layout = QVBoxLayout(replace_group_box)
        replace_layout.addWidget(self.old_char_label)
        replace_layout.addWidget(self.old_char_input)
        replace_layout.addWidget(self.new_char_label)
        replace_layout.addWidget(self.new_char_input)

        remove_group_box = QGroupBox("Remove Word")
        remove_layout = QVBoxLayout(remove_group_box)
        remove_layout.addWidget(self.remove_word_label)
        remove_layout.addWidget(self.remove_word_input)

        button_group_box = QGroupBox("Actions")
        button_layout = QVBoxLayout(button_group_box)
        button_layout.addWidget(self.replace_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.close_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.menubar)
        main_layout.addWidget(file_group_box)
        main_layout.addWidget(replace_group_box)
        main_layout.addWidget(remove_group_box)
        main_layout.addWidget(button_group_box)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        font = QFont()
        font.setPointSize(9)

        self.path_label.setFont(font)
        self.old_char_label.setFont(font)
        self.old_char_input.setFont(font)
        self.new_char_label.setFont(font)
        self.new_char_input.setFont(font)
        self.remove_word_label.setFont(font)
        self.remove_word_input.setFont(font)

        self.select_file_button.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        )
        self.select_dir_button.setStyleSheet(
            """
            QPushButton {
                background-color: #f44336;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """
        )
        self.replace_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """
        )
        self.clear_button.setStyleSheet(
            """
            QPushButton {
                background-color: #9E9E9E;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #757575;
            }
        """
        )
        self.close_button.setStyleSheet(
            """
            QPushButton {
                background-color: #F44336;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #D32F2F;
            }
        """
        )

    def about(self):
        about_text = f"Version: 1.0\nDeveloper: Sparky\nContact: Sparky#2273 on Discord or @Sparky2273 on Telegram"
        QMessageBox.information(self, "About", about_text)

    def manual(self):
        self.manual_window = ManualWindow()
        self.manual_window.show()

    def clear(self):
        self.old_char_input.setText("")
        self.new_char_input.setText("")
        self.remove_word_input.setText("")

    def select_file(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Select File")
        self.path_label.setText(f"File Path:\n{filepath}")
        self.path = filepath

    def select_directory(self):
        dirpath = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.path_label.setText(f"Directory Path:\n{dirpath}")
        self.path = dirpath

    def replace_character(self):
        path = self.path
        old_char = self.old_char_input.text()
        new_char = self.new_char_input.text()
        remove_word = self.remove_word_input.text()

        if not os.path.exists(path):
            self.path_label.setText("Invalid path!")
        elif not old_char:
            self.old_char_label.setText("Enter character to replace!")
        elif not new_char:
            self.new_char_label.setText("Enter new character!")
        else:
            if os.path.isfile(path):
                filename, ext = os.path.splitext(os.path.basename(path))
                new_filename = filename.replace(old_char, new_char)

                if remove_word:
                    new_filename = new_filename.replace(remove_word, "")

                if new_filename[-1] == " ":
                    new_filename = new_filename[:-1]

                new_filename += ext
                new_path = os.path.join(os.path.dirname(path), new_filename)

                os.rename(path, new_path)

                self.path_label.setText(f"New File Name:\n{new_filename}")

            elif os.path.isdir(path):
                for filename in os.listdir(path):
                    filepath = os.path.join(path, filename)

                    if os.path.isfile(filepath):
                        filebasename, fileext = os.path.splitext(filename)
                        new_filebasename = filebasename.replace(old_char, new_char)

                        if remove_word:
                            new_filebasename = new_filebasename.replace(remove_word, "")

                        if new_filebasename[-1] == " ":
                            new_filebasename = new_filebasename[:-1]

                        new_filename = new_filebasename + fileext
                        new_filepath = os.path.join(path, new_filename)

                        os.rename(filepath, new_filepath)

                        self.path_label.setText(f"New Directory Path:\n{path}")


class ManualWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Replace Character Application Manual")
        self.setGeometry(150, 150, 1315, 715)
        self.setFixedSize(1315, 715)
        self.setWindowFlags(
            self.windowFlags()
            & ~(Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        )

        manual_text = """
        ## Replace Character Application Manual

        The Replace Character application allows you to replace characters in file names or remove specific words from file names. It provides a simple graphical user interface (GUI) built using the PyQt5 library.

        ### Prerequisites

        Before using the Replace Character application, make sure you have the following:

        - The executable file for the application (e.g., `replace_character.exe`).
        - Your operating system should be compatible with the executable file.

        ### Running the Application

        To run the Replace Character application, follow these steps:

        1. Locate the executable file (`replace_character.exe`) on your computer.
        2. Double-click the executable file to launch the application.

        ### Using the Application

        Once the Replace Character application is running, you can use the GUI to perform the desired actions. The following sections describe each element in the application interface and how to use them.

        #### File Section

        - **Select File Button:** Click this button to choose a specific file. Once selected, the file path will be displayed below the button.
        - **Select Directory Button:** Click this button to choose a directory. Once selected, the directory path will be displayed below the button.

        #### Replace Character Section

        - **Enter character to replace:** Enter the character that you want to replace in the file names.
        - **Enter new character:** Enter the character that will replace the old character in the file names.

        #### Remove Word Section

        - **Enter word to remove:** Enter a specific word that you want to remove from the file names.

        #### Actions Section

        - **Replace Button:** Click this button to initiate the character replacement or word removal process. The application will update the file names accordingly.
        - **Clear Button:** Click this button to clear the input fields.
        - **Exit Button:** Click this button to exit the application.

        #### Help Menu

        - **About:** Click the **Help** menu and select **About** to view information about the application, including the version, developer, and contact details.
        - **Manual:** Click the **Help** menu and select **Manual** to open a separate window displaying the application manual.

        ### Notes

        - The application limits the character input fields to one character only to ensure accurate replacements.
        - The application prevents minimizing, maximizing, and closing the main window to maintain focus and prevent accidental closure.

        ### Contact Information

        If you have any questions or need further assistance with the Replace Character application, you can contact the developer:

        - Developer: Sparky
        - Contact: Sparky#2273 on Discord or @Sparky2273 on Telegram
        """

        text_edit = QTextEdit(self)
        text_edit.setPlainText(manual_text)
        text_edit.setReadOnly(True)

        font = QFont("Helvetica", 10)
        text_edit.setFont(font)

        manual_groupbox = QGroupBox("Manual")
        manual_layout = QVBoxLayout()
        manual_layout.addWidget(text_edit)
        manual_groupbox.setLayout(manual_layout)

        layout = QVBoxLayout()
        layout.addWidget(manual_groupbox)
        self.setLayout(layout)


def main():
    app = QApplication([])
    widget = ReplaceCharacter()
    widget.show()
    app.exec_()


if __name__ == "__main__":
    main()
