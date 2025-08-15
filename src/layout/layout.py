from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLineEdit,
    QComboBox, QTableWidget, QVBoxLayout,
    QHBoxLayout, QFileDialog, QLabel,QTableWidgetItem
)

class FiltroUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generando una nueva Tabla")
        self.resize(700, 400)
        self.ruta_archivo = None  # Aquí se guarda la ruta elegida
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # --- Selección de archivo ---
        self.file_layout = QHBoxLayout()
        self.btn_elegir_archivo = QPushButton("Elegir archivo")
        self.label_archivo = QLabel("Ningún archivo seleccionado")
        self.file_layout.addWidget(self.btn_elegir_archivo)
        self.file_layout.addWidget(self.label_archivo)
        self.layout.addLayout(self.file_layout)

        # Botón agregar filtros
        self.btn_agregar_filtro = QPushButton("Agregar filtros")
        self.layout.addWidget(self.btn_agregar_filtro)

        # Inputs
        self.inputs_layout = QHBoxLayout()
        self.input_codigo = QLineEdit()
        self.input_codigo.setPlaceholderText("Código")
        self.input_codigo.setEnabled(False)

        self.input_descripcion = QLineEdit()
        self.input_descripcion.setPlaceholderText("Descripción")
        self.input_descripcion.setEnabled(False)

        self.dropdown_condicion = QComboBox()
        self.dropdown_condicion.addItems([">", ">=", "<", "<=", "=="])
        self.dropdown_condicion.setEnabled(False)

        self.input_valor = QLineEdit()
        self.input_valor.setPlaceholderText("Valor")
        self.input_valor.setEnabled(False)

        self.inputs_layout.addWidget(self.input_codigo)
        self.inputs_layout.addWidget(self.input_descripcion)
        self.inputs_layout.addWidget(self.dropdown_condicion)
        self.inputs_layout.addWidget(self.input_valor)
        self.layout.addLayout(self.inputs_layout)

        # Botón guardar
        self.btn_guardar = QPushButton("Guardar filtro")
        self.btn_guardar.setEnabled(False)
        self.layout.addWidget(self.btn_guardar)

        # Tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["Código", "Descripción", "Condición", "Valor", "Acción"])
        self.layout.addWidget(self.tabla)

        # Botón ejecutar
        self.btn_ejecutar = QPushButton("Generar Tabla")
        self.layout.addWidget(self.btn_ejecutar)

        self.setLayout(self.layout)
        
    def create_table_item(self, text):
        """Crea un item de tabla con el texto dado."""
        return QTableWidgetItem(str(text))

    def elegir_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo Excel",
            "",
            "Archivos Excel (*.xls *.xlsx)"
        )
        if ruta:
            self.ruta_archivo = ruta
            self.label_archivo.setText(ruta.split("/")[-1])  # Mostrar solo el nombre
