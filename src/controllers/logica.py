import pandas as pd
from PyQt5.QtWidgets import QMessageBox
from src.controllers.filtros import calcular_resultados 
from src.controllers.exportarPdf import generar_pdf_resultados  # Asegurate de tener este módulo



def habilitar_inputs(window):
    """Activa los campos de entrada para agregar un nuevo filtro."""
    window.input_codigo.setEnabled(True)
    window.input_descripcion.setEnabled(True)
    window.dropdown_condicion.setEnabled(True)
    window.input_valor.setEnabled(True)
    window.btn_guardar.setEnabled(True)

from PyQt5.QtWidgets import QPushButton

def guardar_filtro(window):
    """Guarda el filtro en la tabla de filtros con botón eliminar."""
    codigo = window.input_codigo.text()
    descripcion = window.input_descripcion.text()
    condicion = window.dropdown_condicion.currentText()
    valor = window.input_valor.text()

    if not codigo or not descripcion or not valor:
        QMessageBox.warning(window, "Campos incompletos", "Por favor rellene todos los campos.")
        return

    fila = window.tabla.rowCount()
    window.tabla.insertRow(fila)

    # Agregar los datos
    window.tabla.setItem(fila, 0, window.create_table_item(codigo))
    window.tabla.setItem(fila, 1, window.create_table_item(descripcion))
    window.tabla.setItem(fila, 2, window.create_table_item(condicion))
    window.tabla.setItem(fila, 3, window.create_table_item(valor))

    # Botón eliminar
    btn_eliminar = QPushButton("Eliminar")
    window.tabla.setCellWidget(fila, 4, btn_eliminar)

    # Conectar el botón a la fila correspondiente
    def eliminar_fila():
        index = window.tabla.indexAt(btn_eliminar.pos())
        if index.isValid():
            window.tabla.removeRow(index.row())

    btn_eliminar.clicked.connect(eliminar_fila)

    # Limpiar inputs
    window.input_codigo.clear()
    window.input_descripcion.clear()
    window.input_valor.clear()

def ejecutar_filtros(window):
    """Lee el archivo Excel, aplica los filtros y genera PDF con resultados por departamento."""
    if not window.ruta_archivo:
        QMessageBox.warning(window, "Archivo no seleccionado", "Por favor elija un archivo Excel.")
        return

    try:
        # Leer Excel según extensión
        if window.ruta_archivo.endswith(".xls"):
            df = pd.read_excel(window.ruta_archivo, engine="xlrd")
        elif window.ruta_archivo.endswith(".xlsx"):
            df = pd.read_excel(window.ruta_archivo, engine="openpyxl")
        else:
            QMessageBox.warning(window, "Formato no soportado", "Debe seleccionar un archivo .xls o .xlsx.")
            return

        # Calcular resultados por departamento
        resultados = calcular_resultados(df, window.tabla, columna_departamento="DPTO")

        # Generar PDF
        generar_pdf_resultados(resultados, ruta_salida="resultados_filtros.pdf")

        QMessageBox.information(window, "Listo", "PDF generado correctamente.")

    except Exception as e:
        QMessageBox.critical(window, "Error", f"No se pudo procesar el archivo:\n{e}")
    
    resultados = calcular_resultados(df, window.tabla, columna_departamento="DPTO")

    
    # Generar PDF
    generar_pdf_resultados(resultados, ruta_salida="resultados_filtros.pdf")