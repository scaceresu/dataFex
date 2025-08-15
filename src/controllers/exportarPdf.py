import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generar_pdf_resultados(resultados_df, ruta_salida="resultados.pdf"):
    """
    Genera un PDF con la tabla de resultados por departamento.
    resultados_df: DataFrame con columnas ['departamento', 'total', 'matched', 'porcentaje']
    """
    # Crear documento
    doc = SimpleDocTemplate(ruta_salida, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Título
    elements.append(Paragraph("Resultados por Departamento", styles['Title']))
    elements.append(Spacer(1, 12))
    
    # Crear datos para la tabla
    # Encabezado
    data = [["DPTO", "FEX", "%"]]
    
    # Filas por departamento
    for _, row in resultados_df.iterrows():
        data.append([row['DPTO'], row['matched'], row['porcentaje']])
    
    # Fila de totales
    total_fex = resultados_df['matched'].sum()
    total_porcentaje = (resultados_df['matched'].sum() / resultados_df['total'].sum() * 100).round(2)
    data.append(["Total", total_fex, total_porcentaje])
    
    # Crear la tabla con estilo
    table = Table(data, colWidths=[100, 50, 50])
    style = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.black),
        ('ALIGN',(1,1),(-1,-1),'CENTER'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (-3,-1), (-1,-1), colors.whitesmoke),  # fila de total
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold')
    ])
    table.setStyle(style)
    
    elements.append(table)
    
    # Guardar PDF
    doc.build(elements)
    print(f"PDF generado en: {ruta_salida}")
