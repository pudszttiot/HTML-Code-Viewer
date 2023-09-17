import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QFrame, QVBoxLayout, QWidget, QSplitter
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPalette, QColor

class HTMLViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Live HTML Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a splitter to separate the HTML input and the WebView
        splitter = QSplitter(Qt.Vertical)

        # Create a QTextEdit widget for HTML input
        self.html_text = QTextEdit()
        self.html_text.setStyleSheet("background-color: #282c34; color: white;")
        splitter.addWidget(self.html_text)

        # Create a WebView to display the HTML content
        self.webview = QWebEngineView()
        splitter.addWidget(self.webview)

        # Add the splitter to the layout
        layout.addWidget(splitter)

        # Create an "Open HTML" button
        open_button = QPushButton("Open HTML")
        open_button.clicked.connect(self.open_html)
        layout.addWidget(open_button)

        # Apply a dark color scheme to the application
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(32, 35, 42))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(32, 35, 42))
        dark_palette.setColor(QPalette.AlternateBase, QColor(44, 48, 58))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(64, 69, 82))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(dark_palette)

    def open_html(self):
        html_content = self.html_text.toPlainText()
        self.webview.setHtml(html_content)

def main():
    app = QApplication(sys.argv)
    window = HTMLViewer()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
