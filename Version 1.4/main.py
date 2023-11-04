import sys
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QSplitter,
    QFileDialog,
    QAction,
    QMenuBar,
    QDialog,  # Add QDialog import
    QLabel,   # Add QLabel import
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPalette, QColor, QIcon, QTextCharFormat, QSyntaxHighlighter, QFont

# ENTER PYTHON CODE BELOW

class HTMLSyntaxHighlighter(QSyntaxHighlighter):
    """
    Syntax highlighter for HTML code.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []

        self.keyword_formats = {
            "<!DOCTYPE html>": QColor(248, 200, 100),  # Color for existing keywords
            "<body>": QColor(117, 253, 30), "</body>": QColor(117, 253, 30),
            "<html>": QColor(40, 182, 44), "</html>": QColor(117, 253, 30),
            "<h1": QColor(117, 253, 30), "</h1>": QColor(117, 253, 30),
            "<p>": QColor(117, 253, 30), "</p>": QColor(117, 253, 30),
            "<b>": QColor(117, 253, 30), "</b>": QColor(117, 253, 30),
            "<marquee": QColor(117, 253, 30), "</marquee>": QColor(117, 253, 30),
        }

        self.create_highlighting_rules()

    def create_highlighting_rules(self):
        for keyword, color in self.keyword_formats.items():
            keyword_format = QTextCharFormat()
            keyword_format.setForeground(color)
            self.highlighting_rules.append((QRegExp(keyword), keyword_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

class HTMLViewer(QMainWindow):
    """
    HTML code viewer and editor.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("HTML Code Viewer")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(r"..\Images\WindowLogo.ico"))

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
        placeholder_html = """<!DOCTYPE html>
<html>
<body>
<h1 style="background-color: red;">Hello World!</h1>
<p>This is a paragraph.</p>
<b><marquee width="100%" behavior="alternate">TTIOT - TTIOT - TTIOT</marquee></b>
</body>
</html>"""
        self.html_text.setPlaceholderText("Enter HTML Code Here...")

        self.html_text.setPlainText(placeholder_html)

        # Create a WebView to display the HTML content
        self.webview = QWebEngineView()
        splitter.addWidget(self.webview)

        # Set the initial size of the splitter (adjust this value as needed)
        splitter.setSizes([400, 400])

        # Add the splitter to the layout
        layout.addWidget(splitter)

        # Create a "Run HTML" button with an icon and tooltip
        run_button = QPushButton(QIcon(r"..\Images\run.png"), "Run Code")
        run_button.setToolTip("Load and display the HTML code")
        run_button.clicked.connect(self.open_html)
        layout.addWidget(run_button)

        # Create a "Save Code" button with an icon and tooltip
        save_button = QPushButton(QIcon(r"..\Images\save.png"), "Save Code")
        save_button.setToolTip("Save the HTML code to a file")
        save_button.clicked.connect(self.save_code)
        layout.addWidget(save_button)

        # Create a "Load HTML" button with an icon and tooltip
        load_button = QPushButton(QIcon(r"..\Images\open.png"), "Load HTML")
        load_button.setToolTip("Open and display an HTML file")
        load_button.clicked.connect(self.load_html_file)
        layout.addWidget(load_button)

        # Create an instance of the HTMLSyntaxHighlighter
        self.html_highlighter = HTMLSyntaxHighlighter(self.html_text.document())

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

        # Create a menu bar
        menubar = self.menuBar()

        # Create a "File" menu
        file_menu = menubar.addMenu("File")

        # Create an "Exit" action in the "File" menu
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create a "Help" menu
        help_menu = menubar.addMenu("Help")

        # Create a "How to Use" action in the "Help" menu
        how_to_use_action = QAction("How to Use", self)
        how_to_use_action.triggered.connect(self.show_how_to_use)
        help_menu.addAction(how_to_use_action)

    def show_how_to_use(self):
        # Create a dialog for "How to Use" instructions
        how_to_use_dialog = QDialog(self)
        how_to_use_dialog.setWindowTitle("Help")
        
        # Move the dialog to a new position (adjust the values as needed)
        how_to_use_dialog.move(200, 20)
        
        # Set the size of the dialog (adjust the values as needed)
        how_to_use_dialog.setFixedSize(770, 670)

        # Create a QVBoxLayout for the dialog
        layout = QVBoxLayout(how_to_use_dialog)

        # Create a QLabel for the instructions
        instructions_label = QLabel()
        instructions_label.setText(
            """
            <p style="text-align: center;"><h2><span style="color: #00FF00;">===================================</span></h2>
        <h1><span style="color: #F5F5F5;">🛠 HTML Code Viewer 🛠</span></h1>
        <h2><span style="color: #FFFFFF;">📝 Version: 1.4</span></h2>
        <h2><span style="color: #FFFFFF;">📅 Release Date: October 22, 2023</span></h2>
        <h2><span style="color: #00FF00;">===================================</span></h2>
        
        <p style="text-align: center;">
        <span style="color: #282c34; background-color: yellow;">The
        <strong><span style="color: #000000; background-color: yellow;">HTML Code Viewer</span></strong>
        <span style="color: #282c34; background-color: yellow;"> includes syntax highlighting for working with HTML content.<br>The user can input, edit and view the rendered result live.</span></p>


        <p><h3><span style="color: #FF0080;">Here's how to use it:</span></h3></p>
        <ol>
        
            <li>To open and view a HTML file, click <strong><span style="color: #FF6600;">"Load HTML"</span></strong> in the toolbar. This will allow you to select an HTML file for editing.</li>
            <li>To create or edit a HTML code, type or paste your HTML content into the text editor provided.</li>
            <li>Once you've made changes to the HTML code, click the <strong><span style="color: #FF6600;">"Run Code"</span></strong> button to render and display the result.</li>
            <li>To save your HTML code to a file, click <strong><span style="color: #FF6600;">"Save Code"</span></strong> in the toolbar. You can choose the location and file name <br>for saving your code.</li>

        </ol>

        <p><strong>That's it!</strong>...Thank you for using <strong><span style="color: #FFD700;">HTML Code Viewer!</span></strong></p>

    
        <!-- Add an image here -->
        <p style="text-align: center;"><img src="..\Images\WindowLogo.png" alt="WindowLogo.png" width="100" height="100" border="1"></p>

        <p style="text-align: center;"><h3>▲▲▲👽👽 MY CHANNELS 👽👽▲▲▲</h3></p>
        <p style="text-align: center;">
        <div style="display: inline-block;">
            <img src="..\Images\Github.png" alt="Github.png" width="20" height="20" border="1">
            <span style="color: #1E90FF;"><a href="https://github.com/pudszttiot" style="color: #1E90FF;">Github Page</a></span>
        </div>
        </p>

        <p style="text-align: center;">
            <div style="display: inline-block;">
                <img src="..\Images\Youtube.png" alt="Youtube.png" width="20" height="20" border="5">
                <a href="https://youtube.com/channel/UCwtvRlFsh1-CI1h0g32AlwQ" style="color: #FF0000;">YouTube Page</a>
        </div>
        </p>

        
        """
        )

        # Customize the appearance of the QLabel
        font = QFont()
        font.setPointSize(10)  # Set the font size
        instructions_label.setFont(font)
        instructions_label.setStyleSheet(
            "color: #1E90FF; background-color: #000000; padding: 10px;"
            "border: 2px solid #1E90FF; border-radius: 10px;"
        )  # Customize colors, padding, and border
        instructions_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # Align text

        # Add the QLabel to the layout
        layout.addWidget(instructions_label)

        # Show the dialog
        how_to_use_dialog.exec_()

    def open_html(self):
        html_content = self.html_text.toPlainText()
        self.webview.setHtml(html_content)

    def save_code(self):
        html_content = self.html_text.toPlainText()
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save HTML Code", "", "HTML Files (*.html);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "w") as file:
                file.write(html_content)

    def load_html_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open HTML File", "", "HTML Files (*.html);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "r") as file:
                html_content = file.read()
                self.html_text.setPlainText(html_content)

# ENTER PYTHON CODE ABOVE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HTMLViewer()
    window.show()
    sys.exit(app.exec_())
