# homepage.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from main import HTMLViewer

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HTML Code Viewer")
        self.setFixedSize(800, 600)  # Increased window size
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(r"..\Images\WindowLogo.ico"))

        # Set background color for the main window
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #7030A0; /* Set your desired background color here */
            }
            """
        )

        # Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(100, 40, 610, 470)  # Adjust the position and size as needed
        pixmap = QPixmap(r"..\Images\HTMLCodeViewerLogo.png")  # Provide the path to your image file
        self.image_label.setPixmap(pixmap)

        # Create a button to open the content page
        self.open_button = QPushButton("Open HTML Code Viewer", self)
        self.open_button.setGeometry(300, 525, 200, 50)
        self.open_button.clicked.connect(self.open_content_page)

        # Apply custom style to the button (same as before)
        self.open_button.setStyleSheet(
            """
            QPushButton {
                background-color: #000000;
                color: white;
                border: 1px solid #00ffff;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #00ffff;
                color: #000000;
                border: 1px solid #000000;
            }
            """
        )

    def open_content_page(self):
        # Open the content page frame (imported from your existing code)
        self.content_page = HTMLViewer()
        self.content_page.show()

        # Close the home page
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    homepage = HomePage()
    homepage.show()
    sys.exit(app.exec_())
