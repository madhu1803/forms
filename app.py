from flask import Flask, render_template, request
from datetime import datetime
import forms
import mysql.connector
from mysql.connector.errors import ProgrammingError
import json
from datetime import date

app = Flask(__name__)
import copy

mydb = mysql.connector.connect(
    host="localhost", database="formdata", user="root"
)
mycursor = mydb.cursor(buffered=True)


@app.route("/", methods=["GET", "POST"])
def form():
    today = date.today().strftime('%Y-%m-%d')
    form1 = forms.Form1Form()
    form2 = forms.Form2Form()
    form3 = forms.Form3Form()
    #fetching top 3 reasons
    sql1 = "select id from complaints_table order by no_of_complaints DESC limit 3;"
    mycursor.execute(sql1)
    records = mycursor.fetchall()
    #coping dict
    data1 = copy.deepcopy(form1.data)
    data2 = copy.deepcopy(form2.data)
    data3 = copy.deepcopy(form3.data)
    #deleting csrf token
    del data1['csrf_token']
    del data2['csrf_token']
    del data3['csrf_token']
    #select query for 3 three forms
    mycursor.execute(f"SELECT {", ".join(data.keys())} FROM form1 where date='{today}'")
    raw_data1=mycursor.fetchall()
    mycursor.execute(f"SELECT {", ".join(data.keys())} FROM form2 where date='{today}'")
    raw_data2=mycursor.fetchall()
    mycursor.execute(f"SELECT {", ".join(data.keys())} FROM form3 where date='{today}'")
    raw_data3=mycursor.fetchall()
    #checking for form data
    if len(raw_data1) == 0 and len(raw_data2) == 0 and len(raw_data3) == 0 :
        form1 = forms.Form1Form()
        form2 = forms.Form2Form()
        form3 = forms.Form3Form()
    else:
        #if form data exists retrieve them
        #form1
         values1 = raw_data1[0]
         names1 = [name for name in data1.keys()]
         data_form1 = {} 
         for index in range(len(values1)):
            data_form1[names1[index]] = values1[index]
         form1 = forms.Form1Form(data=data_form1)
        #form2
         values2 = raw_data2[0]
         names2 = [name for name in data2.keys()]
         data_form2 = {} 
         for index in range(len(values2)):
            data_form2[names2[index]] = values2[index]
         form2 = forms.Form1Form(data=data_form2)
        #form3
         values3 = raw_data3[0]
         names3 = [name for name in data3.keys()]
         data_form3 = {} 
         for index in range(len(values3)):
            data_form3[names3[index]] = values3[index]
         form2 = forms.Form1Form(data=data_form3)


    if request.method == "POST":
        #coping dict
        # data1 = copy.deepcopy(form1.data)
        # data2 = copy.deepcopy(form2.data)
        # data3 = copy.deepcopy(form3.data)
    #deleting csrf token
        # del data1['csrf_token']
        # del data2['csrf_token']
        # del data3['csrf_token']
       
        # get the data and seperate as forms
        data = json.loads(request.data)
        form1_data = data["form1"]
        form2_data = data["form2"]
        form3_data = data["form3"]
        # override the forms and create a new form from data
        form1 = forms.Form1Form(data=form1_data)
        form2 = forms.Form2Form(data=form2_data)
        form3 = forms.Form3Form(data=form3_data)
        # breakpoint()
        # check valid
        if form1.validate() and form2.validate() and form3.validate():
         if len(raw_data1) == 0 and len(raw_data2) == 0 and len(raw_data3) == 0 :
            # breakpoint()
            # for form 1
            form1_data.pop("csrf_token")
            for name in form1_data.keys():
                try:
                    mycursor.execute(f"SELECT {name} from `form1`;")
                    mycursor.fetchone()
                except:
                    mycursor.execute(f"ALTER TABLE `form1` add {name} text;")
            form1_names = form1_data.keys()
            form1_values = form1_data.values()
            mycursor.execute(
                f"INSERT INTO form1 ({', '.join(form1_names)}) VALUES {tuple(form1_values)};"
            )
            # for form 2
            form2_data.pop("csrf_token")
            for name in form2_data.keys():
                try:
                    mycursor.execute(f"SELECT {name} from `form2`;")
                    mycursor.fetchone()
                except:
                    mycursor.execute(f"ALTER TABLE `form2` add {name} text;")
            form2_names = form2_data.keys()
            form2_values = form2_data.values()
            mycursor.execute(
                f"INSERT INTO form2 ({', '.join(form2_names)}) VALUES {tuple(form2_values)};"
            )
            # for form 3
            form3_data.pop("csrf_token")
            for name in form3_data.keys():
                try:
                    mycursor.execute(f"SELECT {name} from `form3`;")
                    mycursor.fetchone()
                except:
                    mycursor.execute(f"ALTER TABLE `form3` add {name} text;")
            form3_names = form3_data.keys()
            form3_values = form3_data.values()
            mycursor.execute(
                f"INSERT INTO form3 ({', '.join(form3_names)}) VALUES {tuple(form3_values)};"
            )
            # save
            mydb.commit()

            return "success"

        # form is invalid
        return "error"
        else:
            #form1
            for name, value in form1.items():
                mycursor.execute(f"UPDATE form1 SET {name}='{value}' WHERE date='{today}'")
            mydb.commit()
            #form2
            for name, value in form2.items():
                mycursor.execute(f"UPDATE form1 SET {name}='{value}' WHERE date='{today}'")
            mydb.commit()
            #form3
            for name, value in form3.items():
                mycursor.execute(f"UPDATE form1 SET {name}='{value}' WHERE date='{today}'")
            mydb.commit()

    return render_template(
        "form.html", form1=form1, form2=form2, form3=form3, records=records
    )


if __name__ == "__main__":
    app.secret_key = "secret"
    app.run(debug=True)
