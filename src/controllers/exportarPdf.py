def generar_pdf_resultados(resultados_df, ruta_salida="resultados.pdf"):
    """
    Genera un PDF con la tabla de resultados por departamento.
    resultados_df: DataFrame con columnas ['DPTO', 'fex_total', 'porcentaje']
    """
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    # Crear documento
    doc = SimpleDocTemplate(ruta_salida, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Título
    elements.append(Paragraph("Resultados por Departamento", styles['Title']))
    elements.append(Spacer(1, 12))
    
    # Encabezado
    data = [["DPTO", "FEX", "%"]]
    
    # Filas por departamento
    for _, row in resultados_df.iterrows():
        data.append([row['DPTO'], row['fex_total'], row['porcentaje']])
    
    # Fila de totales
    total_fex = resultados_df['fex_total'].sum()
    data.append(["Total", total_fex, 100])  # El porcentaje total siempre es 100%

    # Crear la tabla con estilo
    table = Table(data, colWidths=[100, 50, 50])
    style = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.black),
        ('ALIGN',(1,1),(-1,-1),'CENTER'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (-3,-1), (-1,-1), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold')
    ])
    table.setStyle(style)
    
    elements.append(table)
    
    # Guardar PDF
    doc.build(elements)
    print(f"PDF generado en: {ruta_salida}")
