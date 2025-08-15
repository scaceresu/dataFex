# filtros.py
import pandas as pd
from PyQt5.QtWidgets import QTableWidget
from src.controllers.exportarPdf import generar_pdf_resultados

def aplicar_filtros_desde_qtable(table: QTableWidget, df: pd.DataFrame) -> pd.DataFrame:
    mask = pd.Series(True, index=df.index)

    for r in range(table.rowCount()):
        codigo_item = table.item(r, 0)
        condicion_item = table.item(r, 2)
        valor_item = table.item(r, 3)

        if not codigo_item or not condicion_item or not valor_item:
            continue

        col = codigo_item.text().strip()
        cond = condicion_item.text().strip()
        raw_val = valor_item.text().strip()

        if col not in df.columns:
            raise KeyError(f"La columna '{col}' no existe en el archivo.")

        series = df[col]

        try:
            val_num = float(raw_val)
            es_num = True
        except ValueError:
            es_num = False

        if es_num:
            series = pd.to_numeric(series, errors="coerce")

        if cond in (">", "<", ">=", "<=", "==", "!="):
            mask &= eval(f"series {cond} {val_num if es_num else repr(raw_val)}")
        elif cond.lower() == "contains":
            mask &= series.astype(str).str.contains(raw_val, case=False, na=False)

    df = df.copy()
    df["FEX_2022"] = mask
    df["FEX_2022"] = mask.astype(int)
    return df

def calcular_resultados(df, tabla_filtros, columna_departamento="DPTO"):
    """
    df: DataFrame completo del Excel
    tabla_filtros: QTableWidget con los filtros ingresados
    columna_departamento: nombre de la columna de departamentos
    """
    mask = pd.Series(True, index=df.index)
    
    # Aplicar filtros dinámicamente
    for r in range(tabla_filtros.rowCount()):
        col = tabla_filtros.item(r, 0).text()
        cond = tabla_filtros.item(r, 2).text()
        val = tabla_filtros.item(r, 3).text()

        if col not in df.columns:
            continue

        try:
            # Detectar tipo numérico
            try:
                val_num = float(val)
                es_num = True
            except:
                es_num = False

            series = df[col]
            if es_num:
                series = pd.to_numeric(series, errors='coerce')
                mask &= eval(f"series {cond} {val_num}")
            else:
                if cond.lower() == "contains":
                    mask &= series.astype(str).str.contains(val, case=False, na=False)
                else:
                    mask &= eval(f"series {cond} '{val}'")
        except Exception as e:
            print(f"No se pudo aplicar filtro {col} {cond} {val}: {e}")

    # Crear columna fex
    df = df.copy()
    df["FEX_2022"] = mask
    df["fex_int"] = mask.astype(int)

    # Agrupar por departamento
    grouped = df.groupby(columna_departamento).agg(
        total=("FEX_2022", "size"),
        matched=("fex_int", "sum")
    ).reset_index()
    
    # Asegurarse de que haya filas para los departamentos 0–12
    for d in range(13):
        if d not in grouped[columna_departamento].values:
            grouped = pd.concat([grouped, pd.DataFrame({columna_departamento:[d], "total":[0], "matched":[0]})], ignore_index=True)
    
    grouped = grouped.sort_values(columna_departamento).reset_index(drop=True)
    grouped["porcentaje"] = (grouped["matched"] / grouped["total"] * 100).fillna(0).round(2)

    return grouped