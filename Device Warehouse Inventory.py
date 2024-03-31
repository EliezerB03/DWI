import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import os, sys, csv, re, subprocess, darkdetect, platform, ctypes

def DWI():
    try:
        if os.path.exists(os.path.join(os.path.dirname(__file__), "init")):
                return
        else:
            with open(os.path.join(os.path.dirname(__file__), "init"), "w") as init_file:
                init_file.write("")
                subprocess.check_call(["attrib","+H", os.path.join(os.path.dirname(__file__), "init")])

            if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data")):
                os.makedirs(os.path.join(os.path.dirname(__file__), "Data"))
            if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data/account.dat")):
                with open(os.path.join(os.path.dirname(__file__), "Data/account.dat"), "w") as accountfile:
                    accountfile.write("admin,12345\n")

            if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv")):
                with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "w") as computersfile:
                    computersfile.write("")

            if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv")):
                with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "w") as mobilesfile:
                    mobilesfile.write("")

            if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv")):
                with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "w") as gadgetsfile:
                    gadgetsfile.write("")

        # ============================================== GLOBAL FUNCTIONS ============================================== #
        # ========== To MENUBAR/BUTTONS ========== #
        def rememberaccount():
            tk.messagebox.showinfo("Your Account is:", "Username: admin\nPassword: 12345")
        def signout():
            mainwindow.destroy()
            login_window()
        def about():
            tk.messagebox.showinfo("About the Program", "Device Warehouse Inventory\nVersion: 1.1.2\n\nThis program is to Add, Edit or Delete Products information in the Inventory from the Local DataBase.\n\nDeveloped By Eliezer Brito\n© Elie-Dev (2023)\nAll rights reserved")

        def exportfile():
            with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "r", newline="") as computersfile:
                computersreader = csv.reader(computersfile)
                computersdata = list(computersreader)
            with open(os.path.join(os.path.dirname(__file__), 'Exported/Computers.txt'), 'w') as export_com:
                export_com.write('ID            Brand                 Model                                  Color                  Manufacturing Date\n-------------------------------------------------------------------------------------------------------------------------\n')
                for row in computersdata:
                    export_com.write('{:<10}    {:<15}       {:<28}           {:<18}     {:<20}\n'.format(row[0], row[1], row[2], row[3], row[4]))
            
            with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "r", newline="") as mobilesfile:
                mobilesreader = csv.reader(mobilesfile)
                mobilesdata = list(mobilesreader)
            with open(os.path.join(os.path.dirname(__file__), 'Exported/Mobiles.txt'), 'w') as export_mob:
                export_mob.write('ID            Brand                 Model                                  Color                  Manufacturing Date\n-------------------------------------------------------------------------------------------------------------------------\n')
                for row in mobilesdata:
                    export_mob.write('{:<10}    {:<15}       {:<28}           {:<18}     {:<20}\n'.format(row[0], row[1], row[2], row[3], row[4]))

            with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "r", newline="") as gadgetsfile:
                gadgetsreader = csv.reader(gadgetsfile)
                gadgetsdata = list(gadgetsreader)
            with open(os.path.join(os.path.dirname(__file__), 'Exported/Gadgets.txt'), 'w') as export_gad:
                export_gad.write('ID            Brand                 Model                                  Color                  Manufacturing Date\n-------------------------------------------------------------------------------------------------------------------------\n')
                for row in gadgetsdata:
                    export_gad.write('{:<10}    {:<15}       {:<28}           {:<18}     {:<20}\n'.format(row[0], row[1], row[2], row[3], row[4]))
            tk.messagebox.showinfo("Exporting content to Files...", "The contents of the database have been EXPORTED to documents successfully!")
                                    
        def changelog():
            tk.messagebox.showinfo("Changelog of this version", "*****                               VERSION 1.1.2                               *****\n\n- Changed DataBase Engine from mySQL > CSV File.\n- Added Show Exported Folder Button in MainWindow.\n- Improved Minor Logic in Some Program Fuctions.\n- Bugs Fixes.")
        def help_main():
            tk.messagebox.showinfo("How can use This Program?", "To start, select one of the available options at the top.")
        def help_addmode():
            tk.messagebox.showinfo("How can use Add Mode", "To start, select the type of devices, then fill in the text fields and press the 'Add to DB' button.")
        def help_editmode():
            tk.messagebox.showinfo("How can use Edit Mode", "To start select the type of devices, then type the correct ID, then fill in all the other text fields and press the 'Edit' button.")
        def help_deletemode():
            tk.messagebox.showinfo("How can use Delete Mode", "To start select the type of devices, then type the correct ID and press the 'Delete' button.")

        # ============================================== LOGIN WINDOW ============================================== #
        # ========== To MENUBAR/BUTTONS ========== #
        def login_help():
            tk.messagebox.showinfo("How can I Sign-in?", "Enter your username and password, if the data is correct the application will start, otherwise you will receive an error message.\n\nIf you still have problems logging in, please notify the developer.")

        # ========================================================================================================= #
        def close_login():
            os.remove(os.path.join(os.path.dirname(__file__), "init"))
            sys.exit(0)
        # ============================================== MAIN WINDOW ============================================== #
        def showexportedfolder():
            os.startfile(os.path.join(os.path.dirname(__file__), "Exported"))
        def main_window():
            def validate_value_id(text):
                    pattern = re.compile(r"^[a-zA-Z0-9-]+$")
                    if pattern.match(text) is not None:
                        return True and len(text) <= 6
                    elif text == "":
                        return True and len(text) <= 6
                    else:
                        return False and len(text) <= 6
            def validate_value_brand(text):
                pattern = re.compile(r"^[a-zA-Z0-9-_ ]+$")
                if pattern.match(text) is not None:
                    return True and len(text) <= 15
                elif text == "":
                    return True and len(text) <= 15
                else:
                    return False and len(text) <= 15
            def validate_value_model(text):
                pattern = re.compile(r"^[a-zA-Z0-9-_ ]+$")
                if pattern.match(text) is not None:
                    return True and len(text) <= 28
                elif text == "":
                    return True and len(text) <= 28 
                else:
                    return False and len(text) <= 28
            def validate_value_color(text):
                pattern = re.compile(r"^[a-zA-Z ]+$")
                if pattern.match(text) is not None:
                    return True and len(text) <= 18
                elif text == "":
                    return True and len(text) <= 18
                else:
                    return False and len(text) <= 18
            def validate_value_date(text):
                pattern = re.compile(r"^[0-9-/]+$")
                if pattern.match(text) is not None:
                    return True and len(text) <= 15
                elif text == "":
                    return True and len(text) <= 15
                else:
                    return False and len(text) <= 15
                
            global username_entry, password_entry, mainwindow
            try:
                with open(os.path.join(os.path.dirname(__file__), "Data/account.dat"), "r") as accountfile:
                        accountreader = csv.reader(accountfile, delimiter=",")
                        accountdata = list(accountreader)
                username = username_entry.get()
                password = password_entry.get()
                if accountdata[0][0] == username and accountdata[0][1] == password:
                    loginwindow.destroy()
                    # ============================================== MAIN WINDOW FUNCTIONS ============================================== #        
                    def labels_mw():
                        global modeslb, idlb, brandlb, modellb, colorlb, datelb, search_exlb
                        modeslb = tk.Label(mainwindow, text="View Mode", font="SegoeUIVariable, 17")
                        modeslb.place(x=75, y=65)
                        search_exlb = tk.Label(mainwindow, text="Example: CM-001", font="SegoeUIVariable, 10")
                        search_exlb.place(x=450, y=393)
                        idlb = tk.Label(mainwindow, text="ID", font="SegoeUIVariable, 11", state="disabled", fg="SystemButtonText")
                        idlb.place(x=220, y=125)
                        brandlb = tk.Label(mainwindow, text="Brand", font="SegoeUIVariable, 11", state="disabled")
                        brandlb.place(x=220, y=165)
                        modellb = tk.Label(mainwindow, text="Model", font="SegoeUIVariable, 11", state="disabled")
                        modellb.place(x=220, y=205)
                        colorlb = tk.Label(mainwindow, text="Color", font="SegoeUIVariable, 11", state="disabled")
                        colorlb.place(x=220, y=245)
                        datelb = tk.Label(mainwindow, text="Date", font="SegoeUIVariable, 11", state="disabled")
                        datelb.place(x=220, y=285)        

                    def entrys_mw():
                        global id_entry, brand_entry, model_entry, color_entry, date_entry, search_entry
                        id_entry =tk.Entry(mainwindow, borderwidth=4, width=41, state="disabled", cursor= "arrow", validate="key", validatecommand=(mainwindow.register(validate_value_id), "%P"))
                        id_entry.place(x=277, y=125)
                        brand_entry =tk.Entry(mainwindow, borderwidth=4, width=41, state="disabled", cursor= "arrow", validate="key", validatecommand=(mainwindow.register(validate_value_brand), "%P"))
                        brand_entry.place(x=277, y=165)
                        model_entry =tk.Entry(mainwindow, borderwidth=4, width=41, state="disabled", cursor= "arrow", validate="key", validatecommand=(mainwindow.register(validate_value_model), "%P"))
                        model_entry.place(x=277, y=205)
                        color_entry =tk.Entry(mainwindow, borderwidth=4, width=41, state="disabled", cursor= "arrow", validate="key", validatecommand=(mainwindow.register(validate_value_color), "%P"))
                        color_entry.place(x=277, y=245)
                        date_entry =tk.Entry(mainwindow, borderwidth=4, width=41, state="disabled", cursor= "arrow", validate="key", validatecommand=(mainwindow.register(validate_value_date), "%P"))
                        date_entry.place(x=277, y=285)
                        search_entry = tk.Entry(mainwindow, borderwidth=4, width=28)
                        search_entry.place(x=450, y=363)
                        search_entry.config(highlightcolor="#A3A3A3", highlightbackground="#A3A3A3", highlightthickness=2)
                        search_entry.insert(0, "Search Inventory by ID...")
                        search_entry.bind("<FocusIn>", lambda event: search_entry.delete(0, tk.END) if search_entry.get() == "Search Inventory by ID..." else search_entry.insert(0, ""))
                        search_entry.bind("<FocusOut>", lambda event: search_entry.insert(0, "Search Inventory by ID...") if search_entry.get() == "" else search_entry.insert(0, ""))

                    def clear_mw():
                        id_entry.delete(0, tk.END)
                        brand_entry.delete(0, tk.END)
                        model_entry.delete(0, tk.END)
                        color_entry.delete(0, tk.END)
                        date_entry.delete(0, tk.END)

                    def table_mw():
                        global db_table, table_scrollbar
                        db_table = ttk.Treeview(mainwindow, selectmode="browse")
                        db_table.place(x=20, y=420)
                        db_table['show']='headings'
                        db_table["columns"]=("id", "brand", "model", "color", "date")
                        
                        db_table.column("id", width=70, minwidth=70, anchor=tk.SW)
                        db_table.column("brand", width=150, minwidth=150, anchor=tk.SW)
                        db_table.column("model", width=230, minwidth=230, anchor=tk.SW)
                        db_table.column("color", width=100, minwidth=100, anchor=tk.SW)
                        db_table.column("date", width=150, minwidth=150, anchor=tk.SW)

                        db_table.heading("id", text= "ID", anchor=tk.SW)
                        db_table.heading("brand", text= "Brand", anchor=tk.SW)
                        db_table.heading("model", text= "Model", anchor=tk.SW)
                        db_table.heading("color", text= "Color", anchor=tk.SW)
                        db_table.heading("date", text= "Manufacturing Date", anchor=tk.SW)
                    
                        table_scrollbar = ttk.Scrollbar(mainwindow, orient="vertical", command=db_table.yview)
                        db_table.configure(yscrollcommand=table_scrollbar.set)

                    def sl_group_mw():
                        global sl_computersrb, sl_mobilesrb, sl_gadgetsrb
                        sl_group = tk.IntVar()
                        sl_computersrb= tk.Radiobutton(mainwindow, text="Computers", value="sl-computers", variable=sl_group, font="15", padx="5", pady="10", state="disabled")
                        sl_computersrb.place(x=277, y=70)
                        sl_computersrb.config(indicatoron=False)
                        sl_mobilesrb= tk.Radiobutton(mainwindow, text="Mobiles", value="sl-mobiles", variable=sl_group, font="15", padx="16", pady="10", state="disabled")
                        sl_mobilesrb.place(x=377, y=70)
                        sl_mobilesrb.config(indicatoron=False)
                        sl_gadgetsrb= tk.Radiobutton(mainwindow, text="Gadgets", value="sl-gadgets", variable=sl_group, font="15", padx="14", pady="10", state="disabled")
                        sl_gadgetsrb.place(x=478, y=70)
                        sl_gadgetsrb.config(indicatoron=False)

                    def buttons_mw():
                        global addbtn, editbtn, deletebtn, clearbtn, refleshbtn, searchbtn, helpmode_btn
                        addbtn = tk.Button(mainwindow, text="   Add to DB  ", font="15", padx=50, width=3, state="disabled")
                        addbtn.place(x=585, y=124)
                        editbtn = tk.Button(mainwindow, text="   Edit             ", font="15", padx=50, width=3, state="disabled")
                        editbtn.place(x=585, y=164)
                        deletebtn = tk.Button(mainwindow, text="   Delete         ", font="15", padx=50, width=3, state="disabled")
                        deletebtn.place(x=585, y=204)
                        clearbtn = tk.Button(mainwindow, text="   Clear Texts  ", font="15", padx=50, width=3, state="disabled")
                        clearbtn.place(x=585, y=244)
                        refleshbtn = tk.Button(mainwindow, text="Reflesh", font="15", cursor= "hand2", padx=15, pady=10, width=3, command=reflesh_tb_com)
                        refleshbtn.place(x=20, y=363)
                        searchbtn = tk.Button(mainwindow, text="Search", font="15", cursor= "hand2", padx=12, pady=10, width=3, command=s_byid_com)
                        searchbtn.place(x=663, y=362)
                        helpmode_btn = tk.Button(mainwindow, text="Help", font="15", padx=12, pady=10, fg="white", activeforeground="white", bg="#0055FF", activebackground= "#0078FF", cursor= "hand2", width=3)
                        helpmode_btn.place_forget()
                    
                    def reflesh_tb_com():
                        db_table.delete(*db_table.get_children())
                        with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "r") as refleshfile:
                            data = refleshfile.readlines()
                        if len(data) > 10:
                            table_scrollbar.place(x=706, y=420, height=219, width=17)
                        else:
                            table_scrollbar.place_forget()
                        for row in data:
                            id, brand, model, color, date = row.strip().split(",")
                            db_table.insert("", "end", values=(id, brand, model, color, date))

                    def reflesh_tb_mob():
                        db_table.delete(*db_table.get_children())
                        with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "r") as refleshfile:
                            data = refleshfile.readlines()
                        if len(data) > 10:
                            table_scrollbar.place(x=706, y=420, height=219, width=17)
                        else:
                            table_scrollbar.place_forget()
                        for row in data:
                            id, brand, model, color, date = row.strip().split(",")
                            db_table.insert("", "end", values=(id, brand, model, color, date))
                    
                    def reflesh_tb_gad():
                        db_table.delete(*db_table.get_children())
                        with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "r") as refleshfile:
                            data = refleshfile.readlines()
                        if len(data) > 10:
                            table_scrollbar.place(x=706, y=420, height=219, width=17)
                        else:
                            table_scrollbar.place_forget()
                        for row in data:
                            id, brand, model, color, date = row.strip().split(",")
                            db_table.insert("", "end", values=(id, brand, model, color, date))
                    
                    def optionselected_vw(action):
                        rb_seleted = action.widget
                        if rb_seleted.cget("value") == "vw-computers":
                            vw_computersrb.select()
                            db_table.destroy()
                            table_mw()
                            refleshbtn.config(command=reflesh_tb_com)
                            searchbtn.config(command=s_byid_com)
                            search_exlb.config(text="Example: CM-001")
                        elif rb_seleted.cget("value") == "vw-mobiles":
                            vw_mobilesrb.select()
                            db_table.destroy()
                            table_mw()                
                            refleshbtn.config(command=reflesh_tb_mob)
                            searchbtn.config(command=s_byid_mob)
                            search_exlb.config(text="Example: MB-001")
                        elif rb_seleted.cget("value") == "vw-gadgets":
                            vw_gadgetsrb.select()
                            db_table.destroy()
                            table_mw()                
                            refleshbtn.config(command=reflesh_tb_gad)
                            searchbtn.config(command=s_byid_gad)
                            search_exlb.config(text="Example: GD-001")

                    def s_byid_com():
                        computersfile = open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "r")
                        computersreader = csv.reader(computersfile)
                        computersdata = list(computersreader)
                        db_table.delete(*db_table.get_children())
                        id_get = search_entry.get()
                        idget = id_get.upper()
                        if any(idget in row[0] for row in computersdata):
                            filtered_data = [row for row in computersdata if idget in row[0].upper()]
                            db_table.delete(*db_table.get_children())
                            if len(filtered_data) > 10:
                                table_scrollbar.place(x=706, y=420, height=219, width=17)
                            else:
                                table_scrollbar.place_forget()
                            for row in filtered_data:
                                db_table.insert('', 'end', values=row)
                    
                    def s_byid_mob():
                        mobilesfile = open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "r")
                        mobilesreader = csv.reader(mobilesfile)
                        mobilesdata = list(mobilesreader)
                        db_table.delete(*db_table.get_children())
                        id_get = search_entry.get()
                        idget = id_get.upper()
                        if any(idget in row[0] for row in mobilesdata):
                            filtered_data = [row for row in mobilesdata if idget in row[0].upper()]
                            db_table.delete(*db_table.get_children())
                            if len(filtered_data) > 10:
                                table_scrollbar.place(x=706, y=420, height=219, width=17)
                            else:
                                table_scrollbar.place_forget()
                            for row in filtered_data:
                                db_table.insert('', 'end', values=row)

                    def s_byid_gad():
                        gadgetsfile = open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "r")
                        gadgetsreader = csv.reader(gadgetsfile)
                        gadgetsdata = list(gadgetsreader)
                        db_table.delete(*db_table.get_children())
                        id_get = search_entry.get()
                        idget = id_get.upper()
                        if any(idget in row[0] for row in gadgetsdata):
                            filtered_data = [row for row in gadgetsdata if idget in row[0].upper()]
                            db_table.delete(*db_table.get_children())
                            if len(filtered_data) > 10:
                                table_scrollbar.place(x=706, y=420, height=219, width=17)
                            else:
                                table_scrollbar.place_forget()
                            for row in filtered_data:
                                db_table.insert('', 'end', values=row)

                    def optionselected_mode(action):
                        rb_seleted = action.widget
                        if rb_seleted.cget("value") == "mw-view_mode":
                            viewrb.select()
                            sl_computersrb.deselect()
                            sl_mobilesrb.deselect()
                            sl_gadgetsrb.deselect()
                            sl_computersrb.unbind("<ButtonRelease-1>")
                            sl_mobilesrb.unbind("<ButtonRelease-1>")
                            sl_gadgetsrb.unbind("<ButtonRelease-1>")
                            clear_mw()
                            addbtn.config(state="disabled", background="SystemButtonFace", fg="SystemButtonText", cursor="arrow")
                            editbtn.config(state="disabled", background="SystemButtonFace", fg="SystemButtonText", cursor="arrow")
                            deletebtn.config(state="disabled", background="SystemButtonFace", fg="SystemButtonText", cursor="arrow")
                            clearbtn.config(state="disabled", background="SystemButtonFace", fg="SystemButtonText", cursor="arrow")
                            helpmode_btn.place_forget()
                            addbtn.place(x=585, y=124)
                            editbtn.place(x=585, y=164)
                            deletebtn.place(x=585, y=204)
                            clearbtn.place(x=585, y=244)

                            idlb.place(x=220, y=125)
                            brandlb.place(x=220, y=165)
                            modellb.place(x=220, y=205)
                            colorlb.place(x=220, y=245)
                            datelb.place(x=220, y=285) 
                            id_entry.place(x=277, y=125)
                            brand_entry.place(x=277, y=165)
                            model_entry.place(x=277, y=205)
                            color_entry.place(x=277, y=245)
                            date_entry.place(x=277, y=285)

                            modeslb.config(text="View Mode", fg="SystemButtonText")
                            modeslb.place(x=75, y=65)
                            idlb.config(state="disabled", fg="SystemButtonText")
                            brandlb.config(state="disabled")
                            modellb.config(state="disabled")
                            colorlb.config(state="disabled")
                            datelb.config(state="disabled")
                            id_entry.config(state="disabled", cursor="arrow", highlightthickness=0)        
                            brand_entry.config(state="disabled", cursor="arrow", highlightthickness=0)
                            model_entry.config(state="disabled", cursor="arrow", highlightthickness=0)
                            color_entry.config(state="disabled", cursor="arrow", highlightthickness=0)
                            date_entry.config(state="disabled", cursor="arrow", highlightthickness=0)

                            sl_computersrb.config(state="disabled", cursor="arrow", activebackground="SystemButtonFace", selectcolor="SystemButtonFace")
                            sl_mobilesrb.config(state="disabled", cursor="arrow", activebackground="SystemButtonFace", selectcolor="SystemButtonFace")
                            sl_gadgetsrb.config(state="disabled", cursor="arrow", activebackground="SystemButtonFace", selectcolor="SystemButtonFace")
                
                        elif rb_seleted.cget("value") == "mw-add_mode":
                            addrb.select()
                            def optionselected_add(action):
                                rb_seleted = action.widget
                                if rb_seleted.cget("value") == "sl-computers":
                                    sl_computersrb.select()
                                    addbtn.config(command=add_com)
                                elif rb_seleted.cget("value") == "sl-mobiles":
                                    sl_mobilesrb.select()
                                    addbtn.config(command=add_mob)
                                elif rb_seleted.cget("value") == "sl-gadgets":
                                    sl_gadgetsrb.select()
                                    addbtn.config(command=add_gad)
                            sl_computersrb.bind("<ButtonRelease-1>", optionselected_add)
                            sl_mobilesrb.bind("<ButtonRelease-1>", optionselected_add)
                            sl_gadgetsrb.bind("<ButtonRelease-1>", optionselected_add)
                            addbtn.place(x=585, y=124)
                            editbtn.place(x=585, y=164)
                            deletebtn.place(x=585, y=204)
                            clearbtn.place(x=585, y=244)
                            helpmode_btn.config(command=help_addmode)    
                            helpmode_btn.place(x=623, y=69)
                            addbtn.place_forget()
                            editbtn.place_forget()
                            deletebtn.place_forget()
                            clearbtn.place_forget()
                            addbtn.place(x=585, y=124)
                            clearbtn.place(x=585, y=164)
                            addbtn.config(state="normal", fg="white", activeforeground="white", bg="#007A05", activebackground= "#00A007", cursor="hand2", command=add_com)
                            clearbtn.config(state="normal", cursor="hand2", command=clear_mw)

                            modeslb.config(text="Add Mode", fg="#007A05")
                            modeslb.place(x=80, y=65)
                            idlb.place(x=220, y=125)
                            brandlb.place(x=220, y=165)
                            modellb.place(x=220, y=205)
                            colorlb.place(x=220, y=245)
                            datelb.place(x=220, y=285) 
                            id_entry.place(x=277, y=125)
                            brand_entry.place(x=277, y=165)
                            model_entry.place(x=277, y=205)
                            color_entry.place(x=277, y=245)
                            date_entry.place(x=277, y=285)
                                        
                            idlb.config(state="normal", fg="#00A007")
                            brandlb.config(state="normal")
                            modellb.config(state="normal")
                            colorlb.config(state="normal")
                            datelb.config(state="normal")
                            id_entry.config(state="normal", cursor= "xterm", highlightcolor="#00A007", highlightbackground="#00A007", highlightthickness=2)            
                            brand_entry.config(state="normal", cursor= "xterm", highlightcolor="#A3A3A3", highlightbackground="#A3A3A3", highlightthickness=2) 
                            model_entry.config(state="normal", cursor= "xterm", highlightcolor="#A3A3A3", highlightbackground="#A3A3A3", highlightthickness=2) 
                            color_entry.config(state="normal", cursor= "xterm", highlightcolor="#A3A3A3", highlightbackground="#A3A3A3", highlightthickness=2) 
                            date_entry.config(state="normal", cursor= "xterm", highlightcolor="#A3A3A3", highlightbackground="#A3A3A3", highlightthickness=2) 

                            sl_computersrb.config(state="normal", cursor="hand2")
                            sl_computersrb.select()
                            sl_mobilesrb.config(state="normal", cursor="hand2")
                            sl_gadgetsrb.config(state="normal", cursor="hand2")

                        elif rb_seleted.cget("value") == "mw-edit_mode":
                            def optionselected_edit(action):
                                rb_seleted = action.widget
                                if rb_seleted.cget("value") == "sl-computers":
                                    sl_computersrb.select()
                                    editbtn.config(command=edit_com)
                                elif rb_seleted.cget("value") == "sl-mobiles":
                                    sl_mobilesrb.select()
                                    editbtn.config(command=edit_mob)
                                elif rb_seleted.cget("value") == "sl-gadgets":
                                    sl_gadgetsrb.select()
                                    editbtn.config(command=edit_gad)
                            sl_computersrb.bind("<ButtonRelease-1>", optionselected_edit)
                            sl_mobilesrb.bind("<ButtonRelease-1>", optionselected_edit)
                            sl_gadgetsrb.bind("<ButtonRelease-1>", optionselected_edit)
                            editrb.select()
                            addbtn.place(x=585, y=124)
                            editbtn.place(x=585, y=164)
                            deletebtn.place(x=585, y=204)
                            clearbtn.place(x=585, y=244)
                            helpmode_btn.config(command=help_editmode)    
                            helpmode_btn.place(x=623, y=69)    
                            addbtn.place_forget()
                            editbtn.place_forget()
                            deletebtn.place_forget()
                            clearbtn.place_forget()
                            editbtn.place(x=585, y=124)
                            clearbtn.place(x=585, y=164)
                            editbtn.config(state="normal", fg="white", activeforeground="white", bg="#0055FF", activebackground= "#0078FF", cursor="hand2", command=edit_com)
                            clearbtn.config(state="normal", cursor="hand2", command=clear_mw)
                            
                            modeslb.config(text="Edit Mode", fg="#0055FF")
                            modeslb.place(x=80, y=65)
                            idlb.place(x=220, y=125)
                            brandlb.place(x=220, y=165)
                            modellb.place(x=220, y=205)
                            colorlb.place(x=220, y=245)
                            datelb.place(x=220, y=285) 
                            id_entry.place(x=277, y=125)
                            brand_entry.place(x=277, y=165)
                            model_entry.place(x=277, y=205)
                            color_entry.place(x=277, y=245)
                            date_entry.place(x=277, y=285)

                            idlb.config(state="normal", fg= "#0078FF")
                            brandlb.config(state="normal")
                            modellb.config(state="normal")
                            colorlb.config(state="normal")
                            datelb.config(state="normal")
                            id_entry.config(state="normal", cursor= "xterm", highlightcolor="#0078FF", highlightbackground="#0078FF", highlightthickness=2)
                            brand_entry.config(state="normal", cursor= "xterm", highlightcolor="#A3A3A3", highlightbackground="#A3A3A3", highlightthickness=2) 
                            model_entry.config(state="normal", cursor= "xterm", highlightcolor="#A3A3A3", highlightbackground="#A3A3A3", highlightthickness=2) 
                            color_entry.config(state="normal", cursor= "xterm", highlightcolor="#A3A3A3", highlightbackground="#A3A3A3", highlightthickness=2) 
                            date_entry.config(state="normal", cursor= "xterm", highlightcolor="#A3A3A3", highlightbackground="#A3A3A3", highlightthickness=2) 

                            sl_computersrb.config(state="normal", cursor="hand2")
                            sl_computersrb.select()
                            sl_mobilesrb.config(state="normal", cursor="hand2")
                            sl_gadgetsrb.config(state="normal", cursor="hand2")

                        elif rb_seleted.cget("value") == "mw-delete_mode":
                            def optionselected_del(action):
                                rb_seleted = action.widget
                                if rb_seleted.cget("value") == "sl-computers":
                                    sl_computersrb.select()
                                    deletebtn.config(command=del_com)
                                elif rb_seleted.cget("value") == "sl-mobiles":
                                    sl_mobilesrb.select()
                                    deletebtn.config(command=del_mob)
                                elif rb_seleted.cget("value") == "sl-gadgets":
                                    sl_gadgetsrb.select()
                                    deletebtn.config(command=del_gad)                
                            sl_computersrb.bind("<ButtonRelease-1>", optionselected_del)
                            sl_mobilesrb.bind("<ButtonRelease-1>", optionselected_del)
                            sl_gadgetsrb.bind("<ButtonRelease-1>", optionselected_del)
                            deleterb.select()
                            addbtn.place(x=585, y=124)
                            editbtn.place(x=585, y=164)
                            deletebtn.place(x=585, y=204)
                            clearbtn.place(x=585, y=244) 
                            helpmode_btn.config(command=help_deletemode)                             
                            helpmode_btn.place(x=623, y=69)
                            addbtn.place_forget()
                            editbtn.place_forget()
                            deletebtn.place_forget()
                            clearbtn.place_forget()
                            deletebtn.place(x=585, y=124)
                            clearbtn.place(x=585, y=164)
                            deletebtn.config(state="normal", fg="white", activeforeground="white", bg="#EB0000", activebackground= "#FE2727", cursor="hand2", command=del_com)
                            clearbtn.config(state="normal", cursor="hand2", command=clear_mw)
                            
                            modeslb.config(text="Delete Mode", fg="#EB0000")
                            modeslb.place(x=67, y=65)
                            brandlb.place_forget()
                            modellb.place_forget()
                            colorlb.place_forget()
                            datelb.place_forget()
                            brand_entry.place_forget()
                            model_entry.place_forget()
                            color_entry.place_forget()
                            date_entry.place_forget()
                            idlb.config(state="normal", fg="#FE2727")
                            id_entry.config(state="normal", cursor= "xterm", highlightcolor="#FE2727", highlightbackground="#FE2727", highlightthickness=2)
                            idlb.place(x=220, y=125)
                            id_entry.place(x=277, y=125)

                            sl_computersrb.config(state="normal", cursor="hand2")
                            sl_computersrb.select()
                            sl_mobilesrb.config(state="normal", cursor="hand2")
                            sl_gadgetsrb.config(state="normal", cursor="hand2")
                    
                    def add_com():
                        id_get = id_entry.get()
                        brand_get = brand_entry.get()
                        model_get = model_entry.get()
                        color_get = color_entry.get()
                        date_get = date_entry.get()
                        id_upper = id_get.upper()
                        brand_upper = brand_get.upper()
                        model_upper = model_get.upper()
                        color_upper = color_get.upper()
                        date_upper = date_get.upper()       
                        if "" in id_upper and brand_upper and model_upper and color_upper and date_upper: 
                            with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "a", newline="") as computersfile:
                                computerswriter = csv.writer(computersfile)
                                computerswriter.writerow([id_upper, brand_upper, model_upper, color_upper, date_upper])
                                computersfile.seek(0, 2)
                            clear_mw()
                            tk.messagebox.showinfo(title="Saving to Inventory...", message="Your Product has been ADDED to Inventory!")
                        else:
                            tk.messagebox.showwarning(title="Saving to Inventory...", message="You can't leave EMPTY Text Fields!")

                    def add_mob():
                        id_get = id_entry.get()
                        brand_get = brand_entry.get()
                        model_get = model_entry.get()
                        color_get = color_entry.get()
                        date_get = date_entry.get()
                        id_upper = id_get.upper()
                        brand_upper = brand_get.upper()
                        model_upper = model_get.upper()
                        color_upper = color_get.upper()
                        date_upper = date_get.upper()
                        if "" in id_upper and brand_upper and model_upper and color_upper and date_upper: 
                            with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "a", newline="") as mobilesfile:
                                mobileswriter = csv.writer(mobilesfile)
                                mobileswriter.writerow([id_upper, brand_upper, model_upper, color_upper, date_upper])
                                mobilesfile.seek(0, 2)
                            clear_mw()
                            tk.messagebox.showinfo(title="Saving to Inventory...", message="Your Product has been ADDED to Inventory!")
                        else:
                            tk.messagebox.showwarning(title="Saving to Inventory...", message="You can't leave EMPTY Text Fields!")

                    def add_gad():
                        id_get = id_entry.get()
                        brand_get = brand_entry.get()
                        model_get = model_entry.get()
                        color_get = color_entry.get()
                        date_get = date_entry.get()
                        id_upper = id_get.upper()
                        brand_upper = brand_get.upper()
                        model_upper = model_get.upper()
                        color_upper = color_get.upper()
                        date_upper = date_get.upper()
                        if "" in id_upper and brand_upper and model_upper and color_upper and date_upper: 
                            with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "a", newline="") as gadgetsfile:
                                gadgetswriter = csv.writer(gadgetsfile)
                                gadgetswriter.writerow([id_upper, brand_upper, model_upper, color_upper, date_upper])
                                gadgetsfile.seek(0, 2)
                            clear_mw()
                            tk.messagebox.showinfo(title="Saving to Inventory...", message="Your Product has been ADDED to Inventory!")
                        else:
                            tk.messagebox.showwarning(title="Saving to Inventory...", message="You can't leave EMPTY Text Fields!")

                    def edit_com():
                        id_get = id_entry.get()
                        brand_get = brand_entry.get()
                        model_get = model_entry.get()
                        color_get = color_entry.get()
                        date_get = date_entry.get()
                        id_upper = id_get.upper()
                        brand_upper = brand_get.upper()
                        model_upper = model_get.upper()
                        color_upper = color_get.upper()
                        date_upper = date_get.upper() 
                        with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "r", newline="") as computersfile:
                            computersreader = csv.reader(computersfile)
                            computersdata = list(computersreader)
                        ids = set([row[0].upper() for row in computersdata])      
                        if id_upper == "" or brand_upper == "" or model_upper == "" or color_upper == "" or date_upper == "":
                            tk.messagebox.showwarning(title="Editing in the Inventory...", message="You can't leave EMPTY Text Fields!")
                        else:
                            if id_upper in ids:     
                                with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "r", newline="") as computersfile:
                                    computersreader = csv.reader(computersfile)
                                    computersdata = list(computersreader)
                                for row in computersdata:
                                    if row[0] == id_upper:
                                        row[1] = brand_upper
                                        row[2] = model_upper
                                        row[3] = color_upper
                                        row[4] = date_upper
                                        break 
                                with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "w", newline="") as computersfile:
                                    computerswriter = csv.writer(computersfile)
                                    computerswriter.writerows(computersdata)
                                    computersfile.seek(0, 2)
                                clear_mw()
                                tk.messagebox.showinfo(title="Editing in the Inventory...", message="Your Product has been EDITED in the Inventory!")
                            elif not id_upper in ids:
                                tk.messagebox.showwarning(title="Editing in the Inventory...", message="This ID does not EXIST!")              
                    
                    def edit_mob():
                        id_get = id_entry.get()
                        brand_get = brand_entry.get()
                        model_get = model_entry.get()
                        color_get = color_entry.get()
                        date_get = date_entry.get()
                        id_upper = id_get.upper()
                        brand_upper = brand_get.upper()
                        model_upper = model_get.upper()
                        color_upper = color_get.upper()
                        date_upper = date_get.upper()       
                        with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "r", newline="") as mobilesfile:
                            mobilesreader = csv.reader(mobilesfile)
                            mobilesdata = list(mobilesreader)
                        ids = set([row[0].upper() for row in mobilesdata])      
                        if id_upper == "" or brand_upper == "" or model_upper == "" or color_upper == "" or date_upper == "":
                            tk.messagebox.showwarning(title="Editing in the Inventory...", message="You can't leave EMPTY Text Fields!")
                        else:
                            if id_upper in ids:     
                                with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "r", newline="") as mobilesfile:
                                    mobilesreader = csv.reader(mobilesfile)
                                    mobilesdata = list(mobilesreader)
                                for row in mobilesdata:
                                    if row[0] == id_upper:
                                        row[1] = brand_upper
                                        row[2] = model_upper
                                        row[3] = color_upper
                                        row[4] = date_upper
                                        break 
                                with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "w", newline="") as mobilesfile:
                                    mobileswriter = csv.writer(mobilesfile)
                                    mobileswriter.writerows(mobilesdata)
                                    mobilesfile.seek(0, 2)
                                clear_mw()
                                tk.messagebox.showinfo(title="Editing in the Inventory...", message="Your Product has been EDITED in the Inventory!")
                            elif not id_upper in ids:
                                tk.messagebox.showwarning(title="Editing in the Inventory...", message="This ID does not EXIST!")              
                    
                    def edit_gad():
                        id_get = id_entry.get()
                        brand_get = brand_entry.get()
                        model_get = model_entry.get()
                        color_get = color_entry.get()
                        date_get = date_entry.get()
                        id_upper = id_get.upper()
                        brand_upper = brand_get.upper()
                        model_upper = model_get.upper()
                        color_upper = color_get.upper()
                        date_upper = date_get.upper()       
                        with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "r", newline="") as gadgetsfile:
                            gadgetsreader = csv.reader(gadgetsfile)
                            gadgetsdata = list(gadgetsreader)
                        ids = set([row[0].upper() for row in gadgetsdata])      
                        if id_upper == "" or brand_upper == "" or model_upper == "" or color_upper == "" or date_upper == "":
                            tk.messagebox.showwarning(title="Editing in the Inventory...", message="You can't leave EMPTY Text Fields!")
                        else:
                            if id_upper in ids:     
                                with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "r", newline="") as gadgetsfile:
                                    gadgetsreader = csv.reader(gadgetsfile)
                                    gadgetsdata = list(gadgetsreader)
                                for row in gadgetsdata:
                                    if row[0] == id_upper:
                                        row[1] = brand_upper
                                        row[2] = model_upper
                                        row[3] = color_upper
                                        row[4] = date_upper
                                        break 
                                with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "w", newline="") as gadgetsfile:
                                    gadgetswriter = csv.writer(gadgetsfile)
                                    gadgetswriter.writerows(gadgetsdata)
                                    gadgetsfile.seek(0, 2)
                                clear_mw()
                                tk.messagebox.showinfo(title="Editing in the Inventory...", message="Your Product has been EDITED in the Inventory!")
                            elif not id_upper in ids:
                                tk.messagebox.showwarning(title="Editing in the Inventory...", message="This ID does not EXIST!")              
                    
                    def del_com():
                        id_get = id_entry.get()
                        id_upper = id_get.upper()
                        with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "r", newline="") as computersfile:
                            computersreader = csv.reader(computersfile)
                            computersdata = list(computersreader)
                        ids = set([row[0].upper() for row in computersdata])
                        if id_upper == "":
                            tk.messagebox.showwarning(title="Deleting in the Inventory...", message="You can't leave EMPTY Text Fields!")
                        else:
                            if id_upper in ids:  
                                for row in computersdata:
                                    if row[0].upper() == id_upper:
                                        computersdata.remove(row)
                                with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "w", newline="") as computersfile:
                                    computerswriter = csv.writer(computersfile)
                                    computerswriter.writerows(computersdata)
                                    computersfile.seek(0, 2)
                                clear_mw()
                                tk.messagebox.showinfo(title="Deleting in the Inventory...", message="Your Product has been DELETED in the Inventory!")
                            if not id_upper in ids: 
                                tk.messagebox.showwarning(title="Delete in the Inventory...", message="This ID does not EXIST!")

                    def del_mob():
                        id_get = id_entry.get()
                        id_upper = id_get.upper()
                        with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "r", newline="") as mobilesfile:
                            mobilesreader = csv.reader(mobilesfile)
                            mobilesdata = list(mobilesreader)
                        ids = set([row[0].upper() for row in mobilesdata])
                        if id_upper == "":
                            tk.messagebox.showwarning(title="Deleting in the Inventory...", message="You can't leave EMPTY Text Fields!")
                        else:
                            if id_upper in ids:  
                                for row in mobilesdata:
                                    if row[0].upper() == id_upper:
                                        mobilesdata.remove(row)
                                with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "w", newline="") as mobilesfile:
                                    mobileswriter = csv.writer(mobilesfile)
                                    mobileswriter.writerows(mobilesdata)
                                    mobilesfile.seek(0, 2)
                                clear_mw()
                                tk.messagebox.showinfo(title="Deleting in the Inventory...", message="Your Product has been DELETED in the Inventory!")
                            if not id_upper in ids: 
                                tk.messagebox.showwarning(title="Delete in the Inventory...", message="This ID does not EXIST!")

                    def del_gad():
                        id_get = id_entry.get()
                        id_upper = id_get.upper()
                        with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "r", newline="") as gadgetsfile:
                            gadgetsreader = csv.reader(gadgetsfile)
                            gadgetsdata = list(gadgetsreader)
                        ids = set([row[0].upper() for row in gadgetsdata])
                        if id_upper == "":
                            tk.messagebox.showwarning(title="Deleting in the Inventory...", message="You can't leave EMPTY Text Fields!")
                        else:
                            if id_upper in ids:  
                                for row in gadgetsdata:
                                    if row[0].upper() == id_upper:
                                        gadgetsdata.remove(row)
                                with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "w", newline="") as gadgetsfile:
                                    gadgetswriter = csv.writer(gadgetsfile)
                                    gadgetswriter.writerows(gadgetsdata)
                                    gadgetsfile.seek(0, 2)
                                clear_mw()
                                tk.messagebox.showinfo(title="Deleting in the Inventory...", message="Your Product has been DELETED in the Inventory!")
                            if not id_upper in ids: 
                                tk.messagebox.showwarning(title="Delete in the Inventory...", message="This ID does not EXIST!")

                    # ========================================================================================================= #
                    # ========================================================================================================= #

                    mainwindow = tk.Tk()
                    mainwindow.withdraw()
                    mainwindow.title("Device Warehouse Inventory ("+ username+")")
                    window_w_total = mainwindow.winfo_screenwidth()
                    window_h_total = mainwindow.winfo_screenheight()
                    window_w = 745
                    window_h = 720
                    login_width = round(window_w_total/2-window_w/2)
                    login_height = round(window_h_total/2-window_h/2-50)
                    mainwindow.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))
                    mainwindow.resizable(width=False, height=False)
                    mainwindow.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/main.ico"))
                    mainwindow.protocol("WM_DELETE_WINDOW", lambda: signout())

                    # ========== DEVICE IMAGE ========== #
                    deviceimg = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/DevicesAccs.png"))
                    deviceimglb = tk.Label(mainwindow, image=deviceimg)
                    deviceimglb.place(x=20, y=150)

                    # ========== DATA BASE TABLE ========== #
                    table_mw()

                    # ========== RADIO BUTTONS ========== #
                    selectmode_group = tk.IntVar()
                    viewrb= tk.Radiobutton(mainwindow, text="View Mode", value="mw-view_mode", variable=selectmode_group, font="15", padx="10", pady="10", cursor="hand2")
                    viewrb.place(x=20, y=5)
                    viewrb.config(indicatoron=False)
                    viewrb.bind("<ButtonRelease-1>", optionselected_mode)
                    viewrb.select()
                    addrb= tk.Radiobutton(mainwindow, text="Add Mode", value="mw-add_mode", variable=selectmode_group, font="15", padx="14", pady="10", fg="white", activeforeground="white", bg="#009003", activebackground="#00AA03", selectcolor="#009A03", cursor="hand2")
                    addrb.place(x=217, y=5)
                    addrb.config(indicatoron=False)
                    addrb.bind("<ButtonRelease-1>", optionselected_mode)
                    editrb= tk.Radiobutton(mainwindow, text="Edit Mode", value="mw-edit_mode", variable=selectmode_group, font="15", padx="14", pady="10", fg="white", activeforeground="white", bg="#0049DE", activebackground="#0059FF", selectcolor="#005BDE", cursor="hand2")
                    editrb.place(x=420, y=5)
                    editrb.config(indicatoron=False)
                    editrb.bind("<ButtonRelease-1>", optionselected_mode)
                    deleterb= tk.Radiobutton(mainwindow, text="Delete Mode", value="mw-delete_mode", variable=selectmode_group, font="15", padx="5", pady="10", fg="white", activeforeground="white", bg="#CE0000", activebackground="#FB0000", selectcolor="#E70000", cursor="hand2")
                    deleterb.place(x=617, y=5)
                    deleterb.config(indicatoron=False)
                    deleterb.bind("<ButtonRelease-1>", optionselected_mode)

                    viewmode_group = tk.IntVar()
                    vw_computersrb= tk.Radiobutton(mainwindow, text="Computers", value="vw-computers", variable=viewmode_group, font="15", padx="5", pady="10", cursor="hand2")
                    vw_computersrb.place(x=105, y=363)
                    vw_computersrb.config(indicatoron=False)
                    vw_computersrb.bind("<ButtonRelease-1>", optionselected_vw)
                    vw_computersrb.select()
                    vw_mobilesrb= tk.Radiobutton(mainwindow, text="Mobiles", value="vw-mobiles", variable=viewmode_group, font="15", padx="16", pady="10", cursor="hand2")
                    vw_mobilesrb.place(x=205, y=363)
                    vw_mobilesrb.config(indicatoron=False)
                    vw_mobilesrb.bind("<ButtonRelease-1>", optionselected_vw)
                    vw_gadgetsrb= tk.Radiobutton(mainwindow, text="Gadgets", value="vw-gadgets", variable=viewmode_group, font="15", padx="14", pady="10", cursor="hand2")
                    vw_gadgetsrb.place(x=305, y=363)
                    vw_gadgetsrb.config(indicatoron=False)
                    vw_gadgetsrb.bind("<ButtonRelease-1>", optionselected_vw)

                    sl_group_mw()

                    # ========== LABELS ========== #
                    labels_mw()

                    inventorylb = tk.Label(mainwindow, text="Inventory Information", font="SegoeUIVariable, 15")
                    inventorylb.place(x=18, y=328)

                    # ========== TEXT ENTRIES ========== #
                    entrys_mw()

                    # ========== BUTTONS ========== #
                    buttons_mw()

                    showexported_folderbtn = tk.Button(mainwindow, text="📂",font="15", cursor= "hand2", width=3, command=showexportedfolder)
                    showexported_folderbtn.place(x=649, y=645)
                    changelogbtn = tk.Button(mainwindow, text="📝",font="15", cursor= "hand2", width=3, command=changelog)
                    changelogbtn.place(x=687, y=645)

                    # ========== SEPARATORS ========== #
                    sec1_separator = tk.ttk.Separator(mainwindow, orient="horizontal")
                    sec1_separator.place(x=0, y=60, width=745)
                    sec2_separator = tk.ttk.Separator(mainwindow, orient="horizontal")
                    sec2_separator.place(x=0, y=323, width=745)

                    # ========== MENU BARS ========== #
                    menubar = tk.Menu(mainwindow)
                    filemenu = tk.Menu(menubar, tearoff=0)
                    filemenu.add_command(label="Save Data to Text File", command=exportfile)
                    filemenu.add_separator()
                    filemenu.add_command(label="Sign-Out", command=signout)
                    menubar.add_cascade(label="Main", menu=filemenu)

                    aboutmenu = tk.Menu(menubar, tearoff=0)
                    aboutmenu.add_command(label="How can use This Program?", command=help_main)
                    aboutmenu.add_separator()
                    aboutmenu.add_command(label="ChangeLog", command=changelog)
                    aboutmenu.add_command(label="About the Program", command=about)
                    menubar.add_cascade(label="About", menu=aboutmenu)
                    mainwindow.config(menu=menubar)
                    # ================================ #
                    mainwindow.deiconify()
                    mainwindow.mainloop()
                else:
                    tk.messagebox.showerror(title="Login Account Error", message="Your Account is incorrect or invalid!")
            except Exception as e:
                tk.messagebox.showerror("An error has occurred!", f"Information About the Error:\n\n{e}")
                os.remove(os.path.join(os.path.dirname(__file__), "init"))
                sys.exit(0)
               
        # ========================================================================================================= #
        # ============================================== LOGIN WINDOW ============================================== #

        def login_window():
            def validate_value_account(text):
                    pattern = re.compile(r"^[a-zA-Z0-9]+$")
                    if pattern.match(text) is not None:
                        return True and len(text) <= 20
                    elif text == "":
                        return True and len(text) <= 20
                    else:
                        return False
            global username_entry, password_entry, loginwindow
            loginwindow = tk.Tk()
            loginwindow.withdraw()
            loginwindow.title("Device Warehouse Inventory (Sign-In)")
            loginwindow.protocol("WM_DELETE_WINDOW", lambda: close_login())
            window_w_total = loginwindow.winfo_screenwidth()
            window_h_total = loginwindow.winfo_screenheight()
            window_w = 500
            window_h = 360
            login_width = round(window_w_total/2-window_w/2)
            login_height = round(window_h_total/2-window_h/2-100)
            loginwindow.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))
            loginwindow.resizable(width=False, height=False)
            loginwindow.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))

            # ========== DEVICE IMAGE ========== #
            loginprofile = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/login.png"))
            loginprofilelb = tk.Label(loginwindow, image=loginprofile)
            loginprofilelb.pack()

            # ========== LABELS ========== #
            username_label = tk.Label(loginwindow, text="Username:", font="ubuntu")
            username_label.place(x=115, y=120)
            password_label = tk.Label(loginwindow, text="Password:", font="ubuntu")
            password_label.place(x=115, y=185)
            rememberlb =tk.Label(loginwindow, text="Don't Remember your Account?", cursor='hand2', fg="#0055FF", activeforeground="#0083FF", font="ubuntu")
            rememberlb.place(x=6, y=298)
            rememberlb.bind("<ButtonRelease-1>", lambda event: rememberaccount())
            rememberlb.bind("<Enter>", lambda event: rememberlb.config(fg="#0083FF"))
            rememberlb.bind("<Leave>", lambda event: rememberlb.config(fg="#0055FF"))

            # ========== TEXT ENTRIES ========== #
            username_entry = tk.Entry(loginwindow, borderwidth=3, width=30, font="ubuntu", validate="key", validatecommand=(loginwindow.register(validate_value_account), "%P"))
            username_entry.place(x=115, y=145)
            password_entry = tk.Entry(loginwindow, show="*", borderwidth=3, width=30, font="ubuntu", validate="key", validatecommand=(loginwindow.register(validate_value_account), "%P"))
            password_entry.place(x=115, y=210)

            # ========== BUTTONS ========== #
            loginbtn = tk.Button(loginwindow, text="Sign-In", fg="white", activeforeground="white", bg="#007A05", activebackground= "#00A007", cursor= "hand2",
                                    padx=20, pady=3, width=3, command=main_window)
            loginbtn.place(x=215, y=250)

            infobtn = tk.Button(loginwindow, text="!", font=("SegoeUIVariable", 12, "bold"), fg="white", activeforeground="white", bg="#0055FF", activebackground= "#0078FF", cursor= "hand2",
                                    padx=3, pady=3, width=3, command=about)
            infobtn.place(x=448, y=280)

            # ========== MENU BAR ========== #
            menubar = tk.Menu(loginwindow)
            aboutmenu = tk.Menu(menubar, tearoff=0)
            aboutmenu.add_command(label="How can I Sign-in?", command=login_help)
            aboutmenu.add_separator()
            aboutmenu.add_command(label="ChangeLog", command=changelog)
            aboutmenu.add_command(label="About the Program", command=about)
            menubar.add_cascade(label="About", menu=aboutmenu)
            loginwindow.config(menu=menubar)
            # ============================== #
            loginwindow.deiconify()
            loginwindow.mainloop()
        login_window()
    except Exception as e:
        tk.messagebox.showerror("An error has occurred!", f"Information About the Error:\n\n{e}")
        os.remove(os.path.join(os.path.dirname(__file__), "init"))
        sys.exit(0)

# ============= REQUIREMENTS ============= #
os_version = int(platform.version().split('.')[2])
min_req = 9200

display_res = ctypes.windll.user32.GetDesktopWindow()
res = ctypes.wintypes.RECT()
ctypes.windll.user32.GetWindowRect(display_res, ctypes.byref(res))
res_width = res.right - res.left 
res_height = res.bottom - res.top 

if os_version < min_req:
    tk.messagebox.showerror("OS Version Not supported", "Windows 8 x64 (Build 9200) or Higher is Required to Work!\nPlease Update the O.S, If you still have Problems contact the Developer.")
    sys.exit(0)
elif res_width < 1024 or res_height < 768: 
    tk.messagebox.showerror("Low Screen Resolution Detected!", "A Display Resolution of 1024 x 768 or Higher is Required to Work!\nIf you still have Problems contact the Developer.")
    sys.exit(0)
else: 
    DWI()