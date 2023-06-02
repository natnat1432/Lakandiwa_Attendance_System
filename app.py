from flask import Flask, render_template, request,  redirect, url_for, session, abort, jsonify,send_from_directory
import re
import os
from os.path import exists
from datetime import date, datetime
import uuid
from datetime import timedelta
from flask_mysqldb import MySQL
from PIL import Image
import shutil
import subprocess
import docgenerator
import calendar


app=Flask(__name__)
app.secret_key = "Lakandiwa2023"

env = app.jinja_env
env.add_extension('jinja2.ext.do')
app.jinja_env.add_extension('jinja2.ext.do')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'lakandiwa123' 
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_DB'] = 'lakandiwa'
app.config["REPORT_PATH"] = "reports/"

mysql = MySQL(app)

p = 'logging.txt'


app.config['MEMBER_PATH'] = 'static/members/'
def check_logging():
    try:
        f = open(p,'r')
        print("File Exists")
    except IOError:
        f = open(p, 'w+')
        
        text = open('logging.txt', 'a')
        now = datetime.now()
        date_now = now.strftime("%d/%m/%Y %H:%M:%S")
        text.write("----------------------------------------"+"\n")
        text.write(f"LAKANDIWA LOGGING"+"\n")
        text.write(f"created at {date_now}")
        text.write("\n\n\n\n\n")
        text.close()
        print("File Created")


def generateID(id:str)->str:
    final_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, id)).replace("-", "")[:8]

    return final_id


def make_path(path:str):
    try: 
        os.mkdir(path) 
    except OSError as error: 
        print(error)  

def check_date(date:str)->bool:
   
    valid = False
    try:
        date_format = '%Y-%m-%d'
        dateObject = datetime.strptime(date,date_format)
        valid = True
    except ValueError:
        print("Date is not valid")

    try:
        date_format = '%Y-%m'
        dateObject = datetime.strptime(date,date_format)
        valid = True
    except ValueError:
        print("Date is not valid")
    
    return valid


# def backup_database():
#     subprocess.call([r'C:/Lakandiwa_Attendance_System/Lakandiwa_Attendance_System/backup.bat'])


def format_timedelta(td):
    if td is not None:
        minutes, seconds = divmod(td.seconds + td.days * 86400, 60)
        hours, minutes = divmod(minutes, 60)
        return '{:d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
    else:
        return '{:d}:{:02d}:{:02d}'.format(0, 0, 0)
#============================================================================================
#Database
def get_data(table:str, field:str, value:str)->dict:
    cur = mysql.connection.cursor() 
    cur.execute(f"SELECT * FROM {table} WHERE `{field}` = '{value}' ")
    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data


def count_data(table:str)->dict:
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT COUNT(*) AS total FROM `{table}`")
    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data



def get_all_data(table:str)->dict:
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM {table}")
    data:dict = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return data


def get_today_data_attendance(id_number)->dict:
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM `attendance` WHERE `id_number` = '{id_number}' AND DATE(`time_in`) = CURDATE() ORDER BY `time_in` ASC")
    data:dict = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return data

def get_member_data_attendance(id_number, sort, filter, data, page)->dict:
    cur = mysql.connection.cursor()
    scope = page*10

    if filter == 'all':
        cur.execute(f"SELECT * FROM `attendance` WHERE `id_number` = '{id_number}' ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")
    if filter == 'today':
        cur.execute(f"SELECT * FROM `attendance` WHERE `id_number` = '{id_number}' AND DATE(`time_in`) = CURDATE() ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")
    if filter == 'thisweek':
        cur.execute(f"SELECT * FROM `attendance` WHERE `id_number` = '{id_number}' AND WEEKOFYEAR(DATE(`time_in`))=WEEKOFYEAR(NOW()) ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")
    if filter == 'lastweek':
        cur.execute(f"SELECT * FROM `attendance` WHERE `id_number` = '{id_number}' AND `time_in` >= CURDATE() - INTERVAL WEEKDAY(CURDATE()) day - INTERVAL 5 week AND `time_in` < CURDATE() - INTERVAL WEEKDAY(CURDATE()) day ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")
    if filter == 'day':
        cur.execute(f"SELECT * FROM `attendance` WHERE `id_number` = '{id_number}' AND DATE(`time_in`) = '{data}' ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")
    if filter == 'month':
        cur.execute(f"SELECT * FROM `attendance` WHERE `id_number` = '{id_number}' AND MONTH(`time_in`) = {data.split('-')[1]} AND YEAR(`time_in`) = {data.split('-')[0]} ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")

    data:dict = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return data

def get_all_data_attendance(sort, filter, data, page)->dict:
    cur = mysql.connection.cursor()
    scope = page*10

    if filter == 'all':
        cur.execute(f"SELECT * FROM `attendance` ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")
    if filter == 'today':
        cur.execute(f"SELECT * FROM `attendance` WHERE DATE(`time_in`) = CURDATE() ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")
    if filter == 'thisweek':
        cur.execute(f"SELECT * FROM `attendance` WHERE WEEKOFYEAR(DATE(`time_in`))=WEEKOFYEAR(NOW()) ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")
    if filter == 'lastweek':
        cur.execute(f"SELECT * FROM `attendance` WHERE `time_in` >= CURDATE() - INTERVAL WEEKDAY(CURDATE()) day - INTERVAL 5 week AND `time_in` < CURDATE() - INTERVAL WEEKDAY(CURDATE()) day ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")
    if filter == 'day':
        cur.execute(f"SELECT * FROM `attendance` WHERE DATE(`time_in`) = '{data}' ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")
    if filter == 'month':
        cur.execute(f"SELECT * FROM `attendance` WHERE MONTH(`time_in`) = {data.split('-')[1]} AND YEAR(`time_in`) = {data.split('-')[0]} ORDER BY `time_in` {sort.upper()} LIMIT {scope-10},{scope}")

    data:dict = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return data

def count_member_attendance(id_number, filter, data)->dict:
    cur = mysql.connection.cursor()

    if filter == 'all':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` WHERE `id_number` = '{id_number}' ")
    if filter == 'today':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` WHERE `id_number` = '{id_number}' AND DATE(`time_in`) = CURDATE()")
    if filter == 'thisweek':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` WHERE `id_number` = '{id_number}' AND WEEKOFYEAR(DATE(`time_in`))=WEEKOFYEAR(NOW()) ")
    if filter == 'lastweek':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` WHERE `id_number` = '{id_number}' AND `time_in` >= CURDATE() - INTERVAL WEEKDAY(CURDATE()) day - INTERVAL 5 week AND `time_in` < CURDATE() - INTERVAL WEEKDAY(CURDATE()) day")
    if filter == 'day':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` WHERE `id_number` = '{id_number}' AND DATE(`time_in`) = '{data}' ")
    if filter == 'month':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` WHERE `id_number` = '{id_number}' AND MONTH(`time_in`) = {data.split('-')[1]} AND YEAR(`time_in`) = {data.split('-')[0]}  ")


    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data
    
def count_all_attendance(filter, data)->dict:
    cur = mysql.connection.cursor()

    if filter == 'all':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` ")
    if filter == 'today':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` WHERE DATE(`time_in`) = CURDATE()")
    if filter == 'thisweek':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` WHERE WEEKOFYEAR(DATE(`time_in`))=WEEKOFYEAR(NOW()) ")
    if filter == 'lastweek':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` WHERE `time_in` >= CURDATE() - INTERVAL WEEKDAY(CURDATE()) day - INTERVAL 5 week AND `time_in` < CURDATE() - INTERVAL WEEKDAY(CURDATE()) day")
    if filter == 'day':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` WHERE DATE(`time_in`) = '{data}' ")
    if filter == 'month':
        cur.execute(f"SELECT COUNT(*) AS total FROM `attendance` WHERE MONTH(`time_in`) = {data.split('-')[1]} AND YEAR(`time_in`) = {data.split('-')[0]}  ")

    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data

def get_oldest_date_member(id_number)->dict:
    cur = mysql.connection.cursor()
    cur.execute(f'select DATE_FORMAT(time_in, "%Y-%m-%d") AS oldest_date from attendance WHERE id_number = "{id_number}" ORDER BY time_in ASC LIMIT 1')
    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data

def get_newest_date_member(id_number)->dict:
    cur = mysql.connection.cursor()
    cur.execute(f'select DATE_FORMAT(time_in, "%Y-%m-%d") AS newest_date from attendance WHERE id_number = "{id_number}" ORDER BY time_in DESC LIMIT 1')
    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data

def get_oldest_date_all()->dict:
    cur = mysql.connection.cursor()
    cur.execute(f'select DATE_FORMAT(time_in, "%Y-%m-%d") AS oldest_date from attendance ORDER BY time_in ASC LIMIT 1')
    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data

def get_newest_date_all()->dict:
    cur = mysql.connection.cursor()
    cur.execute(f'select DATE_FORMAT(time_in, "%Y-%m-%d") AS newest_date from attendance ORDER BY time_in DESC LIMIT 1')
    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data

def get_total_today_rendered_hours(id_number)->dict:
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT SEC_TO_TIME(SUM(TIME_TO_SEC(`time_rendered`))) AS total_rendered FROM `attendance` WHERE `id_number` = '{id_number}' AND DATE(`time_in`) = CURDATE()")
    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data

def get_total_week_rendered_hours(id_number)->dict:
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT SEC_TO_TIME(SUM(TIME_TO_SEC(`time_rendered`))) AS total_rendered from `attendance` WHERE WEEKOFYEAR(DATE(`time_in`))=WEEKOFYEAR(NOW()) AND `id_number` = '{id_number}' ")
    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data

def get_total_month_rendered_hours(id_number, month, year)->dict:
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT SEC_TO_TIME(SUM(TIME_TO_SEC(`time_rendered`))) AS total_rendered from `attendance` WHERE MONTH(`time_in`) = '{month}' AND YEAR(`time_in`) = '{year}' AND `id_number` = '{id_number}' ")
    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data

def get_reports_month_rendered_hours(month, year)->dict:
    cur = mysql.connection.cursor()
    cur.execute(f'SELECT CONCAT(member.lastname,", ", member.firstname," ", left(member.middlename,1),".") AS name, CONCAT(position.position_level, " ", position.position) AS position, SEC_TO_TIME(SUM(TIME_TO_SEC(attendance.time_rendered))) AS total_rendered, IF(HOUR(SEC_TO_TIME(SUM(TIME_TO_SEC(attendance.time_rendered))))>40,"Complete", "Incomplete") AS remarks from member,position,attendance  WHERE member.id_number = attendance.id_number AND member.positionID = position.positionID AND MONTH(attendance.time_in) = "{month}" AND YEAR(attendance.time_in) = "{year}" GROUP BY member.id_number ORDER BY total_rendered DESC')
    data:dict = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return data

def get_unsigned_time_in()->dict:
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM `attendance` WHERE `signature_time_in` IS NULL")
    data:dict = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return data

def get_unsigned_time_out()->dict:
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM `attendance` WHERE `signature_time_out` IS NULL AND `time_out` IS NOT NULL")
    data:dict = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return data

def get_latest(id:str):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM `attendance` WHERE id_number = '{id}' AND `time_out` IS NULL ORDER BY `time_in` DESC LIMIT 1")
    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data

def insert_data(table:str, fields, value)->bool:
    cur = mysql.connection.cursor()

    flds = '`,`'.join(fields)
    dta = "','".join(value)
    cur.execute(f"INSERT INTO `{table}`(`{flds}`) VALUES('{dta}')")
    mysql.connection.commit()
    cur.close()
    return True


def delete_data(table:str, field, value)->bool:
    cur = mysql.connection.cursor()
    cur.execute(f"DELETE FROM `{table}` WHERE `{field}` = '{value}' ")
    mysql.connection.commit()
    cur.close()
    return True

def update_data(table:str, fields, values)->bool:
    cur = mysql.connection.cursor()
    flds = []
    if len(fields) == len(values):
        for i in range(len(fields)):
            flds.append(f"`{fields[i]}` = '{values[i]}'")
        flds_final = ", ".join(flds)
        cur.execute(f'''UPDATE `{table}` SET {flds_final} WHERE `{fields[0]}` = "{values[0]}" ''')
        mysql.connection.commit()
        cur.close()
        return True
    else:
        return False

def get_specific_data(table:str, fields, values):
    cur = mysql.connection.cursor()
    flds = []
    
    if len(fields) == len(values):
        for i in range(len(fields)):
            if type(values[i]) == str:
                flds.append(f'`{fields[i]}` = "{values[i]}"')
            else:
                flds.append(f"`{fields[i]}` = {values[i]}")
        flds_final = " AND ".join(flds)
        cur.execute(f'SELECT * FROM {table} WHERE {flds_final}')
        data:dict = cur.fetchone()
        mysql.connection.commit()
        cur.close()
        return data

#delete stamps that are not timed out on a previous day
def void_forgotten_stamps():
    cur = mysql.connection.cursor()
    cur.execute(f'''DELETE FROM `attendance` WHERE time_out IS NULL AND date(`time_in`) != curdate()''')
    mysql.connection.commit()
    cur.close()

def get_oldest_newest_record():
    cur = mysql.connection.cursor()
    cur.execute(f'''SELECT DATE(MIN(time_in)) as min, DATE(MAX(time_in)) as max FROM lakandiwa.attendance''')
    data:dict = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return data

@app.route("/")
def index():
    #delete forgotten stamps
    void_forgotten_stamps()
    # backup_database()
    return redirect(url_for('login', message= 'ok'))


@app.route("/login/<message>")
def login(message:str):
    #delete forgotten stamps
    void_forgotten_stamps()

    title = "Log in"
    if message == 'ok':
        return render_template("index.html", title=title)
    
    if message == 'invalid':
        message = 'Invalid credentials. Please log in again.'

        return render_template("index.html", message=message, title=title)
    if message == 'Login first':
        message = 'Please log in first.'

        return render_template("index.html", message=message, title=title)  
    else:
        return abort(404, "Page not found")
@app.route("/loginAccount" , methods=['POST'])
def loginAccount():
    #delete forgotten stamps
    void_forgotten_stamps()

    user = request.form['username']
    password = request.form['password']

    fields = ['id_number','password']
    data = [user, password]
    check_user = get_specific_data('member', fields, data)

    if check_user:
        session['user_id'] = user
        return redirect(url_for('dashboard'))

    if user == 'admin' and password == 'antifragile' and not check_user:
        session['user_id'] = user
        return redirect(url_for('accountlist'))
    


    else:
        return redirect(url_for('login', message='invalid'))

@app.route("/dashboard")
def dashboard():
    #delete forgotten stamps
    void_forgotten_stamps()
    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))
    title = "Dashboard"

    now = datetime.now()

    if session['user_id'] != 'admin':
        accountuser = get_data('member', 'id_number', session['user_id'])
        current_timed = get_latest(accountuser['id_number'])
        current_attendance = get_today_data_attendance(accountuser['id_number'])
        today_totalhours = get_total_today_rendered_hours(accountuser['id_number'])
        week_totalhours = get_total_week_rendered_hours(accountuser['id_number'])
        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        month_totalhours = get_total_month_rendered_hours(accountuser['id_number'], currentMonth, currentYear)
    else:
        accountuser = None
        current_timed = None
        current_attendance = None
        today_totalhours = None
        week_totalhours = None
        month_totalhours = None
    
    log_user = session['user_id']
    members = get_all_data('member')
    positions = get_all_data('position')

    if today_totalhours is not None:
        today_totalhours =  str(format_timedelta(today_totalhours['total_rendered']))
    if week_totalhours is not None:
        week_totalhours =  str(format_timedelta(week_totalhours['total_rendered']))
    
    if month_totalhours is not None:
        month_totalhours =  str(format_timedelta(month_totalhours['total_rendered']))
   


    return render_template("dashboard.html", title=title,
    today_totalhours = today_totalhours,
    week_totalhours = week_totalhours,
    month_totalhours = month_totalhours,
    current_attendance = current_attendance,
    accountuser = accountuser,
    positions = positions,
    current_timed = current_timed,
    members = members,
    log_user = log_user,
    now = now)

@app.route("/time_in", methods=['POST'])
def time_in():
    id_number = request.form['id_number']
    now = datetime.now()
    fields = ['attendanceID','id_number','time_in']
    attendanceID = generateID(str(id_number) + str(now))
    data = [attendanceID, id_number, str(now)]
    insert_data('attendance',fields, data)
    # backup_database()
    return redirect(url_for('dashboard'))

@app.route("/time_out", methods=['POST'])
def time_out():
    attendanceID = request.form['attendanceID']
    work_done = request.form['work_done']
    now = datetime.now()
    fields = ['attendanceID', 'time_out', 'work_done']
    data = [attendanceID, str(now), work_done]
    update_data('attendance', fields, data)
    # backup_database()
    return redirect(url_for('dashboard'))


@app.route("/positions")
def positions():
    #delete forgotten stamps
    void_forgotten_stamps()

    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))
    

    accountuser = get_data('member', 'id_number', session['user_id'])
    title = "Positions"
    position_levels = get_all_data("position_level")
    positions = get_all_data("position")
    log_user = session['user_id']
    success = request.args.get('success')
    error = request.args.get('error')
    return render_template("positions.html", 
    title=title,
    positions = positions,
    position_levels = position_levels,
    success = success,
    error = error,
    log_user = log_user,
    accountuser = accountuser
    )

@app.route("/addpositionlevel", methods=['POST'])
def addpositionlevel():
    #delete forgotten stamps
    void_forgotten_stamps()
    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))
    position_level = request.form['position_level']
    exist = get_data('position_level', 'position_level', position_level)
    if not exist and position_level:
        now = datetime.now()
        date_now = now.strftime("%d/%m/%Y %H:%M:%S")
        print('\n\n')
        print("----------------------------------------")
        print(f"New position level added | {date_now}")
        print("position level : " + position_level)
        print("----------------------------------------")
        print("\n\n")


        #Write to logging.txt
        check_logging()
        text = open('logging.txt', 'a')
        text.write('\n\n')
        text.write("----------------------------------------"+"\n")
        text.write(f"New position level added | {date_now}")
        text.write("position level : " + position_level)
        text.write("----------------------------------------"+"\n")
        text.write("\n\n")
        text.close()

        fields = []
        fields.append('position_level')
        data = []
        data.append(position_level)
        insert_data('position_level', fields, data)
        message = f"Position level {position_level} successfully added"
        # backup_database()
        return redirect(url_for("positions", sucess=message))
    else:
        message = f"Position level {position_level} already exist!"
        return redirect(url_for("positions", error=message))

@app.route("/addposition", methods=['POST'])
def addposition():
    #delete forgotten stamps
    void_forgotten_stamps()

    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))

    position_level = request.form['position_level']
    position = request.form['position']
    positionID = generateID(position+position_level)

    flds = []
    flds.append('positionID')
    flds.append('position')
    flds.append('position_level')


    data = []
    data.append(positionID)
    data.append(position)
    data.append(position_level)



    exist = get_specific_data('position', flds, data)

    if not exist and position_level != 'none' and position:
        now = datetime.now()
        date_now = now.strftime("%d/%m/%Y %H:%M:%S")
        print('\n\n')
        print("----------------------------------------\n")
        print(f"New position added | {date_now}\n")
        print("positionID : " + positionID+"\n")
        print("position : " + position+"\n")
        print("position level : " + position_level+"\n")
        print("----------------------------------------"+"\n")
        print("\n\n")


        #Write to logging.txt
        check_logging()
        text = open('logging.txt', 'a')
        text.write('\n\n')
        text.write("----------------------------------------"+"\n")
        text.write(f"New position added | {date_now}"+"\n")
        text.write("positionID : " + positionID+"\n")
        text.write("position : " + position+"\n")
        text.write("position level : " + position_level+"\n")
        text.write("----------------------------------------"+"\n")
        text.write("\n\n")
        text.close()
        insert_data('position', flds, data)
        message = f"Position {position } successfully added."
        # backup_database()
        return redirect(url_for('positions', success=message))
    else:
        message = f"Position {position} already exist!"
        return redirect(url_for("positions", error=message))




@app.route("/deletepositionlevel", methods=['POST'])
def deletepositionlevel():
 

   position_level = request.form.getlist('position_level')
   for pos in position_level:
        now = datetime.now()
        date_now = now.strftime("%d/%m/%Y %H:%M:%S")
        print('\n\n')
        print("----------------------------------------"+"\n")
        print(f"Position level {pos} deleted | {date_now}"+"\n")
        print("----------------------------------------"+"\n")
        print("\n\n")


        #Write to logging.txt
        check_logging()
        text = open('logging.txt', 'a')
        text.write('\n\n')
        text.write("----------------------------------------"+"\n")
        text.write(f"Position level  {pos} deleted | {date_now}"+"\n")
        text.write("Position Level : " + pos)
        text.write("----------------------------------------"+"\n")
        text.write("\n\n")
        text.close()
        delete_data('position_level', 'position_level', pos)
        # backup_database()
   success = f'Position level(s) deleted'
   return redirect(url_for("positions", success=success))

@app.route("/deleteposition", methods=['POST'])
def deleteposition():
   position = request.form.getlist('position')
   for pos in position:
        now = datetime.now()
        date_now = now.strftime("%d/%m/%Y %H:%M:%S")
        print('\n\n')
        print("----------------------------------------")
        print(f"Position {pos} deleted | {date_now}")
        print("----------------------------------------")
        print("\n\n")


        #Write to logging.txt
        check_logging()
        text = open('logging.txt', 'a')
        text.write('\n\n')
        text.write("----------------------------------------"+"\n")
        text.write(f"Position {pos} deleted | {date_now}"+"\n")
        text.write("Position: " + pos+"\n")
        text.write("----------------------------------------"+"\n")
        text.write("\n\n")
        text.close()
        delete_data('position', 'positionID', pos)
        # backup_database()
   success = f'Position(s) deleted'
   return redirect(url_for("positions", success=success))

@app.route("/deleteaccount", methods=['POST'])
def deleteaccount():
    accounts = request.form.getlist('accounts')

    for account in accounts:

        flds = ['id_number']
        data = [account]
        user = get_specific_data('member', flds, data)
        now = datetime.now()
        date_now = now.strftime("%d/%m/%Y %H:%M:%S")
        print('\n\n')
        print("----------------------------------------")
        print(f"Account {user['lastname']},{user['firstname']} {user['middlename'][0]}. with ID_Number: {account} deleted | {date_now}")
        print("----------------------------------------")
        print("\n\n")


        #Write to logging.txt
        check_logging()
        text = open('logging.txt', 'a')
        text.write('\n\n')
        text.write("----------------------------------------"+"\n")
        text.write(f"Account {user['lastname']},{user['firstname']} {user['middlename'][0]}. with ID_Number: {account} deleted | {date_now}"+"\n")
        text.write("----------------------------------------"+"\n")
        text.write("\n\n")
        text.close()
        delete_data('member', 'id_number', account)
        path = app.config['MEMBER_PATH']+ account
        shutil.rmtree(path)
        # backup_database()
    success = 'Account(s) deleted'
    return redirect(url_for('accountlist', success= success))

@app.route("/accountlist")
def accountlist():
    #delete forgotten stamps
    void_forgotten_stamps()
    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))
    
    accountuser = get_data('member', 'id_number', session['user_id'])
    title = "Account List"
    accounts = get_all_data('member')
    positions = get_all_data('position')
    error = request.args.get('error')
    success = request.args.get('success')
    log_user = session['user_id']
    return render_template(
        "accountlist.html",
        title=title,
        positions = positions,
        accounts = accounts,
        success=success,
        error=error,
        log_user = log_user,
        accountuser = accountuser
    )

@app.route("/addmember", methods=['POST'])
def addmember():
    #delete forgotten stamps
    void_forgotten_stamps()
    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))

    id_number = request.form['id_number']
    firstname = request.form['firstname'].upper()
    middlename = request.form['middlename'].upper()
    lastname = request.form['lastname'].upper()
    birthdate = request.form['birthdate']
    position = request.form['position']
    contact_number = request.form['contact_number']

    dp_filename = "user_pic.jpg"
    password = "lakandiwa123"
    
    dp_final = f"{id_number}.jpg"


    existing_member = get_data('member', 'id_number', id_number)


    if id_number and firstname and lastname and birthdate and position and not existing_member:
        now = datetime.now()
        date_now = now.strftime("%d/%m/%Y %H:%M:%S")
        print('\n\n')
        print("----------------------------------------")
        print(f"New member added | {date_now}")
        print("ID Number: " + id_number)
        print("Name:" + firstname+ " "+ middlename + " " + lastname)
        print("Birthdate: " + birthdate)
        print("PositionID: " + position)
        print("Contact Number: "+ contact_number)
        print("----------------------------------------")
        print("\n\n")
        member_path = app.config['MEMBER_PATH']+str(id_number)
        make_path(member_path)
        file = f"static/images/{dp_filename}"
        img = Image.open(file)
        img.save(f"{member_path}/{id_number}.jpg")
   
        #Write to logging.txt
        check_logging()
        text = open('logging.txt', 'a')
        text.write('\n\n')
        text.write("----------------------------------------"+"\n")
        text.write(f"New lakandiwa member added | {date_now}"+"\n")
        text.write("ID Number: " + id_number+"\n")
        text.write("Name:" + firstname+ " "+ middlename + " " + lastname+"\n")
        text.write("Birthdate: " + birthdate+"\n")
        text.write("PositionID: " + position+"\n")
        text.write("Contact Number: "+ contact_number+"\n")
        text.write("----------------------------------------"+"\n")
        text.write("\n\n")
        text.close()

        fields = ['id_number','password', 'firstname', 'middlename', 'lastname', 'birthdate', 'positionID', 'contact_number', 'dp_filename']
        data = [id_number,password, firstname,middlename,lastname,birthdate,position, contact_number, dp_final ]

        insert_data('member', fields, data)
        # backup_database()
        message = f"Successfully added { lastname}, {firstname} {middlename} as member"
        return redirect(url_for('accountlist', success=message))

    if id_number and firstname and lastname and birthdate and position and  existing_member:
        message = f"Member { lastname}, {firstname} {middlename} is already a member"
        return redirect(url_for('accountlist', error=message))
    else:
        message = f"Invalid credential inputs. Please fill the fields properly."
        return redirect(url_for('accountlist', error=message))


@app.route("/signing")
def signing():
    #delete forgotten stamps
    void_forgotten_stamps()
    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))

    accountuser = get_data('member', 'id_number', session['user_id'])
    title = "Signing"
    log_user = session['user_id']
    unsigned_time_in = get_unsigned_time_in()
    unsigned_time_out = get_unsigned_time_out()
    members = get_all_data('member')
    positions = get_all_data('position')
    error = request.args.get('error')
    success = request.args.get('success')
    return render_template('signing.html',
    accountuser = accountuser,
    unsigned_time_in = unsigned_time_in,
    unsigned_time_out = unsigned_time_out,
    members = members,
    positions = positions,
    error = error,
    success = success,
    title = title,
    log_user = log_user
    )


@app.route("/countersign/<type>/<attendanceID>/<id_number>")
def countersign(type:str, attendanceID:str, id_number:str):
    #delete forgotten stamps
    void_forgotten_stamps()
    exist_attendance = get_specific_data('attendance', ['attendanceID'], [attendanceID])
    exist_member = get_specific_data('member', ['id_number'], [id_number])
    accepted_type = ['in', 'out']
    if exist_attendance and exist_member and type in accepted_type:

        if type == 'in':
            update_data('attendance', ['attendanceID', 'countersign_time_in'], [attendanceID, id_number])
        if type == 'out':
            update_data('attendance', ['attendanceID', 'countersign_time_out'], [attendanceID, id_number])

        attendance_signed = get_data('attendance', 'attendanceID', attendanceID)
        user_signed = get_data('member', 'id_number', attendance_signed['id_number'])
        user_signer = get_data('member', 'id_number', id_number)
        # backup_database()
        message = f"{user_signer['lastname']}, {user_signer['firstname']} {user_signer['middlename'][0].capitalize()} countersigned {user_signed['lastname']}, {user_signed['firstname']} {user_signed['middlename'][0].capitalize()}'s Time {type.capitalize()} Stamp"  
        return redirect(url_for('signing', success = message))
    else:
        return abort(404, "Page not found")
@app.route("/sign/<type>/<attendanceID>/<id_number>")
def sign(type:str, attendanceID:str, id_number:str):
    #delete forgotten stamps
    void_forgotten_stamps()
    exist_attendance = get_specific_data('attendance', ['attendanceID'], [attendanceID])
    exist_member = get_specific_data('member', ['id_number'], [id_number])
    accepted_type = ['in', 'out']

 
    if exist_attendance and exist_member and type in accepted_type:

        if type == 'in':
            update_data('attendance', ['attendanceID', 'signature_time_in'], [attendanceID, id_number])
        if type == 'out':
            time_in = exist_attendance['time_in']
            time_out = exist_attendance['time_out']

            time_rendered = format_timedelta(time_out - time_in)
            print(f"TIME RENDERED: {time_rendered}")
      
            update_data('attendance', ['attendanceID', 'signature_time_out', 'time_rendered'], [attendanceID, id_number, time_rendered])
        # backup_database()
        attendance_signed = get_data('attendance', 'attendanceID', attendanceID)
        user_signed = get_data('member', 'id_number', attendance_signed['id_number'])
        user_signer = get_data('member', 'id_number', id_number)

        message = f"{user_signer['lastname']}, {user_signer['firstname']} {user_signer['middlename'][0].capitalize()} signed {user_signed['lastname']}, {user_signed['firstname']} {user_signed['middlename'][0].capitalize()}'s Time {type.capitalize()} Stamp"  
        return redirect(url_for('signing', success = message))
    else:
        return abort(404, "Page not found")

@app.route("/rejectsign/<type>/<attendanceID>")
def rejectsign(type:str, attendanceID:str):
    #delete forgotten stamps
    void_forgotten_stamps()
    exist_attendance = get_specific_data('attendance', ['attendanceID'], [attendanceID])
    allowed_type = ['in', 'out']
    if exist_attendance:
        attendance_signed = get_data('attendance', 'attendanceID', attendanceID)
        del_attendance = delete_data('attendance', 'attendanceID', attendanceID)

        if del_attendance and type in allowed_type:
            
            user_signed = get_data('member', 'id_number', attendance_signed['id_number'])


            message = f"Successfully rejected {user_signed['lastname']}, {user_signed['firstname']} {user_signed['middlename'][0].capitalize()}'s Time {type.capitalize()} Stamp"  
            # backup_database()
            return redirect(url_for('signing', success = message))
        else:
            
            return redirect(url_for('signing'))
    else:
        return abort(404, "Page not found")

@app.route("/deleteRecord")
def deleteRecord():
    attendanceID = request.args.get("attendanceID")

    target = request.args.get('target')
    filter = request.args.get('filter')
    sort = request.args.get('sort')
    page = request.args.get('page')

    delete = delete_data('attendance', 'attendanceID', attendanceID)

    if delete:
        return redirect(url_for('attendance', target=target, filter=filter, sort=sort, page=page))
    
@app.route("/attendance")
def attendance():
    #delete forgotten stamps
    void_forgotten_stamps()
    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))
    
    sortList = ['asc', 'desc']
    filterList = ['all', 'today', 'thisweek', 'lastweek', 'day', 'month']
    targetList = ['myrecord', 'allrecord']
    title = "Attendance"
    log_user = session['user_id']
    page = request.args.get('page')
    
    paginated_consumption = {}
    count_attendance = None
    data = None
    
    if page is None:
        page = '1'

    target = request.args.get('target')
    if target is not None and target not in targetList:
        return abort(404, 'Page not found')
    if target is None:
        target = 'myrecord'

    sort = request.args.get('sort')
    if sort is not None and sort not in sortList:
        return abort(404, "Page not found")
    if sort is None:
        sort = 'asc'

    filter = request.args.get('filter')
    if filter is None:
        filter = 'all'
    if filter is not None and filter not in filterList:
        return abort(404, 'Page not found')
    



    day = request.args.get('day')
    if day is not None and not check_date(day):
        return abort(404, "Page not found")
    if day is not None and check_date(day):
        data = day
    
    month = request.args.get('month')
    if month is not None and not check_date(month):
        return abort(404, "Page not found")
    if month is not None and check_date(month):
        data = month
    


    accountuser = get_data('member', 'id_number', session['user_id'])
    count_attendance = None
    if target == 'myrecord':
        count_attendance = count_member_attendance(accountuser['id_number'], filter, data)
    if target == 'allrecord':
        count_attendance = count_all_attendance(filter,data)


    total_page = int(count_attendance['total']/10)
    remainder = int(count_attendance['total']%10)

    paginated_consumption['start'] = (int(page)*10) - 10
    paginated_consumption['end'] = int(page)*10

    if paginated_consumption['start'] < 0:
        paginated_consumption['start'] = 0
    if paginated_consumption['end'] > int(count_attendance['total']):
        paginated_consumption['end'] = count_attendance['total']
    
    if remainder>0:
        total_page+=1

    if int(page)< 0 or int(page) == 0 and total_page>0 :
        return abort(404, description="Page not found")
    

    if int(page)>total_page and total_page>0:
        return abort(404, "Page not found")
    

    total_attendance = None

    if target == 'myrecord':
        total_attendance = get_member_data_attendance(accountuser['id_number'],sort, filter,data,int(page))
    if target == 'allrecord':
        total_attendance = get_all_data_attendance(sort, filter,data,int(page))

    error = request.args.get('error')
    success = request.args.get('success')
   
    members = get_all_data('member')
    positions = get_all_data('position')
    
    current = None
    oldest = None
    if target == 'myrecord':
        current = get_newest_date_member(accountuser['id_number'])
        oldest = get_oldest_date_member(accountuser['id_number'])
    if target == 'allrecord':
        current = get_newest_date_all()
        oldest = get_oldest_date_all()
        
    if current is not None:
        current = current['newest_date']
    if oldest is not None:
        oldest = oldest['oldest_date']
    return render_template("attendance.html",
    title = title,
    log_user = log_user,
    error = error,
    page = page,
    current=current,
    target = target,
    oldest=oldest,
    total_page = total_page,
    paginated_consumption = paginated_consumption,
    count_attendance = count_attendance,
    sort = sort,
    day = day,
    month = month,
    filter = filter,
    members = members,
    total_attendance = total_attendance,
    positions = positions,
    success = success,
    accountuser = accountuser
    )

@app.route("/profile")
def profile():
    #delete forgotten stamps
    void_forgotten_stamps()
    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))
    title = "Profile"
    log_user = session['user_id']
    error = request.args.get('error')
    success = request.args.get('success')
    accountuser = get_data('member', 'id_number', session['user_id'])
    members = get_all_data('member')
    positions = get_all_data('position')

    return render_template("profile.html",
    title = title,
    log_user = log_user,
    error =  error,
    success = success,
    accountuser = accountuser,
    members = members ,
    positions = positions
    )

@app.route("/changepassword", methods=['POST'])
def changepassword():
    #delete forgotten stamps
    void_forgotten_stamps()
    id_number = request.form['id_number']
    newpassword = request.form['newpassword']
    confirmpassword = request.form['confirmpassword']

    update_data('member', ['id_number', 'password'], [id_number,confirmpassword])
    message = "You have successfully changed your password."
    # backup_database()
    return redirect(url_for('profile', success = message))

@app.route("/changeprofilepicture")
def changeprofilepicture():
    #delete forgotten stamps
    void_forgotten_stamps()

    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))
    title = "Change Profile Picture"
    
    log_user = session['user_id']
    accountuser = get_data('member', 'id_number', session['user_id'])
    members = get_all_data('member')
    positions = get_all_data('position')
    # backup_database()
    return render_template("changeprofileimage.html", 
    title=title,
    log_user = log_user,
    members = members,
    positions = positions,
    accountuser=accountuser)

@app.route("/updateprofilepicture", methods=['POST'])
def updateprofilepicture():
    #delete forgotten stamps
    void_forgotten_stamps()

    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))
    if 'profile_picture' in request.files:
        profile_picture = request.files['profile_picture']
        accountuser = get_data('member', 'id_number', session['user_id'])
        member_path = app.config['MEMBER_PATH']+str(accountuser['id_number'])
        profile_picture.save(f"{member_path}/{accountuser['id_number']}.jpg")

        foo = Image.open(f"{member_path}/{accountuser['id_number']}.jpg") 
        foo = foo.convert('RGB')
        foo = foo.resize((500,500),Image.ANTIALIAS)
        foo.save(f"{member_path}/{accountuser['id_number']}.jpg",optimize=True, quality=95)
        # backup_database()
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('profile'))


@app.route("/updateprofileinfo", methods=['POST'])
def updateprofileinfo():
    #delete forgotten stamps
    void_forgotten_stamps()

    id_number = request.form['id_number']
    firstname = request.form['firstname']
    middlename = request.form['middlename']
    lastname = request.form['lastname']
    birthdate = request.form['birthdate']
    contact_number = request.form['contact_number']

    if id_number and firstname and middlename and lastname and birthdate and contact_number:
        update_data('member', ['id_number', 'firstname', 'middlename', 'lastname', 'birthdate', 'contact_number'], [id_number,firstname.upper(),middlename.upper(),lastname.upper(),birthdate,contact_number])
        message = "Profile Info updated successfully"
        # backup_database()
        return redirect(url_for('profile', success=message))
    else:
        message = "Error updating profile info"
        return redirect(url_for('profile', error=message))

@app.route("/reports")
def reports():
    #delete forgotten stamps
    void_forgotten_stamps()
    if 'user_id' not in session:
        return redirect(url_for('login', message= 'Login first'))
    title = "Reports"
    date = request.args.get('date')
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    mnth = str(currentMonth)
    data_old_new = get_oldest_newest_record()

    min = str(data_old_new['min'])[0:7]
    max = str(data_old_new['max'])[0:7]

    if date is None:
        if currentMonth < 10:
            mnth = f'0{currentMonth}'
        date = f'{currentYear}-{mnth}'

    print("DATE", date)
    log_user = session['user_id']
    error = request.args.get('error')
    success = request.args.get('success')
    accountuser = get_data('member', 'id_number', session['user_id'])
    members = get_all_data('member')
    positions = get_all_data('position')
    

    date_data = date.split('-')
    
    month_totalhours = get_reports_month_rendered_hours(date_data[1], date_data[0])
    for each in month_totalhours:
        each['total_rendered'] = str(format_timedelta(each['total_rendered']))
    
    return render_template("reports.html",
    title = title,
    month_totalhours = month_totalhours,
    log_user = log_user,
    error =  error,
    success = success,
    accountuser = accountuser,
    members = members ,
    positions = positions,
    date=date,
    mnth = currentMonth,
    year = currentYear,
    min = min,
    max = max
    )
    
@app.route("/generatereport", methods=['POST'])
def generatereport():

    date = request.form['value_date']
    final_date = date.split('-')

    #delete forgotten stamps
    void_forgotten_stamps()
    docgenerator.generatedoc(int(final_date[1]), int(final_date[0]))
    try:
        month = calendar.month_name[int(final_date[1])]
        year = int(final_date[0])
        filename = f'{month}_{year}_DTR_report.docx'
        return send_from_directory(directory=app.config["REPORT_PATH"], path=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route("/logout")
def logout():
    #delete forgotten stamps
    void_forgotten_stamps()
    session.clear()
    return redirect(url_for('index'))



@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')   
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


