import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QGraphicsView
)
from parser import Parser
from tree_visualizer import TreeVisualizer

class ChessApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess Game Parser")
        self.resize(1200, 700)

        # Widgets de entrada
        self.text_area = QTextEdit()
        self.text_area.setFixedWidth(300)  # Reducir ancho del área de texto
        self.validate_btn = QPushButton("Validar")
        self.result_label = QLabel("")

        # Visualización del árbol
        self.graphics_view = QGraphicsView()
        self.tree_visualizer = TreeVisualizer(self.graphics_view)

        # Conectar botón
        self.validate_btn.clicked.connect(self.validate_input)

        # Layout de entrada (columna izquierda)
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.text_area)
        input_layout.addWidget(self.validate_btn)
        input_layout.addWidget(self.result_label)

        input_container = QWidget()
        input_container.setLayout(input_layout)

        # Layout general (izquierda: entradas, derecha: árbol)
        main_layout = QHBoxLayout()
        main_layout.addWidget(input_container)
        main_layout.addWidget(self.graphics_view, stretch=1)  # El área del árbol ocupa más espacio

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def validate_input(self):
        text = self.text_area.toPlainText()
        parser = Parser(text)
        is_valid, message, turns = parser.validate()
        self.result_label.setText(message)

        if is_valid:
            self.tree_visualizer.draw_tree(turns)
        else:
            self.tree_visualizer.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChessApp()
    window.show()
    sys.exit(app.exec_())

