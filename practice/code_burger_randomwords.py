from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout

from random import choice

#Main App Objects and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Recipe Book")
main_window.resize(300,200)

#Create All Object/Widgets below here
title =  QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")

my_words = ["player", "button", "curse", "palindrome", "jerma", "work", "irritation"]

#All Design Here
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

#Add Objects
row1.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignmentFlag.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignmentFlag.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignmentFlag.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

#Add Functions
def random_word1():
    word = choice(my_words)
    text1.setText(word)
    
def random_word2():
    word = choice(my_words)
    text2.setText(word)
    
def random_word3():
    word = choice(my_words)
    text3.setText(word)

#Events
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)

#Show/Run
main_window.show()
app.exec()