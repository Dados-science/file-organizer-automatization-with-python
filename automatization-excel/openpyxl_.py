from openpyxl import load_workbook
import os



# pegando caminho raiz 
base_path = os.path.abspath(os.path.dirname(__file__))
# caminho completo
path = os.path.join(base_path, "exemplo.xlsx")


wb = load_workbook(path)

# abas = wb.get_sheet_names()
print(wb['Sheet1']['A3'].value)
