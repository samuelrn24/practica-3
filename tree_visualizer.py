from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsScene
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class TreeVisualizer:
    def __init__(self, graphics_view):
        self.scene = QGraphicsScene()
        graphics_view.setScene(self.scene)
        self.graphics_view = graphics_view

    def clear(self):
        self.scene.clear()

    def draw_tree(self, turns):
        self.clear()
        node_radius = 30
        x_spacing = 120
        y_spacing = 120

        root_x = 400
        root_y = 50
        self.add_node(root_x, root_y, "Partida", color=QColor("gray"))

        if turns:
            self._draw_branch(root_x, root_y, turns, 0, x_spacing, y_spacing)

    def _draw_branch(self, parent_x, parent_y, turns, level, x_spacing, y_spacing):
        if level >= len(turns):
            return

        turn_number, white_move, black_move = turns[level]

        white_x = parent_x - x_spacing
        black_x = parent_x + x_spacing
        child_y = parent_y + y_spacing

        # Blancas: Nodo blanco
        self.add_node(white_x, child_y, white_move, color=QColor("white"))
        self.scene.addLine(parent_x, parent_y + 30, white_x, child_y - 30)

        # Negras: Nodo negro
        self.add_node(black_x, child_y, black_move, color=QColor("black"), text_color=QColor("white"))
        self.scene.addLine(parent_x, parent_y + 30, black_x, child_y - 30)

        # Solo las blancas continúan expandiéndose
        self._draw_branch(white_x, child_y, turns, level + 1, x_spacing, y_spacing)

    def add_node(self, x, y, text, color=QColor("lightgray"), text_color=QColor("black")):
        ellipse = QGraphicsEllipseItem(x - 30, y - 30, 60, 60)
        ellipse.setBrush(color)
        self.scene.addItem(ellipse)

        label = QGraphicsTextItem(text)
        label.setDefaultTextColor(text_color)
        label.setPos(x - 20, y - 10)
        self.scene.addItem(label)

