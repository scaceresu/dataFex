# generarTabla.py
import sys
from PyQt5.QtWidgets import QApplication
from layout import FiltroUI
import src.controllers.logica as logica

class MainApp(FiltroUI):
    def __init__(self):
        super().__init__()

        # Conectar botones
        self.btn_agregar_filtro.clicked.connect(lambda: logica.habilitar_inputs(self))
        self.btn_guardar.clicked.connect(lambda: logica.guardar_filtro(self))
        self.btn_ejecutar.clicked.connect(lambda: logica.ejecutar_filtros(self))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainApp()
    ventana.show()
    sys.exit(app.exec_())
