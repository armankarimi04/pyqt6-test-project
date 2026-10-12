from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow


# need for access to command line arguments
import sys


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)


# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.


# Start the event loop. (i moved it to if name is main block)
# app.exec()



if __name__ == "__main__":
    app.exec()


# Your application won't reach here until you exit and the event loop has stopped.
print("END OF SCRIPT")