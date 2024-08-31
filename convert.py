import openpyxl
write_wb = openpyxl.load_workbook("steps.xlsx")
write_ws = write_wb["Sheet1"]
with open('./list.txt','r') as f:
    writelist=f.readlines()
    writelist=[i.rstrip() for i in writelist]
for i in range(len(writelist)):
    write_ws.cell(i,1).value=writelist[i]

