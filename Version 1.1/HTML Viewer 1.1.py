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

        # Set a custom HTML code as a placeholder
        placeholder_html = "Enter your HTML code here...."
        self.html_text.setPlaceholderText(placeholder_html)

        # Create a WebView to display the HTML content
        self.webview = QWebEngineView()
        splitter.addWidget(self.webview)

        # Set the initial size of the splitter (adjust this value as needed)
        splitter.setSizes([400, 400])

        # Add the splitter to the layout
        layout.addWidget(splitter)

        # Create an "Open HTML" button with custom styling
        open_button = QPushButton("Run HTML")
        open_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")
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
        dark_palette.setColor(QPalette.ButtonText, Qt.black)
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
    # Set custom text in the QTextEdit widget
    custom_text = """<!DOCTYPE html>
<html>
<body>
<h1 style="background-color: red;">Hello World!</h1>
<p>This is a paragraph.</p>
<b><marquee width="100%" behavior="alternate">TTIOT - TTIOT - TTIOT</marquee></b>
</body>
</html>"""
    window.html_text.setPlainText(custom_text)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
