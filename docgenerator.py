import docx
import pandas as pd
from datetime import date, datetime
import calendar
from app import get_reports_month_rendered_hours, format_timedelta



def generatedoc(month,year):
    # Initialise the Word document
    doc = docx.Document()
    month = int(month)
    year = int(year)
    headers = ['Name', 'Total Hours Rendered', 'Remarks']
    month_totalhours = get_reports_month_rendered_hours(month, year)
    month_totalhours = list(month_totalhours)
    
    members = []
    total_rendered = []
    remarks = []
    position = []
    for each in month_totalhours:
        members.append(each['name'])
        total_rendered.append(str(format_timedelta(each['total_rendered'])))
        remarks.append(each['remarks'])
        position.append(each['position'])
    
    
    
    data = {
        'Name' : members,
        'Position':position,
        'Total Rendered Hours' : total_rendered,
        'Remarks': remarks
    }

    df = pd.DataFrame(data)
    print(df)
    month = calendar.month_name[int(month)]

    doc.add_heading(f'Lakandiwa {month} {year} DTR Report', 0)

    p = doc.add_paragraph(f"These are the heirarchy of the Lakandiwa members based on their rendered hours of duty for the month of {month} {year}.")

    # Initialise the table
    t = doc.add_table(rows=1, cols=df.shape[1])

    # Add borders
    t.style = 'TableGrid'

    # Add the column headings
    for j in range(df.shape[1]):
        t.cell(0, j).text = df.columns[j]
    # Add the body of the data frame
    for i in range(df.shape[0]):
        row = t.add_row()
        for j in range(df.shape[1]):
            cell = df.iat[i, j]
            row.cells[j].text = str(cell)

    # Save the Word doc
    doc.save(f'reports/{month}_{year}_DTR_report.docx')