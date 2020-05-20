def set_int_format(ws, rnge):
    # ---set integer value for non text cells---
    for row in ws[rnge]:
        for cell in row:
            text = cell.value
            try:
                text = int(text)
                cell.value = text
            except Exception:
                cell.value = text


def adjust_column_width(ws):
    # adjust excel column width to have a better view of the data
    try:
        for col in ws.columns:
            max_length = 0
            column = col[0].column
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            ws.column_dimensions[column].width = adjusted_width
        return ws
    except Exception as e:
        logging.error('Failed while adjusting excel column width')
        print('Failed while adjusting excel column width: {}'.format(e))