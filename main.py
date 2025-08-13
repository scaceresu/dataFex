import sys
from PyQt5.QtWidgets import QApplication
from src.layout.layout import FiltroUI
import src.controllers.logica as logic

app = QApplication(sys.argv)
window = FiltroUI()

# Conectar botones con funciones de logic.py
window.btn_agregar_filtro.clicked.connect(lambda: logic.habilitar_inputs(window))
window.btn_guardar.clicked.connect(lambda: logic.guardar_filtro(window))
window.btn_ejecutar.clicked.connect(lambda: logic.ejecutar_filtros(window))

window.show()
sys.exit(app.exec())



# path = "./static/data/REG02_EPHC_ANUAL_2023.xls"


# encuesta_2023 = pd.read_excel(path, engine="xlrd")

# encuesta = pd.read_excel(path)

# ages = encuesta_2023["P08A"]


# print(ages.head(4))