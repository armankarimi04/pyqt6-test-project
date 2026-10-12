from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

if __name__ == "__main__":
    app.exec()

print("end of script.")