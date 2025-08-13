from PyQt5.QtWidgets import QMessageBox, QPushButton,QTableWidgetItem

def habilitar_inputs(ui):
    ui.input_codigo.setEnabled(True)
    ui.input_descripcion.setEnabled(True)
    ui.dropdown_condicion.setEnabled(True)
    ui.input_valor.setEnabled(True)
    ui.btn_guardar.setEnabled(True)

def guardar_filtro(ui):
    # Leer y limpiar los valores de los inputs
    def limpiar(texto):
        if texto is None:
            return ""
        return texto.strip().replace("\n", "").replace("\r", "")

    codigo = limpiar(ui.input_codigo.text())
    descripcion = limpiar(ui.input_descripcion.text())
    valor = limpiar(ui.input_valor.text())
    condicion = ui.dropdown_condicion.currentText()

    # Verificar que no estén vacíos
    if not codigo or not descripcion or not valor:
        QMessageBox.warning(ui, "Error", "Todos los campos deben estar completos")
        return

    # Insertar nueva fila en la tabla
    row_position = ui.tabla.rowCount()
    ui.tabla.insertRow(row_position)

    ui.tabla.setItem(row_position, 0, QTableWidgetItem(codigo))
    ui.tabla.setItem(row_position, 1, QTableWidgetItem(descripcion))
    ui.tabla.setItem(row_position, 2, QTableWidgetItem(condicion))
    ui.tabla.setItem(row_position, 3, QTableWidgetItem(valor))

    # Botón eliminar
    btn_eliminar = QPushButton("Eliminar")

    def eliminar_fila():
        index = ui.tabla.indexAt(btn_eliminar.pos())
        if index.isValid():
            ui.tabla.removeRow(index.row())

    btn_eliminar.clicked.connect(eliminar_fila)
    ui.tabla.setCellWidget(row_position, 4, btn_eliminar)

    # Limpiar inputs
    ui.input_codigo.clear()
    ui.input_descripcion.clear()
    ui.input_valor.clear()
def ejecutar_filtros(ui):
    print("Ejecutando filtros...")
