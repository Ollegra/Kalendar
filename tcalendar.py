from tkinter import *
from tkcalendar import Calendar
import json
from datetime import datetime

year_today = datetime.now().year


def printdate():
    root.destroy()
    # sel_data = cal.get_date()
    # print(sel_data)


def d_today():
    cal.selection_set(today)
    lab.configure(text=('%s' % today.strftime('%m/%d/%Y')))


def updatelabel(e):
    # lab.config(text='Select date: ' + str(cal.selection_get()))
    sel = cal.selection_get()
    if sel is not None:
        lab.configure(text='%s' % sel.strftime('%m/%d/%Y'))


root = Tk()
root.title("Calendar")
root.iconbitmap('cal.ico')
today = datetime.now()

cal = Calendar(root, selectmode='day',
               locale='ru_RU',
               mindate=datetime(2020, 1, 1),
               maxdate=datetime(2050, 1, 1),
               showweeknumbers=False,
               showothermonthdays=False,
               background='white',
               foreground='blue',
               selectbackground='#009B76',
               selectforeground='yellow',
               normalbackground='aquamarine',
               weekendbackground='#FF6347',
               weekendforeground='yellow',
               font="Arial 10")

with open('bdays.json', encoding='UTF-8') as f:
    birthday = json.load(f)
    for key in birthday.keys():
        bd_date = str(year_today) + birthday[key]["bdasy"][4:]
        years_old = year_today - int(birthday[key]["bdasy"][:4])
        cal.calevent_create(datetime.strptime(bd_date, "%Y-%m-%d").date(),
                            birthday[key]["btext"] + ' - ' + str(years_old),
                            'reminder')

cal.tag_config('reminder', background='red', foreground='white')
cal.pack()
cal.bind('<<CalendarSelected>>', updatelabel)

lab = Label(root, text=('%s' % today.strftime('%m/%d/%Y')), fg='red')
lab.pack()

but_t = Button(root, text='Сегодня', fg='blue', command=d_today)
but_t.pack(expand=1, fill=X, padx=10, pady=5)

but = Button(root, text='Закрыть', fg='darkblue', command=printdate)
but.pack(expand=1, fill=X, padx=10, pady=5)

mw = root.geometry()
mw = mw.split('+')
mw = mw[0].split('x')
w_win = int(mw[0])
h_win = int(mw[1])
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
ws = ws // 2 - w_win // 2
hs = hs // 2 - h_win // 2
root.geometry(f'+{ws}+{hs}')

root.mainloop()
