import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Gastos Trimestrales")
        self.layout = QVBoxLayout()

        trimestres = ["1er trimestre", "2do trimestre", "3er trimestre"]
        gastos = [
            ["Agua Q120", "Luz Q85", "Gas Q180"],
            ["Agua Q420", "Luz Q105", "Gas Q225"],
            ["Agua Q360", "Luz Q90", "Gas Q160"],
        ]

        for i in range(3):
            fig, ax = plt.subplots()
            gastos_labels = ["Agua", "Luz", "Gas"]
            gastos_valores = [int(g.split(" ")[-1][1:]) for g in gastos[i]]
            ax.bar(gastos_labels, gastos_valores)
            ax.set_title(trimestres[i])
            ax.set_xlabel("Concepto")
            ax.set_ylabel("Gasto")
            ax.spines["right"].set_visible(False)
            ax.spines["top"].set_visible(False)

            # Agregar el gráfico a un widget de matplotlib
            canvas = FigureCanvasQTAgg(fig)
            canvas.draw()

            # Agregar el widget de matplotlib al layout de la ventana
            self.layout.addWidget(canvas)

        # Crear un widget contenedor y establecer el layout
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
