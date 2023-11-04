import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5.QtCore import QSize, Qt
from main import HTMLViewer

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HTML Code Viewer")
        self.setFixedSize(800, 600)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(r"..\Images\WindowLogo.ico"))

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #000000;
            }
            """
        )

        # Create a central widget to hold the content
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QLabel widget to display an animated GIF
        image_label = QLabel(self)
        image_label.setGeometry(0, 0, 480, 55)  # Adjust the position and size as needed

        movie = QMovie(r"..\Images\HTMLCodeViewerFlashing.gif")
        movie.setScaledSize(QSize(480, 55))  # Adjust these dimensions to match the QLabel

        image_label.setMovie(movie)

        center_x = (self.width() - image_label.width()) // 2
        center_y = 30  # Place the GIF at the top

        image_label.move(center_x, center_y)

        movie.start()

        # Create a QLabel widget to display the top image
        self.image_label = QLabel(self)
        pixmap = QPixmap(r"..\Images\WindowLogo.png")
        self.image_label.setPixmap(pixmap)

        # Create a horizontal layout to hold the image label
        image_layout = QHBoxLayout()
        image_layout.addWidget(self.image_label)
        layout.addLayout(image_layout)

        # Adjust the horizontal alignment of the image within the layout
        image_layout.setAlignment(Qt.AlignHCenter)  # You may need to import Qt

        # Adjust the margin to control the horizontal position
        image_layout.setContentsMargins(100, 0, 100, 50)  # This will move the image to the left

        # Create a button to open the content page
        self.open_button = QPushButton("Open HTML Code Viewer", self)
        self.open_button.setGeometry(295, 460, 210, 50)
        self.open_button.clicked.connect(self.open_content_page)

        self.open_button.setStyleSheet(
            """
            QPushButton {
                background-color: #333333;
                color: #F5F5F5;
                border: 1px solid #00ffff;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #00ffff;
                color: #333333;
                border: 1px solid #F5F5F5;
                border-radius: 5px;
            }
            """
        )

    def open_content_page(self):
        self.content_page = HTMLViewer()
        self.content_page.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    homepage = HomePage()
    homepage.show()
    sys.exit(app.exec_())
