import docx
import pandas as pd
from datetime import date, datetime
import calendar
from app import get_reports_month_rendered_hours, format_timedelta, get_month_info, get_reports_month_weekly



def generatedoc(month,year):
    # Initialise the Word document
    doc = docx.Document()
    month = int(month)
    year = int(year)
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
    # print(df)
    word_month = calendar.month_name[int(month)]

    doc.add_heading(f'Lakandiwa {word_month} {year} DTR Report', 0)

    p = doc.add_paragraph(f"These are the heirarchy of the Lakandiwa members based on their rendered hours of duty for the month of {word_month} {year}.")

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


    month_weekly_totalhours = get_reports_month_weekly(month, year)
    month_weekly_totalhours = list(month_weekly_totalhours)
    month_info = get_month_info(month, year)

    for info in month_info:
        doc.add_heading(f'Week '+ str(info['week_number']) +' Report | '+str(info['week_start']) +' - '+ str(info['week_end']) , 0)
        weekly_members = []
        weekly_total_rendered = []
        weekly_remarks = []
        weekly_position = []
        for each in month_weekly_totalhours:
            if each['week_number'] == info['week_number']:
                weekly_members.append(each['member_name'])
                weekly_total_rendered.append(str(format_timedelta(each['time_total'])))
                weekly_remarks.append(each['remarks'])
                weekly_position.append(each['position'])
        weekly_data = {
            'Name' : weekly_members,
            'Position':weekly_position,
            'Week Total Rendered Hours' : weekly_total_rendered,
            'Remarks': weekly_remarks
        }

        
        wdf = pd.DataFrame(weekly_data)
    

        pa = doc.add_paragraph(f"These are the heirarchy of the Lakandiwa members based on their weekly rendered hours of duty for the month of {word_month} {year}.")

        # Initialise the table
        ta = doc.add_table(rows=1, cols=df.shape[1])

        # Add borders
        ta.style = 'TableGrid'

        # Add the column headings
        for j in range(wdf.shape[1]):
            ta.cell(0, j).text = wdf.columns[j]
        # Add the body of the data frame
        for i in range(wdf.shape[0]):
            row = ta.add_row()
            for j in range(wdf.shape[1]):
                cell = wdf.iat[i, j]
                row.cells[j].text = str(cell)
    # Save the Word doc
    doc.save(f'reports/{word_month}_{year}_DTR_report.docx')