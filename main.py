import sys
from PyQt5.QtWidgets import QApplication
from src.layout.layout import FiltroUI
import src.controllers.logica as logica

app = QApplication(sys.argv)
window = FiltroUI()

# Conectar botones con funciones de logic.py
window.btn_elegir_archivo.clicked.connect(window.elegir_archivo)
window.btn_agregar_filtro.clicked.connect(lambda: logica.habilitar_inputs(window))
window.btn_guardar.clicked.connect(lambda: logica.guardar_filtro(window))
window.btn_ejecutar.clicked.connect(lambda: logica.ejecutar_filtros(window))

window.show()
sys.exit(app.exec())
