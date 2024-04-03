import tkinter as tk
from tkinter import *
from tkinter import ttk, font, messagebox
import os, sys, csv, re, random, wmi, datetime, darkdetect, platform, ctypes

if os.path.exists(os.path.join(os.path.dirname(__file__), "DWI.exe")):
    process_query = "SELECT Name, ProcessId FROM Win32_Process WHERE Name = 'DWI.exe'"
    processes = wmi.WMI().query(process_query)
    if len(processes) >= 2:
        sys.exit()
else:
    sys.exit(0)

def DWI():
    global dynamic_window
    try:
        # ======================================================================================================================= #
        dynamic_window = tk.Tk() # ----- MAIN WINDOW
        dynamic_window.protocol("WM_DELETE_WINDOW", lambda: close())
        dynamic_window.withdraw()
        
        if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data")):
            os.makedirs(os.path.join(os.path.dirname(__file__), "Data"))
        if not os.path.exists(os.path.join(os.path.dirname(__file__), "Exported")):   
            os.makedirs(os.path.join(os.path.dirname(__file__), "Exported"))
        
        if not os.path.exists(os.path.join(os.path.dirname(__file__), "settings.dat")):
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
                settingfile.write("theme=dark_theme\nlanguage=eng_lang\n")
        if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data/account_data.csv")):
            with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "w") as accountfile:
                accountfile.write("admin,12345\n")
        if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv")):
            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "w") as inventoryfile:
                inventoryfile.write("")
                
        errorinfo_wm = tk.Toplevel(dynamic_window)
        errorinfo_wm.transient(dynamic_window)
        errorinfo_wm.withdraw()
        error_close_btn = tk.Button(errorinfo_wm, padx=35, pady=3, width=3)
        errorimg = tk.PhotoImage()
        errorimglb = tk.Label(errorinfo_wm, image=errorimg)
        errorlb = tk.Label(errorinfo_wm)
        infotxtlb = tk.Label(errorinfo_wm, wraplength=520, cursor="hand2", justify="left")
        eMenu = Menu(errorinfo_wm, tearoff=False)
        e_icons = tk.Label(text="📄 ❎")
        
        def close():
            sys.exit(0)

        def error_wn():
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            settingsdata = set([row[0]for row in settingdata])
            if "language=eng_lang" and "language=esp_lang" in settingsdata:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
            elif "theme=dark_theme" and "theme=light_theme" in settingsdata:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
            else:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
                    settingfile.write("theme=dark_theme\nlanguage=eng_lang\n")
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)

            errorinfo_wm.resizable(width=False, height=False)
            errorinfo_wm.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "main.ico"))
            errorinfo_wm.grab_set()
            errorinfo_wm.focus_set()
            
            eMenu.add_command(compound=tk.LEFT)
            def copy_text():
                errorinfo_wm.clipboard_clear()
                errorinfo_wm.clipboard_append(infotxtlb.cget("text"))
            def e_menu(action):
                eMenu.entryconfigure(0, command=lambda: copy_text())
                eMenu.post(action.x_root, action.y_root)
            infotxtlb.bind("<ButtonRelease-1>", e_menu)
            infotxtlb.bind("<ButtonRelease-3>", e_menu)
            errorimg.config(file=os.path.join(os.path.dirname(__file__), "error.png"))
                        
            themedata = set([row[0]for row in settingdata])
            if "theme=dark_theme" in themedata:                     
                eMenu.entryconfigure(0, background="black", foreground="white")
                errorinfo_wm.config(bg="black")
                errorlb.config(bg="black", fg="white")
                errorimglb.config(bg="black")
                infotxtlb.config(background="black", foreground="#FF9E9E")
                error_close_btn.config(bg="black", fg="white", activeforeground="white", activebackground="#111111")
            elif "theme=light_theme" in themedata:
                eMenu.entryconfigure(0, background="white", foreground="black")
                errorinfo_wm.config(bg="white")
                errorlb.config(bg="white", fg="black")
                errorimglb.config(bg="white")
                infotxtlb.config(background="white", foreground="#9E0000")
                error_close_btn.config(bg="white", fg="black", activeforeground="black", activebackground="#EFEFEF")

        def corruptprogram_error_msg():
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            settingsdata = set([row[0]for row in settingdata])
            if "language=eng_lang" and "language=esp_lang" in settingsdata:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
            elif "theme=dark_theme" and "theme=light_theme" in settingsdata:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
            else:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
                    settingfile.write("theme=dark_theme\nlanguage=eng_lang\n")
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)

            errorinfo_wm.protocol("WM_DELETE_WINDOW", lambda: close())
            languagedata = set([row[0]for row in settingdata])
            if "language=eng_lang" in languagedata:
                window_w_total = errorinfo_wm.winfo_screenwidth()
                window_h_total = errorinfo_wm.winfo_screenheight()
                window_w = 533
                window_h = 175
                error_width = round(window_w_total/2-window_w/2)
                error_height = round(window_h_total/2-window_h/2-50)
                errorinfo_wm.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(error_height))
                errorwm_height = round(window_h_total/2-window_h/2-999999999999999999999999999999999999999)
                dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(errorwm_height))
                dynamic_window.deiconify()

                off_elements_msg()
                errorinfo_wm.protocol("WM_DELETE_WINDOW", lambda: close())    
                errorinfo_wm.title("An Fatal Error has occurred!")
                errorinfo_wm.resizable(width=False, height=False)
                errorinfo_wm.grab_set()
                errorinfo_wm.focus_set()
                
                errorimglb.place(x=15, y=30)
                errorlb.config(justify="center", text="Corrupt Program Files have been found.\nReinstall/Restore the Program.\n\nIf you still have problems, Please notify the Developer!", font="SegoeUIVariable, 12")
                errorlb.place(x=120, y=30)

                error_close_btn.config(text="❎ Close", font="SegoeUIVariable, 12", cursor="hand2", command=close)
                error_close_btn.place(x=210, y=125)
                errorinfo_wm.transient(dynamic_window)
            elif "language=esp_lang" in languagedata:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 615
                window_h = 175
                error_width = round(window_w_total/2-window_w/2)
                error_height = round(window_h_total/2-window_h/2-50)
                errorinfo_wm.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(error_height))
                errorwm_height = round(window_h_total/2-window_h/2-999999999999999999999999999999999999999)
                dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(errorwm_height))
                dynamic_window.deiconify()

                off_elements_msg()
                errorinfo_wm.protocol("WM_DELETE_WINDOW", lambda: close())    
                errorinfo_wm.title("Ha ocurrido un Error Fatal!")
                errorinfo_wm.resizable(width=False, height=False)
                errorinfo_wm.grab_set()
                errorinfo_wm.focus_set()
                
                errorimglb.place(x=15, y=30)
                errorlb.config(justify="center", text="Se han Encontrado Archivos del Programa Corruptos.\nReinstale/Restaure el Programa\n\nSi aun tienes problemas, Por favor notifica al Desarrollador!", font="SegoeUIVariable, 12")
                errorlb.place(x=120, y=30)

                error_close_btn.config(text="❎ Cerrar", font="SegoeUIVariable, 12", cursor="hand2", command=close)
                error_close_btn.place(x=255, y=125)
                errorinfo_wm.transient(dynamic_window)
            dynamic_window.withdraw()
            basics_msg.withdraw()
            settings_window.withdraw()
            errorinfo_wm.deiconify()
            dynamic_window.mainloop()

        def loadfile_error_msg():
            window_w_total = errorinfo_wm.winfo_screenwidth()
            window_h_total = errorinfo_wm.winfo_screenheight()
            window_w = 704
            window_h = 260
            error_width = round(window_w_total/2-window_w/2)
            error_height = round(window_h_total/2-window_h/2-50)
            errorinfo_wm.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(error_height))
            errorwm_height = round(window_h_total/2-window_h/2-999999999999999999999999999999999999999)
            dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(errorwm_height))
            errorinfo_wm.protocol("WM_DELETE_WINDOW", lambda: close())
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            settingsdata = set([row[0]for row in settingdata])
            if "language=eng_lang" and "language=esp_lang" in settingsdata:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
            elif "theme=dark_theme" and "theme=light_theme" in settingsdata:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
            else:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
                    settingfile.write("theme=dark_theme\nlanguage=eng_lang\n")
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                    
            languagedata = set([row[0]for row in settingdata])
            if "language=eng_lang" in languagedata:
                errorinfo_wm.title("An error has occurred!")
                eMenu.entryconfigure(0, label="📄  Copy", font="SegoeUIVariable, 12")
                errorlb.config(justify="left", text="The Required Files Could Not be Loaded!\n\nError Information:", font="SegoeUIVariable, 12")
                infotxtlb.config(text=str(sys.exc_info()), font=font.Font(family="Consolas", size=11))
                errorlb.place(x=110, y=25)
                infotxtlb.place(x=110, y=85)
                error_close_btn.config(text="❎ Close", font="SegoeUIVariable, 12", cursor="hand2", command=close)
                error_close_btn.place(x=298, y=210)
                errorimglb.place(x=15, y=15)
            elif "language=esp_lang" in languagedata:
                errorinfo_wm.title("Ha ocurrido un Error!")
                eMenu.entryconfigure(0, label="📄  Copiar", font="SegoeUIVariable, 12")
                errorlb.config(justify="left", text="No se han Podido Cargar los Archivos Requeridos!\n\nInformacion acerca del Error:", font="SegoeUIVariable, 12")
                infotxtlb.config(text=str(sys.exc_info()), font=font.Font(family="Consolas", size=11))
                errorlb.place(x=110, y=25)
                infotxtlb.place(x=110, y=85)
                error_close_btn.config(text="❎ Cerrar", font="SegoeUIVariable, 12", cursor="hand2", command=close)
                error_close_btn.place(x=298, y=210)
                errorimglb.place(x=15, y=15)
            dynamic_window.withdraw()
            basics_msg.withdraw()
            settings_window.withdraw()
            errorinfo_wm.deiconify()
            dynamic_window.mainloop()

        def loaddata_error_msg():
            window_w_total = errorinfo_wm.winfo_screenwidth()
            window_h_total = errorinfo_wm.winfo_screenheight()
            window_w = 704
            window_h = 260
            error_width = round(window_w_total/2-window_w/2)
            error_height = round(window_h_total/2-window_h/2-50)
            errorinfo_wm.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(error_height))
            errorwm_height = round(window_h_total/2-window_h/2-999999999999999999999999999999999999999)
            dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(errorwm_height))
            errorinfo_wm.protocol("WM_DELETE_WINDOW", lambda: close())
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            settingsdata = set([row[0]for row in settingdata])
            if "language=eng_lang" and "language=esp_lang" in settingsdata:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
            elif "theme=dark_theme" and "theme=light_theme" in settingsdata:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
            else:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
                    settingfile.write("theme=dark_theme\nlanguage=eng_lang\n")
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                    
            languagedata = set([row[0]for row in settingdata])
            if "language=eng_lang" in languagedata:
                errorinfo_wm.title("An error has occurred!")
                eMenu.entryconfigure(0, label="📄  Copy", font="SegoeUIVariable, 12")
                errorlb.config(justify="left", text="Inventory Data contains non valid values or the File is Corrupt!\n\nError Information:", font="SegoeUIVariable, 12")
                infotxtlb.config(text=str(sys.exc_info()), font=font.Font(family="Consolas", size=11))
                errorlb.place(x=110, y=25)
                infotxtlb.place(x=110, y=85)
                error_close_btn.config(text="❎ Close", font="SegoeUIVariable, 12", cursor="hand2", command=close)
                error_close_btn.place(x=298, y=210)
                errorimglb.place(x=15, y=15)
            elif "language=esp_lang" in languagedata:
                errorinfo_wm.title("Ha ocurrido un Error!")
                eMenu.entryconfigure(0, label="📄  Copiar", font="SegoeUIVariable, 12")
                errorlb.config(justify="left", text="Los Datos del Inventario contiene valores no validos o el archivo esta corrupto!\n\nInformacion acerca del Error:", font="SegoeUIVariable, 12")
                infotxtlb.config(text=str(sys.exc_info()), font=font.Font(family="Consolas", size=11))
                errorlb.place(x=110, y=25)
                infotxtlb.place(x=110, y=85)
                error_close_btn.config(text="❎ Cerrar", font="SegoeUIVariable, 12", cursor="hand2", command=close)
                error_close_btn.place(x=298, y=210)
                errorimglb.place(x=15, y=15)
            dynamic_window.withdraw()
            basics_msg.withdraw()
            settings_window.withdraw()
            errorinfo_wm.deiconify()
            dynamic_window.mainloop()

        # ============================================== LOAD LOGIN WINDOWELEMENTS ============================================== #
        def load_loginwindow():
            def validate_value_account(text):
                pattern = re.compile(r"^[a-zA-Z0-9]+$")
                if pattern.match(text) is not None:
                    return True and len(text) <= 20
                elif text == "":
                    return True and len(text) <= 20
                else:
                    return False

            global laboutmbar, laboutmbar_btn, lmbar_separator, loginprofile_img, loginprofile_imglb, modeshelp_btn, welcome_login
            global username_label, password_label, changeaccountlb, username_entry, password_entry, loginbtn, infobtn, settingsbtn, changeaccount_btn
            laboutmbar_btn = Menubutton(dynamic_window)
            laboutmbar = Menu(laboutmbar_btn, tearoff=False)
            laboutmbar_btn["menu"]= laboutmbar
            laboutmbar.add_command()
            laboutmbar.add_separator()				
            laboutmbar.add_command()
            laboutmbar.add_command()
            laboutmbar_btn.place(x=0, y=0, height=31, width=100)

            modeshelp_btn = tk.Button(dynamic_window, cursor= "hand2", width=3, height=1)
            changeaccount_btn = tk.Button(dynamic_window, cursor= "hand2", width=3, height=1)
            settingsbtn = tk.Button(dynamic_window, cursor= "hand2", width=3, height=1)

            lmbar_separator = tk.Frame(dynamic_window)
            loginprofile_img = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/login.png"))
            loginprofile_imglb = tk.Label(dynamic_window, image=loginprofile_img)
            welcome_login = tk.Label(dynamic_window)
            username_label = tk.Label(dynamic_window)
            username_entry = tk.Entry(dynamic_window, width=30, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font="SegoeUIVariable, 12")
            password_label = tk.Label(dynamic_window)
            password_entry = tk.Entry(dynamic_window, width=30, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font="SegoeUIVariable, 12", show="*")
            loginbtn = tk.Button(dynamic_window, cursor= "hand2", pady=3, width=3, command=main_window)
            changeaccountlb = tk.Label(dynamic_window, cursor='hand2', fg="#0055FF", activeforeground="#0083FF")
            infobtn = tk.Button(dynamic_window, cursor= "hand2", width=3, height=1)

        # ============================================== LOAD MAIN WINDOW ELEMENTS ============================================== #
        def load_inventory_window():
            def validate_value_id(text):
                pattern = re.compile(r"^[0-9]+$")
                if pattern.match(text) is not None and len(text) <= 7:
                    return True
                elif text == "":
                    return True
                else:
                    return False
            def validate_value_brand(text):
                pattern = re.compile(r"^[a-zA-Z0-9-_ ]+$")
                if pattern.match(text) is not None and len(text) <= 15:
                    return True
                elif text == "":
                    return True
                else:
                    return False
            def validate_value_model(text):
                pattern = re.compile(r"^[a-zA-Z0-9-_ ]+$")
                if pattern.match(text) is not None and len(text) <= 28:
                    return True
                elif text == "":
                    return True
                else:
                    return False
            def validate_value_color(text):
                pattern = re.compile(r"^[a-zA-Z ]+$")
                if pattern.match(text) is not None and len(text) <= 13:
                    return True
                elif text == "":
                    return True
                else:
                    return False
            def validate_value_date(text):
                pattern = re.compile(r"^[a-zA-Z0-9-: ]+$")
                if pattern.match(text) is not None and len(text) <= 19:
                    return True
                elif text == "":
                    return True
                else:
                    return False

            global mainmbar_btn, aboutmbar_btn, mainmbar, aboutmbar, idlb, brandlb, modellb, colorlb, datelb, inventorylb, searchlb, device_img, device_imglb
            global id_entry, brand_entry, model_entry, color_entry, date_entry, search_entry, inventory_table, table_scrollbar, addrb, editrb, deleterb, modes_group
            global addbtn, checkbtn, editbtn, cancelbtn, deletebtn, clearbtn, separator1, separator2, separator3, foundlb
            mainmbar_btn = Menubutton(dynamic_window)	
            mainmbar = Menu(mainmbar_btn, tearoff=False)
            mainmbar_btn["menu"]= mainmbar
            mainmbar.add_command()
            mainmbar.add_command()
            mainmbar.add_separator()				
            mainmbar.add_command()
            aboutmbar_btn = Menubutton(dynamic_window)	
            aboutmbar = Menu(aboutmbar_btn, tearoff=False)
            aboutmbar_btn["menu"]= aboutmbar
            aboutmbar.add_command()
            aboutmbar.add_separator()				
            aboutmbar.add_command()
            aboutmbar.add_command()

            separator1 = tk.Frame(dynamic_window)
            modes_group = tk.IntVar()
            addrb = tk.Radiobutton(dynamic_window, value=1, variable=modes_group, padx="14", pady="5", cursor="hand2")
            editrb = tk.Radiobutton(dynamic_window, value=2, variable=modes_group, padx="14", pady="5", cursor="hand2")
            deleterb = tk.Radiobutton(dynamic_window, value=3, variable=modes_group, padx="5", pady="5",cursor="hand2")
            separator2 = tk.Frame(dynamic_window, height=1, bd=0)
            inventorylb = tk.Label(dynamic_window)
            searchlb = tk.Label(dynamic_window)
            search_entry = tk.Entry(dynamic_window, width=30, font="SegoeUIVariable, 12")

            inventory_table = ttk.Treeview(dynamic_window, selectmode="browse")
            inventory_table['show']='headings'
            inventory_table["columns"]=("id", "brand", "model", "color", "date")
            inventory_table.column("id", width=85, minwidth=85, anchor=tk.SW)
            inventory_table.column("brand", width=160, minwidth=160, anchor=tk.SW)
            inventory_table.column("model", width=300, minwidth=300, anchor=tk.SW)
            inventory_table.column("color", width=150, minwidth=150, anchor=tk.SW)
            inventory_table.column("date", width=185, minwidth=185, anchor=tk.SW)
            table_scrollbar = ttk.Scrollbar(dynamic_window, orient="vertical", command=inventory_table.yview)
            inventory_table.configure(yscrollcommand=table_scrollbar.set)
            foundlb = tk.Label(dynamic_window)

            separator3 = tk.Frame(dynamic_window, height=1, bd=0)
            device_img = tk.PhotoImage()
            device_imglb = tk.Label(dynamic_window)
            idlb = tk.Label(dynamic_window)
            brandlb = tk.Label(dynamic_window)
            modellb = tk.Label(dynamic_window)
            colorlb = tk.Label(dynamic_window)
            datelb = tk.Label(dynamic_window)
            id_entry =tk.Entry(dynamic_window, width=31, validate="key", validatecommand=(dynamic_window.register(validate_value_id), "%P"), cursor= "xterm", font="SegoeUIVariable, 12")
            brand_entry =tk.Entry(dynamic_window, width=31, validate="key", validatecommand=(dynamic_window.register(validate_value_brand), "%P"), cursor= "xterm", font="SegoeUIVariable, 12")
            model_entry =tk.Entry(dynamic_window, width=31, validate="key", validatecommand=(dynamic_window.register(validate_value_model), "%P"), cursor= "xterm", font="SegoeUIVariable, 12")
            color_entry =tk.Entry(dynamic_window, width=31, validate="key", validatecommand=(dynamic_window.register(validate_value_color), "%P"), cursor= "xterm", font="SegoeUIVariable, 12")
            date_entry =tk.Entry(dynamic_window, width=31, validate="key", validatecommand=(dynamic_window.register(validate_value_date), "%P"), cursor= "xterm", font="SegoeUIVariable, 12")
            
            addbtn = tk.Button(dynamic_window, cursor= "hand2", padx=50, width=3)
            checkbtn = tk.Button(dynamic_window, cursor= "hand2", padx=50, width=3)
            editbtn = tk.Button(dynamic_window, cursor= "hand2", padx=50, width=3)
            cancelbtn = tk.Button(dynamic_window, cursor= "hand2", padx=50, width=3)
            deletebtn = tk.Button(dynamic_window, cursor= "hand2", padx=50, width=3)
            clearbtn = tk.Button(dynamic_window, cursor= "hand2", padx=50, width=3)

            icons_wm = tk.Label(text="💾 📝 🔐 👤 🔑 🔁 ✖️ 🧹 ➕ ✏️ ➖ 🔎 📂 ✅ ❎ 🔓 🌙 🔆")

        # ============================================== LANGUAGES ============================================== #
        def eng_lang_login():
            eng_langrb.select()
            setting_btn_apply.config(command=apply_settings_login)

            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            for row in settingdata:
                if row[0] == "language=esp_lang":
                    row[0] = "language=eng_lang"
                    break 
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                writer = csv.writer(settingfile)
                writer.writerows(settingdata)
                settingfile.seek(0, 2)

            dynamic_window.title("Device Warehouse Inventory (Sign-In)")

            laboutmbar_btn.config(text = "About", font="SegoeUIVariable, 12")
            laboutmbar.entryconfigure(0, label="❔  How to Sign-In?", font="SegoeUIVariable, 12", command=login_help_eng)
            laboutmbar.entryconfigure(2, label="📝  ChangeLog", font="SegoeUIVariable, 12", command=changelog_eng)
            laboutmbar.entryconfigure(3, label="❕  About the Program", font="SegoeUIVariable, 12", command=about_eng)

            welcome_login.config(text="Login with your Account", font="SegoeUIVariable, 17")
            welcome_login.place(x=158)
            username_label.config(text="Username:", font="SegoeUIVariable, 12")
            password_label.config(text="Password:", font="SegoeUIVariable, 12")
            changeaccountlb.config(text="👤 Account Settings", font="SegoeUIVariable, 12")
            changeaccountlb.bind("<Button-1>", lambda event: changeaccount())

            loginbtn.config(text="🔓 Sign-In", font="SegoeUIVariable, 12", padx=30)
            loginbtn.place(x=228)
            infobtn.config(text="❕", font="SegoeUIVariable, 12", command=about_eng)
            settingsbtn.config(text="⚙️", font="SegoeUIVariable, 12", command=settings)
            settings_eng()
            changeaccount_eng()

        def esp_lang_login():
            esp_langrb.select()
            setting_btn_apply.config(command=apply_settings_login)

            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            for row in settingdata:
                if row[0] == "language=eng_lang":
                    row[0] = "language=esp_lang"
                    break 
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                writer = csv.writer(settingfile)
                writer.writerows(settingdata)
                settingfile.seek(0, 2)

            dynamic_window.title("Device Warehouse Inventory (Inicia Sesion)")

            laboutmbar_btn.config(text = "Acerca de", font="SegoeUIVariable, 12")
            laboutmbar.entryconfigure(0, label="❔  Como Iniciar Sesion?", font="SegoeUIVariable, 12", command=login_help_esp)
            laboutmbar.entryconfigure(2, label="📝  Registro de Cambios", font="SegoeUIVariable, 12", command=changelog_esp)
            laboutmbar.entryconfigure(3, label="❕  Acerca del Programa", font="SegoeUIVariable, 12", command=about_esp)

            welcome_login.config(text="Inicia Sesion con tu Cuenta", font="SegoeUIVariable, 17")
            welcome_login.place(x=140)
            username_label.config(text="Nombre de Usuario:", font="SegoeUIVariable, 12")
            password_label.config(text="Contraseña:", font="SegoeUIVariable, 12")
            changeaccountlb.config(text="👤 Configuracion de la Cuenta", font="SegoeUIVariable, 12")
            changeaccountlb.bind("<Button-1>", lambda event: changeaccount())

            loginbtn.config(text="🔓 Iniciar Sesion", font="SegoeUIVariable, 12", padx=50)
            loginbtn.place(x=210)
            infobtn.config(text="❕", font="SegoeUIVariable, 12", command=about_esp)
            settingsbtn.config(text="⚙️", font="SegoeUIVariable, 12", command=settings)
            settings_esp()
            changeaccount_esp()

        def eng_lang_mainwindow():
            def reflesh_inventory():
                inventory_table.delete(*inventory_table.get_children())
                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r") as refleshfile:
                    data = refleshfile.readlines()
                if len(data) > 10:
                    table_scrollbar.place(x=885, y=153, height=222, width=17)
                else:
                    table_scrollbar.place_forget()
                for row in data:
                    id, brand, model, color, date = row.strip().split(",")
                    inventory_table.insert("", "end", values=(id, brand, model, color, date))
            
            eng_langrb.select()
            dynamic_window.protocol("WM_DELETE_WINDOW", lambda: signout_ask_eng())

            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            for row in settingdata:
                if row[0] == "language=esp_lang":
                    row[0] = "language=eng_lang"
                    break 
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                writer = csv.writer(settingfile)
                writer.writerows(settingdata)
                settingfile.seek(0, 2)

            mainmbar_btn.config(text = "Main", font="SegoeUIVariable, 12")	
            mainmbar.entryconfigure(0, label="📂  Show (Exported) Folder", font="SegoeUIVariable, 12")	
            mainmbar.entryconfigure(1, label="💾  Export Inventory to Text File", font="SegoeUIVariable, 12")		
            mainmbar.entryconfigure(3, label="🔐  Sign-Out", font="SegoeUIVariable, 12", command=signout_ask_eng)

            aboutmbar_btn.config(text = "About", font="SegoeUIVariable, 12")
            aboutmbar_btn.place(x=100)	
            aboutmbar.entryconfigure(0, label="❔  How to use This Program?", font="SegoeUIVariable, 12", command=main_help_eng)
            aboutmbar.entryconfigure(2, label="📝  ChangeLog", font="SegoeUIVariable, 12", command=changelog_eng)
            aboutmbar.entryconfigure(3, label="❕  About the Program", font="SegoeUIVariable, 12", command=about_eng)

            addrb.config(text="➕\nAdd Mode", font="SegoeUIVariable, 12")
            editrb.config(text="✏️\nEdit Mode", font="SegoeUIVariable, 12")
            deleterb.config(text="➖\nDelete Mode", font="SegoeUIVariable, 12")
            
            search_entry.delete(0, tk.END)
            search_entry.insert(0, "Search by ID...")
            search_entry.bind("<FocusIn>", lambda event: search_entry.delete(0, tk.END) if search_entry.get() == "Search by ID..." else search_entry.insert(0, ""))
            search_entry.bind("<FocusOut>", lambda event: search_entry.insert(0, "Search by ID...") if search_entry.get() == "" else search_entry.insert(0, ""))
            foundlb.config(text="Not Found", font="SegoeUIVariable, 12")
            foundlb.place_forget()
            reflesh_inventory()

            inventory_table.heading("id", text= " ID", anchor=tk.SW)
            inventory_table.heading("brand", text= " Brand", anchor=tk.SW)
            inventory_table.heading("model", text= " Model", anchor=tk.SW)
            inventory_table.heading("color", text= " Color", anchor=tk.SW)
            inventory_table.heading("date", text= " Registered Date", anchor=tk.SW)

            idlb.config(text="ID", font="SegoeUIVariable, 12")
            brandlb.config(text="Brand", font="SegoeUIVariable, 12")
            modellb.config(text="Model", font="SegoeUIVariable, 12")
            colorlb.config(text="Color", font="SegoeUIVariable, 12")
            datelb.config(text="Date", font="SegoeUIVariable, 12")
            inventorylb.config(text="Inventory Information", font="SegoeUIVariable, 15")

            addbtn.config(text="➕   Add             ", font="SegoeUIVariable, 12")
            checkbtn.config(text="🔎   Check         ", font="SegoeUIVariable, 12")
            cancelbtn.config(text="✖️  Cancel        ", font="SegoeUIVariable, 12")
            editbtn.config(text="✏️  Edit             ", font="SegoeUIVariable, 12")
            deletebtn.config(text="➖  Delete        ", font="SegoeUIVariable, 12")
            clearbtn.config(text="🧹   Clear          ", font="SegoeUIVariable, 12")
            changeaccount_btn.config(text="👤", font="SegoeUIVariable, 12", command=changeaccount)
            modeshelp_btn.config(text="❔", font="SegoeUIVariable, 12")
            modes_value = modes_group.get()
            if modes_value == 1:
                modeshelp_btn.config(command=addmode_help_eng)
            elif modes_value == 2:
                modeshelp_btn.config(command=editmode_help_eng)
            elif modes_value == 3:
                modeshelp_btn.config(command=deletemode_help_eng)
            settings_eng()
            changeaccount_eng()

        def esp_lang_mainwindow():
            def reflesh_inventory():
                inventory_table.delete(*inventory_table.get_children())
                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r") as refleshfile:
                    data = refleshfile.readlines()
                if len(data) > 10:
                    table_scrollbar.place(x=885, y=153, height=222, width=17)
                else:
                    table_scrollbar.place_forget()
                for row in data:
                    id, brand, model, color, date = row.strip().split(",")
                    inventory_table.insert("", "end", values=(id, brand, model, color, date))
                    
            esp_langrb.select()
            dynamic_window.protocol("WM_DELETE_WINDOW", lambda: signout_ask_esp())

            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            for row in settingdata:
                if row[0] == "language=eng_lang":
                    row[0] = "language=esp_lang"
                    break 
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                writer = csv.writer(settingfile)
                writer.writerows(settingdata)
                settingfile.seek(0, 2)

            mainmbar_btn.config(text = "Principal", font="SegoeUIVariable, 12")
            mainmbar.entryconfigure(0, label="📂  Mostrar Carpeta (Exported)", font="SegoeUIVariable, 12")	
            mainmbar.entryconfigure(1, label="💾  Exportar Inventario en el Archivo de Texto", font="SegoeUIVariable, 12")
            mainmbar.entryconfigure(3, label="🔐  Cerrar Sesion", font="SegoeUIVariable, 12", command=signout_ask_esp)

            aboutmbar_btn.config(text = "Acerca de", font="SegoeUIVariable, 12")	
            aboutmbar_btn.place(x=100)	
            aboutmbar.entryconfigure(0, label="❔  Como usar Este Programa?", font="SegoeUIVariable, 12", command=main_help_esp)
            aboutmbar.entryconfigure(2, label="📝  Registro de Cambios", font="SegoeUIVariable, 12", command=changelog_esp)
            aboutmbar.entryconfigure(3, label="❕  Acerca del Programa", font="SegoeUIVariable, 12", command=about_esp)

            addrb.config(text="➕\nModo Agregar", font="SegoeUIVariable, 12")
            editrb.config(text="✏️\nModo Editar", font="SegoeUIVariable, 12")
            deleterb.config(text="➖\nModo Eliminar", font="SegoeUIVariable, 12")

            search_entry.delete(0, tk.END)
            search_entry.insert(0, "Buscar por ID...")
            search_entry.bind("<FocusIn>", lambda event: search_entry.delete(0, tk.END) if search_entry.get() == "Buscar por ID..." else search_entry.insert(0, ""))
            search_entry.bind("<FocusOut>", lambda event: search_entry.insert(0, "Buscar por ID...") if search_entry.get() == "" else search_entry.insert(0, ""))
            foundlb.config(text="No Encontrado", font="SegoeUIVariable, 12")
            foundlb.place_forget()

            reflesh_inventory()

            inventory_table.heading("id", text= " ID", anchor=tk.SW)
            inventory_table.heading("brand", text= " Marca", anchor=tk.SW)
            inventory_table.heading("model", text= " Modelo", anchor=tk.SW)
            inventory_table.heading("color", text= " Color", anchor=tk.SW)
            inventory_table.heading("date", text= " Fecha de Registro", anchor=tk.SW)

            idlb.config(text="ID", font="SegoeUIVariable, 12")
            brandlb.config(text="Marca", font="SegoeUIVariable, 12")
            modellb.config(text="Modelo", font="SegoeUIVariable, 12")
            colorlb.config(text="Color", font="SegoeUIVariable, 12")
            datelb.config(text="Fecha", font="SegoeUIVariable, 12")
            inventorylb.config(text="Informacion del Inventario", font="SegoeUIVariable, 15")

            addbtn.config(text="➕   Agregar      ", font="SegoeUIVariable, 12")
            checkbtn.config(text="🔎   Comprobar", font="SegoeUIVariable, 12")
            cancelbtn.config(text="✖️  Cancelar    ", font="SegoeUIVariable, 12")
            editbtn.config(text="✏️  Editar         ", font="SegoeUIVariable, 12")
            deletebtn.config(text="➖  Eliminar      ", font="SegoeUIVariable, 12")
            clearbtn.config(text="🧹   Limpiar       ", font="SegoeUIVariable, 12")
            changeaccount_btn.config(text="👤", font="SegoeUIVariable, 12", command=changeaccount)
            modeshelp_btn.config(text="❔", font="SegoeUIVariable, 12")
            modes_value = modes_group.get()
            if modes_value == 1:
                modeshelp_btn.config(command=addmode_help_esp)
            elif modes_value == 2:
                modeshelp_btn.config(command=editmode_help_esp)
            elif modes_value == 3:
                modeshelp_btn.config(command=deletemode_help_esp)
            settings_esp()
            changeaccount_esp()

        # ============================================== LIGHT\DARK THEME ============================================== #
        def window_light():
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            for row in settingdata:
                if row[0] == "theme=dark_theme":
                    row[0] = "theme=light_theme"
                    break 
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                writer = csv.writer(settingfile)
                writer.writerows(settingdata)
                settingfile.seek(0, 2)
            
            dynamic_window.config(bg="white")
            lightthemerb.select()
            settings_light()
            settingsbtn.config(fg="black", activeforeground="black", bg="white", activebackground="#EFEFEF")

            # ====== LOGIN ====== #
            loginmenubar_light()
            loginlabels_light()
            loginentrys_light()    
            loginbuttons_light()
            changeaccount_light()

            # ====== MAINWINDOW ====== #
            mainseparators_light()
            mainmenubar_mw_light()
            labels_main_light()
            entrys_mw_light()
            mainrbs_light()
            mainbtns_light()
            table_light()

            # ====== GENERAL ====== #
            basics_msg_light()

            modes_value = modes_group.get()
            if modes_value == 2:
                if editbtn.winfo_ismapped():
                    brandlb.config(fg="#0078FF")
                    modellb.config(fg="#0078FF")
                    colorlb.config(fg="#0078FF")
                    datelb.config(fg="#0078FF")
                    id_entry.config(foreground="black", insertbackground="black", disabledforeground="#0078FF", disabledbackground="white")
                    brand_entry.config(background="#F9F9F9", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="black", insertbackground="black", highlightthickness=2)
                    model_entry.config(background="#F9F9F9", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="black", insertbackground="black", highlightthickness=2)
                    color_entry.config(background="#F9F9F9", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="black", insertbackground="black", highlightthickness=2)
                    date_entry.config(background="#F9F9F9", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="black", insertbackground="black", highlightthickness=2)
                else:
                    id_entry.config(foreground="black", insertbackground="black", background="#F9F9F9", highlightcolor="#0078FF", highlightbackground="#0078FF", highlightthickness=2)
                    brand_entry.config(highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2)
                    model_entry.config(highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2)
                    color_entry.config(highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2)
                    date_entry.config(highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2)
            elif modes_value == 3:
                id_entry.config(fg="#FE2727", insertbackground="#FE2727", highlightcolor="#FE2727", highlightbackground="#FE2727", highlightthickness=2)
            
        def window_dark():
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            for row in settingdata:
                if row[0] == "theme=light_theme":
                    row[0] = "theme=dark_theme"
                    break 
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                writer = csv.writer(settingfile)
                writer.writerows(settingdata)
                settingfile.seek(0, 2)
                    
            dynamic_window.config(bg="black")
            darkthemerb.select()
            settings_dark()
            settingsbtn.config(fg="white", activeforeground="white", bg="black", activebackground="#111111")

            # ====== LOGIN ====== #
            loginmenubar_dark()
            loginlabels_dark()
            loginentrys_dark()    
            loginbuttons_dark()
            changeaccount_dark()

            # ====== MAINWINDOW ====== #
            mainmenubar_mw_dark()
            mainseparators_dark()
            labels_main_dark()
            entrys_mw_dark()
            mainrbs_dark()
            mainbtns_dark()
            table_dark()

            # ====== MSGS ====== #
            basics_msg_dark()

            modes_value = modes_group.get()
            if modes_value == 2:
                if editbtn.winfo_ismapped():
                    brandlb.config(fg="#0078FF")
                    modellb.config(fg="#0078FF")
                    colorlb.config(fg="#0078FF")
                    datelb.config(fg="#0078FF")
                    id_entry.config(foreground="white", insertbackground="white", disabledforeground="#0078FF", disabledbackground="black")
                    brand_entry.config(background="#111111", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2)
                    model_entry.config(background="#111111", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2)
                    color_entry.config(background="#111111", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2)
                    date_entry.config(background="#111111", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2)
                else:
                    id_entry.config(foreground="white", insertbackground="white", background="#111111", highlightcolor="#0078FF", highlightbackground="#0078FF", highlightthickness=2)
                    brand_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
                    model_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
                    color_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
                    date_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
            elif modes_value == 3:
                id_entry.config(fg="#FE2727", insertbackground="#FE2727", highlightcolor="#FE2727", highlightbackground="#FE2727", highlightthickness=2)
                
        # ============================================== SET PLACE WINDOWS ============================================== #
        def login_window_place():
            window_w_total = dynamic_window.winfo_screenwidth()
            window_h_total = dynamic_window.winfo_screenheight()
            window_w = 550
            window_h = 410
            login_width = round(window_w_total/2-window_w/2)
            login_height = round(window_h_total/2-window_h/2-100)
            dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

        def main_window_place():
            window_w_total = dynamic_window.winfo_screenwidth()
            window_h_total = dynamic_window.winfo_screenheight()
            window_w = 923
            window_h = 585
            login_width = round(window_w_total/2-window_w/2)
            login_height = round(window_h_total/2-window_h/2-100)
            dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

        login_window_place()
        # =================================================================================================================== #
        # ========== LOAD SETTINGS WINDOW ========== #
        settings_window = tk.Toplevel(dynamic_window)
        settings_window.withdraw()

        themeframe = tk.Frame(settings_window, height=1, bd=0)
        themelb = tk.Label(settings_window)
        themegroup = tk.IntVar()
        lightthemerb = tk.Radiobutton(settings_window, value=2, variable=themegroup, indicatoron=False) 
        darkthemerb = tk.Radiobutton(settings_window, value=1, variable=themegroup, indicatoron=False)
        languageframe = tk.Frame(settings_window, height=1, bd=0)
        languagelb = tk.Label(settings_window)
        languagegroup = tk.IntVar()
        eng_langrb = tk.Radiobutton(settings_window, text="English", value=1, variable=languagegroup, font="SegoeUIVariable, 12", cursor="hand2") 
        esp_langrb = tk.Radiobutton(settings_window, text="Español", value=2, variable=languagegroup, font="SegoeUIVariable, 12", cursor="hand2")
        setting_btn_close = tk.Button(settings_window, cursor="hand2")
        setting_btn_apply = tk.Button(settings_window)

        setting_w_total = dynamic_window.winfo_screenwidth()
        setting_h_total = dynamic_window.winfo_screenheight()
        setting_w = 1
        setting_h = 1
        setting_width = round(setting_w_total/2-setting_w/2)
        setting_height = round(setting_h_total/2-setting_h/2)
        settings_window.geometry(str(setting_w)+"x"+str(setting_h)+"+"+str(setting_width)+"+"+str(setting_height))

        def hide_settings():
            restore_elements()
            settings_window.grab_release()
            settings_window.transient(None)
            settings_window.withdraw()

            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            languagedata = set([row[0]for row in settingdata])
            if "language=eng_lang" in languagedata:
                eng_langrb.select()
            elif "language=esp_lang" in languagedata:
                esp_langrb.select()
            themedata = set([row[0]for row in settingdata])
            if "theme=dark_theme" in themedata:                     
                darkthemerb.select()
            elif "theme=light_theme" in themedata:
                lightthemerb.select()

        def change_setting():
            setting_btn_apply.config(state="normal", cursor="hand2")

        def apply_settings_login():
            lang_value = languagegroup.get()
            if lang_value == 1:
                eng_lang_login()
            elif lang_value == 2:
                esp_lang_login()
            theme_value = themegroup.get()
            if theme_value == 1:
                window_dark()
            elif theme_value == 2:
                window_light()
            setting_btn_apply.config(state="disabled", cursor="arrow")

        def apply_settings_main():
            lang_value = languagegroup.get()
            if lang_value == 1:
                eng_lang_mainwindow()
            elif lang_value == 2:
                esp_lang_mainwindow()
            theme_value = themegroup.get()
            if theme_value == 1:      
                window_dark()
            elif theme_value == 2:
                window_light()
            setting_btn_apply.config(state="disabled", cursor="arrow")

        def settings_eng():
            settings_window.title("Settings")
            themelb.config(text="🎨  Theme", font="SegoeUIVariable, 12")
            languagelb.config(text="💬  Languages", font="SegoeUIVariable, 12")
            lightthemerb.config(text="🔆  Light", font="SegoeUIVariable, 12", cursor="hand2", padx=30, pady=7, width=3)
            darkthemerb.config(text="🌙  Dark", font="SegoeUIVariable, 12", cursor="hand2", padx=30, pady=7, width=3)    
            setting_btn_close.config(text="❎ Close", font="SegoeUIVariable, 12", padx=35, pady=3, width=3)
            setting_btn_apply.config(text="✅ Apply", font="SegoeUIVariable, 12", padx=35, pady=3, width=3)

        def settings_esp():
            settings_window.title("Configuracion")
            themelb.config(text="🎨  Tema", font="SegoeUIVariable, 12")
            languagelb.config(text="💬  Idiomas", font="SegoeUIVariable, 12")
            lightthemerb.config(text="🔆  Claro", font="SegoeUIVariable, 12", cursor="hand2", padx=30, pady=7, width=3)
            darkthemerb.config(text="🌙  Oscuro", variable=themegroup, font="SegoeUIVariable, 12", cursor="hand2", padx=30, pady=7, width=3)
            setting_btn_close.config(text="❎ Cerrar", padx=35, pady=3, width=3, font="SegoeUIVariable, 12")
            setting_btn_apply.config(text="✅ Aplicar", padx=35, pady=3, width=3, font="SegoeUIVariable, 12")

        def changeaccount_eng():
            changeaccount_msg.title("Account Settings")

            changeaccount_msg_lbm.config(text="Select one of the options\nto change your account information.", font="SegoeUIVariable, 12")
            changeaccount_msg_lbm.place(x=69, y=25)

            changeusername_btn.config(text="👤 Change Username       ", font="SegoeUIVariable, 12", padx=88, pady=3, width=3, cursor="hand2", command=changeusername)
            changepassword_btn.config(text="🔑 Change Paswword       ", font="SegoeUIVariable, 12", padx=88, pady=3, width=3, cursor="hand2", command=changepassword)
            resetaccount_btn.config(text="🔁 Reset Default Account ", font="SegoeUIVariable, 12", padx=88, pady=3, width=3, cursor="hand2", command=resetaccount_eng)
            changeusername_btn.place(x=87, y=97)
            changepassword_btn.place(x=87, y=155)
                
            changeaccount_btn_close.config(text="❎ Close", font="SegoeUIVariable, 12")
            changeaccount_btn_change.config(text="✅ Change", font="SegoeUIVariable, 12")    

        def changeaccount_esp():
            changeaccount_msg.title("Configuracion de la Cuenta")

            changeaccount_msg_lbm.config(text="Selecciona una de las opciones\npara cambiar información de tu cuenta.", font="SegoeUIVariable, 12")
            changeaccount_msg_lbm.place(x=56, y=25)

            changeusername_btn.config(text="👤 Cambiar Nombre de Usuario               ", font="SegoeUIVariable, 12", padx=135, pady=3, width=3, cursor="hand2", command=changeusername)
            changepassword_btn.config(text="🔑 Cambiar Contraseña                            ", font="SegoeUIVariable, 12", padx=135, pady=3, width=3, cursor="hand2", command=changepassword)
            resetaccount_btn.config(text="🔁 Restablecer Cuenta Predeterminada ", font="SegoeUIVariable, 12", padx=135, pady=3, width=3, cursor="hand2", command=resetaccount_esp)
            changeusername_btn.place(x=40, y=97)
            changepassword_btn.place(x=40, y=155)

            changeaccount_btn_close.config(text="❎ Cerrar", font="SegoeUIVariable, 12")
            changeaccount_btn_change.config(text="✅ Cambiar", font="SegoeUIVariable, 12")

        # ============================================== LOAD/HIDE MSG ELEMENTS ============================================== #
        # ========== LOAD BASIC WINDOW CORE ========== #
        basics_msg = tk.Toplevel(dynamic_window)
        basics_msg.withdraw()
        basics_msg.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))

        basics_img = tk.PhotoImage()
        basics_imglb = tk.Label(basics_msg, image=basics_img)
        basics_msg_lb = tk.Label(basics_msg)
        changeaccount_btn_reset = tk.Button(basics_msg)
        basics_btn_ok = tk.Button(basics_msg, text="✅ OK", padx=15, pady=3, width=3, font="SegoeUIVariable, 12")
        basics_btn_yes = tk.Button(basics_msg, padx=15, pady=3, width=3, font="SegoeUIVariable, 12")
        basics_btn_no = tk.Button(basics_msg, padx=15, pady=3, width=3, font="SegoeUIVariable, 12")
        info_bf_lb = tk.Label(basics_msg)
        info_af_lb = tk.Label(basics_msg)
        id_inf = tk.Label(basics_msg, font=("SegoeUIVariable", 11, "bold"))
        brand_bf = tk.Label(basics_msg, font="SegoeUIVariable, 11")
        model_bf = tk.Label(basics_msg, font="SegoeUIVariable, 11")
        color_bf = tk.Label(basics_msg, font="SegoeUIVariable, 11")
        date_bf = tk.Label(basics_msg, font="SegoeUIVariable, 11")
        brand_af = tk.Label(basics_msg, font="SegoeUIVariable, 11")
        model_af = tk.Label(basics_msg, font="SegoeUIVariable, 11")
        color_af = tk.Label(basics_msg, font="SegoeUIVariable, 11")
        date_af = tk.Label(basics_msg, font="SegoeUIVariable, 11")


        basics_w_total = dynamic_window.winfo_screenwidth()
        basics_h_total = dynamic_window.winfo_screenheight()
        basics_w = 1
        basics_h = 1
        basics_width = round(basics_w_total/2-basics_w/2)
        basics_height = round(basics_h_total/2-basics_h/2)
        basics_msg.geometry(str(basics_w)+"x"+str(basics_h)+"+"+str(basics_width)+"+"+str(basics_height))

        # ========== LOAD CHANGEACCOUNT WINDOW ========== #
        changeaccount_msg = tk.Toplevel(dynamic_window)
        changeaccount_msg.withdraw()

        changeaccount_btn_back = tk.Button(changeaccount_msg, width=3, height=1)
        changeaccount_frame = tk.Frame(changeaccount_msg, height=1, bd=0)
        changeaccount_msg_lbm = tk.Label(changeaccount_msg)
        changeaccount_msg_lb1 = tk.Label(changeaccount_msg)
        changeaccount_msg_lb2 = tk.Label(changeaccount_msg)
        changeaccount_msg_lb3 = tk.Label(changeaccount_msg)
        changeaccount_msg_lb4 = tk.Label(changeaccount_msg)

        changeusername_btn = tk.Button(changeaccount_msg)
        changepassword_btn = tk.Button(changeaccount_msg)
        resetaccount_btn = tk.Button(changeaccount_msg)

        actual_username = tk.Entry(changeaccount_msg)
        new_username = tk.Entry(changeaccount_msg)
        actual_password = tk.Entry(changeaccount_msg, show="*")
        new_password = tk.Entry(changeaccount_msg, show="*")

        changeaccount_btn_close = tk.Button(changeaccount_msg)
        changeaccount_btn_change = tk.Button(changeaccount_msg)

        def hide_basic_msg():
            restore_elements()
            basics_msg.grab_release()
            basics_msg.transient(None)
            basics_msg.withdraw()
            basics_msg_lb.place_forget()
            basics_imglb.place_forget()
            basics_btn_ok.place_forget()
            basics_btn_yes.place_forget()
            basics_btn_no.place_forget()

        def hide_changeaccount_msg():
            restore_elements()
            changeaccount_msg.grab_release()
            changeaccount_msg.transient(None)
            changeaccount_msg.withdraw()
            changeaccount_back()

        def changeaccount_back():
            changeaccount_btn_back.place_forget()
            changeaccount_msg_lb1.place_forget()
            changeaccount_msg_lb2.place_forget()
            changeaccount_msg_lb3.place_forget()
            changeaccount_msg_lb4.place_forget()
            changeaccount_frame.place_forget()
            actual_username.place_forget()
            new_username.place_forget()
            actual_password.place_forget()
            new_password.place_forget()
            actual_username.delete(0, tk.END)
            new_username.delete(0, tk.END)
            actual_password.delete(0, tk.END)
            new_password.delete(0, tk.END)
            if loginprofile_imglb.winfo_ismapped():
                lang_value = languagegroup.get()
                if lang_value == 1:
                    resetaccount_btn.place(x=87, y=213)
                elif lang_value == 2:
                    resetaccount_btn.place(x=40, y=213)
            changeaccount_btn_close.place(x=138, y=300)
            changeaccount_btn_change.place_forget()
            lang_value = languagegroup.get()
            if lang_value == 1:
                changeaccount_eng()
            elif lang_value == 2:
                changeaccount_esp()

        def hide_reset_msg():
            restore_elements()
            basics_msg.grab_release()
            basics_msg.transient(None)
            basics_msg.withdraw()
            basics_btn_ok.place_forget()
            basics_btn_ok.config(text="✅ OK", padx=15, pady=3, width=3)
            changeaccount_btn_reset.place_forget()
            changeaccount_msg.grab_set()
            changeaccount_msg.focus_set()

        def resetaccount():
            if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data")):
                os.makedirs(os.path.join(os.path.dirname(__file__), "Data"))
            with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "w") as accountfile:
                accountfile.write("admin,12345\n")
            lang_value = languagegroup.get()
            if lang_value == 1:
                changeaccount_btn_reset.config(text="✅ Restored!", disabledforeground="#007A05", cursor="arrow", state="disabled")
            elif lang_value == 2:
                changeaccount_btn_reset.config(text="✅ Restablecido!", disabledforeground="#007A05", cursor="arrow", state="disabled")

        def enable_change_userdata():
            if actual_username.get() == "" or new_username.get() == "" or actual_password.get() == "":
                changeaccount_btn_change.config(state="disabled", cursor="arrow")
            else:
                changeaccount_btn_change.config(state="normal", cursor="hand2", command=change_userdata)

        def enable_change_passworddata():
            if actual_username.get() == "" or actual_password.get() == "" or new_password.get() == "":
                changeaccount_btn_change.config(state="disabled", cursor="arrow")
            else:
                changeaccount_btn_change.config(state="normal", cursor="hand2", command=change_passworddata)

        def change_userdata():
            try:
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "r") as accountfile:
                    accountreader = csv.reader(accountfile, delimiter=",")
                    accountdata = list(accountreader)
                actualusername = actual_username.get()
                newusername = new_username.get()
                if accountdata[0][0] == actualusername.lower() and accountdata[0][1] == actual_password.get():
                    for row in accountdata:
                        if row[0] == actualusername.lower() or row[1] == actual_password.get():
                            row[0] = newusername.lower()
                            break 
                    with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(accountdata)
                        file.seek(0, 2)
                    changeaccount_back()
                    if device_imglb.winfo_ismapped():
                        dynamic_window.title("Device Warehouse Inventory ("+newusername.lower()+")")
                    changeusername_correct_msg()
                else:
                    changeaccount_error_msg()
            except FileNotFoundError:
                error_wn()
                loadfile_error_msg()

        def change_passworddata():
            try:
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "r") as accountfile:
                    accountreader = csv.reader(accountfile, delimiter=",")
                    accountdata = list(accountreader)
                actualusername = actual_username.get()
                if accountdata[0][0] == actualusername.lower() and accountdata[0][1] == actual_password.get():
                    for row in accountdata:
                        if row[0] == actualusername.lower() or row[1] == actual_password.get():
                            row[1] = new_password.get()
                            break 
                    with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(accountdata)
                        file.seek(0, 2)
                    changeaccount_back()
                    changepassword_correct_msg()
                else:
                    changeaccount_error_msg()
            except FileNotFoundError:
                error_wn()
                loadfile_error_msg()

        # ============================================== LOAD/HIDE MSG WINDOWS ============================================== #
        # ========== CHANGE USERNAME WINDOW ========== #
        def changeusername():
            changeaccount_msg_lbm.place_forget()
            changeusername_btn.place_forget()
            changepassword_btn.place_forget()
            resetaccount_btn.place_forget()

            def validate_value_account(text):
                pattern = re.compile(r"^[a-zA-Z0-9]+$")
                if pattern.match(text) is not None:
                    return True and len(text) <= 20
                elif text == "":
                    return True and len(text) <= 20
                else:
                    return False
            
            changeaccount_frame.place(x=40, y=40, width=310, height=235)
            actual_username.focus()
            actual_username.config(width=25, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font="SegoeUIVariable, 12")
            new_username.config(width=25, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font="SegoeUIVariable, 12")
            actual_password.config(width=25, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font="SegoeUIVariable, 12") 
            
            actual_username.bind("<KeyRelease>", lambda event: enable_change_userdata())
            new_username.bind("<KeyRelease>", lambda event: enable_change_userdata())
            actual_password.bind("<KeyRelease>", lambda event: enable_change_userdata())

            lang_value = languagegroup.get()
            if lang_value == 1:
                changeaccount_msg_lb1.config(text="👤 Change Username", font="SegoeUIVariable, 12")
                changeaccount_msg_lb2.config(text="Actual Username:", font="SegoeUIVariable, 12")
                changeaccount_msg_lb3.config(text="New Username:", font="SegoeUIVariable, 12")
                changeaccount_msg_lb4.config(text="Password to Confirm:", font="SegoeUIVariable, 12")
            elif lang_value == 2:
                changeaccount_msg_lb1.config(text="👤 Cambiar Nombre de Usuario", font="SegoeUIVariable, 12")
                changeaccount_msg_lb2.config(text="Nombre de Usuario Actual:", font="SegoeUIVariable, 12")
                changeaccount_msg_lb3.config(text="Nuevo Nombre de Usuario:", font="SegoeUIVariable, 12")
                changeaccount_msg_lb4.config(text="Contraseña para Confirmar:", font="SegoeUIVariable, 12")

            actual_username.place(x=75, y=97, height=30)
            new_username.place(x=75, y=160, height=30)
            actual_password.place(x=75, y=223, height=30)

            changeaccount_msg_lb1.place(x=55, y=27)
            changeaccount_msg_lb2.place(x=75, y=72)
            changeaccount_msg_lb3.place(x=75, y=135)
            changeaccount_msg_lb4.place(x=75, y=198)

            changeaccount_btn_back.config(text="⬅️", font="SegoeUIVariable, 12", cursor="hand2", command=changeaccount_back)
            changeaccount_btn_back.place(x=0)

            changeaccount_btn_close.config(padx=35, pady=3, width=3, cursor="hand2", command=hide_changeaccount_msg)
            changeaccount_btn_change.config(padx=35, pady=3, width=3, state="disabled", cursor="arrow")
            changeaccount_btn_close.place(x=78, y=300)
            changeaccount_btn_change.place(x=210, y=300)

        # ========== CHANGE PASSWORD WINDOW ========== #
        def changepassword():
            changeaccount_msg_lbm.place_forget()
            changeusername_btn.place_forget()
            changepassword_btn.place_forget()
            resetaccount_btn.place_forget()

            def validate_value_account(text):
                pattern = re.compile(r"^[a-zA-Z0-9]+$")
                if pattern.match(text) is not None:
                    return True and len(text) <= 20
                elif text == "":
                    return True and len(text) <= 20
                else:
                    return False

            changeaccount_frame.place(x=40, y=40, width=310, height=235)
            actual_username.focus()
            actual_username.config(width=25, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font="SegoeUIVariable, 12")
            actual_password.config(width=25, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font="SegoeUIVariable, 12")
            new_password.config(width=25, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font="SegoeUIVariable, 12") 
            
            actual_username.bind("<KeyRelease>", lambda event: enable_change_passworddata())
            actual_password.bind("<KeyRelease>", lambda event: enable_change_passworddata())
            new_password.bind("<KeyRelease>", lambda event: enable_change_passworddata()) 

            lang_value = languagegroup.get()
            if lang_value == 1:
                changeaccount_msg_lb1.config(text="🔑 Change Password", font="SegoeUIVariable, 12")
                changeaccount_msg_lb2.config(text="Actual Username:", font="SegoeUIVariable, 12")
                changeaccount_msg_lb3.config(text="Actual Password:", font="SegoeUIVariable, 12")
                changeaccount_msg_lb4.config(text="New Password:", font="SegoeUIVariable, 12")
            elif lang_value == 2:
                changeaccount_msg_lb1.config(text="🔑 Cambiar Contraseña", font="SegoeUIVariable, 12")
                changeaccount_msg_lb2.config(text="Nombre de Usuario Actual:", font="SegoeUIVariable, 12")
                changeaccount_msg_lb3.config(text="Contraseña Actual:", font="SegoeUIVariable, 12")
                changeaccount_msg_lb4.config(text="Nueva Contraseña:", font="SegoeUIVariable, 12")

            actual_username.place(x=75, y=97, height=30)
            actual_password.place(x=75, y=160, height=30)
            new_password.place(x=75, y=223, height=30)

            changeaccount_msg_lb1.place(x=55, y=27)
            changeaccount_msg_lb2.place(x=75, y=72)
            changeaccount_msg_lb3.place(x=75, y=135)
            changeaccount_msg_lb4.place(x=75, y=198)

            changeaccount_btn_back.config(text="⬅️", font="SegoeUIVariable, 12", cursor="hand2", command=changeaccount_back)
            changeaccount_btn_back.place(x=0)

            changeaccount_btn_close.config(padx=35, pady=3, width=3, cursor="hand2", command=hide_changeaccount_msg)
            changeaccount_btn_change.config(padx=35, pady=3, width=3, state="disabled", cursor="arrow")
            changeaccount_btn_close.place(x=78, y=300)
            changeaccount_btn_change.place(x=210, y=300)

        # ========== CHANGE ACCOUNT ERROR MSG ========== #
        def changeaccount_error_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 417  
                elif lang_value == 2:
                    window_w = 495  
                window_h = 175
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))
                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_reset_msg())    
                if new_username.winfo_ismapped():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        basics_msg.title("Change Username")
                    elif lang_value == 2:
                        basics_msg.title("Cambiar Nombre de Usuario")
                if new_password.winfo_ismapped():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        basics_msg.title("Change Password")
                    elif lang_value == 2:
                        basics_msg.title("Cambiar Contraseña")   
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basics_imglb.place(x=15, y=30)
                actualusername = actual_username.get()
                if not accountdata[0][0] == actualusername.lower():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        basics_msg_lb.config(justify="center", text="Your Username/Password is incorrect!", font="SegoeUIVariable, 12")
                    elif lang_value == 2:
                        basics_msg_lb.config(justify="center", text="Tu Nombre de Usuario/Contraseña es incorrecto!", font="SegoeUIVariable, 12")
                if not accountdata[0][1] == actual_password.get():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        basics_msg_lb.config(justify="center", text="Your Username/Password is incorrect!", font="SegoeUIVariable, 12")
                    elif lang_value == 2:
                        basics_msg_lb.config(justify="center", text="Tu Nombre de Usuario/Contraseña es incorrecto!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)
                basics_btn_ok.config(command=hide_reset_msg)
                if lang_value == 1:
                    basics_btn_ok.place(x=177, y=125)
                elif lang_value == 2:
                    basics_btn_ok.place(x=216, y=125)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== CHANGE USERNMAME CORRECT MSG ========== #
        def changeusername_correct_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 417
                elif lang_value == 2:
                    window_w = 447
                window_h = 175
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_reset_msg()) 
                if lang_value == 1:
                    basics_msg.title("Change Username")
                elif lang_value == 2:
                    basics_msg.title("Cambiar Nombre de Usuario")  
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                if lang_value == 1:
                    basics_msg_lb.config(justify="center", text="Your Username has been CHANGED!", font="SegoeUIVariable, 12")
                elif lang_value == 2:
                    basics_msg_lb.config(justify="center", text="Tu Nombre de Usuario se ha CAMBIADO!", font="SegoeUIVariable, 12")
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_reset_msg)
                if lang_value == 1:
                    basics_btn_ok.place(x=177, y=125)
                elif lang_value == 2:
                    basics_btn_ok.place(x=192, y=125)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== CHANGE PASSWORD CORRECT MSG ========== #
        def changepassword_correct_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 417 
                elif lang_value == 2:
                    window_w = 393 
                window_h = 175
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_reset_msg()) 
                lang_value = languagegroup.get()
                if lang_value == 1:
                    basics_msg.title("Change Password")
                elif lang_value == 2:
                    basics_msg.title("Cambiar Contraseña")    
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                lang_value = languagegroup.get()
                if lang_value == 1:
                    basics_msg_lb.config(justify="center", text="Your Password has been CHANGED!", font="SegoeUIVariable, 12")
                elif lang_value == 2:
                    basics_msg_lb.config(justify="center", text="Tu Contraseña se ha CAMBIADO!", font="SegoeUIVariable, 12")
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_reset_msg)
                if lang_value == 1:
                    basics_btn_ok.place(x=177, y=125)
                elif lang_value == 2:
                    basics_btn_ok.place(x=165, y=125)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== RESET ACCOUNT MSG ENGLISH ========== #
        def resetaccount_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 290
                window_h = 225
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_reset_msg())
                basics_msg.title("Reset Default Account")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/remember.png"))
                basics_imglb.place(x=15, y=20)
                basics_msg_lb.config(justify="center", text="Default Account:\n\nUsername:  >   admin\nPassword:  >   12345", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=100, y=20)
                changeaccount_btn_reset.config(text="🔁 Reset to Default", padx=60, pady=3, width=3, font="SegoeUIVariable, 12", cursor="hand2", state="normal", command=resetaccount) 
                changeaccount_btn_reset.place(x=65, y=120)
                basics_btn_ok.config(text="❎ Close", padx=35, pady=3, width=3) #pady 15
                basics_btn_ok.config(command=hide_reset_msg)
                basics_btn_ok.place(x=89, y=175)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== RESET ACCOUNT MSG SPANISH ========== #
        def resetaccount_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 355
                window_h = 225
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_reset_msg())
                basics_msg.title("Restablecer Cuenta Predeterminada")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/remember.png"))
                basics_imglb.place(x=20, y=20)
                basics_msg_lb.config(justify="center", text="Cuenta Predeterminada:\n\nNombre de Usuario:  >  admin\nContraseña:               >  12345", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=105, y=20)

                changeaccount_btn_reset.config(text="🔁 Restablecer a Predeterminado", padx=110, pady=3, width=3, font="SegoeUIVariable, 12", cursor="hand2", state="normal", command=resetaccount) 
                changeaccount_btn_reset.place(x=50, y=120)
                basics_btn_ok.config(text="❎ Cerrar", padx=35, pady=3, width=3) #pady 15
                basics_btn_ok.config(command=hide_reset_msg)
                basics_btn_ok.place(x=124, y=175)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== CHANGEACCOUNT MSG ========== #
        def changeaccount():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 390
                window_h = 350
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                changeaccount_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                changeaccount_msg.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/changeaccount.ico"))
                changeaccount_msg.protocol("WM_DELETE_WINDOW", lambda: hide_changeaccount_msg())
                changeaccount_msg.resizable(width=False, height=False)
                changeaccount_msg.grab_set()
                changeaccount_msg.focus_set()
                if loginprofile_imglb.winfo_ismapped():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        resetaccount_btn.place(x=87, y=213)
                    elif lang_value == 2:
                        resetaccount_btn.place(x=40, y=213)
                changeaccount_btn_close.config(padx=35, pady=3, width=3, cursor="hand2", command=hide_changeaccount_msg)
                changeaccount_btn_close.place(x=138, y=300)
                changeaccount_btn_change.config(padx=35, pady=3, width=3, state="disabled", cursor="arrow")
                changeaccount_msg.transient(dynamic_window)
                changeaccount_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== CHANGELOG MSG ENGLISH ========== #
        def changelog_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 535 
                window_h = 450 
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Changelog in this Version")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/changelog.png"))
                basics_imglb.place(x=198, y=5)
                basics_msg_lb.config(justify="left", text="=====================  CHANGELOG  =====================\n\n                     <<<<<   VERSION 2.4 (21-FEB-2024)   >>>>>\n\n- Minor UI Tweaks.\n- Improved Some Dialog Window in Edit Mode and Delete Mode.\n- Deleted Date Entry in Add Mode (Now it will take the Date of the O.S).\n- Improved Error Window Program Logic.\n- Minor Improvements and Bugs Fixes.\n\n                                     Developed By Eliezer Brito\n                                             © Elie-Dev (2024)\n                                             All rights reserved", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=17, y=140)
                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=235, y=400)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== CHANGELOG MSG SPANISH ========== #
        def changelog_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 745 #445
                window_h = 450 #410
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Registro de Cambios en esta Version")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/changelog.png"))
                basics_imglb.place(x=304, y=5)
                basics_msg_lb.config(justify="left", text="==============================  Registro de Cambios  ==============================\n\n                                                <<<<<   VERSION 2.4 (21-FEB-2024)   >>>>>\n\n- Modificaciones Menores en la Interfaz de Usuario.\n- Se mejoro algunas Ventanas de Dialogo en el Modo Editar y Modo Eliminar.\n- El Campo de Texto (Fecha) se ha Eliminado para el Modo Agregar (Ahora tomara la Fecha del S.O.\n- Se Mejoro la Logica de las Ventanas de Error.\n- Mejoras Menores y Errores Corregidos.\n\n                                                                Desarrollado por Eliezer Brito\n                                                                        © Elie-Dev (2024)\n                                                             Todos los Derechos Reservados", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=17, y=140)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=338, y=400)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== ABOUT MSG ========== #
        def about_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 308
                window_h = 390
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("About the Program")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/about.png"))
                basics_imglb.place(x=90, y=5)
                basics_msg_lb.config(justify="center", text="Device Warehouse Inventory\nVersion: 2.4\n\nThis Program is to Add, Edit or Delete \nDevice information in the Inventory \nfrom the Local DataBase.\n\nDeveloped By Eliezer Brito\n© Elie-Dev (2024)\nAll rights reserved", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=17, y=140)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=122, y=340)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== ABOUT MSG SPANISH ========== #
        def about_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 390
                window_h = 390
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Acerca del Programa")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/about.png"))
                basics_imglb.place(x=132, y=5)
                basics_msg_lb.config(justify="center", text="Device Warehouse Inventory\nVersion: 2.4\n\nEste Programa es para Agregar, Editar o Eliminar \nInformacion del Dispositivo en el Inventario \nde la Base de Datos Local.\n\nDesarrollado por Eliezer Brito\n © Elie-Dev (2024) \nTodos los Derechos Reservados", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=17, y=140)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=340)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== HELP LOGIN MSG ENGLISH ========== #
        def login_help_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 460
                window_h = 210
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("How to Sign-In?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/helplogin.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Type your username and password, \nif the data is correct the application will start, \notherwise you will receive an error message.\n\nIf you still have problems logging in, \nPlease notify the Developer.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=20)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=198, y=160)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== HELP LOGIN MSG SPANISH ========== #
        def login_help_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 475
                window_h = 210
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Como Iniciar Sesion?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/helplogin.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Escribe tu Nombre de Usuario y Contraseña, \nsi los datos son correctos la aplicacion iniciara, \nde lo contrario recibiras un mensaje de error.\n\nSi aun tienes problemas para iniciar sesion, \nPor Favor Contacta al Desarrollador.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=20) 

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=208, y=160)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()
                
        # ========== LOGIN ERROR MSG ENGLISH ========== #
        def login_error_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 393
                window_h = 175
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Failed to Login")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Your Account is incorrect or invalid!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=125)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== LOGIN ERROR MSG SPANISH ========== #
        def login_error_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 393
                window_h = 175
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Error al Iniciar Sesion")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Tu Cuenta es Incorrecta o Invalida!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=125)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # =============================================================================================================================
        # ========== HELP MAIN MSG ENGLISH ========== #
        def main_help_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 445
                window_h = 185
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("How to use This Program?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/helplogin.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="To start, select one of the available options \nat the top to open each mode.\n\nIf you still have problems, \nPlease notify the Developer.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=20)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=185, y=135)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== HELP MAIN MSG SPANISH ========== #
        def main_help_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 480
                window_h = 185
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Como usar Este Programa?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/helplogin.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Para empezar, selecciona una de las opciones \ndisponibles en la parte superior de cada modo.\n\nSi aun tienes problemas, \nPor Favor Contacta al Desarrollador.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=20)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=210, y=135)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== ADD MODE HELP MSG ENGLISH ========== #
        def addmode_help_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 368
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("How to use ➕ Add Mode?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="To start, fill in the text fields and \npress the [➕ Add ] button.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=48)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=153, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== ADD MODE HELP MSG SPANISH ========== #
        def addmode_help_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 450
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Como usar el ➕ Modo Agregar?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Para empezar, llena los campos de texto y \npresiona el Boton [➕ Agregar ].", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=48)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=193, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EDIT MODE HELP MSG ENGLISH ========== #
        def editmode_help_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 387
                window_h = 180
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("How to use ✏️ Edit Mode?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="To start, type the correct ID, \npress the [🔎 Check ] button,\nthen choose the text field(s) to edit \nand press the [✏️ Edit ] button.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=30)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=154, y=130)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EDIT MODE HELP MSG SPANISH ========== #
        def editmode_help_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 444
                window_h = 180
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Como usar el ✏️ Modo Editar?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Para empezar, escribe el ID correcto, \npresiona el Boton [🔎 Comprobar ],\nluego elige el/los campos de texto a editar \ny presiona el Boton [✏️ Editar ].", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=30)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=190, y=130)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()
            
        # ========== DELETE MODE HELP MSG ENGLISH ========== #
        def deletemode_help_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 385
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("How can use ➖ Delete Mode")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="To start, type the correct ID \nand press the [➖ Delete ] button.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=48)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=161, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== DELETE MODE HELP SPANISH ========== #
        def deletemode_help_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 410
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Como usar el ➖ Modo Eliminar?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Para empezar, escribe el ID correcto \ny presiona el Boton [➖ Eliminar ].", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=48)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=173, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== ADD PRODUCT SAVE MSG ENGLISH ========== #
        def add_prod_save_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 450
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Adding to Inventory...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Your Product has been ADDED to Inventory!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=193, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== ADD PRODUCT SAVE MSG SPANISH ========== #
        def add_prod_save_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 465
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Agregando al Inventario...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Tu Producto se ha AGREGADO al Inventario!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=201, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== ADD PRODUCT EMPTY MSG ENGLISH ========== #
        def add_prod_empty_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 393
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Adding to Inventory...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="You can't leave EMPTY Text Fields!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== ADD PRODUCT EMPTY MSG SPANISH ========== #
        def add_prod_empty_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 490
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Agregando al Inventario...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="No Puedes dejar VACIOS los Campos de Texto!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=215, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EDIT PRODUCT SAVE MSG ENGLISH ========== #
        def edit_prod_save_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 478
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Editing in the Inventory...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Your Product has been EDITED in the Inventory!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=205, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EDIT PRODUCT SAVE MSG SPANIHS ========== #
        def edit_prod_save_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 465
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Editando en el Inventario...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Tu Producto se ha EDITADO en el Inventario!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=201, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EDIT PRODUCT NOTFOUND MSG ENGLISH ========== #
        def edit_prod_notfound_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 320
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Editing in the Inventory...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="This ID does not EXIST!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=130, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EDIT PRODUCT NOTFOUND MSG SPANISH ========== #
        def edit_prod_notfound_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 315
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Editando en el Inventario...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Este ID no Existe!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=128, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EDIT PRODUCT EMPTY MSG ENGLISH ========== #
        def edit_prod_empty_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 393
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Editing in the Inventory...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="You can't leave EMPTY Text Fields!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EDIT PRODUCT EMPTY MSG SPANISH ========== #
        def edit_prod_empty_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 490
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Editando en el Inventario...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="No Puedes dejar VACIOS los Campos de Texto!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=215, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EDIT PRODUCT ASK MSG ENGLISH ========== #
        def edit_prod_ask_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 890 
                window_h = 280 
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: edit_no())    
                basics_msg.title("Editing in the Inventory...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/ask.png"))
                basics_imglb.place(x=15, y=90) 
                basics_msg_lb.config(justify="center", text="Are you sure you want to EDIT it from inventory?\nThis action is IRREVERSIBLE!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=270, y=15) 
                info_bf_lb.config(justify="center", text="Before:", font=("SegoeUIVariable", 12, "bold"))
                info_bf_lb.place(x=120, y=70)
                id_inf.config(fg="#0078FF")
                id_inf.place(x=120, y=240)
                brand_bf.place(x=120, y=95)
                model_bf.place(x=310, y=95)
                color_bf.place(x=555, y=95)
                date_bf.place(x=720, y=95)

                info_af_lb.config(justify="center", text="After:", font=("SegoeUIVariable", 12, "bold"))
                info_af_lb.place(x=120, y=150)
                brand_af.place(x=120, y=175)
                model_af.place(x=310, y=175)
                color_af.place(x=555, y=175)
                date_af.place(x=720, y=175)

                basics_btn_yes.config(text="✅ Yes", fg="#0078FF", activeforeground="#0078FF")
                basics_btn_yes.place(x=365, y=230) 
                basics_btn_no.config(text="❎ No")
                basics_btn_no.place(x=460, y=230) 
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EDIT PRODUCT ASK MSG SPANISH ========== #
        def edit_prod_ask_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 890 
                window_h = 280 
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: edit_no())    
                basics_msg.title("Editando en el Inventario...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/ask.png"))
                basics_imglb.place(x=15, y=90) 
                basics_msg_lb.config(justify="center", text="Estas Seguro que quieres EDITARLO del Inventario?\nEsta accion es INRREVERSIBLE!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=270, y=15) 
                info_bf_lb.config(justify="center", text="Antes:", font=("SegoeUIVariable", 12, "bold"))
                info_bf_lb.place(x=120, y=70)
                id_inf.config(fg="#0078FF")
                id_inf.place(x=120, y=240)
                brand_bf.place(x=120, y=95)
                model_bf.place(x=310, y=95)
                color_bf.place(x=555, y=95)
                date_bf.place(x=720, y=95)

                info_af_lb.config(justify="center", text="Despues:", font=("SegoeUIVariable", 12, "bold"))
                info_af_lb.place(x=120, y=150)
                brand_af.place(x=120, y=175)
                model_af.place(x=310, y=175)
                color_af.place(x=555, y=175)
                date_af.place(x=720, y=175)

                basics_btn_yes.config(text="✅ Si", fg="#0078FF", activeforeground="#0078FF")
                basics_btn_yes.place(x=365, y=230) 
                basics_btn_no.config(text="❎ No")
                basics_btn_no.place(x=460, y=230) 
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== DELETE PRODUCT DEL MSG ENGLISH ========== #
        def delete_prod_del_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 495
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Deleting in the Inventory...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Your Product has been DELETED in the Inventory!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=210, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== DELETE PRODUCT DEL MSG SPANISH ========== #
        def delete_prod_del_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 470
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Eliminando en el Inventario...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Tu Profucto ha sido ELIMINADO del Inventario!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=203, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== DELETE PRODUCT NOTFOUND MSG ENGLISH ========== #
        def delete_prod_notfound_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 325
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Deleting in the Inventory...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="This ID does not EXIST!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=133, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== DELETE PRODUCT NOTFOUND MSG SPANISH ========== #
        def delete_prod_notfound_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 315
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Eliminando en el Inventario...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Este ID no Existe!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=128, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== DELETE PRODUCT EMPTY MSG ENGLISH ========== #
        def delete_prod_empty_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 393
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Deleting in the Inventory...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="You can't leave EMPTY Text Fields!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== DELETE PRODUCT EMPTY MSG SPANISH ========== #
        def delete_prod_empty_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 490
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Eliminando en el Inventario...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="No Puedes dejar VACIOS los Campos de Texto!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=215, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== DELETE PRODUCT ASK MSG ENGLISH ========== #
        def delete_prod_ask_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 890 
                window_h = 200 
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: del_no())    
                basics_msg.title("Deleting in the Inventory...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/ask.png"))
                basics_imglb.place(x=15, y=50) 
                basics_msg_lb.config(justify="center", text="Are you sure you want to DELETE it from inventory?\nThis action is IRREVERSIBLE!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=270, y=15) 
                info_bf_lb.config(justify="center", text="Info:", font=("SegoeUIVariable", 12, "bold"))
                info_bf_lb.place(x=120, y=70)
                id_inf.config(fg="#EB0000")
                id_inf.place(x=120, y=160)
                
                brand_bf.place(x=120, y=95)
                model_bf.place(x=310, y=95)
                color_bf.place(x=555, y=95)
                date_bf.place(x=720, y=95)

                basics_btn_yes.config(text="✅ Yes", fg="#EB0000", activeforeground="#EB0000")
                basics_btn_yes.place(x=365, y=150) 
                basics_btn_no.config(text="❎ No")
                basics_btn_no.place(x=460, y=150) 
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== DELETE PRODUCT ASK MSG SPANISH ========== #
        def delete_prod_ask_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 890 
                window_h = 200 
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: del_no())    
                basics_msg.title("Eliminando en el Inventario...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/ask.png"))
                basics_imglb.place(x=15, y=50) 
                basics_msg_lb.config(justify="center", text="Estas Seguro que quieres ELIMINARLO del Inventario?\nEsta accion es INRREVERSIBLE!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=270, y=15) 
                info_bf_lb.config(justify="center", text="Info:", font=("SegoeUIVariable", 12, "bold"))
                info_bf_lb.place(x=120, y=70)
                id_inf.config(fg="#EB0000")
                id_inf.place(x=120, y=160)
                
                brand_bf.place(x=120, y=95)
                model_bf.place(x=310, y=95)
                color_bf.place(x=555, y=95)
                date_bf.place(x=720, y=95)

                basics_btn_yes.config(text="✅ Si", fg="#EB0000", activeforeground="#EB0000")
                basics_btn_yes.place(x=365, y=150) 
                basics_btn_no.config(text="❎ No")
                basics_btn_no.place(x=460, y=150) 
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EXPORT FILE MSG ENGLISH ========== #
        def export_file_msg_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 513
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Exporting content to Text Files...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="The contents of the inventory have been EXPORTED \nto Text Files successfully!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=45)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=223, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== EXPORT FILE MSG SPANISH ========== #
        def export_file_msg_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 493
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Exportando el Contenido a los Archivos de Textos...")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="El contenido del Inventario ha sido EXPORTADO \na los Archivos de Texto Exitosamente!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=45)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=213, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== SIGN-OUT ASK MSG ENGLISH ========== #
        def signout_ask_eng():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 395
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Sign-Out")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/ask.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Are you sure you want to Sign-Out?", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=55)

                basics_btn_yes.config(text="✅ Yes", fg="#C19300", activeforeground="#C19300", command=signout)
                basics_btn_yes.place(x=118, y=115)
                basics_btn_no.config(text="❎ No", command=hide_basic_msg)
                basics_btn_no.place(x=213, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========== SIGN-OUT ASK MSG SPANISH ========== #
        def signout_ask_esp():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 440
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Cerrar Sesion")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/ask.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(justify="center", text="Estas Seguro que quieres Cerrar Sesion?", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=55)

                basics_btn_yes.config(text="✅ Si", fg="#C19300", activeforeground="#C19300", command=signout)
                basics_btn_yes.place(x=138, y=115)
                basics_btn_no.config(text="❎ No", command=hide_basic_msg)
                basics_btn_no.place(x=233, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ========================================================================================================= #
        def off_elements_msg(): 
            id_entry.config(cursor="arrow")
            brand_entry.config(cursor="arrow")
            model_entry.config(cursor="arrow")
            color_entry.config(cursor="arrow")
            date_entry.config(cursor="arrow")
            search_entry.config(cursor="arrow")

            addbtn.config(cursor="arrow")
            checkbtn.config(cursor="arrow")
            editbtn.config(cursor="arrow")
            cancelbtn.config(cursor="arrow")
            deletebtn.config(cursor="arrow")
            clearbtn.config(cursor="arrow")
            changeaccount_btn.config(cursor="arrow")
            modeshelp_btn.config(cursor="arrow")

            addrb.config(cursor="arrow")
            editrb.config(cursor="arrow")
            deleterb.config(cursor="arrow")
            
            settingsbtn.config(cursor="arrow")

            username_entry.config(cursor="arrow")
            password_entry.config(cursor="arrow")
            loginbtn.config(cursor="arrow")
            changeaccountlb.config(cursor="arrow")
            infobtn.config(cursor="arrow")

        def restore_elements():
            modes_value = modes_group.get()
            if modes_value == 1:
                brand_entry.config(cursor="xterm")
                model_entry.config(cursor="xterm")
                color_entry.config(cursor="xterm")
                date_entry.config(cursor="xterm")
            elif modes_value == 2:
                if editbtn.winfo_ismapped():
                    id_entry.config(cursor="arrow")
                    brand_entry.config(cursor="xterm")
                    model_entry.config(cursor="xterm")
                    color_entry.config(cursor="xterm")
                    date_entry.config(cursor="xterm")
                else:
                    id_entry.config(cursor="xterm")
                    brand_entry.config(cursor="arrow")
                    model_entry.config(cursor="arrow")
                    color_entry.config(cursor="arrow")
                    date_entry.config(cursor="arrow")
            elif modes_value == 3:
                id_entry.config(cursor="xterm")
            search_entry.config(cursor="xterm")

            addbtn.config(cursor="hand2")
            checkbtn.config(cursor="hand2")
            cancelbtn.config(cursor="hand2")
            editbtn.config(cursor="hand2")
            deletebtn.config(cursor="hand2")
            clearbtn.config(cursor="hand2")
            changeaccount_btn.config(cursor="hand2")
            modeshelp_btn.config(cursor="hand2")

            addrb.config(cursor="hand2")
            editrb.config(cursor="hand2")
            deleterb.config(cursor="hand2")

            settingsbtn.config(cursor="hand2")

            username_entry.config(cursor="xterm")
            password_entry.config(cursor="xterm")
            loginbtn.config(cursor="hand2")
            changeaccountlb.config(cursor="hand2")
            infobtn.config(cursor="hand2")

        # ========================================================================================================= #
        def signout():
            try:
                dynamic_window.withdraw()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    eng_lang_login()
                elif lang_value == 2:
                    esp_lang_login()
                hide_basic_msg()

                separator1.place_forget()
                separator3.place_forget()
                separator2.place_forget()

                mainmbar_btn.place_forget()
                aboutmbar_btn.place_forget()

                idlb.place_forget()
                brandlb.place_forget()
                modellb.place_forget()
                colorlb.place_forget()
                datelb.place_forget()
                inventorylb.place_forget()
                searchlb.place_forget()
                foundlb.place_forget()

                id_entry.place_forget()
                brand_entry.place_forget()
                model_entry.place_forget()
                color_entry.place_forget()
                date_entry.place_forget()
                search_entry.place_forget()

                inventory_table.place_forget()
                table_scrollbar.place_forget()

                addbtn.place_forget()
                checkbtn.place_forget()
                editbtn.place_forget()
                cancelbtn.place_forget()
                deletebtn.place_forget()
                clearbtn.place_forget()
                changeaccount_btn.place_forget()
                modeshelp_btn.place_forget()

                device_imglb.place_forget()

                addrb.place_forget()
                editrb.place_forget()
                deleterb.place_forget()
                
                setting_btn_apply.config(command=apply_settings_login)

                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                
                dynamic_window.protocol("WM_DELETE_WINDOW", lambda: close())
                dynamic_window.resizable(width=False, height=False)
                login_window_place()
                dynamic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))

                laboutmbar_btn.place(x=0, y=0)
                lmbar_separator.place(x=0, y=31, width=550, height=1)
                loginprofile_imglb.place(x=225, y=35)
                welcome_login.place(y=140)
                username_label.place(x=140, y=185)
                password_label.place(x=140, y=250)
                changeaccountlb.place(x=6, y=378)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    resetaccount_btn.place(x=87, y=213)
                elif lang_value == 2:
                    resetaccount_btn.place(x=40, y=213)
                username_entry.place(x=140, y=210, height=30)
                password_entry.place(x=140, y=275, height=30)
                loginbtn.place(y=320)
                infobtn.place(x=507, y=369)
                settingsbtn.place(x=514, y=0)
                basics_msg.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))
                dynamic_window.deiconify()
                dynamic_window.focus_force()
                username_entry.focus()
            except TclError:
                error_wn()
                loadfile_error_msg()
                
        def main_window():
            global username_entry, password_entry, dynamic_window, username, info_bf, info_af
            username_get = username_entry.get()
            username = username_get.lower()
            try:
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "r") as accountfile:
                    accountreader = csv.reader(accountfile, delimiter=",")
                    accountdata = list(accountreader)
                if accountdata[0][0] == username and accountdata[0][1] == password_entry.get():
                    dynamic_window.withdraw()
                    laboutmbar_btn.place_forget()
                    lmbar_separator.place_forget()
                    loginprofile_imglb.place_forget()
                    welcome_login.place_forget()
                    username_label.place_forget()
                    password_label.place_forget()
                    changeaccountlb.place_forget()
                    resetaccount_btn.place_forget()
                    username_entry.place_forget()
                    password_entry.place_forget()
                    loginbtn.place_forget()
                    infobtn.place_forget()
                    settingsbtn.place_forget()
                    setting_btn_apply.config(command=apply_settings_main)
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        eng_lang_mainwindow()
                        modeshelp_btn.config(command=addmode_help_eng)
                    elif lang_value == 2:
                        esp_lang_mainwindow()
                        modeshelp_btn.config(command=addmode_help_esp)

                    # ============================================== MAIN WINDOW FUNCTIONS ============================================== #  
                    def mainmenubar_mw():
                        mainmbar_btn.place(x=0, y=0, height=31, width=100)
                        aboutmbar_btn.place(y=0, height=31, width=100)

                    def labels_mw():
                        brandlb.place(x=388, y=403)
                        modellb.place(x=388, y=443)
                        colorlb.place(x=388, y=483)
                        inventorylb.place(x=18, y=116)
                        searchlb.place(x=596, y=114)

                    def separators_mw():
                        separator1.place(x=0, y=31, width=924, height=1)
                        separator2.place(x=0, y=108, width=924)
                        separator3.place(x=0, y=385, width=924)
            
                    def entrys_mw():
                        brand_entry.place(x=457, y=400, height=30)
                        model_entry.place(x=457, y=439, height=30)
                        color_entry.place(x=457, y=479, height=30)
                        search_entry.place(x=623, y=116, height=30)
                        
                    def clear_mw():
                        id_entry.delete(0, tk.END)
                        brand_entry.delete(0, tk.END)
                        model_entry.delete(0, tk.END)
                        color_entry.delete(0, tk.END)
                        date_entry.delete(0, tk.END)
                        modes_value = modes_group.get()
                        if modes_value == 1:
                            brand_entry.focus()
                        elif modes_value == 2:
                            id_entry.focus()
                        elif modes_value == 3:
                            id_entry.focus()

                    def buttons_mw():
                        addbtn.place(x=763, y=398, width=139)
                        clearbtn.place(x=763, y=438, width=139)
                        modeshelp_btn.place(x=815, y=0)
                        changeaccount_btn.place(x=851, y=0)

                    # ================================================================================================================== #  
                    def reflesh_inventory():
                        inventory_table.delete(*inventory_table.get_children())
                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r") as refleshfile:
                            data = refleshfile.readlines()
                        if len(data) > 10:
                            table_scrollbar.place(x=885, y=153, height=222, width=17)
                        else:
                            table_scrollbar.place_forget()
                        for row in data:
                            id, brand, model, color, date = row.strip().split(",")
                            inventory_table.insert("", "end", values=(id, brand, model, color, date))


                    def search_byid():
                        file = open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r")
                        reader = csv.reader(file)
                        data = list(reader)
                        inventory_table.delete(*inventory_table.get_children())
                        id_get = search_entry.get()
                        idget = id_get.upper()
                        if any(idget in row[0] for row in data):
                            foundlb.place_forget()
                            filtered_data = [row for row in data if idget in row[0].upper()]
                            inventory_table.delete(*inventory_table.get_children())
                            if len(filtered_data) > 10:
                                table_scrollbar.place(x=885, y=153, height=222, width=17)
                            else:
                                table_scrollbar.place_forget()
                            for row in filtered_data:
                                inventory_table.insert('', 'end', values=row)
                        else:
                            table_scrollbar.place_forget()
                            lang_value = languagegroup.get()
                            if lang_value == 1:
                                foundlb.config(text="Not Found")
                                foundlb.place(x=421, y=250)
                            elif lang_value == 2:
                                foundlb.config(text="No Encontrado")
                                foundlb.place(x=406, y=250)
                            
                    def optionselected_mode(action):
                        global rb_selected
                        rb_selected = action.widget
                        if rb_selected.cget("value") == 1:
                            try:
                                addrb.select()
                                device_imglb.place(x=15, y=396)
                                dynamic_window.geometry("923x585")
                                device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/devices1.png"))
                                device_imglb.config(image=device_img)
                                clear_mw()
                                brandlb.config(state="normal")
                                modellb.config(state="normal")
                                colorlb.config(state="normal")
                                brand_entry.config(state="normal", cursor="xterm")
                                model_entry.config(state="normal", cursor="xterm")
                                color_entry.config(state="normal", cursor="xterm")
                                checkbtn.place_forget()
                                cancelbtn.place_forget()
                                editbtn.place_forget()
                                deletebtn.place_forget()
                                addbtn.config(cursor="hand2", command=add_inventory)
                                clearbtn.config(cursor="hand2", command=clear_mw)
                                addbtn.place(x=763, y=398, width=139)
                                clearbtn.place(x=763, y=438, width=139)
                                
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    modeshelp_btn.config(command=addmode_help_eng)
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Search by ID...")
                                elif lang_value == 2:
                                    modeshelp_btn.config(command=addmode_help_esp)
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Buscar por ID...")

                                idlb.place_forget()
                                id_entry.place_forget()
                                datelb.place_forget()
                                date_entry.place_forget()
                                brandlb.config(fg="#00A007")
                                modellb.config(fg="#00A007")
                                colorlb.config(fg="#00A007")
                                brand_entry.config(cursor= "xterm", highlightcolor="#00A007", highlightbackground="#00A007", highlightthickness=2)
                                model_entry.config(cursor= "xterm", highlightcolor="#00A007", highlightbackground="#00A007", highlightthickness=2)
                                color_entry.config(cursor= "xterm", highlightcolor="#00A007", highlightbackground="#00A007", highlightthickness=2) 
                                brand_entry.focus()
                                brandlb.place(x=388, y=403)
                                modellb.place(x=388, y=443)
                                colorlb.place(x=388, y=483)
                                brand_entry.place(x=457, y=400, height=30)
                                model_entry.place(x=457, y=439, height=30)
                                color_entry.place(x=457, y=479, height=30)
                                
                                reflesh_inventory()
                            except ValueError:
                                error_wn()
                                loaddata_error_msg()
                            except TclError:
                                error_wn()
                                loadfile_error_msg()

                        elif rb_selected.cget("value") == 2:
                            try:
                                editrb.select()
                                device_imglb.place(x=15, y=396)
                                dynamic_window.geometry("923x610")
                                device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/devices1.png"))
                                device_imglb.config(image=device_img)
                                clear_mw()
                                brandlb.config(state="disabled")
                                modellb.config(state="disabled")
                                colorlb.config(state="disabled")
                                datelb.config(state="disabled")
                                brand_entry.config(state="disabled", cursor="arrow")
                                model_entry.config(state="disabled", cursor="arrow")
                                color_entry.config(state="disabled", cursor="arrow")
                                date_entry.config(state="disabled", cursor="arrow")

                                addbtn.place_forget()
                                deletebtn.place_forget()
                                editbtn.config(cursor="hand2", command=edit_inventory)
                                checkbtn.config(cursor="hand2", command=edit_check_inventory)
                                cancelbtn.config(cursor="hand2", command=edit_cancel_inventory)
                                clearbtn.config(cursor="hand2", command=clear_mw)
                                
                                checkbtn.place(x=763, y=398, width=139)
                                clearbtn.place(x=763, y=438, width=139)
                                editbtn.place_forget()

                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    modeshelp_btn.config(command=editmode_help_eng)
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Search by ID...")
                                elif lang_value == 2:
                                    modeshelp_btn.config(command=editmode_help_esp)
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Buscar por ID...")
                                theme_value = themegroup.get()
                                if theme_value == 1:
                                    id_entry.config(fg="white", insertbackground="white", highlightcolor="#0078FF", highlightbackground="#0078FF", highlightthickness=2, cursor="xterm", state="normal")
                                    brand_entry.config(background="#111111", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                    model_entry.config(background="#111111", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                    color_entry.config(background="#111111", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                    date_entry.config(background="#111111", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                elif theme_value == 2:
                                    id_entry.config(fg="black", insertbackground="black", highlightcolor="#0078FF", highlightbackground="#0078FF", highlightthickness=2, cursor="xterm", state="normal")
                                    brand_entry.config(background="#F9F9F9", highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, state="disabled")
                                    model_entry.config(background="#F9F9F9", highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, state="disabled")
                                    color_entry.config(background="#F9F9F9", highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, state="disabled")
                                    date_entry.config(background="#F9F9F9", highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, state="disabled")
                                    
                                idlb.place(x=388, y=403)
                                id_entry.place(x=457, y=400, height=30)

                                idlb.config(fg="#0078FF")
                                brandlb.config(fg="#0078FF")
                                modellb.config(fg="#0078FF")
                                colorlb.config(fg="#0078FF")
                                datelb.config(fg="#0078FF")

                                id_entry.delete(0, tk.END)
                                id_entry.focus()
                                brandlb.place(x=388, y=443)
                                modellb.place(x=388, y=483)
                                colorlb.place(x=388, y=523)
                                datelb.place(x=388, y=563)
                                brand_entry.place(x=457, y=439, height=30)
                                model_entry.place(x=457, y=479, height=30)
                                color_entry.place(x=457, y=519, height=30)
                                date_entry.place(x=457, y=559, height=30)
                                reflesh_inventory()
                            except ValueError:
                                error_wn()
                                loaddata_error_msg()
                            except TclError:
                                error_wn()
                                loadfile_error_msg()

                        elif rb_selected.cget("value") == 3:
                            try:
                                deleterb.select()
                                device_imglb.place(x=15, y=396)
                                dynamic_window.geometry("923x490")
                                device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/devices2.png"))
                                device_imglb.config(image=device_img)
                                addbtn.place_forget()
                                checkbtn.place_forget()
                                cancelbtn.place_forget()
                                editbtn.place_forget()
                                deletebtn.config(cursor="hand2", command=del_inventory)
                                clearbtn.config(cursor="hand2", command=clear_mw)
                                deletebtn.place(x=763, y=398, width=139)
                                clearbtn.place(x=763, y=438, width=139)
                                
                                brandlb.place_forget()
                                modellb.place_forget()
                                colorlb.place_forget()
                                datelb.place_forget()
                                brand_entry.place_forget()
                                model_entry.place_forget()
                                color_entry.place_forget()
                                date_entry.place_forget()

                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    modeshelp_btn.config(command=deletemode_help_eng)
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Search by ID...")
                                elif lang_value == 2:
                                    modeshelp_btn.config(command=deletemode_help_esp)
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Buscar por ID...")

                                idlb.place(x=388, y=403)
                                id_entry.place(x=457, y=400, height=30)
                                idlb.config(fg="#FE2727")
                                id_entry.config(fg="#FE2727", insertbackground="#FE2727", highlightcolor="#FE2727", highlightbackground="#FE2727", highlightthickness=2, cursor="xterm", state="normal")
                                clear_mw()
                                id_entry.focus()
                                reflesh_inventory()
                            except ValueError:
                                error_wn()
                                loaddata_error_msg()
                            except TclError:
                                error_wn()
                                loadfile_error_msg()
                    
                    def add_inventory():
                        id_get = id_entry.get()
                        brand_get = brand_entry.get()
                        model_get = model_entry.get()
                        color_get = color_entry.get()
                        id_upper = id_get.upper()
                        brand_upper = brand_get.upper()
                        model_upper = model_get.upper()
                        color_upper = color_get.upper()
                        date_os = datetime.datetime.now()
                        date_format = date_os.strftime("%d-%m-%Y %I:%M %p")      
                        if "" in id_upper and brand_upper and model_upper and color_upper and date_format: 
                            try:
                                def id_custom():
                                    generated_ids = set()
                                    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r", newline="") as file:
                                        for line in file:
                                            id_number = line.split(",")[0]
                                            generated_ids.add(id_number)
                                    while True:
                                        id_number = random.randint(1000000, 9999999)
                                        if id_number not in generated_ids:
                                            generated_ids.add(id_number)
                                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "a", newline="") as file:
                                                writer = csv.writer(file)
                                                writer.writerow([id_number, brand_upper, model_upper, color_upper, date_format])
                                                file.seek(0, 2)
                                            return id_number
                                id_custom()
                                clear_mw() 
                                reflesh_inventory()         
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Search by ID...")
                                    add_prod_save_eng()
                                elif lang_value == 2:
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Buscar por ID...")
                                    add_prod_save_esp()
                            except ValueError:
                                error_wn()
                                loaddata_error_msg()
                            except TclError:
                                error_wn()
                                loadfile_error_msg()  
                        else:
                            lang_value = languagegroup.get()
                            if lang_value == 1:
                                add_prod_empty_eng()
                            elif lang_value == 2:
                                add_prod_empty_esp()

                    def edit_check_inventory():
                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r", newline="") as file:
                                reader = csv.reader(file)
                                data = list(reader)
                        id_get = id_entry.get()
                        id_upper = id_get.upper()
                        ids = set([row[0].upper() for row in data])
                        if not id_upper in ids:
                            if id_upper == "":
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    edit_prod_empty_eng()
                                elif lang_value == 2:
                                    edit_prod_empty_esp() 
                            else:
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    edit_prod_notfound_eng()
                                elif lang_value == 2:
                                    edit_prod_notfound_esp()
                        elif id_upper in ids:
                            clearbtn.place_forget()
                            cancelbtn.place(x=763, y=438, width=139)
                            editbtn.place(x=763, y=398, width=139)
                            theme_value = themegroup.get()
                            if theme_value == 1:
                                brandlb.config(fg="#0078FF", state="normal")
                                modellb.config(fg="#0078FF", state="normal")
                                colorlb.config(fg="#0078FF", state="normal")
                                datelb.config(fg="#0078FF", state="normal")
                                id_entry.config(disabledforeground="#0078FF", disabledbackground="black", cursor="arrow", state="disabled")
                                brand_entry.config(background="#111111", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                                model_entry.config(background="#111111", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                                color_entry.config(background="#111111", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                                date_entry.config(background="#111111", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                            elif theme_value == 2:
                                brandlb.config(fg="#0078FF", state="normal")
                                modellb.config(fg="#0078FF", state="normal")
                                colorlb.config(fg="#0078FF", state="normal")
                                datelb.config(fg="#0078FF", state="normal")
                                id_entry.config(disabledforeground="#0078FF", disabledbackground="white", cursor="arrow", state="disabled")
                                brand_entry.config(background="#F9F9F9", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="black", insertbackground="black", highlightthickness=2, cursor="xterm", state="normal")
                                model_entry.config(background="#F9F9F9", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="black", insertbackground="black", highlightthickness=2, cursor="xterm", state="normal")
                                color_entry.config(background="#F9F9F9", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="black", insertbackground="black", highlightthickness=2, cursor="xterm", state="normal")
                                date_entry.config(background="#F9F9F9", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="black", insertbackground="black", highlightthickness=2, cursor="xterm", state="normal")
                            clear_mw()
                            brand_entry.focus()
                            for row in data:
                                if row[0] == id_upper:
                                    brand_entry.insert(tk.END, row[1])
                                    model_entry.insert(tk.END, row[2])
                                    color_entry.insert(tk.END, row[3])
                                    date_entry.insert(tk.END, row[4])
                                    break 
                    
                    def edit_cancel_inventory():
                        clear_mw()
                        checkbtn.place(x=763, y=398, width=139)
                        clearbtn.place(x=763, y=438, width=139)
                        editbtn.place_forget()
                        cancelbtn.place_forget()
                        theme_value = themegroup.get()
                        if theme_value == 1:
                            brandlb.config(fg="#0078FF", state="disabled")
                            modellb.config(fg="#0078FF", state="disabled")
                            colorlb.config(fg="#0078FF", state="disabled")
                            datelb.config(fg="#0078FF", state="disabled")
                            id_entry.config(background="#111111", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                            brand_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, cursor="arrow", state="disabled")
                            model_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, cursor="arrow", state="disabled")
                            color_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, cursor="arrow", state="disabled")
                            date_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, cursor="arrow", state="disabled")
                        elif theme_value == 2:
                            brandlb.config(fg="#0078FF", state="disabled")
                            modellb.config(fg="#0078FF", state="disabled")
                            colorlb.config(fg="#0078FF", state="disabled")
                            datelb.config(fg="#0078FF", state="disabled")
                            id_entry.config(background="#F9F9F9", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="black", insertbackground="black", highlightthickness=2, cursor="xterm", state="normal")
                            brand_entry.config(highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, cursor="arrow", state="disabled")
                            model_entry.config(highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, cursor="arrow", state="disabled")
                            color_entry.config(highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, cursor="arrow", state="disabled")
                            date_entry.config(highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, cursor="arrow", state="disabled")
                        id_entry.delete(0, tk.END)
                        id_entry.focus()

                    def edit_inventory():
                        global edit_no
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
                        info_bf()    
                        info_af()
                        if "" in id_upper and brand_upper and model_upper and color_upper and date_upper:
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r", newline="") as file:
                                reader = csv.reader(file)
                                data = list(reader)
                            ids = set([row[0].upper() for row in data])
                            if id_upper in ids:                     
                                basics_btn_ok.place_forget()
                                lang_value = languagegroup.get()   
                                if lang_value == 1:
                                    edit_prod_ask_eng()
                                elif lang_value == 2:
                                    edit_prod_ask_esp()
                            def edit_yes():
                                try:
                                    basics_msg.withdraw()
                                    basics_btn_yes.place_forget()
                                    basics_btn_no.place_forget()
                                    info_bf_lb.place_forget()
                                    info_af_lb.place_forget()
                                    id_inf.place_forget()
                                    brand_bf.place_forget()
                                    model_bf.place_forget()
                                    color_bf.place_forget()
                                    date_bf.place_forget()
                                    brand_af.place_forget()
                                    model_af.place_forget()
                                    color_af.place_forget()
                                    date_af.place_forget()
                                    for row in data:
                                        if row[0] == id_upper:
                                            row[1] = brand_upper
                                            row[2] = model_upper
                                            row[3] = color_upper
                                            row[4] = date_upper
                                            break 
                                    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "w", newline="") as file:
                                        writer = csv.writer(file)
                                        writer.writerows(data)
                                        file.seek(0, 2)
                                    clear_mw()
                                    reflesh_inventory()
                                    edit_cancel_inventory()
                                    id_entry.delete(0, tk.END)
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        search_entry.delete(0, tk.END)
                                        search_entry.insert(0, "Search by ID...")
                                        edit_prod_save_eng()
                                    elif lang_value == 2:
                                        search_entry.delete(0, tk.END)
                                        search_entry.insert(0, "Buscar por ID...")
                                        edit_prod_save_esp()
                                except ValueError:
                                    error_wn()
                                    loaddata_error_msg()
                                except TclError:
                                    error_wn()
                                    loadfile_error_msg() 
                            def edit_no():
                                restore_elements()
                                basics_msg.withdraw()
                                basics_btn_yes.place_forget()
                                basics_btn_no.place_forget()
                                info_bf_lb.place_forget()
                                info_af_lb.place_forget()
                                id_inf.place_forget()
                                brand_bf.place_forget()
                                model_bf.place_forget()
                                color_bf.place_forget()
                                date_bf.place_forget()
                                brand_af.place_forget()
                                model_af.place_forget()
                                color_af.place_forget()
                                date_af.place_forget()
                                basics_msg.grab_release()
                                basics_msg.transient(None)
                            basics_btn_yes.config(command=edit_yes)
                            basics_btn_no.config(command=edit_no)  
                        elif brand_upper == "" or model_upper == "" or color_upper == "" or date_upper == "":
                            lang_value = languagegroup.get()
                            if lang_value == 1:
                                edit_prod_empty_eng()
                            elif lang_value == 2:
                                edit_prod_empty_esp() 

                    def info_bf():
                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r", newline="") as file:
                                reader = csv.reader(file)
                                data = list(reader)
                        ids = set([row[0].upper() for row in data])
                        if id_entry.get() in ids:
                            lang_value = languagegroup.get()
                            if lang_value == 1:
                                for row in data:
                                    if row[0] == id_entry.get():
                                        id_inf.config(text="ID: "+str(row[0]))
                                        brand_bf.config(text="Brand:\n"+str(row[1]))
                                        model_bf.config(text="Model:\n"+str(row[2]))
                                        color_bf.config(text="Color:\n"+str(row[3]))
                                        date_bf.config(text="Registered Date:\n"+str(row[4]))
                                        break 
                            elif lang_value == 2:
                                for row in data:
                                    if row[0] == id_entry.get():
                                        id_inf.config(text="ID: "+str(row[0]))
                                        brand_bf.config(text="Marca:\n"+str(row[1]))
                                        model_bf.config(text="Modelo:\n"+str(row[2]))
                                        color_bf.config(text="Color:\n"+str(row[3]))
                                        date_bf.config(text="Fecha de Registro:\n"+str(row[4]))
                                        break 
                    
                    def info_af():
                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r", newline="") as file:
                                reader = csv.reader(file)
                                data = list(reader)
                        brand_get = brand_entry.get()
                        brand_upper = brand_get.upper()
                        model_get = model_entry.get()
                        model_upper = model_get.upper()
                        color_get = color_entry.get()
                        color_upper = color_get.upper()
                        date_get = date_entry.get()
                        date_upper = date_get.upper()
                        ids = set([row[0].upper() for row in data])
                        if id_entry.get() in ids:
                            lang_value = languagegroup.get()
                            if lang_value == 1:
                                for row in data:
                                    if row[0] == id_entry.get():
                                        theme_value = themegroup.get()
                                        if row[1] != brand_upper:
                                            brand_af.config(fg="#C19300")
                                            brand_af.config(text="Brand:\n"+str(brand_upper))
                                        else:
                                            if theme_value == 1:
                                                brand_af.config(fg="white")
                                            elif theme_value == 2:
                                                brand_af.config(fg="black")
                                            brand_af.config(text="Brand:\n"+str(brand_upper))
                                        if row[2] != model_upper:
                                            model_af.config(fg="#C19300")
                                            model_af.config(text="Model:\n"+str(model_upper))
                                        else:
                                            if theme_value == 1:
                                                model_af.config(fg="white")
                                            elif theme_value == 2:
                                                model_af.config(fg="black")
                                            model_af.config(text="Model:\n"+str(model_upper))
                                        if row[3] != color_upper:
                                            color_af.config(fg="#C19300")
                                            color_af.config(text="Color:\n"+str(color_upper))
                                        else:
                                            if theme_value == 1:
                                                color_af.config(fg="white")
                                            elif theme_value == 2:
                                                color_af.config(fg="black")
                                            color_af.config(text="Color:\n"+str(color_upper))
                                        if row[4] != date_upper:
                                            date_af.config(fg="#C19300")
                                            date_af.config(text="Registered Date:\n"+str(date_upper))
                                        else:
                                            if theme_value == 1:
                                                date_af.config(fg="white")
                                            elif theme_value == 2:
                                                date_af.config(fg="black")
                                            date_af.config(text="Registered Date:\n"+str(date_upper))
                                        break 
                            elif lang_value == 2:
                                for row in data:
                                    if row[0] == id_entry.get():
                                        theme_value = themegroup.get()
                                        if row[1] != brand_upper:
                                            brand_af.config(fg="#C19300")
                                            brand_af.config(text="Marca:\n"+str(brand_upper))
                                        else:
                                            if theme_value == 1:
                                                brand_af.config(fg="white")
                                            elif theme_value == 2:
                                                brand_af.config(fg="black")
                                            brand_af.config(text="Marca:\n"+str(brand_upper))
                                        if row[2] != model_upper:
                                            model_af.config(fg="#C19300")
                                            model_af.config(text="Modelo:\n"+str(model_upper))
                                        else:
                                            if theme_value == 1:
                                                model_af.config(fg="white")
                                            elif theme_value == 2:
                                                model_af.config(fg="black")
                                            model_af.config(text="Modelo:\n"+str(model_upper))
                                        if row[3] != color_upper:
                                            color_af.config(fg="#C19300")
                                            color_af.config(text="Color:\n"+str(color_upper))
                                        else:
                                            if theme_value == 1:
                                                color_af.config(fg="white")
                                            elif theme_value == 2:
                                                color_af.config(fg="black")
                                            color_af.config(text="Color:\n"+str(color_upper))
                                        if row[4] != date_upper:
                                            date_af.config(fg="#C19300")
                                            date_af.config(text="Fecha de Registro:\n"+str(date_upper))
                                        else:
                                            if theme_value == 1:
                                                date_af.config(fg="white")
                                            elif theme_value == 2:
                                                date_af.config(fg="black")
                                            date_af.config(text="Fecha de Registro:\n"+str(date_upper))
                                        break 

                    def del_inventory():
                        global del_no
                        id_get = id_entry.get()
                        id_upper = id_get.upper()
                        info_bf()
                        if "" in id_upper:
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r", newline="") as file:
                                reader = csv.reader(file)
                                data = list(reader)
                            ids = set([row[0].upper() for row in data])
                            if id_upper in ids:                     
                                basics_btn_ok.place_forget()
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    delete_prod_ask_eng()
                                elif lang_value == 2:
                                    delete_prod_ask_esp()
                            ids = set([row[0].upper() for row in data])
                            if not id_upper in ids:
                                if id_upper == "":
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        delete_prod_empty_eng()
                                    elif lang_value == 2:
                                        delete_prod_empty_esp()
                                else:
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        delete_prod_notfound_eng()
                                    elif lang_value == 2:
                                        delete_prod_notfound_esp()
                            def del_yes():
                                info_bf_lb.place_forget()
                                id_inf.place_forget()
                                brand_bf.place_forget()
                                model_bf.place_forget()
                                color_bf.place_forget()
                                date_bf.place_forget()
                                try:
                                    basics_msg.withdraw()
                                    basics_btn_yes.place_forget()
                                    basics_btn_no.place_forget() 
                                    for row in data:
                                        if row[0].upper() == id_upper:
                                            data.remove(row)
                                    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "w", newline="") as file:
                                        writer = csv.writer(file)
                                        writer.writerows(data)
                                        file.seek(0, 2)
                                    clear_mw()
                                    reflesh_inventory()
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        search_entry.delete(0, tk.END)
                                        search_entry.insert(0, "Search by ID...")                            
                                        delete_prod_del_eng()
                                    elif lang_value == 2:
                                        search_entry.delete(0, tk.END)
                                        search_entry.insert(0, "Buscar por ID...")
                                        delete_prod_del_esp()
                                except ValueError:
                                    error_wn()
                                    loaddata_error_msg()
                                except TclError:
                                    error_wn()
                                    loadfile_error_msg() 
                            def del_no():
                                info_bf_lb.place_forget()
                                id_inf.place_forget()
                                brand_bf.place_forget()
                                model_bf.place_forget()
                                color_bf.place_forget()
                                date_bf.place_forget()
                                restore_elements()
                                basics_msg.withdraw()
                                basics_btn_yes.place_forget()
                                basics_btn_no.place_forget()
                                basics_msg.grab_release()
                                basics_msg.transient(None)
                            basics_btn_yes.config(command=del_yes)
                            basics_btn_no.config(command=del_no)  
                
                    def showexpotedfolder():
                        if not os.path.exists(os.path.join(os.path.dirname(__file__), "Exported")):   
                            os.makedirs(os.path.join(os.path.dirname(__file__), "Exported"))
                        os.startfile(os.path.join(os.path.dirname(__file__), "Exported"))

                    def exportfile():
                        try:
                            if not os.path.exists(os.path.join(os.path.dirname(__file__), "Exported")):   
                                os.makedirs(os.path.join(os.path.dirname(__file__), "Exported"))
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r", newline="") as file:
                                reader = csv.reader(file)
                                data = list(reader)
                            with open(os.path.join(os.path.dirname(__file__), 'Exported/Inventory List.txt'), 'w') as export_inventory:
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    export_inventory.write('ID            Brand                 Model                                  Color                  Registered Date\n-------------------------------------------------------------------------------------------------------------------------\n')
                                elif lang_value == 2:
                                    export_inventory.write('ID            Marca                 Modelo                                 Color                  Fecha de Registro\n-------------------------------------------------------------------------------------------------------------------------\n')
                                for row in data:
                                    export_inventory.write('{:<10}    {:<15}       {:<28}           {:<18}     {:<20}\n'.format(row[0], row[1], row[2], row[3], row[4]))
                            lang_value = languagegroup.get()
                            if lang_value == 1:
                                export_file_msg_eng()
                            elif lang_value == 2:
                                export_file_msg_esp()
                        except FileNotFoundError:
                            error_wn()
                            loadfile_error_msg()

                    # ========================================================================================================= #
                    dynamic_window.title("Device Warehouse Inventory ("+username+")")
                    dynamic_window.resizable(width=False, height=False)
                    main_window_place()
                    dynamic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/main.ico"))
                    basics_msg.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/main.ico"))
                        
                    # ========== DEVICE IMAGE ========== #
                    device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/devices1.png"))
                    device_imglb.config(image=device_img)
                    device_imglb.place(x=15, y=396)

                    # ========== DATA BASE TABLE ========== #
                    reflesh_inventory()
                    inventory_table.place(x=20, y=153)
                        
                    # ========== RADIO BUTTONS ========== #
                    addrb.config(indicatoron=False)
                    addrb.bind("<ButtonRelease-1>", optionselected_mode)
                    addrb.bind("<KeyRelease-space>", optionselected_mode)
                    addrb.place(x=57, y=42, width=120)
                    addrb.select()
                    editrb.config(indicatoron=False)
                    editrb.bind("<ButtonRelease-1>", optionselected_mode)
                    editrb.bind("<KeyRelease-space>", optionselected_mode)
                    editrb.place(x=403, y=42, width=120)
                    deleterb.config(indicatoron=False)
                    deleterb.bind("<ButtonRelease-1>", optionselected_mode)
                    deleterb.bind("<KeyRelease-space>", optionselected_mode)
                    deleterb.place(x=748, y=42, width=120)
                    
                    # ========== LABELS ========== #
                    brandlb.config(fg="#00A007", state="normal")
                    modellb.config(fg="#00A007", state="normal")
                    colorlb.config(fg="#00A007", state="normal")
                    searchlb.config(text="🔍", font="SegoeUIVariable, 15")
                    labels_mw()
                
                    # ========== TEXT ENTRIES ========== #
                    brand_entry.config(cursor="xterm", highlightcolor="#00A007", highlightbackground="#00A007", highlightthickness=2)
                    model_entry.config(cursor="xterm", highlightcolor="#00A007", highlightbackground="#00A007", highlightthickness=2)
                    color_entry.config(cursor="xterm", highlightcolor="#00A007", highlightbackground="#00A007", highlightthickness=2)
                    brand_entry.delete(0, tk.END)
                    model_entry.delete(0, tk.END)
                    color_entry.delete(0, tk.END)
                    search_entry.bind("<KeyRelease>", lambda event: search_byid())         
                    entrys_mw()

                    # ========== BUTTONS ========== #
                    addbtn.config(cursor="hand2", command=add_inventory)
                    checkbtn.config(cursor="hand2",)
                    cancelbtn.config(cursor="hand2")
                    editbtn.config(cursor="hand2")
                    deletebtn.config(cursor="hand2")
                    clearbtn.config(cursor="hand2", command=clear_mw)
                    buttons_mw()
                    settingsbtn.place(x=887, y=0)
                    
                    # ========== SEPARATORS ========== #
                    separators_mw()

                    # ========== MENU BARS ========== #
                    mainmbar.entryconfigure(0, command=showexpotedfolder)
                    mainmbar.entryconfigure(1, command=exportfile)
                    mainmenubar_mw()
                    dynamic_window.deiconify()
                else:
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        login_error_eng()
                    elif lang_value == 2:
                        login_error_esp()
            except NameError:
                error_wn()
                corruptprogram_error_msg()
            except TclError:
                error_wn()
                loadfile_error_msg()
            except ValueError:
                error_wn()
                loaddata_error_msg()
            except FileNotFoundError:
                error_wn()
                loadfile_error_msg()

        # ============================================== LOAD ALL WINDOWS ELEMENTS ============================================== #
        def settings():
            try:
                setting_w_total = dynamic_window.winfo_screenwidth()
                setting_h_total = dynamic_window.winfo_screenheight()
                setting_w = 389
                setting_h = 300
                setting_width = round(setting_w_total/2-setting_w/2)
                setting_height = round(setting_h_total/2-setting_h/2-100)
                settings_window.geometry(str(setting_w)+"x"+str(setting_h)+"+"+str(setting_width)+"+"+str(setting_height))

                off_elements_msg()
                settings_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/settings.ico"))
                settings_window.protocol("WM_DELETE_WINDOW", lambda: hide_settings())
                settings_window.resizable(width=False, height=False)
                settings_window.grab_set()
                settings_window.focus_set()

                themeframe.place(x=70, y=33, width=250, height=75)
                languageframe.place(x=70, y=145, width=250, height=75)

                themelb.place(x=85, y=20)
                languagelb.place(x=85, y=132)

                lightthemerb.config(command=change_setting)
                darkthemerb.config(command=change_setting)
                eng_langrb.config(command=change_setting)
                esp_langrb.config(command=change_setting)

                lightthemerb.place(x=90, y=51)
                darkthemerb.place(x=205, y=51)
                eng_langrb.place(x=90, y=170)
                esp_langrb.place(x=205,y=170)

                setting_btn_close.config(command=hide_settings)
                setting_btn_close.place(x=78, y=250)

                setting_btn_apply.config(state="disabled", cursor="arrow")
                setting_btn_apply.place(x=210, y=250)

                settings_window.transient(dynamic_window)
                settings_window.deiconify()
            except NameError:
                error_wn()
                corruptprogram_error_msg()
            except TclError:
                error_wn()
                loadfile_error_msg()

        # ============================================== LIGHT/DARK LOGIN WINDOWS THEME ============================================== #
        def loginmenubar_dark():
            lmbar_separator.config(bg="#404040")
            laboutmbar_btn.config(background="black", foreground="white", activebackground="#292929", activeforeground="white")
            laboutmbar.config(bg="black")
            laboutmbar.entryconfigure(0, background="black", foreground="white")
            laboutmbar.entryconfigure(1, background="black")
            laboutmbar.entryconfigure(2, background="black", foreground="white")
            laboutmbar.entryconfigure(3, background="black", foreground="white")

        def loginmenubar_light():
            lmbar_separator.config(bg="#C0C0C0")
            laboutmbar_btn.config(background="white", foreground="black", activebackground="#E7E7E7", activeforeground="black")
            laboutmbar.config(bg="white")
            laboutmbar.entryconfigure(0, background="white", foreground="black")
            laboutmbar.entryconfigure(1, background="white")
            laboutmbar.entryconfigure(2, background="white", foreground="black")
            laboutmbar.entryconfigure(3, background="white", foreground="black")

        def loginlabels_light():
            loginprofile_imglb.config(bg="white")
            welcome_login.config(fg="black", bg="white")
            username_label.config(fg="black", bg="white")
            password_label.config(fg="black", bg="white")
            changeaccountlb.config(bg="white")

        def loginlabels_dark():
            loginprofile_imglb.config(bg="black")
            welcome_login.config(fg="white", bg="black")
            username_label.config(fg="white", bg="black")
            password_label.config(fg="white", bg="black")
            changeaccountlb.config(bg="black")

        def loginentrys_light():    
            username_entry.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
            password_entry.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)

        def loginentrys_dark():
            username_entry.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
            password_entry.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
            
        def loginbuttons_light():
            loginbtn.config(fg="#C19300", activeforeground="#C19300", bg="white", activebackground= "#EFEFEF")
            infobtn.config(fg="black", activeforeground="black", bg="white", activebackground= "#EFEFEF")

        def loginbuttons_dark():
            loginbtn.config(fg="#C19300", activeforeground="#C19300", bg="black", activebackground= "#111111")
            infobtn.config(fg="white", activeforeground="white", bg="black", activebackground= "#111111")

        def changeaccount_light():
            changeaccount_msg.config(bg="white")
            changeaccount_msg_lbm.config(bg="white", fg="black")
            changeaccount_msg_lb1.config(bg="white", fg="black")
            changeaccount_msg_lb2.config(bg="white", fg="black")
            changeaccount_msg_lb3.config(bg="white", fg="black")
            changeaccount_msg_lb4.config(bg="white", fg="black")
            changeaccount_frame.config(highlightbackground="#C0C0C0", highlightthickness=2, bg="white")

            actual_username.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
            actual_password.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
            new_username.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
            new_password.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)

            changeusername_btn.config(bg="white", fg="black", activeforeground="black", activebackground="#EFEFEF")
            changepassword_btn.config(bg="white", fg="black", activeforeground="black", activebackground="#EFEFEF")
            resetaccount_btn.config(bg="white", fg="#C19300", activeforeground="#C19300", activebackground="#EFEFEF")
            changeaccount_btn_back.config(bg="white", fg="black", activeforeground="black", activebackground="#EFEFEF")
            changeaccount_btn_close.config(bg="white", fg="black", activeforeground="black", activebackground="#EFEFEF")
            changeaccount_btn_change.config(bg="white", fg="black", activeforeground="black", activebackground="#EFEFEF", disabledforeground="#999999")
            changeaccount_btn_reset.config(bg="white", fg="#C19300", activeforeground="#C19300", activebackground="#EFEFEF")

        def changeaccount_dark():
            changeaccount_msg.config(bg="black")
            changeaccount_msg_lbm.config(bg="black", fg="white")
            changeaccount_msg_lb1.config(bg="black", fg="white")
            changeaccount_msg_lb2.config(bg="black", fg="white")
            changeaccount_msg_lb3.config(bg="black", fg="white")
            changeaccount_msg_lb4.config(bg="black", fg="white")
            changeaccount_frame.config(highlightbackground="#404040", highlightthickness=2, bg="black")

            actual_username.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
            actual_password.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
            new_username.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
            new_password.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)

            changeusername_btn.config(bg="black", fg="white", activeforeground="white", activebackground="#111111")
            changepassword_btn.config(bg="black", fg="white", activeforeground="white", activebackground="#111111")
            resetaccount_btn.config(bg="black", fg="#C19300", activeforeground="#C19300", activebackground="#111111")
            changeaccount_btn_back.config(bg="black", fg="white", activeforeground="white", activebackground="#111111")
            changeaccount_btn_close.config(bg="black", fg="white", activeforeground="white", activebackground="#111111")
            changeaccount_btn_change.config(bg="black", fg="white", activeforeground="white", activebackground="#111111", disabledforeground="#777777")
            changeaccount_btn_reset.config(bg="black", fg="#C19300", activeforeground="#C19300", activebackground="#111111")

        # ============================================== LIGHT/DARK MAIN WINDOWS THEME ============================================== #
        def mainmenubar_mw_dark():
            mainmbar_btn.config(background="black", foreground="white", activebackground="#292929", activeforeground="white")
            mainmbar.entryconfigure(0, background="black", foreground="white")
            mainmbar.entryconfigure(1, background="black", foreground="white")
            mainmbar.entryconfigure(2, background="black")
            mainmbar.entryconfigure(3, background="black", foreground="#C19300")

            aboutmbar_btn.config(background="black", foreground="white", activebackground="#292929", activeforeground="white")
            aboutmbar.entryconfigure(0, background="black", foreground="white")
            aboutmbar.entryconfigure(1, background="black")
            aboutmbar.entryconfigure(2, background="black", foreground="white")
            aboutmbar.entryconfigure(3, background="black", foreground="white")

        def mainmenubar_mw_light():
            mainmbar_btn.config(background="white", foreground="black", activebackground="#E7E7E7", activeforeground="black")
            mainmbar.entryconfigure(0, background="white", foreground="black")
            mainmbar.entryconfigure(1, background="white", foreground="black")
            mainmbar.entryconfigure(2, background="white")
            mainmbar.entryconfigure(3, background="white", foreground="#C19300")

            aboutmbar_btn.config(background="white", foreground="black", activebackground="#E7E7E7", activeforeground="black")
            aboutmbar.entryconfigure(0, background="white", foreground="black")
            aboutmbar.entryconfigure(1, background="white")
            aboutmbar.entryconfigure(2, background="white", foreground="black")
            aboutmbar.entryconfigure(3, background="white", foreground="black")

        def labels_main_light():
            device_imglb.config(background="white", foreground="black")
            idlb.config(background="white")
            brandlb.config(background="white", disabledforeground="#A9A9A9")
            modellb.config(background="white", disabledforeground="#A9A9A9")
            colorlb.config(background="white", disabledforeground="#A9A9A9")
            datelb.config(background="white", disabledforeground="#A9A9A9")
            inventorylb.config(background="white", foreground="black")
            searchlb.config(background="white", foreground="black")
            device_imglb.config(background="white")
            foundlb.config(background="white", foreground="black")

        def labels_main_dark():
            device_imglb.config(background="black", foreground="white")
            idlb.config(background="black")
            brandlb.config(background="black", disabledforeground="#696969")
            modellb.config(background="black", disabledforeground="#696969")
            colorlb.config(background="black", disabledforeground="#696969")
            datelb.config(background="black", disabledforeground="#696969")
            inventorylb.config(background="black", foreground="white")
            searchlb.config(background="black", foreground="white")
            device_imglb.config(background="black")
            foundlb.config(background="black", foreground="white")

        def entrys_mw_light():
            id_entry.config(fg="black", insertbackground="black", bg="#F9F9F9")
            brand_entry.config(fg="black", insertbackground="black", bg="#F9F9F9", disabledforeground="black", disabledbackground="white")
            model_entry.config(fg="black", insertbackground="black", bg="#F9F9F9", disabledforeground="black", disabledbackground="white")
            color_entry.config(fg="black", insertbackground="black", bg="#F9F9F9", disabledforeground="black", disabledbackground="white")
            date_entry.config(fg="black", insertbackground="black", bg="#F9F9F9", disabledforeground="black", disabledbackground="white")
            search_entry.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
            
        def entrys_mw_dark():
            id_entry.config(fg="white", insertbackground="white", bg="#111111")
            brand_entry.config(fg="white", insertbackground="white", bg="#111111", disabledforeground="white", disabledbackground="black")
            model_entry.config(fg="white", insertbackground="white", bg="#111111", disabledforeground="white", disabledbackground="black")
            color_entry.config(fg="white", insertbackground="white", bg="#111111", disabledforeground="white", disabledbackground="black")
            date_entry.config(fg="white", insertbackground="white",bg="#111111", disabledforeground="white", disabledbackground="black")
            search_entry.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)           
                
        def table_light():
            style_table = ttk.Style()
            style_table.theme_use("default")
            style_table.configure("light.Treeview", fieldbackground="white", background="white", foreground="black", font="SegoeUIVariable, 10")
            style_table.configure("Treeview.Heading", background="white", foreground="black", relief="ridge", font="SegoeUIVariable, 12")
            style_table.map("Treeview.Heading", background=[('active', 'white')])
            style_table.map("light.Treeview", background=[('selected', '#0078D7')])
            inventory_table.config(style="light.Treeview")
            style_table.map("Vertical.TScrollbar", background=[('active', '#F9F9F9')])
            style_table.configure("Vertical.TScrollbar", background="#EFEFEF", arrowcolor="black", troughcolor="white", arrowsize=32)

        def table_dark():
            style_table = ttk.Style()
            style_table.theme_use("default")
            style_table.configure("dark.Treeview", fieldbackground="black", background="black", foreground="white", font="SegoeUIVariable, 10")
            style_table.configure("Treeview.Heading", background="black", foreground="white", relief="ridge", font="SegoeUIVariable, 12")
            style_table.map("Treeview.Heading", background=[('active', 'black')])
            style_table.map("dark.Treeview", background=[('selected', '#0078D7')])
            inventory_table.config(style="dark.Treeview")
            style_table.map("Vertical.TScrollbar", background=[('active', '#292929')])
            style_table.configure("Vertical.TScrollbar", background="#191919", arrowcolor="white", troughcolor="black", arrowsize=32)
            
        def mainrbs_light():
            addrb.config(bg="white", foreground="#009003", activebackground="#F1F1F1", activeforeground="#009003", selectcolor="#E7E7E7")
            editrb.config(bg="white", foreground="#0049DE", activebackground="#F1F1F1", activeforeground="#0049DE", selectcolor="#E7E7E7")
            deleterb.config(bg="white", foreground="#CE0000", activebackground="#F1F1F1", activeforeground="#CE0000", selectcolor="#E7E7E7")

        def mainrbs_dark():
            addrb.config(bg="black", foreground="#009003", activebackground="#191919", activeforeground="#009003", selectcolor="#111111")
            editrb.config(bg="black", foreground="#0049DE", activebackground="#191919", activeforeground="#0049DE", selectcolor="#111111")
            deleterb.config(bg="black", foreground="#CE0000", activebackground="#191919", activeforeground="#CE0000", selectcolor="#111111")

        def mainbtns_light():
            addbtn.config(foreground="#007A05", activeforeground="#007A05", bg="white", activebackground="#EFEFEF")
            checkbtn.config(foreground="#0055FF", activeforeground="#0055FF", bg="white", activebackground="#EFEFEF")
            editbtn.config(foreground="#0055FF", activeforeground="#0055FF", bg="white", activebackground="#EFEFEF")
            cancelbtn.config(foreground="#EB0000", activeforeground="#EB0000", bg="white", activebackground="#EFEFEF")
            deletebtn.config(foreground="#EB0000", activeforeground="#EB0000", bg="white", activebackground="#EFEFEF")
            clearbtn.config(foreground="black", activeforeground="black", bg="white", activebackground="#EFEFEF")  
            changeaccount_btn.config(fg="black", activeforeground="black", bg="white", activebackground="#EFEFEF")     
            modeshelp_btn.config(fg="black", activeforeground="black", bg="white", activebackground="#EFEFEF")
            
        def mainbtns_dark():
            addbtn.config(foreground="#007A05", activeforeground="#007A05", bg="black", activebackground="#111111")
            checkbtn.config(foreground="#0055FF", activeforeground="#0055FF", bg="black", activebackground="#111111")
            editbtn.config(foreground="#0055FF", activeforeground="#0055FF", bg="black", activebackground="#111111")
            cancelbtn.config(foreground="#EB0000", activeforeground="#EB0000", bg="black", activebackground="#111111")
            deletebtn.config(foreground="#EB0000", activeforeground="#EB0000", bg="black", activebackground="#111111")
            clearbtn.config(foreground="white", activeforeground="white", bg="black", activebackground="#111111")
            changeaccount_btn.config(fg="white", activeforeground="white", bg="black", activebackground="#111111") 
            modeshelp_btn.config(fg="white", activeforeground="white", bg="black", activebackground="#111111") 

        def mainseparators_light():
            separator1.config(bg="#C0C0C0")
            separator3.config(bg="#C0C0C0")
            separator2.config(bg="#C0C0C0")

        def mainseparators_dark():
            separator1.config(bg="#404040")
            separator3.config(bg="#404040")
            separator2.config(bg="#404040")

        def basics_msg_light():
            basics_msg.config(bg="white")
            basics_imglb.config(bg="white")
            basics_msg_lb.config(bg="white", fg="black")
            basics_btn_ok.config(bg="white", fg="black", cursor= "hand2", activeforeground="black", activebackground="#EFEFEF")
            basics_btn_yes.config(bg="white", cursor= "hand2", activebackground="#EFEFEF")
            basics_btn_no.config(bg="white", fg="black", cursor= "hand2", activeforeground="black", activebackground="#EFEFEF")
            info_bf_lb.config(bg="white", fg="black")
            info_af_lb.config(bg="white", fg="black")
            id_inf.config(bg="white")
            brand_bf.config(bg="white", fg="black")
            model_bf.config(bg="white", fg="black")
            color_bf.config(bg="white", fg="black")
            date_bf.config(bg="white", fg="black")
            brand_af.config(bg="white", fg="black")
            model_af.config(bg="white", fg="black")
            color_af.config(bg="white", fg="black")
            date_af.config(bg="white", fg="black")

        def basics_msg_dark():
            basics_msg.config(bg="black")
            basics_imglb.config(bg="black")
            basics_msg_lb.config(bg="black", fg="white")
            basics_btn_ok.config(bg="black", fg="white", cursor= "hand2", activeforeground="white", activebackground="#111111")
            basics_btn_yes.config(bg="black", cursor= "hand2", activebackground="#111111")
            basics_btn_no.config(bg="black", fg="white", cursor= "hand2", activeforeground="white", activebackground="#111111")
            info_bf_lb.config(bg="black", fg="white")
            info_af_lb.config(bg="black", fg="white")
            id_inf.config(bg="black")
            brand_bf.config(bg="black", fg="white")
            model_bf.config(bg="black", fg="white")
            color_bf.config(bg="black", fg="white")
            date_bf.config(bg="black", fg="white")
            brand_af.config(bg="black", fg="white")
            model_af.config(bg="black", fg="white")
            color_af.config(bg="black", fg="white")
            date_af.config(bg="black", fg="white")

        # ============================================== LIGHT/DARK ALL WINDOWS THEME ============================================== #
        def settings_light():
            settings_window.config(bg="white")
            themelb.config(bg="white", fg="black")
            languagelb.config(bg="white", fg="black")
            themeframe.config(highlightbackground="#C0C0C0", highlightthickness=2, bg="white")
            languageframe.config(highlightbackground="#C0C0C0", highlightthickness=2, bg="white")
            lightthemerb.config(bg="white", foreground="black", activebackground="#F1F1F1", activeforeground="black", selectcolor="#E7E7E7")
            darkthemerb.config(bg="white", foreground="black", activebackground="#F1F1F1", activeforeground="black", selectcolor="#E7E7E7")
            eng_langrb.config(bg="white", foreground="black", activebackground="#F1F1F1", activeforeground="black", selectcolor="white")
            esp_langrb.config(bg="white", foreground="black", activebackground="#F1F1F1", activeforeground="black", selectcolor="white")
            setting_btn_close.config(bg="white", fg="black", activeforeground="black", activebackground="#EFEFEF")
            setting_btn_apply.config(bg="white", fg="black", activeforeground="black", activebackground="#EFEFEF", disabledforeground="#999999")

        def settings_dark():
            settings_window.config(bg="black")
            themelb.config(bg="black", fg="white")
            languagelb.config(bg="black", fg="white")
            themeframe.config(highlightbackground="#404040", highlightthickness=2, bg="black")
            languageframe.config(highlightbackground="#404040", highlightthickness=2, bg="black")
            lightthemerb.config(bg="black", foreground="white", activebackground="#191919", activeforeground="white", selectcolor="#111111")
            darkthemerb.config(bg="black", foreground="white", activebackground="#191919", activeforeground="white", selectcolor="#111111")
            eng_langrb.config(bg="black", foreground="white", activebackground="#191919", activeforeground="white", selectcolor="black")
            esp_langrb.config(bg="black", foreground="white", activebackground="#191919", activeforeground="white", selectcolor="black")
            setting_btn_close.config(bg="black", fg="white", activeforeground="white", activebackground="#111111")
            setting_btn_apply.config(bg="black", fg="white", activeforeground="white", activebackground="#111111", disabledforeground="#777777")
            
        # ========== RESTORE DEFAULT SETTINGS (IF THE SETTINGS FILE IS CORRUPT)========== #
        with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
            loadsettings = csv.reader(settingfile)
            settingdata = list(loadsettings)
        settingsdata = set([row[0]for row in settingdata])
        if "language=eng_lang" and "language=esp_lang" in settingsdata:
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
        elif "theme=dark_theme" and "theme=light_theme" in settingsdata:
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
        else:
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
                settingfile.write("theme=dark_theme\nlanguage=eng_lang\n")
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)

        with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "r") as accountfile:
                accountreader = csv.reader(accountfile, delimiter=",")
                accountdata = list(accountreader)

        login_window_place()
        dynamic_window.resizable(width=False, height=False)
        dynamic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))

        # ============================================== LOAD ELEMENTS IN MEMORY ============================================== #
        # ========== LOAD LOGIN WINDOW ========== #
        load_loginwindow()

        lmbar_separator.place(x=0, y=31, width=550, height=1)
        loginprofile_imglb.place(x=225, y=35)
        welcome_login.place(y=140)
        username_label.place(x=140, y=185)
        password_label.place(x=140, y=250)
        username_entry.place(x=140, y=210, height=30)
        password_entry.place(x=140, y=275, height=30)
        loginbtn.place(y=320)
        infobtn.place(x=507, y=369)
        settingsbtn.place(x=514, y=0)
        
        changeaccountlb.place(x=6, y=378)
        changeaccountlb.bind("<Enter>", lambda event: changeaccountlb.config(fg="#0083FF"))
        changeaccountlb.bind("<Leave>", lambda event: changeaccountlb.config(fg="#0055FF"))

        # ========== LOAD INVENTORY WINDOW ========== #
        load_inventory_window()

        # ========== LOAD LANGUAGE ========== #
        languagedata = set([row[0]for row in settingdata])
        if "language=eng_lang" in languagedata:
            eng_lang_login()
        elif "language=esp_lang" in languagedata:
            esp_lang_login()
        
        # ========== LOAD THEME ========== #
        themedata = set([row[0]for row in settingdata])
        if "theme=dark_theme" in themedata:                     
            window_dark()
        elif "theme=light_theme" in themedata:
            window_light()
        
        # ============================== #
        dynamic_window.deiconify()
        dynamic_window.focus_force()
        username_entry.focus()
        dynamic_window.mainloop()  # ---- END of the Main Code

    # ============================================== EXCEPTION ============================================== #
    except NameError:
        error_wn()
        corruptprogram_error_msg()
    except TclError:
        error_wn()
        loadfile_error_msg()

# ============= REQUIREMENTS ============= #
os_version = int(platform.version().split('.')[2])
min_req = 14393

display_res = ctypes.windll.user32.GetDesktopWindow()
res = ctypes.wintypes.RECT()
ctypes.windll.user32.GetWindowRect(display_res, ctypes.byref(res))
res_width = res.right - res.left 
res_height = res.bottom - res.top 

if os_version < min_req:
    tk.messagebox.showerror("OS Version Not supported | Version del S.O No compatible!", "Windows 10 x64 (Build 14393) or Higher is Required to Work!\nPlease Update the O.S, If you still have Problems contact the Developer.\n\nSe Necesita Windows 10 x64 (Compilacion 14393) o Superior para Funcionar!\nPor Favor Actualice el S.O, Si aun tienes Problemas contacta con el Desarrollador.")
    sys.exit(0)
elif res_width < 1024 or res_height < 768: 
    tk.messagebox.showerror("Low Screen Resolution Detected! | Baja Resolución de Pantalla Detectada!", "A Display Resolution of 1024 x 768 or Higher is Required to Work!\nIf you still have Problems contact the Developer.\n\nSe requiere una Resolucion de Pantalla de 1024 x 768 para Funcionar!\nSi aun tienes Problemas contacta con el Desarrollador.")
    sys.exit(0)
else: 
    DWI()
