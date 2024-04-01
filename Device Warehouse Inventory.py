import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import os, sys, csv, re, subprocess, darkdetect, platform, ctypes

def DWI():
    global dynamic_window
    try:
        if os.path.exists(os.path.join(os.path.dirname(__file__), "init")):
            return
        else:
            with open(os.path.join(os.path.dirname(__file__), "init"), "w") as init_file:
                init_file.write("")
                subprocess.check_call(["attrib","+H", os.path.join(os.path.dirname(__file__), "init")])

            if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data")):
                os.makedirs(os.path.join(os.path.dirname(__file__), "Data"))
            if not os.path.exists(os.path.join(os.path.dirname(__file__), "Exported")):
                os.makedirs(os.path.join(os.path.dirname(__file__), "Exported"))
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

            def close():
                os.remove(os.path.join(os.path.dirname(__file__), "init"))
                sys.exit(0)

            # ============================================== LANGUAGES ============================================== #
            def eng_lang_login():
                eng_langrb.select()
                eng_langrb.config(command=eng_lang_login)
                dynamic_window.title("Device Warehouse Inventory (Sign-In)")

                laboutmbar_btn.config(text = "About", font="SegoeUIVariable, 12", padx=10)
                laboutmbar.entryconfigure(0, label="   How to Sign-In?", font="SegoeUIVariable, 12", command=login_help_eng)
                laboutmbar.entryconfigure(2, label="   ChangeLog", font="SegoeUIVariable, 12", command=changelog_eng)
                laboutmbar.entryconfigure(3, label="   About the Program", font="SegoeUIVariable, 12", command=about_eng)

                username_label.config(text="Username:", font="SegoeUIVariable, 12")
                password_label.config(text="Password:", font="SegoeUIVariable, 12")
                rememberlb.config(text="Don't Remember your Account?", font="SegoeUIVariable, 12")
                rememberlb.bind("<Button-1>", lambda event: rememberaccount_eng())

                loginbtn.config(text="Sign-In", font="SegoeUIVariable, 12", padx=20)
                loginbtn.place(x=213)
                infobtn.config(text="❕", font="SegoeUIVariable, 12", command=about_eng)
                settingsbtn.config(text="⚙️", font="SegoeUIVariable, 12", command=settings)
                settings_eng()

            def esp_lang_login():
                esp_langrb.select()
                esp_langrb.config(command=esp_lang_login)
                dynamic_window.title("Device Warehouse Inventory (Inicia Sesion)")

                laboutmbar_btn.config(text = "Acerca de", font="SegoeUIVariable, 12", padx=10)
                laboutmbar.entryconfigure(0, label="   Como Iniciar Sesion?", font="SegoeUIVariable, 12", command=login_help_esp)
                laboutmbar.entryconfigure(2, label="   Registro de Cambios", font="SegoeUIVariable, 12", command=changelog_esp)
                laboutmbar.entryconfigure(3, label="   Acerca del Programa", font="SegoeUIVariable, 12", command=about_esp)

                username_label.config(text="Nombre de Usuario:", font="SegoeUIVariable, 12")
                password_label.config(text="Contraseña:", font="SegoeUIVariable, 12")
                rememberlb.config(text="No Recuerdas Tu Cuenta?", font="SegoeUIVariable, 12")
                rememberlb.bind("<Button-1>", lambda event: rememberaccount_esp())

                loginbtn.place(x=195)
                loginbtn.config(text="Iniciar Sesion", font="SegoeUIVariable, 12", padx=40)
                infobtn.config(text="❕", font="SegoeUIVariable, 12", command=about_esp)
                settingsbtn.config(text="⚙️", font="SegoeUIVariable, 12", command=settings)
                settings_esp()

            def eng_lang_mainwindow():
                eng_langrb.select()
                dynamic_window.protocol("WM_DELETE_WINDOW", lambda: signout_ask_eng())

                mainmbar_btn.config(text = "Main", font="SegoeUIVariable, 12", padx=10)	
                mainmbar.entryconfigure(0, label="   Save Data to Text Files", font="SegoeUIVariable, 12")				
                mainmbar.entryconfigure(2, label="   Sign-Out", font="SegoeUIVariable, 12", command=signout_ask_eng)

                aboutmbar_btn.config(text = "About", font="SegoeUIVariable, 12", padx=10, pady=6)
                aboutmbar_btn.place(x=56)	
                aboutmbar.entryconfigure(0, label="   How to use This Program?", font="SegoeUIVariable, 12", command=main_help_eng)
                aboutmbar.entryconfigure(2, label="   ChangeLog", font="SegoeUIVariable, 12", command=changelog_eng)
                aboutmbar.entryconfigure(3, label="   About the Program", font="SegoeUIVariable, 12", command=about_eng)

                addrb.config(text="Add Mode", pady=14, font="SegoeUIVariable, 12")
                editrb.config(text="Edit Mode", pady=14, font="SegoeUIVariable, 12")
                deleterb.config(text="Delete Mode", pady=14, font="SegoeUIVariable, 12")
                sl_computersrb.config(text="Computers", pady=14, font="SegoeUIVariable, 12")
                sl_mobilesrb.config(text="Mobiles", pady=14, font="SegoeUIVariable, 12")
                sl_gadgetsrb.config(text="Gadgets", pady=14, font="SegoeUIVariable, 12")

                search_entry.delete(0, tk.END)
                search_entry.insert(0, "Search Inventory by ID...")
                search_entry.bind("<Button-1>", lambda event: search_entry.delete(0, tk.END) if search_entry.get() == "Search Inventory by ID..." else search_entry.insert(0, ""))
                search_entry.bind("<FocusOut>", lambda event: search_entry.insert(0, "Search Inventory by ID...") if search_entry.get() == "" else search_entry.insert(0, ""))
                search_exlb.config(text="Example: CM-001")

                db_table.heading("id", text= "ID", anchor=tk.SW)
                db_table.heading("brand", text= "Brand", anchor=tk.SW)
                db_table.heading("model", text= "Model", anchor=tk.SW)
                db_table.heading("color", text= "Color", anchor=tk.SW)
                db_table.heading("date", text= "Manufacturing Date", anchor=tk.SW)

                idlb.config(text="ID", font="SegoeUIVariable, 12")
                brandlb.config(text="Brand", font="SegoeUIVariable, 12")
                modellb.config(text="Model", font="SegoeUIVariable, 12")
                colorlb.config(text="Color", font="SegoeUIVariable, 12")
                datelb.config(text="Date", font="SegoeUIVariable, 12")
                inventorylb.config(text="Inventory Information", font="SegoeUIVariable, 15")

                addbtn.config(text="    Add             ", font="SegoeUIVariable, 12")
                editbtn.config(text="    Edit            ", font="SegoeUIVariable, 12")
                deletebtn.config(text="    Delete        ", font="SegoeUIVariable, 12")
                clearbtn.config(text="    Clear          ", font="SegoeUIVariable, 12")
                searchbtn.config(text="Search", pady=10, font="SegoeUIVariable, 12")
                addmodehelp_btn.config(text="❔", font="SegoeUIVariable, 12", command=addmode_help_eng)
                editmodehelp_btn.config(text="❔", font="SegoeUIVariable, 12", command=editmode_help_eng)
                deletemodehelp_btn.config(text="❔", font="SegoeUIVariable, 12", command=deletemode_help_eng)
                settings_eng()

            def esp_lang_mainwindow():
                esp_langrb.select()
                dynamic_window.protocol("WM_DELETE_WINDOW", lambda: signout_ask_esp())

                mainmbar_btn.config(text = "Principal", font="SegoeUIVariable, 12", padx=10)	
                mainmbar.entryconfigure(0, label="   Guardar Datos en los Archivos de Texto", font="SegoeUIVariable, 12")				
                mainmbar.entryconfigure(2, label="   Cerrar Sesion", font="SegoeUIVariable, 12", command=signout_ask_esp)

                aboutmbar_btn.config(text = "Acerca de", font="SegoeUIVariable, 12", padx=10)	
                aboutmbar_btn.place(x=83)	
                aboutmbar.entryconfigure(0, label="   Como usar Este Programa?", font="SegoeUIVariable, 12", command=main_help_esp)
                aboutmbar.entryconfigure(2, label="   Registro de Cambios", font="SegoeUIVariable, 12", command=changelog_esp)
                aboutmbar.entryconfigure(3, label="   Acerca del Programa", font="SegoeUIVariable, 12", command=about_esp)

                addrb.config(text="Modo Agregar", pady=14, font="SegoeUIVariable, 12")
                editrb.config(text="Modo Editar", pady=14, font="SegoeUIVariable, 12")
                deleterb.config(text="Modo Eliminar", pady=14, font="SegoeUIVariable, 12")
                sl_computersrb.config(text="Computadoras", pady=14, font="SegoeUIVariable, 12")
                sl_mobilesrb.config(text="Portatiles", pady=14, font="SegoeUIVariable, 12")
                sl_gadgetsrb.config(text="Accesorios", pady=14, font="SegoeUIVariable, 12")

                search_entry.delete(0, tk.END)
                search_entry.insert(0, "Buscar en el Inventario por ID...")
                search_entry.bind("<Button-1>", lambda event: search_entry.delete(0, tk.END) if search_entry.get() == "Buscar en el Inventario por ID..." else search_entry.insert(0, ""))
                search_entry.bind("<FocusOut>", lambda event: search_entry.insert(0, "Buscar en el Inventario por ID...") if search_entry.get() == "" else search_entry.insert(0, ""))
                search_exlb.config(text="Ejemplo: CM-001")

                db_table.heading("id", text= "ID", anchor=tk.SW)
                db_table.heading("brand", text= "Marca", anchor=tk.SW)
                db_table.heading("model", text= "Modelo", anchor=tk.SW)
                db_table.heading("color", text= "Color", anchor=tk.SW)
                db_table.heading("date", text= "Fecha de Fabricacion", anchor=tk.SW)

                idlb.config(text="ID", font="SegoeUIVariable, 12")
                brandlb.config(text="Marca", font="SegoeUIVariable, 12")
                modellb.config(text="Modelo", font="SegoeUIVariable, 12")
                colorlb.config(text="Color", font="SegoeUIVariable, 12")
                datelb.config(text="Fecha", font="SegoeUIVariable, 12")
                inventorylb.config(text="Informacion del Inventario", font="SegoeUIVariable, 15")

                addbtn.config(text="    Agregar      ", font="SegoeUIVariable, 12")
                editbtn.config(text="    Editar        ", font="SegoeUIVariable, 12")
                deletebtn.config(text="    Eliminar     ", font="SegoeUIVariable, 12")
                clearbtn.config(text="    Limpiar       ", font="SegoeUIVariable, 12")
                searchbtn.config(text="Buscar", pady=10, font="SegoeUIVariable, 12")
                addmodehelp_btn.config(text="❔", font="SegoeUIVariable, 12", command=addmode_help_esp) 
                editmodehelp_btn.config(text="❔", font="SegoeUIVariable, 12", command=editmode_help_esp)
                deletemodehelp_btn.config(text="❔", font="SegoeUIVariable, 12", command=deletemode_help_esp) 
                settings_esp()

            # ============================================== LIGHT\DARK THEME ============================================== #
            def window_light():
                dynamic_window.config(bg="white")
                lightthemerb.select()
                settings_light()
                settingsbtn.config(fg="black", activeforeground="black", bg="white", activebackground="#EFEFEF")

                # ====== LOGIN ====== #
                loginmenubar_light()
                loginlabels_light()
                loginentrys_light()    
                loginbuttons_light()

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
                
            def window_dark():
                dynamic_window.config(bg="black")
                darkthemerb.select()
                settings_dark()
                settingsbtn.config(fg="white", activeforeground="white", bg="black", activebackground="#111111")

                # ====== LOGIN ====== #
                loginmenubar_dark()
                loginlabels_dark()
                loginentrys_dark()    
                loginbuttons_dark()

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
                
            # ============================================== SET PLACE WINDOWS ============================================== #
            def login_window_place():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 500
                window_h = 360
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

            def main_window_place():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 745
                window_h = 720
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

            dynamic_window = tk.Tk() # ----- MAIN WINDOW
            dynamic_window.withdraw()
            dynamic_window.protocol("WM_DELETE_WINDOW", lambda: close())
            login_window_place()
            # =================================================================================================================== #
            # ========== LOAD SETTINGS ========== #
            settings_window = tk.Toplevel()
            settings_window.withdraw()

            themeframe = tk.Frame(settings_window, height=1, bd=0)
            languageframe = tk.Frame(settings_window, height=1, bd=0)
            themelb = tk.Label(settings_window)
            languagelb = tk.Label(settings_window)

            themegroup = tk.IntVar()
            lightthemerb = tk.Radiobutton(settings_window, value="light", variable=themegroup, indicatoron=False, command=window_light) 
            darkthemerb = tk.Radiobutton(settings_window, value="dark", variable=themegroup, indicatoron=False, command=window_dark)
            languagegroup = tk.IntVar()
            eng_langrb = tk.Radiobutton(settings_window, text="English", value=1, variable=languagegroup, font="SegoeUIVariable, 12", cursor="hand2", command=eng_lang_login) 
            esp_langrb = tk.Radiobutton(settings_window, text="Español", value=2, variable=languagegroup, font="SegoeUIVariable, 12", cursor="hand2", command=esp_lang_login)

            setting_btn_close = tk.Button(settings_window, cursor="hand2")

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

            def settings_eng():
                settings_window.title("Settings")
                themelb.config(text="🎨  Theme", font="SegoeUIVariable, 12")
                languagelb.config(text="💬  Languages", font="SegoeUIVariable, 12")
                lightthemerb.config(text="🔆  Light", value="light", variable=themegroup, font="SegoeUIVariable, 12", cursor="hand2", padx=30, pady=7, width=3, command=window_light)
                darkthemerb.config(text="🌙  Dark", value="dark", variable=themegroup, font="SegoeUIVariable, 12", cursor="hand2", padx=30, pady=7, width=3, command=window_dark)    
                setting_btn_close.config(text="Close", padx=35, pady=3, width=3, font="SegoeUIVariable, 12")

            def settings_esp():
                settings_window.title("Ajustes")
                themelb.config(text="🎨  Tema", font="SegoeUIVariable, 12")
                languagelb.config(text="💬  Idiomas", font="SegoeUIVariable, 12")
                lightthemerb.config(text="🔆  Claro", value="light", variable=themegroup, font="SegoeUIVariable, 12", cursor="hand2", padx=30, pady=7, width=3, command=window_light)
                darkthemerb.config(text="🌙  Oscuro", value="dark", variable=themegroup, font="SegoeUIVariable, 12", cursor="hand2", padx=30, pady=7, width=3, command=window_dark)    
                setting_btn_close.config(text="Cerrar", padx=35, pady=3, width=3, font="SegoeUIVariable, 12")

            # ============================================== LOAD/HIDE MSG WINDOWS ============================================== #
            # ========== LOAD MSG CORE ========== #
            basics_msg = tk.Toplevel()
            basics_msg.withdraw()
            basics_msg.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))

            basics_img = tk.PhotoImage()
            basics_imglb = tk.Label(basics_msg, image=basics_img)
            basics_msg_lb = tk.Label(basics_msg)
            basics_btn_ok = tk.Button(basics_msg, text="OK", padx=15, pady=3, width=3, font="SegoeUIVariable, 12")
            basics_btn_yes = tk.Button(basics_msg, padx=15, pady=3, width=3, font="SegoeUIVariable, 12")
            basics_btn_no = tk.Button(basics_msg, padx=15, pady=3, width=3, font="SegoeUIVariable, 12")

            basics_w_total = dynamic_window.winfo_screenwidth()
            basics_h_total = dynamic_window.winfo_screenheight()
            basics_w = 1
            basics_h = 1
            basics_width = round(basics_w_total/2-basics_w/2)
            basics_height = round(basics_h_total/2-basics_h/2)
            basics_msg.geometry(str(basics_w)+"x"+str(basics_h)+"+"+str(basics_width)+"+"+str(basics_height))

            def hide_basic_msg():
                restore_elements()
                basics_msg.grab_release()
                basics_msg.transient(None)
                basics_msg.withdraw()
                basics_btn_ok.place_forget()
                basics_btn_yes.place_forget()
                basics_btn_no.place_forget()

            def hide_error_msg():
                restore_elements()
                basics_msg.grab_release()
                basics_msg.transient(None)
                basics_msg.withdraw()
                sys.exit(0)

            # ========== REMEMBER MSG ENGLISH ========== #
            def rememberaccount_eng():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 290
                window_h = 150
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())
                basics_msg.title("Your Account is:")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/remember.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="Username: admin\n\nPassword: 12345", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=20)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=113, y=100)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== REMEMBER MSG SPANISH ========== #
            def rememberaccount_esp():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 345
                window_h = 150
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())
                basics_msg.title("Tu cuenta es:")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/remember.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="Nombre de Usuario: admin\n\nContraseña: 12345", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=20)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=143, y=100)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== CHANGELOG MSG ENGLISH ========== #
            def changelog_eng():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 430
                window_h = 415
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
                basics_imglb.place(x=146, y=5)
                basics_msg_lb.config(text="-------------------------   CHANGELOG   -------------------------\n*** VERSION 2.0.2 (16-Oct-2023) ***\n\n- Changed DataBase Engine from MySQL > CSV File.\n- Added Show (Exported) Folder Button in MainWindow.\n- Improved Minor Logic in Some Program Fuctions.\n- Bugs Fixes.\n\nDeveloped By Eliezer Brito\n© Elie-Dev (2023)\nAll rights reserved", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=17, y=140)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=182, y=365)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== CHANGELOG MSG SPANISH ========== #
            def changelog_esp():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 509
                window_h = 415
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
                basics_imglb.place(x=184, y=5)
                basics_msg_lb.config(text="----------------------------   Registro de Cambios   ----------------------------\n*** VERSION 2.0.2 (16-Oct-2023) ***\n\n- Motor de Base de Datos cambiado de MySQL > Archivo CSV.\n- Se agrego el Boton Mostrar Carpeta (Exported).\n- Se mejoro Logicas Menores en algunas Funciones del Programa.\n- Errores Corregidos.\n\nDesarrollado por Eliezer Brito\n© Elie-Dev (2023)\nTodos los Derechos Reservados", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=17, y=140)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=220, y=365)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== ABOUT MSG ========== #
            def about_eng():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 308
                window_h = 400
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
                basics_msg_lb.config(text="Device Warehouse Inventory\nVersion: 2.0.2\n\nThis Program is to Add, Edit or Delete \nProducts information in the Inventory \nfrom the Local DataBase.\n\nDeveloped By Eliezer Brito\n© Elie-Dev (2023)\nAll rights reserved", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=17, y=140)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=122, y=350)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== ABOUT MSG SPANISH ========== #
            def about_esp():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 390
                window_h = 400
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
                basics_msg_lb.config(text="Device Warehouse Inventory\nVersion: 2.0.2\n\nEste Programa es para Agregar, Editar o Eliminar \nInformacion del Producto en el Inventario \nde la Base de Datos Local.\n\nDesarrollado por Eliezer Brito\n© Elie-Dev (2023) \nTodos los Derechos Reservados", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=17, y=140)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=350)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== HELP LOGIN MSG ENGLISH ========== #
            def login_help_eng():
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
                basics_msg_lb.config(text="Type your username and password, \nif the data is correct the application will start, \notherwise you will receive an error message.\n\nIf you still have problems logging in, \nPlease notify the Developer.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=20)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=198, y=160)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== HELP LOGIN MSG SPANISH ========== #
            def login_help_esp():
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
                basics_msg_lb.config(text="Escribe tu Nombre de Usuario y Contraseña, \nsi los datos son correctos la aplicacion iniciara, \nde lo contrario recibiras un mensaje de error.\n\nSi aun tienes problemas para iniciar sesion, \nPor Favor Contacta al Desarrollador.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=20) 

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=208, y=160)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
                    
            # ========== LOGIN ERROR MSG ENGLISH ========== #
            def login_error_eng():
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
                basics_msg_lb.config(text="Your Account is incorrect or invalid!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=125)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== LOGIN ERROR MSG SPANISH ========== #
            def login_error_esp():
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
                basics_msg_lb.config(text="Tu Cuenta es Incorrecta o Invalida!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=125)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== DATABASE ERROR MSG ENGLISH ========== #
            def database_error_eng():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 363
                window_h = 175
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("DataBase Access Error")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="Error connecting to DataBase!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=150, y=125)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== DATABASE ERROR MSG SPANISH ========== #
            def database_error_esp():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 430
                window_h = 175
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Error de acceso a la Base de Datos")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="Error al Conectarse a la Base de Datos!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=183, y=125)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== FATAL ERROR MSG ENGLISH ========== #
            def fatal_error_eng():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 363
                window_h = 175
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_error_msg())    
                basics_msg.title("Fatal Error")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="FATAL PROGRAM ERROR!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_error_msg)
                basics_btn_ok.place(x=150, y=125)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== FATAL ERROR MSG SPANISH ========== #
            def fatal_error_esp():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 395
                window_h = 175
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_error_msg())    
                basics_msg.title("Error Fatal")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="ERROR FATAL DEL PROGRAMA!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_error_msg)
                basics_btn_ok.place(x=165, y=125)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # =============================================================================================================================
            # ========== HELP MAIN MSG ENGLISH ========== #
            def main_help_eng():
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
                basics_msg_lb.config(text="To start, select one of the available options \nat the top to open each mode.\n\nIf you still have problems, \nPlease notify the Developer.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=20)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=185, y=135)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== HELP MAIN MSG SPANISH ========== #
            def main_help_esp():
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
                basics_msg_lb.config(text="Para empezar, selecciona una de las opciones \ndisponibles en la parte superior de cada modo.\n\nSi aun tienes problemas, \nPor Favor Contacta al Desarrollador.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=20)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=210, y=135)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== ADD MODE HELP MSG ENGLISH ========== #
            def addmode_help_eng():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 388
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("How to use Add Mode?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="To start, select the type of devices, \nthen fill in the text fields and \npress the 'Add' button.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=38)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=163, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== ADD MODE HELP MSG SPANISH ========== #
            def addmode_help_esp():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 480
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Como usar el Modo Agregar?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="Para empezar, selecciona el tipo de dispositivo\n luego llena los campos de texto y \npresiona el Boton 'Agregar'.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=38)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=208, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EDIT MODE HELP MSG ENGLISH ========== #
            def editmode_help_eng():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 383
                window_h = 180
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("How to use Edit Mode?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="To start select the type of devices, \nthen type the correct ID, \nthen fill in all the other text fields \nand press the 'Edit' button.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=30)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=160, y=130)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EDIT MODE HELP MSG SPANISH ========== #
            def editmode_help_esp():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 480
                window_h = 180
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Como usar el Modo Editar?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="Para empezar, selecciona el tipo de dispositivo\n luego escribe el ID correcto, \nluego llena los demas campos de texto y \npresiona el Boton 'Editar'.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=30)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=208, y=130)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()
                
            # ========== DELETE MODE HELP MSG ENGLISH ========== #
            def deletemode_help_eng():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 383
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("How can use Delete Mode")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="To start select the type of devices, \nthen type the correct ID \nand press the 'Delete' button.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=38)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=160, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== DELETE MODE HELP SPANISH ========== #
            def deletemode_help_esp():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 480
                window_h = 165
                login_width = round(window_w_total/2-window_w/2)
                login_height = round(window_h_total/2-window_h/2-100)
                basics_msg.geometry(str(window_w)+"x"+str(window_h)+"+"+str(login_width)+"+"+str(login_height))

                off_elements_msg()
                basics_msg.protocol("WM_DELETE_WINDOW", lambda: hide_basic_msg())    
                basics_msg.title("Como usar el Modo Eliminar?")
                basics_msg.resizable(width=False, height=False)
                basics_msg.grab_set()
                basics_msg.focus_set()
                
                basics_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="Para empezar, selecciona el tipo de dispositivo\n luego escribe el ID correcto \ny presiona el Boton 'Eliminar'.", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=38)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=208, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== ADD PRODUCT SAVE MSG ENGLISH ========== #
            def add_prod_save_eng():
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
                basics_msg_lb.config(text="Your Product has been ADDED to Inventory!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=193, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== ADD PRODUCT SAVE MSG SPANISH ========== #
            def add_prod_save_esp():
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
                basics_msg_lb.config(text="Tu Producto se ha AGREGADO al Inventario!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=201, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== ADD PRODUCT EMPTY MSG ENGLISH ========== #
            def add_prod_empty_eng():
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
                basics_msg_lb.config(text="You can't leave EMPTY Text Fields!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== ADD PRODUCT EMPTY MSG SPANISH ========== #
            def add_prod_empty_esp():
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
                basics_msg_lb.config(text="No Puedes dejar VACIOS los Campos de Texto!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=215, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EDIT PRODUCT SAVE MSG ENGLISH ========== #
            def edit_prod_save_eng():
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
                basics_msg_lb.config(text="Your Product has been EDITED in the Inventory!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=205, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EDIT PRODUCT SAVE MSG SPANIHS ========== #
            def edit_prod_save_esp():
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
                basics_msg_lb.config(text="Tu Producto se ha EDITADO en el Inventario!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=201, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EDIT PRODUCT NOTFOUND MSG ENGLISH ========== #
            def edit_prod_notfound_eng():
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
                basics_msg_lb.config(text="This ID does not EXIST!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=130, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EDIT PRODUCT NOTFOUND MSG SPANISH ========== #
            def edit_prod_notfound_esp():
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
                basics_msg_lb.config(text="Este ID no Existe!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=128, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EDIT PRODUCT EMPTY MSG ENGLISH ========== #
            def edit_prod_empty_eng():
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
                basics_msg_lb.config(text="You can't leave EMPTY Text Fields!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EDIT PRODUCT EMPTY MSG SPANISH ========== #
            def edit_prod_empty_esp():
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
                basics_msg_lb.config(text="No Puedes dejar VACIOS los Campos de Texto!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=215, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EDIT PRODUCT ASK MSG ENGLISH ========== #
            def edit_prod_ask_eng():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 480
                window_h = 165
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
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="Are you sure you want to EDIT it from inventory?\nThis action is IRREVERSIBLE!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=50)

                basics_btn_yes.config(text="Yes", fg="#0078FF", activeforeground="#0078FF")
                basics_btn_yes.place(x=160, y=115)
                basics_btn_no.config(text="No")
                basics_btn_no.place(x=255, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EDIT PRODUCT ASK MSG SPANISH ========== #
            def edit_prod_ask_esp():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 510
                window_h = 165
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
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="Estas Seguro que quieres EDITARLO del Inventario?\nEsta accion es INRREVERSIBLE!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=50)

                basics_btn_yes.config(text="Si", fg="#0078FF", activeforeground="#0078FF")
                basics_btn_yes.place(x=173, y=115)
                basics_btn_no.config(text="No")
                basics_btn_no.place(x=268, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== DELETE PRODUCT DEL MSG ENGLISH ========== #
            def delete_prod_del_eng():
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
                basics_msg_lb.config(text="Your Product has been DELETED in the Inventory!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=210, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== DELETE PRODUCT DEL MSG SPANISH ========== #
            def delete_prod_del_esp():
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
                basics_msg_lb.config(text="Tu Profucto ha sido ELIMINADO del Inventario!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=203, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== DELETE PRODUCT NOTFOUND MSG ENGLISH ========== #
            def delete_prod_notfound_eng():
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
                basics_msg_lb.config(text="This ID does not EXIST!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=133, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== DELETE PRODUCT NOTFOUND MSG SPANISH ========== #
            def delete_prod_notfound_esp():
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
                basics_msg_lb.config(text="Este ID no Existe!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=128, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== DELETE PRODUCT EMPTY MSG ENGLISH ========== #
            def delete_prod_empty_eng():
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
                basics_msg_lb.config(text="You can't leave EMPTY Text Fields!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=165, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== DELETE PRODUCT EMPTY MSG SPANISH ========== #
            def delete_prod_empty_esp():
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
                basics_msg_lb.config(text="No Puedes dejar VACIOS los Campos de Texto!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=57)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=215, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== DELETE PRODUCT ASK MSG ENGLISH ========== #
            def delete_prod_ask_eng():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 508
                window_h = 165
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
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="Are you sure you want to DELETE it from inventory?\nThis action is IRREVERSIBLE!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=50)

                basics_btn_yes.config(text="Yes", fg="#EB0000", activeforeground="#EB0000")
                basics_btn_yes.place(x=170, y=115)
                basics_btn_no.config(text="No")
                basics_btn_no.place(x=265, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== DELETE PRODUCT ASK MSG SPANISH ========== #
            def delete_prod_ask_esp():
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 530
                window_h = 165
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
                basics_imglb.place(x=15, y=30)
                basics_msg_lb.config(text="Estas Seguro que quieres ELIMINARLO del Inventario?\nEsta accion es INRREVERSIBLE!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=50)

                basics_btn_yes.config(text="Si", fg="#0078FF", activeforeground="#0078FF")
                basics_btn_yes.place(x=185, y=115)
                basics_btn_no.config(text="No")
                basics_btn_no.place(x=280, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EXPORT FILE MSG ENGLISH ========== #
            def export_file_msg_eng():
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
                basics_msg_lb.config(text="The contents of the inventory have been EXPORTED \nto Text Files successfully!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=45)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=223, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== EXPORT FILE MSG SPANISH ========== #
            def export_file_msg_esp():
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
                basics_msg_lb.config(text="El contenido del Inventario ha sido EXPORTADO \na los Archivos de Texto Exitosamente!", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=45)

                basics_btn_ok.config(command=hide_basic_msg)
                basics_btn_ok.place(x=213, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== SIGN-OUT ASK MSG ENGLISH ========== #
            def signout_ask_eng():
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
                basics_msg_lb.config(text="Are you sure you want to Sign-Out?", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=50)

                basics_btn_yes.config(text="Yes", fg="#C19300", activeforeground="#C19300", command=signout)
                basics_btn_yes.place(x=118, y=115)
                basics_btn_no.config(text="No", command=hide_basic_msg)
                basics_btn_no.place(x=213, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========== SIGN-OUT ASK MSG SPANISH ========== #
            def signout_ask_esp():
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
                basics_msg_lb.config(text="Estas Seguro que quieres Cerrar Sesion?", font="SegoeUIVariable, 12")
                basics_msg_lb.place(x=120, y=50)

                basics_btn_yes.config(text="Si", fg="#C19300", activeforeground="#C19300", command=signout)
                basics_btn_yes.place(x=138, y=115)
                basics_btn_no.config(text="No", command=hide_basic_msg)
                basics_btn_no.place(x=233, y=115)
                basics_msg.transient(dynamic_window)
                basics_msg.deiconify()

            # ========================================================================================================= #
            def off_elements_msg(): 
                id_entry.config(cursor="arrow")
                brand_entry.config(cursor="arrow")
                model_entry.config(cursor="arrow")
                color_entry.config(cursor="arrow")
                date_entry.config(cursor="arrow")
                search_entry.config(cursor="arrow")

                sl_computersrb.config(cursor="arrow")
                sl_mobilesrb.config(cursor="arrow")
                sl_gadgetsrb.config(cursor="arrow")

                addbtn.config(cursor="arrow")
                editbtn.config(cursor="arrow")
                deletebtn.config(cursor="arrow")
                clearbtn.config(cursor="arrow")
                searchbtn.config(cursor="arrow")
                addmodehelp_btn.config(cursor="arrow")
                editmodehelp_btn.config(cursor="arrow")
                deletemodehelp_btn.config(cursor="arrow")
                showexported_folderbtn.config(cursor="arrow")

                addrb.config(cursor="arrow")
                editrb.config(cursor="arrow")
                deleterb.config(cursor="arrow")
                
                settingsbtn.config(cursor="arrow")

                username_entry.config(cursor="arrow")
                password_entry.config(cursor="arrow")
                loginbtn.config(cursor="arrow")
                rememberlb.config(cursor="arrow")
                infobtn.config(cursor="arrow")

            def restore_elements(): 
                id_entry.config(cursor="xterm")
                brand_entry.config(cursor="xterm")
                model_entry.config(cursor="xterm")
                color_entry.config(cursor="xterm")
                date_entry.config(cursor="xterm")
                search_entry.config(cursor="xterm")

                sl_computersrb.config(cursor="hand2")
                sl_mobilesrb.config(cursor="hand2")
                sl_gadgetsrb.config(cursor="hand2")

                addbtn.config(cursor="hand2")
                editbtn.config(cursor="hand2")
                deletebtn.config(cursor="hand2")
                clearbtn.config(cursor="hand2")
                searchbtn.config(cursor="hand2")
                addmodehelp_btn.config(cursor="hand2")
                editmodehelp_btn.config(cursor="hand2")
                deletemodehelp_btn.config(cursor="hand2")
                showexported_folderbtn.config(cursor="hand2")

                addrb.config(cursor="hand2")
                editrb.config(cursor="hand2")
                deleterb.config(cursor="hand2")

                settingsbtn.config(cursor="hand2")

                username_entry.config(cursor="xterm")
                password_entry.config(cursor="xterm")
                loginbtn.config(cursor="hand2")
                rememberlb.config(cursor="hand2")
                infobtn.config(cursor="hand2")

            # ========================================================================================================= #
            def signout():
                dynamic_window.withdraw()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    eng_lang_login()
                elif lang_value == 2:
                    esp_lang_login()
                hide_basic_msg()

                menubar_separator.place_forget()
                modes_separator.place_forget()
                inventory_separator.place_forget()
                devices_separator.place_forget()

                mainmbar_btn.place_forget()
                aboutmbar_btn.place_forget()

                search_exlb.place_forget()
                idlb.place_forget()
                brandlb.place_forget()
                modellb.place_forget()
                colorlb.place_forget()
                datelb.place_forget()
                inventorylb.place_forget()   

                id_entry.place_forget()
                brand_entry.place_forget()
                model_entry.place_forget()
                color_entry.place_forget()
                date_entry.place_forget()
                search_entry.place_forget()

                db_table.place_forget()

                sl_computersrb.place_forget()
                sl_mobilesrb.place_forget()
                sl_gadgetsrb.place_forget()

                addbtn.place_forget()
                editbtn.place_forget()
                deletebtn.place_forget()
                clearbtn.place_forget()
                searchbtn.place_forget()
                addmodehelp_btn.place_forget()
                editmodehelp_btn.place_forget()
                deletemodehelp_btn.place_forget()
                showexported_folderbtn.place_forget()

                device_imglb.place_forget()

                addrb.place_forget()
                editrb.place_forget()
                deleterb.place_forget()
                
                eng_langrb.config(command=eng_lang_login)
                esp_langrb.config(command=esp_lang_login)

                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                
                dynamic_window.protocol("WM_DELETE_WINDOW", lambda: close())
                dynamic_window.resizable(width=False, height=False)
                login_window_place()
                dynamic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))

                laboutmbar_btn.place(x=0, y=0)
                lmbar_separator.place(x=0, y=31, width=500)
                loginprofile_imglb.place(x=190, y=31)
                username_label.place(x=115, y=150)
                password_label.place(x=115, y=215)
                rememberlb.place(x=6, y=328)
                username_entry.place(x=115, y=175, height=30)
                password_entry.place(x=115, y=240, height=30)
                loginbtn.place(y=280)
                infobtn.place(x=457, y=319)
                settingsbtn.place(x=464, y=0)
                basics_msg.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))
                dynamic_window.deiconify()
                dynamic_window.focus_force()
                username_entry.focus()
                    
            def main_window():
                global username_entry, password_entry, dynamic_window, username
                username_get = username_entry.get()
                password_get = password_entry.get()
                username = username_get.lower()
                password = password_get.lower()
                try:
                    with open(os.path.join(os.path.dirname(__file__), "Data/account.dat"), "r") as accountfile:
                            accountreader = csv.reader(accountfile, delimiter=",")
                            accountdata = list(accountreader)
                    if accountdata[0][0] == username and accountdata[0][1] == password:     
                        laboutmbar_btn.place_forget()
                        lmbar_separator.place_forget()
                        loginprofile_imglb.place_forget()
                        username_label.place_forget()
                        password_label.place_forget()
                        rememberlb.place_forget()
                        username_entry.place_forget()
                        password_entry.place_forget()
                        loginbtn.place_forget()
                        infobtn.place_forget()
                        settingsbtn.place_forget()
                        dynamic_window.withdraw()

                        eng_langrb.config(command=eng_lang_mainwindow)
                        esp_langrb.config(command=esp_lang_mainwindow)

                        lang_value = languagegroup.get()
                        if lang_value == 1:
                            eng_lang_mainwindow()
                        elif lang_value == 2:
                            esp_lang_mainwindow()

                        # ============================================== MAIN WINDOW FUNCTIONS ============================================== #  
                        def mainmenubar_mw():
                            mainmbar_btn.place(x=0, y=0)
                            aboutmbar_btn.place(y=0)

                        def labels_mw():
                            search_exlb.place(x=373, y=151)
                            idlb.place(x=210, y=507)
                            brandlb.place(x=210, y=547)
                            modellb.place(x=210, y=587)
                            colorlb.place(x=210, y=627)
                            datelb.place(x=210, y=667)
                            inventorylb.place(x=18, y=146)    

                        def separators_mw():
                            menubar_separator.place(x=0, y=31, width=745)
                            inventory_separator.place(x=0, y=108, width=745)
                            modes_separator.place(x=0, y=415, width=745)
                            devices_separator.place(x=0, y=490, width=745)
                
                        def entrys_mw():
                            id_entry.place(x=277, y=503, height=30)
                            brand_entry.place(x=277, y=543, height=30)
                            model_entry.place(x=277, y=583, height=30)
                            color_entry.place(x=277, y=623, height=30)
                            date_entry.place(x=277, y=663, height=30)
                            search_entry.place(x=373, y=120, height=30)
                            
                        def clear_mw():
                            id_entry.delete(0, tk.END)
                            brand_entry.delete(0, tk.END)
                            model_entry.delete(0, tk.END)
                            color_entry.delete(0, tk.END)
                            date_entry.delete(0, tk.END)
                            id_entry.focus()

                        def sl_group_mw():
                            sl_group = tk.IntVar()
                            sl_computersrb.config(variable=sl_group, fg="#00A007", activeforeground="#00A007")
                            sl_computersrb.place(x=57, y=426, width=120)
                            sl_computersrb.config(indicatoron=False)
                            sl_mobilesrb.config(variable=sl_group, fg="#00A007", activeforeground="#00A007")
                            sl_mobilesrb.place(x=315, y=426, width=120)
                            sl_mobilesrb.config(indicatoron=False)
                            sl_gadgetsrb.config(variable=sl_group, fg="#00A007", activeforeground="#00A007")
                            sl_gadgetsrb.place(x=570, y=426, width=120)
                            sl_gadgetsrb.config(indicatoron=False)

                        def buttons_mw():
                            addbtn.place(x=585, y=502, width=139)
                            clearbtn.place(x=585, y=542, width=139)
                            searchbtn.config(command=s_byid_com)
                            searchbtn.place(x=664, y=121)
                            addmodehelp_btn.place(x=673, y=0)
                            showexported_folderbtn.place(x=636, y=0)
                            showexported_folderbtn.config(command=showexportedfolder)

                        # ================================================================================================================== #  
                        def reflesh_tb_com():
                            db_table.delete(*db_table.get_children())
                            with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "r") as refleshfile:
                                data = refleshfile.readlines()
                            if len(data) > 10:
                                table_scrollbar.place(x=706, y=183, height=219, width=17)
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
                                table_scrollbar.place(x=706, y=183, height=219, width=17)
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
                                table_scrollbar.place(x=706, y=183, height=219, width=17)
                            else:
                                table_scrollbar.place_forget()
                            for row in data:
                                id, brand, model, color, date = row.strip().split(",")
                                db_table.insert("", "end", values=(id, brand, model, color, date))

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
                                    table_scrollbar.place(x=706, y=183, height=219, width=17)
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
                                    table_scrollbar.place(x=706, y=183, height=219, width=17)
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
                                    table_scrollbar.place(x=706, y=183, height=219, width=17)
                                else:
                                    table_scrollbar.place_forget()
                                for row in filtered_data:
                                    db_table.insert('', 'end', values=row)

                        def optionselected_default(action):
                            rb_selected = action.widget
                            if rb_selected.cget("value") == "computers":
                                sl_computersrb.select()
                                device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Computers1.png"))
                                device_imglb.config(image=device_img)
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    search_exlb.config(text="Example: CM-001")
                                elif lang_value == 2:
                                    search_exlb.config(text="Ejemplo: CM-001")
                                reflesh_tb_com()
                                addbtn.config(command=add_com)
                                searchbtn.config(command=s_byid_com)
                            elif rb_selected.cget("value") == "mobiles":
                                sl_mobilesrb.select()
                                device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Mobiles1.png"))
                                device_imglb.config(image=device_img)
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    search_exlb.config(text="Example: MB-001")
                                elif lang_value == 2:
                                    search_exlb.config(text="Ejemplo: MB-001")
                                reflesh_tb_mob()
                                addbtn.config(command=add_mob)
                                searchbtn.config(command=s_byid_mob)
                            elif rb_selected.cget("value") == "gadgets":
                                sl_gadgetsrb.select()
                                device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Gadgets1.png"))
                                device_imglb.config(image=device_img)
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    search_exlb.config(text="Example: GD-001")
                                elif lang_value == 2:
                                    search_exlb.config(text="Ejemplo: GD-001")
                                reflesh_tb_gad()
                                addbtn.config(command=add_gad)
                                searchbtn.config(command=s_byid_gad)
                                
                        def optionselected_mode(action):
                            global rb_selected
                            rb_selected = action.widget
                            if rb_selected.cget("value") == "addmode":
                                addrb.select()
                                device_imglb.place(x=15, y=500)
                                dynamic_window.geometry("745x720")
                                device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Computers1.png"))
                                addmodehelp_btn.place(x=673, y=0)
                                device_imglb.config(image=device_img)
                                clear_mw()
                                def optionselected_default(action):
                                    rb_selected = action.widget
                                    if rb_selected.cget("value") == "computers":
                                        sl_computersrb.select()
                                        device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Computers1.png"))
                                        device_imglb.config(image=device_img)
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            search_exlb.config(text="Example: CM-001")
                                        elif lang_value == 2:
                                            search_exlb.config(text="Ejemplo: CM-001")
                                        reflesh_tb_com()
                                        addbtn.config(command=add_com)
                                        searchbtn.config(command=s_byid_com)
                                    elif rb_selected.cget("value") == "mobiles":
                                        sl_mobilesrb.select()
                                        device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Mobiles1.png"))
                                        device_imglb.config(image=device_img)
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            search_exlb.config(text="Example: MB-001")
                                        elif lang_value == 2:
                                            search_exlb.config(text="Ejemplo: MB-001")
                                        reflesh_tb_mob()
                                        addbtn.config(command=add_mob)
                                        searchbtn.config(command=s_byid_mob)
                                    elif rb_selected.cget("value") == "gadgets":
                                        sl_gadgetsrb.select()
                                        device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Gadgets1.png"))
                                        device_imglb.config(image=device_img)
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            search_exlb.config(text="Example: GD-001")
                                        elif lang_value == 2:
                                            search_exlb.config(text="Ejemplo: GD-001")
                                        reflesh_tb_gad()
                                        addbtn.config(command=add_gad)
                                        searchbtn.config(command=s_byid_gad)
                                sl_computersrb.bind("<ButtonRelease-1>", optionselected_default)
                                sl_computersrb.bind("<KeyRelease-space>", optionselected_default)
                                sl_mobilesrb.bind("<ButtonRelease-1>", optionselected_default)
                                sl_mobilesrb.bind("<KeyRelease-space>", optionselected_default)
                                sl_gadgetsrb.bind("<ButtonRelease-1>", optionselected_default)
                                sl_gadgetsrb.bind("<KeyRelease-space>", optionselected_default)
                                lang_value = languagegroup.get()
            
                                editbtn.place_forget()
                                deletebtn.place_forget()
                                addbtn.config(cursor="hand2", command=add_com)
                                clearbtn.config(cursor="hand2", command=clear_mw)
                                addbtn.place(x=585, y=502, width=139)
                                clearbtn.place(x=585, y=542, width=139)
                                
                                idlb.config(fg="#00A007")
                                id_entry.config(cursor= "xterm", highlightcolor="#00A007", highlightbackground="#00A007", highlightthickness=2) 
                                id_entry.focus()
                                brandlb.place(x=210, y=547)
                                modellb.place(x=210, y=587)
                                colorlb.place(x=210, y=627)
                                datelb.place(x=210, y=667)  
                                brand_entry.place(x=277, y=543, height=30)
                                model_entry.place(x=277, y=583, height=30)
                                color_entry.place(x=277, y=623, height=30)
                                date_entry.place(x=277, y=663, height=30)

                                editmodehelp_btn.place_forget()
                                deletemodehelp_btn.place_forget()                    
                                
                                sl_computersrb.config(cursor="hand2", fg="#00A007", activeforeground="#00A007")
                                sl_computersrb.select()
                                sl_mobilesrb.config(cursor="hand2", fg="#00A007", activeforeground="#00A007")
                                sl_gadgetsrb.config(cursor="hand2", fg="#00A007", activeforeground="#00A007")
                                searchbtn.config(command=s_byid_com)
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    search_exlb.config(text="Example: CM-001")
                                elif lang_value == 2:
                                    search_exlb.config(text="Ejemplo: CM-001")
                                reflesh_tb_com()

                            elif rb_selected.cget("value") == "editmode":
                                editrb.select()
                                device_imglb.place(x=15, y=500)
                                dynamic_window.geometry("745x720")
                                device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Computers1.png"))
                                editmodehelp_btn.place(x=673, y=0)
                                device_imglb.config(image=device_img)
                                clear_mw()
                                def optionselected_edit(action):
                                    rb_selected = action.widget
                                    if rb_selected.cget("value") == "computers":
                                        sl_computersrb.select()
                                        device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Computers1.png"))
                                        device_imglb.config(image=device_img)
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            search_exlb.config(text="Example: CM-001")
                                        elif lang_value == 2:
                                            search_exlb.config(text="Ejemplo: CM-001")
                                        reflesh_tb_com()
                                        editbtn.config(command=edit_com)
                                        searchbtn.config(command=s_byid_com)
                                    elif rb_selected.cget("value") == "mobiles":
                                        sl_mobilesrb.select()
                                        device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Mobiles1.png"))
                                        device_imglb.config(image=device_img)
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            search_exlb.config(text="Example: MB-001")
                                        elif lang_value == 2:
                                            search_exlb.config(text="Ejemplo: MB-001")
                                        reflesh_tb_mob()
                                        editbtn.config(command=edit_mob)
                                        searchbtn.config(command=s_byid_mob)
                                    elif rb_selected.cget("value") == "gadgets":
                                        sl_gadgetsrb.select()
                                        device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Gadgets1.png"))
                                        device_imglb.config(image=device_img)
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            search_exlb.config(text="Example: GD-001")
                                        elif lang_value == 2:
                                            search_exlb.config(text="Ejemplo: GD-001")
                                        reflesh_tb_gad()
                                        editbtn.config(command=edit_gad)
                                        searchbtn.config(command=s_byid_gad)
                                sl_computersrb.bind("<ButtonRelease-1>", optionselected_edit)
                                sl_computersrb.bind("<KeyRelease-space>", optionselected_edit)
                                sl_mobilesrb.bind("<ButtonRelease-1>", optionselected_edit)
                                sl_mobilesrb.bind("<KeyRelease-space>", optionselected_edit)
                                sl_gadgetsrb.bind("<ButtonRelease-1>", optionselected_edit)
                                sl_gadgetsrb.bind("<KeyRelease-space>", optionselected_edit)
            
                                addbtn.place_forget()
                                deletebtn.place_forget()
                                editbtn.config(cursor="hand2", command=edit_com)
                                clearbtn.config(cursor="hand2", command=clear_mw)
                                editbtn.place(x=585, y=502, width=139)
                                clearbtn.place(x=585, y=542, width=139)

                                idlb.config(fg= "#0078FF")
                                id_entry.config(highlightcolor="#0078FF", highlightbackground="#0078FF", highlightthickness=2)
                                id_entry.focus()
                                brandlb.place(x=210, y=547)
                                modellb.place(x=210, y=587)
                                colorlb.place(x=210, y=627)
                                datelb.place(x=210, y=667)                   
                                brand_entry.place(x=277, y=543, height=30)
                                model_entry.place(x=277, y=583, height=30)
                                color_entry.place(x=277, y=623, height=30)
                                date_entry.place(x=277, y=663, height=30)

                                addmodehelp_btn.place_forget()
                                deletemodehelp_btn.place_forget()

                                sl_computersrb.config(cursor="hand2", fg= "#0078FF", activeforeground="#0078FF")
                                sl_computersrb.select()
                                sl_mobilesrb.config(cursor="hand2", fg= "#0078FF", activeforeground="#0078FF")
                                sl_gadgetsrb.config(cursor="hand2", fg= "#0078FF", activeforeground="#0078FF")
                                searchbtn.config(command=s_byid_com)
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    search_exlb.config(text="Example: CM-001")
                                elif lang_value == 2:
                                    search_exlb.config(text="Ejemplo: CM-001")
                                reflesh_tb_com()

                            elif rb_selected.cget("value") == "deletemode":
                                deleterb.select()
                                device_imglb.place(x=90, y=500)
                                dynamic_window.geometry("745x590")
                                device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Computers2.png"))
                                deletemodehelp_btn.place(x=673, y=0)
                                device_imglb.config(image=device_img)
                                clear_mw()
                                def optionselected_del(action):
                                    rb_selected = action.widget
                                    if rb_selected.cget("value") == "computers":
                                        sl_computersrb.select()
                                        device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Computers2.png"))
                                        device_imglb.config(image=device_img)
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            search_exlb.config(text="Example: CM-001")
                                        elif lang_value == 2:
                                            search_exlb.config(text="Ejemplo: CM-001")
                                        reflesh_tb_com()
                                        deletebtn.config(command=del_com)
                                        searchbtn.config(command=s_byid_com)
                                    elif rb_selected.cget("value") == "mobiles":
                                        sl_mobilesrb.select()
                                        device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Mobiles2.png"))
                                        device_imglb.config(image=device_img)
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            search_exlb.config(text="Example: MB-001")
                                        elif lang_value == 2:
                                            search_exlb.config(text="Ejemplo: MB-001")
                                        reflesh_tb_mob()
                                        deletebtn.config(command=del_mob)
                                        searchbtn.config(command=s_byid_mob)
                                    elif rb_selected.cget("value") == "gadgets":
                                        sl_gadgetsrb.select()
                                        device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Gadgets2.png"))
                                        device_imglb.config(image=device_img)
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            search_exlb.config(text="Example: GD-001")
                                        elif lang_value == 2:
                                            search_exlb.config(text="Ejemplo: GD-001")
                                        reflesh_tb_gad()
                                        deletebtn.config(command=del_gad)
                                        searchbtn.config(command=s_byid_gad) 
                                sl_computersrb.bind("<ButtonRelease-1>", optionselected_del)
                                sl_computersrb.bind("<KeyRelease-space>", optionselected_del)
                                sl_mobilesrb.bind("<ButtonRelease-1>", optionselected_del)
                                sl_mobilesrb.bind("<KeyRelease-space>", optionselected_del)
                                sl_gadgetsrb.bind("<ButtonRelease-1>", optionselected_del)
                                sl_gadgetsrb.bind("<KeyRelease-space>", optionselected_del)

                                addbtn.place_forget()
                                editbtn.place_forget()
                                deletebtn.config(cursor="hand2", command=del_com)
                                clearbtn.config(cursor="hand2", command=clear_mw)
                                deletebtn.place(x=585, y=502, width=139)
                                clearbtn.place(x=585, y=542, width=139)
                                
                                brandlb.place_forget()
                                modellb.place_forget()
                                colorlb.place_forget()
                                datelb.place_forget()
                                brand_entry.place_forget()
                                model_entry.place_forget()
                                color_entry.place_forget()
                                date_entry.place_forget()
                                idlb.config(fg="#FE2727")
                                id_entry.config(highlightcolor="#FE2727", highlightbackground="#FE2727", highlightthickness=2)
                                id_entry.focus()

                                addmodehelp_btn.place_forget()
                                editmodehelp_btn.place_forget()

                                sl_computersrb.config(cursor="hand2", fg="#FE2727", activeforeground="#FE2727")
                                sl_computersrb.select()
                                sl_mobilesrb.config(cursor="hand2", fg="#FE2727", activeforeground="#FE2727")
                                sl_gadgetsrb.config(cursor="hand2", fg="#FE2727", activeforeground="#FE2727")
                                searchbtn.config(command=s_byid_com)
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    search_exlb.config(text="Example: CM-001")
                                elif lang_value == 2:
                                    search_exlb.config(text="Ejemplo: CM-001")
                                reflesh_tb_com()
                        
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
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    add_prod_save_eng()
                                elif lang_value == 2:
                                    add_prod_save_esp()
                                reflesh_tb_com()
                            else:
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    add_prod_empty_eng()
                                elif lang_value == 2:
                                    add_prod_empty_esp()

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
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    add_prod_save_eng()
                                elif lang_value == 2:
                                    add_prod_save_esp()
                                reflesh_tb_mob()
                            else:
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    add_prod_empty_eng()
                                elif lang_value == 2:
                                    add_prod_empty_esp()

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
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    add_prod_save_eng()
                                elif lang_value == 2:
                                    add_prod_save_esp()
                                reflesh_tb_gad()
                            else:
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    add_prod_empty_eng()
                                elif lang_value == 2:
                                    add_prod_empty_esp()

                        def edit_com():
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
                            if "" in id_upper and brand_upper and model_upper and color_upper and date_upper:
                                with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "r", newline="") as computersfile:
                                    computersreader = csv.reader(computersfile)
                                    computersdata = list(computersreader)
                                ids = set([row[0].upper() for row in computersdata])
                                if id_upper in ids:                     
                                    basics_btn_ok.place_forget()
                                    lang_value = languagegroup.get()   
                                    if lang_value == 1:
                                        edit_prod_ask_eng()
                                    elif lang_value == 2:
                                        edit_prod_ask_esp()
                                    def edit_yes():
                                        basics_msg.withdraw()
                                        basics_btn_yes.place_forget()
                                        basics_btn_no.place_forget() 
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
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            edit_prod_save_eng()
                                        elif lang_value == 2:
                                            edit_prod_save_esp()
                                        clear_mw()
                                        reflesh_tb_com()
                                    def edit_no():
                                        restore_elements()
                                        basics_msg.withdraw()
                                        basics_btn_yes.place_forget()
                                        basics_btn_no.place_forget()
                                        basics_msg.grab_release()
                                        basics_msg.transient(None)
                                    basics_btn_ok.place_forget()
                                    basics_btn_yes.config(command=edit_yes)
                                    basics_btn_no.config(command=edit_no)
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        edit_prod_ask_eng()
                                    elif lang_value == 2:
                                        edit_prod_ask_esp()
                                elif id_upper == "":
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
                            else:
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    edit_prod_empty_eng()
                                elif lang_value == 2:
                                    edit_prod_empty_esp() 

                        def edit_mob():
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
                            if "" in id_upper and brand_upper and model_upper and color_upper and date_upper:
                                with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "r", newline="") as mobilesfile:
                                    mobilesreader = csv.reader(mobilesfile)
                                    mobilesdata = list(mobilesreader)
                                ids = set([row[0].upper() for row in mobilesdata])
                                if id_upper in ids:                     
                                    basics_btn_ok.place_forget()
                                    lang_value = languagegroup.get()   
                                    if lang_value == 1:
                                        edit_prod_ask_eng()
                                    elif lang_value == 2:
                                        edit_prod_ask_esp()
                                    def edit_yes():
                                        basics_msg.withdraw()
                                        basics_btn_yes.place_forget()
                                        basics_btn_no.place_forget() 
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
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            edit_prod_save_eng()
                                        elif lang_value == 2:
                                            edit_prod_save_esp()
                                        clear_mw()
                                        reflesh_tb_mob()
                                    def edit_no():
                                        restore_elements()
                                        basics_msg.withdraw()
                                        basics_btn_yes.place_forget()
                                        basics_btn_no.place_forget()
                                        basics_msg.grab_release()
                                        basics_msg.transient(None)
                                    basics_btn_ok.place_forget()
                                    basics_btn_yes.config(command=edit_yes)
                                    basics_btn_no.config(command=edit_no)
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        edit_prod_ask_eng()
                                    elif lang_value == 2:
                                        edit_prod_ask_esp()
                                elif id_upper == "":
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
                            else:
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    edit_prod_empty_eng()
                                elif lang_value == 2:
                                    edit_prod_empty_esp() 

                        def edit_gad():
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
                            if "" in id_upper and brand_upper and model_upper and color_upper and date_upper:
                                with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "r", newline="") as gadgetsfile:
                                    gadgetsreader = csv.reader(gadgetsfile)
                                    gadgetsdata = list(gadgetsreader)
                                ids = set([row[0].upper() for row in gadgetsdata])
                                if id_upper in ids:                     
                                    basics_btn_ok.place_forget()
                                    lang_value = languagegroup.get()   
                                    if lang_value == 1:
                                        edit_prod_ask_eng()
                                    elif lang_value == 2:
                                        edit_prod_ask_esp()
                                    def edit_yes():
                                        basics_msg.withdraw()
                                        basics_btn_yes.place_forget()
                                        basics_btn_no.place_forget() 
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
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            edit_prod_save_eng()
                                        elif lang_value == 2:
                                            edit_prod_save_esp()
                                        clear_mw()
                                        reflesh_tb_gad()
                                    def edit_no():
                                        restore_elements()
                                        basics_msg.withdraw()
                                        basics_btn_yes.place_forget()
                                        basics_btn_no.place_forget()
                                        basics_msg.grab_release()
                                        basics_msg.transient(None)
                                    basics_btn_ok.place_forget()
                                    basics_btn_yes.config(command=edit_yes)
                                    basics_btn_no.config(command=edit_no)
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        edit_prod_ask_eng()
                                    elif lang_value == 2:
                                        edit_prod_ask_esp()
                                elif id_upper == "":
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

                        def del_com():
                            global del_no
                            id_get = id_entry.get()
                            id_upper = id_get.upper()
                            if "" in id_upper:
                                with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "r", newline="") as computersfile:
                                    computersreader = csv.reader(computersfile)
                                    computersdata = list(computersreader)
                                ids = set([row[0].upper() for row in computersdata])
                                if id_upper in ids:                     
                                    basics_btn_ok.place_forget()
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        delete_prod_ask_eng()
                                    elif lang_value == 2:
                                        delete_prod_ask_esp()
                                ids = set([row[0].upper() for row in computersdata])
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
                                    basics_msg.withdraw()
                                    basics_btn_yes.place_forget()
                                    basics_btn_no.place_forget()
                                    for row in computersdata:
                                        if row[0].upper() == id_upper:
                                            computersdata.remove(row)
                                    with open(os.path.join(os.path.dirname(__file__), "Data/computers_list.csv"), "w", newline="") as computersfile:
                                        computerswriter = csv.writer(computersfile)
                                        computerswriter.writerows(computersdata)
                                        computersfile.seek(0, 2)
                                    clear_mw()
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        delete_prod_del_eng()
                                    elif lang_value == 2:
                                        delete_prod_del_esp()
                                    reflesh_tb_com()
                                def del_no():
                                    restore_elements()
                                    basics_msg.withdraw()
                                    basics_btn_yes.place_forget()
                                    basics_btn_no.place_forget()
                                    basics_msg.grab_release()
                                    basics_msg.transient(None)
                                basics_btn_yes.config(command=del_yes)
                                basics_btn_no.config(command=del_no)
                                        
                        def del_mob():
                            global del_no
                            id_get = id_entry.get()
                            id_upper = id_get.upper()
                            if "" in id_upper:
                                with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "r", newline="") as mobilesfile:
                                    mobilesreader = csv.reader(mobilesfile)
                                    mobilesdata = list(mobilesreader)
                                ids = set([row[0].upper() for row in mobilesdata])
                                if id_upper in ids:                     
                                    basics_btn_ok.place_forget()
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        delete_prod_ask_eng()
                                    elif lang_value == 2:
                                        delete_prod_ask_esp()
                                ids = set([row[0].upper() for row in mobilesdata])
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
                                    basics_msg.withdraw()
                                    basics_btn_yes.place_forget()
                                    basics_btn_no.place_forget()
                                    for row in mobilesdata:
                                        if row[0].upper() == id_upper:
                                            mobilesdata.remove(row)
                                    with open(os.path.join(os.path.dirname(__file__), "Data/mobiles_list.csv"), "w", newline="") as mobilesfile:
                                        mobileswriter = csv.writer(mobilesfile)
                                        mobileswriter.writerows(mobilesdata)
                                        mobilesfile.seek(0, 2)
                                    clear_mw()
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        delete_prod_del_eng()
                                    elif lang_value == 2:
                                        delete_prod_del_esp()
                                    reflesh_tb_mob()
                                def del_no():
                                    restore_elements()
                                    basics_msg.withdraw()
                                    basics_btn_yes.place_forget()
                                    basics_btn_no.place_forget()
                                    basics_msg.grab_release()
                                    basics_msg.transient(None)
                                basics_btn_yes.config(command=del_yes)
                                basics_btn_no.config(command=del_no)

                        def del_gad():
                            global del_no
                            id_get = id_entry.get()
                            id_upper = id_get.upper()
                            if "" in id_upper:
                                with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "r", newline="") as gadgetsfile:
                                    gadgetsreader = csv.reader(gadgetsfile)
                                    gadgetsdata = list(gadgetsreader)
                                ids = set([row[0].upper() for row in gadgetsdata])
                                if id_upper in ids:                     
                                    basics_btn_ok.place_forget()
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        delete_prod_ask_eng()
                                    elif lang_value == 2:
                                        delete_prod_ask_esp()
                                ids = set([row[0].upper() for row in gadgetsdata])
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
                                    basics_msg.withdraw()
                                    basics_btn_yes.place_forget()
                                    basics_btn_no.place_forget()
                                    for row in gadgetsdata:
                                        if row[0].upper() == id_upper:
                                            gadgetsdata.remove(row)
                                    with open(os.path.join(os.path.dirname(__file__), "Data/gadgets_list.csv"), "w", newline="") as gadgetsfile:
                                        gadgetswriter = csv.writer(gadgetsfile)
                                        gadgetswriter.writerows(gadgetsdata)
                                        gadgetsfile.seek(0, 2)
                                    clear_mw()
                                    lang_value = languagegroup.get()
                                    if lang_value == 1:
                                        delete_prod_del_eng()
                                    elif lang_value == 2:
                                        delete_prod_del_esp()
                                    reflesh_tb_gad()
                                def del_no():
                                    restore_elements()
                                    basics_msg.withdraw()
                                    basics_btn_yes.place_forget()
                                    basics_btn_no.place_forget()
                                    basics_msg.grab_release()
                                    basics_msg.transient(None)
                                basics_btn_yes.config(command=del_yes)
                                basics_btn_no.config(command=del_no)
                        
                        def showexportedfolder():
                            os.startfile(os.path.join(os.path.dirname(__file__), "Exported"))

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
                            lang_value = languagegroup.get()
                            if lang_value == 1:
                                export_file_msg_eng()
                            elif lang_value == 2:
                                export_file_msg_esp()

                        # ========================================================================================================= #
                        dynamic_window.title("Device Warehouse Inventory ("+username+")")
                        dynamic_window.resizable(width=False, height=False)
                        main_window_place()
                        dynamic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/main.ico"))
                        basics_msg.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/main.ico"))
                            
                        # ========== DEVICE IMAGE ========== #
                        device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/Computers1.png"))
                        device_imglb.config(image=device_img)
                        device_imglb.place(x=15, y=500)

                        # ========== DATA BASE TABLE ========== #
                        reflesh_tb_com()
                        db_table.place(x=20, y=183) 
                            
                        # ========== RADIO BUTTONS ========== #
                        addrb.bind("<ButtonRelease-1>", optionselected_mode)
                        addrb.bind("<KeyRelease-space>", optionselected_mode)
                        addrb.config(variable=selectmode_group)
                        addrb.place(x=57, y=42, width=120)
                        addrb.config(indicatoron=False)
                        addrb.select()
                        editrb.bind("<ButtonRelease-1>", optionselected_mode)
                        editrb.bind("<KeyRelease-space>", optionselected_mode)
                        editrb.config(variable=selectmode_group)
                        editrb.place(x=315, y=42, width=120)
                        editrb.config(indicatoron=False)
                        deleterb.bind("<ButtonRelease-1>", optionselected_mode)
                        deleterb.bind("<KeyRelease-space>", optionselected_mode)
                        deleterb.config(variable=selectmode_group)
                        deleterb.place(x=570, y=42, width=120)
                        deleterb.config(indicatoron=False)
                        
                        sl_computersrb.bind("<ButtonRelease-1>", optionselected_default)
                        sl_computersrb.bind("<KeyRelease-space>", optionselected_default)
                        sl_mobilesrb.bind("<ButtonRelease-1>", optionselected_default)
                        sl_mobilesrb.bind("<KeyRelease-space>", optionselected_default)
                        sl_gadgetsrb.bind("<ButtonRelease-1>", optionselected_default)
                        sl_gadgetsrb.bind("<KeyRelease-space>", optionselected_default)
                        sl_group_mw()
                        sl_computersrb.select()
                        
                        # ========== LABELS ========== #
                        idlb.config(fg="#00A007")
                        id_entry.config(cursor= "xterm", highlightcolor="#00A007", highlightbackground="#00A007", highlightthickness=2)
                        brand_entry.config(cursor= "xterm", highlightthickness=2)
                        model_entry.config(cursor= "xterm", highlightthickness=2)
                        color_entry.config(cursor= "xterm", highlightthickness=2)
                        date_entry.config(cursor= "xterm", highlightthickness=2)
                        labels_mw()
                    
                        # ========== TEXT ENTRIES ========== #
                        id_entry.config(cursor="xterm")
                        brand_entry.config(cursor="xterm")
                        model_entry.config(cursor="xterm")
                        color_entry.config(cursor="xterm")
                        date_entry.config(cursor="xterm")
                        entrys_mw()

                        # ========== BUTTONS ========== #
                        addbtn.config(cursor="hand2", command=add_com)
                        editbtn.config(cursor="hand2")
                        deletebtn.config(cursor="hand2")
                        clearbtn.config(cursor="hand2", command=clear_mw)
                        buttons_mw()
                        settingsbtn.place(x=709, y=0)

                        # ========== SEPARATORS ========== #
                        separators_mw()

                        # ========== MENU BARS ========== #
                        mainmbar.entryconfigure(0, command=exportfile)
                        mainmenubar_mw()
                        dynamic_window.deiconify()
                        clear_mw()
                    else:
                        lang_value = languagegroup.get()
                        if lang_value == 1:
                            login_error_eng()
                        elif lang_value == 2:
                            login_error_esp()
                    dynamic_window.mainloop()
                except Exception as e:
                    tk.messagebox.showerror("An error has occurred!", f"Information About the Error:\n\n{e}")
                    os.remove(os.path.join(os.path.dirname(__file__), "init"))
                    sys.exit(0)
            
            # ============================================== LOAD MAIN WINDOW ELEMENTS ============================================== #
            def load_mainmenubar():
                global mainmbar_btn, aboutmbar_btn, mainmbar, aboutmbar
                mainmbar_btn = Menubutton(dynamic_window, padx=10, pady=6)	
                mainmbar = Menu(mainmbar_btn, tearoff=False)
                mainmbar_btn["menu"]= mainmbar
                mainmbar.add_command()
                mainmbar.add_separator()				
                mainmbar.add_command()

                aboutmbar_btn = Menubutton(dynamic_window, padx=10, pady=6)	
                aboutmbar = Menu(aboutmbar_btn, tearoff=False)
                aboutmbar_btn["menu"]= aboutmbar
                aboutmbar.add_command()
                aboutmbar.add_separator()				
                aboutmbar.add_command()
                aboutmbar.add_command()

            def load_mainlabels():
                global idlb, brandlb, modellb, colorlb, datelb, search_exlb, inventorylb, device_img, device_imglb
                search_exlb = tk.Label(dynamic_window, font="SegoeUIVariable, 12")
                idlb = tk.Label(dynamic_window)
                brandlb = tk.Label(dynamic_window)
                modellb = tk.Label(dynamic_window)
                colorlb = tk.Label(dynamic_window)
                datelb = tk.Label(dynamic_window)
                inventorylb = tk.Label(dynamic_window)

                device_img = tk.PhotoImage()
                device_imglb = tk.Label(dynamic_window)
                icons_wm = tk.Label(dynamic_window, text="📝 💾 🔐 📂")

            def load_mainentrys():
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
                    
                global id_entry, brand_entry, model_entry, color_entry, date_entry, search_entry
                id_entry =tk.Entry(dynamic_window, width=31, cursor= "xterm", font="SegoeUIVariable, 12", validate="key", validatecommand=(dynamic_window.register(validate_value_id), "%P"))
                brand_entry =tk.Entry(dynamic_window, width=31, cursor= "xterm", font="SegoeUIVariable, 12", validate="key", validatecommand=(dynamic_window.register(validate_value_brand), "%P"))
                model_entry =tk.Entry(dynamic_window, width=31, cursor= "xterm", font="SegoeUIVariable, 12", validate="key", validatecommand=(dynamic_window.register(validate_value_model), "%P"))
                color_entry =tk.Entry(dynamic_window, width=31, cursor= "xterm", font="SegoeUIVariable, 12", validate="key", validatecommand=(dynamic_window.register(validate_value_color), "%P"))
                date_entry =tk.Entry(dynamic_window, width=31, cursor= "xterm", font="SegoeUIVariable, 12", validate="key", validatecommand=(dynamic_window.register(validate_value_date), "%P"))
                search_entry = tk.Entry(dynamic_window, width=30, font="SegoeUIVariable, 12")
                        
            def load_maintable():
                global db_table, table_scrollbar
                db_table = ttk.Treeview(dynamic_window, selectmode="browse")
                db_table['show']='headings'
                db_table["columns"]=("id", "brand", "model", "color", "date")
                
                db_table.column("id", width=70, minwidth=70, anchor=tk.SW)
                db_table.column("brand", width=150, minwidth=150, anchor=tk.SW)
                db_table.column("model", width=230, minwidth=230, anchor=tk.SW)
                db_table.column("color", width=100, minwidth=100, anchor=tk.SW)
                db_table.column("date", width=150, minwidth=150, anchor=tk.SW)

                table_scrollbar = ttk.Scrollbar(dynamic_window, orient="vertical", command=db_table.yview)
                db_table.configure(yscrollcommand=table_scrollbar.set)

            def load_mainrbs():
                global addrb, editrb, deleterb, sl_computersrb, sl_mobilesrb, sl_gadgetsrb, selectmode_group, modes_group
                modes_group = tk.IntVar()
                addrb = tk.Radiobutton(dynamic_window, value="addmode", variable=modes_group, padx="14", pady="5", cursor="hand2")
                editrb = tk.Radiobutton(dynamic_window, value="editmode", variable=modes_group, padx="14", pady="5", cursor="hand2")
                deleterb = tk.Radiobutton(dynamic_window, value="deletemode", variable=modes_group, padx="5", pady="5",cursor="hand2")

                selectmode_group = tk.IntVar()
                sl_computersrb = tk.Radiobutton(dynamic_window, value="computers", variable=selectmode_group, padx="5", pady="5", cursor="hand2")
                sl_mobilesrb = tk.Radiobutton(dynamic_window, value="mobiles", variable=selectmode_group, padx="16", pady="5", cursor="hand2")
                sl_gadgetsrb = tk.Radiobutton(dynamic_window, value="gadgets", variable=selectmode_group, padx="14", pady="5", cursor="hand2")

                
            def load_mainbtns():
                global addbtn, editbtn, deletebtn, clearbtn, searchbtn, addmodehelp_btn, editmodehelp_btn, deletemodehelp_btn, showexported_folderbtn
                addbtn = tk.Button(dynamic_window, cursor= "hand2", padx=50, width=3)
                editbtn = tk.Button(dynamic_window, cursor= "hand2", padx=50, width=3)
                deletebtn = tk.Button(dynamic_window, cursor= "hand2", padx=50, width=3)
                clearbtn = tk.Button(dynamic_window, cursor= "hand2", padx=50, width=3)
                searchbtn = tk.Button(dynamic_window, cursor= "hand2", padx=12, width=3)

                addmodehelp_btn = tk.Button(dynamic_window, cursor= "hand2")
                editmodehelp_btn = tk.Button(dynamic_window, cursor= "hand2")
                deletemodehelp_btn = tk.Button(dynamic_window, cursor= "hand2")

                showexported_folderbtn = tk.Button(dynamic_window, text="📂",font="15", cursor= "hand2", width=3)

            def load_mainseparators():
                global menubar_separator, modes_separator, inventory_separator, devices_separator
                menubar_separator = tk.Frame(dynamic_window, height=1, bd=0)
                modes_separator = tk.Frame(dynamic_window, height=1, bd=0)
                inventory_separator = tk.Frame(dynamic_window, height=1, bd=0)
                devices_separator = tk.Frame(dynamic_window, height=1, bd=0)

            # ============================================== LOAD ALL WINDOWS ELEMENTS ============================================== #
            def settings():
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

                lightthemerb.place(x=90, y=51)
                darkthemerb.place(x=205, y=51)
                eng_langrb.place(x=90, y=170)
                esp_langrb.place(x=205,y=170)

                setting_btn_close.config(command=hide_settings)
                setting_btn_close.place(x=144, y=250)

                settings_window.transient(dynamic_window)
                settings_window.deiconify()

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
                username_label.config(fg="black", bg="white")
                password_label.config(fg="black", bg="white")
                rememberlb.config(bg="white")

            def loginlabels_dark():
                loginprofile_imglb.config(bg="black")
                username_label.config(fg="white", bg="black")
                password_label.config(fg="white", bg="black")
                rememberlb.config(bg="black")

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

            # ============================================== LIGHT/DARK MAIN WINDOWS THEME ============================================== #
            def mainmenubar_mw_dark():
                mainmbar_btn.config(background="black", foreground="white", activebackground="#292929", activeforeground="white")
                mainmbar.entryconfigure(0, background="black", foreground="white")
                mainmbar.entryconfigure(1, background="black")
                mainmbar.entryconfigure(2, background="black", foreground="white")

                aboutmbar_btn.config(background="black", foreground="white", activebackground="#292929", activeforeground="white")
                aboutmbar.entryconfigure(0, background="black", foreground="white")
                aboutmbar.entryconfigure(1, background="black")
                aboutmbar.entryconfigure(2, background="black", foreground="white")
                aboutmbar.entryconfigure(3, background="black", foreground="white")

            def mainmenubar_mw_light():
                mainmbar_btn.config(background="white", foreground="black", activebackground="#E7E7E7", activeforeground="black")
                mainmbar.entryconfigure(0, background="white", foreground="black")
                mainmbar.entryconfigure(1, background="white")
                mainmbar.entryconfigure(2, background="white", foreground="black")

                aboutmbar_btn.config(background="white", foreground="black", activebackground="#E7E7E7", activeforeground="black")
                aboutmbar.entryconfigure(0, background="white", foreground="black")
                aboutmbar.entryconfigure(1, background="white")
                aboutmbar.entryconfigure(2, background="white", foreground="black")
                aboutmbar.entryconfigure(3, background="white", foreground="black")

            def labels_main_light():
                device_imglb.config(background="white", foreground="black")
                search_exlb.config(background="white", foreground="black")
                idlb.config(background="white")
                brandlb.config(background="white", foreground="black")
                modellb.config(background="white", foreground="black")
                colorlb.config(background="white", foreground="black")
                datelb.config(background="white", foreground="black")
                inventorylb.config(background="white", foreground="black")
                device_imglb.config(background="white")

            def labels_main_dark():
                device_imglb.config(background="black", foreground="white")
                search_exlb.config(background="black", foreground="white")
                idlb.config(background="black")
                brandlb.config(background="black", foreground="white")
                modellb.config(background="black", foreground="white")
                colorlb.config(background="black", foreground="white")
                datelb.config(background="black", foreground="white")
                inventorylb.config(background="black", foreground="white")
                device_imglb.config(background="black")

            def entrys_mw_light():
                id_entry.config(fg="black", bg="#F9F9F9", insertbackground="black")
                brand_entry.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
                model_entry.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
                color_entry.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
                date_entry.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
                search_entry.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
                
            def entrys_mw_dark():
                id_entry.config(fg="white", bg="#111111", insertbackground="white")
                brand_entry.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
                model_entry.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
                color_entry.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
                date_entry.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
                search_entry.config(fg="white", bg="#111111", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)           
                    
            def table_light():
                style_table = ttk.Style()
                style_table.theme_use("default")
                style_table.configure("light.Treeview", fieldbackground="white", background="white", foreground="black")
                style_table.configure("Treeview.Heading", background="white", foreground="black", relief="ridge")
                style_table.map("Treeview.Heading", background=[('active', 'white')])
                style_table.map("light.Treeview", background=[('selected', '#0078D7')])
                db_table.config(style="light.Treeview")
                style_table.map("Vertical.TScrollbar", background=[('active', '#F9F9F9')])
                style_table.configure("Vertical.TScrollbar", background="#EFEFEF", arrowcolor="black", troughcolor="white")    

            def table_dark():
                style_table = ttk.Style()
                style_table.theme_use("default")
                style_table.configure("dark.Treeview", fieldbackground="black", background="black", foreground="white")
                style_table.configure("Treeview.Heading", background="black", foreground="white", relief="ridge")
                style_table.map("Treeview.Heading", background=[('active', 'black')])
                style_table.map("dark.Treeview", background=[('selected', '#0078D7')])
                db_table.config(style="dark.Treeview")
                style_table.map("Vertical.TScrollbar", background=[('active', '#292929')])
                style_table.configure("Vertical.TScrollbar", background="#191919", arrowcolor="white", troughcolor="black")

            def mainrbs_light():
                addrb.config(bg="white", foreground="#009003", activebackground="#F1F1F1", activeforeground="#009003", selectcolor="#E7E7E7")
                editrb.config(bg="white", foreground="#0049DE", activebackground="#F1F1F1", activeforeground="#0049DE", selectcolor="#E7E7E7")
                deleterb.config(bg="white", foreground="#CE0000", activebackground="#F1F1F1", activeforeground="#CE0000", selectcolor="#E7E7E7")
                sl_computersrb.config(bg="white", activebackground="#F1F1F1", selectcolor="#E7E7E7")
                sl_mobilesrb.config(bg="white", activebackground="#F1F1F1", selectcolor="#E7E7E7")
                sl_gadgetsrb.config(bg="white", activebackground="#F1F1F1", selectcolor="#E7E7E7")

            def mainrbs_dark():
                addrb.config(bg="black", foreground="#009003", activebackground="#191919", activeforeground="#009003", selectcolor="#111111")
                editrb.config(bg="black", foreground="#0049DE", activebackground="#191919", activeforeground="#0049DE", selectcolor="#111111")
                deleterb.config(bg="black", foreground="#CE0000", activebackground="#191919", activeforeground="#CE0000", selectcolor="#111111")
                sl_computersrb.config(bg="black", activebackground="#191919", selectcolor="#111111")
                sl_mobilesrb.config(bg="black", activebackground="#191919", selectcolor="#111111")
                sl_gadgetsrb.config(bg="black", activebackground="#191919", selectcolor="#111111")

            def mainbtns_light():
                addbtn.config(foreground="#007A05", activeforeground="#007A05", bg="white", activebackground="#EFEFEF")
                editbtn.config(foreground="#0055FF", activeforeground="#0055FF", bg="white", activebackground="#EFEFEF")
                deletebtn.config(foreground="#EB0000", activeforeground="#EB0000", bg="white", activebackground="#EFEFEF")
                clearbtn.config(foreground="black", activeforeground="black", bg="white", activebackground="#EFEFEF")                
                searchbtn.config(foreground="black", activeforeground="black", bg="white", activebackground="#EFEFEF")
                addmodehelp_btn.config(fg="black", activeforeground="black", bg="white", activebackground="#EFEFEF")
                editmodehelp_btn.config(fg="black", activeforeground="black", bg="white", activebackground="#EFEFEF")
                deletemodehelp_btn.config(fg="black", activeforeground="black", bg="white", activebackground="#EFEFEF")
                showexported_folderbtn.config(fg="black", activeforeground="black", bg="white", activebackground="#EFEFEF")
                
                
            def mainbtns_dark():
                addbtn.config(foreground="#007A05", activeforeground="#007A05", bg="black", activebackground="#111111")
                editbtn.config(foreground="#0055FF", activeforeground="#0055FF", bg="black", activebackground="#111111")
                deletebtn.config(foreground="#EB0000", activeforeground="#EB0000", bg="black", activebackground="#111111")
                clearbtn.config(foreground="white", activeforeground="white", bg="black", activebackground="#111111")
                searchbtn.config(foreground="white", activeforeground="white", bg="black", activebackground="#111111")
                addmodehelp_btn.config(fg="white", activeforeground="white", bg="black", activebackground="#111111") 
                editmodehelp_btn.config(fg="white", activeforeground="white", bg="black", activebackground="#111111")
                deletemodehelp_btn.config(fg="white", activeforeground="white", bg="black", activebackground="#111111")
                showexported_folderbtn.config(fg="white", activeforeground="white", bg="black", activebackground="#111111")

            def mainseparators_light():
                menubar_separator.config(bg="#C0C0C0")
                modes_separator.config(bg="#C0C0C0")
                inventory_separator.config(bg="#C0C0C0")
                devices_separator.config(bg="#C0C0C0")

            def mainseparators_dark():
                menubar_separator.config(bg="#404040")
                modes_separator.config(bg="#404040")
                inventory_separator.config(bg="#404040")
                devices_separator.config(bg="#404040")

            def basics_msg_light():
                basics_msg.config(bg="white")
                basics_imglb.config(bg="white")
                basics_msg_lb.config(bg="white", fg="black")
                basics_btn_ok.config(bg="white", fg="black", cursor= "hand2", activeforeground="black", activebackground="#EFEFEF")
                basics_btn_yes.config(bg="white", cursor= "hand2", activebackground="#EFEFEF")
                basics_btn_no.config(bg="white", fg="black", cursor= "hand2", activeforeground="black", activebackground="#EFEFEF")    

            def basics_msg_dark():
                basics_msg.config(bg="black")
                basics_imglb.config(bg="black")
                basics_msg_lb.config(bg="black", fg="white")
                basics_btn_ok.config(bg="black", fg="white", cursor= "hand2", activeforeground="white", activebackground="#111111")
                basics_btn_yes.config(bg="black", cursor= "hand2", activebackground="#111111")
                basics_btn_no.config(bg="black", fg="white", cursor= "hand2", activeforeground="white", activebackground="#111111")

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
                
            # ============================================== LOAD LOGIN WINDOWELEMENTS ============================================== #
            def load_loginmenubar():
                global laboutmbar, laboutmbar_btn, lmbar_separator
                laboutmbar_btn = Menubutton(dynamic_window, pady=6)	
                laboutmbar = Menu(laboutmbar_btn, tearoff=False)
                laboutmbar_btn["menu"]= laboutmbar
                laboutmbar.add_command()
                laboutmbar.add_separator()				
                laboutmbar.add_command()
                laboutmbar.add_command()
                laboutmbar_btn.place(x=0, y=0)
                lmbar_separator = tk.Frame(dynamic_window, height=1, bd=0)

            def load_loginlabels():
                global loginprofile_img, loginprofile_imglb, username_label, password_label, rememberlb
                loginprofile_img = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/login.png"))
                loginprofile_imglb = tk.Label(dynamic_window, image=loginprofile_img)
                username_label = tk.Label(dynamic_window)
                password_label = tk.Label(dynamic_window)
                rememberlb = tk.Label(dynamic_window, cursor='hand2', fg="#0055FF", activeforeground="#0083FF")

            def load_loginentrys():
                def validate_value_account(text):
                    pattern = re.compile(r"^[a-zA-Z0-9]+$")
                    if pattern.match(text) is not None:
                        return True and len(text) <= 20
                    elif text == "":
                        return True and len(text) <= 20
                    else:
                        return False
                global username_entry, password_entry
                username_entry = tk.Entry(dynamic_window, width=30, font="SegoeUIVariable, 12", validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"))
                password_entry = tk.Entry(dynamic_window, width=30, font="SegoeUIVariable, 12", show="*", validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"))

            def load_loginbuttons():
                global loginbtn, infobtn, settingsbtn
                loginbtn = tk.Button(dynamic_window, cursor= "hand2", pady=3, width=3, command=main_window)
                infobtn = tk.Button(dynamic_window, cursor= "hand2")
                settingsbtn = tk.Button(dynamic_window, cursor= "hand2")

            # ============================================== LOAD LOGIN ============================================== #
            login_window_place()
            dynamic_window.resizable(width=False, height=False)
            dynamic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))

            # ============================================== LOAD ELEMENTS IN MEMORY ============================================== #
            # ========== LOAD LOGIN WINDOW ========== #
            load_loginlabels()
            load_loginmenubar()
            load_loginentrys()
            load_loginbuttons()

            lmbar_separator.place(x=0, y=31, width=500)
            username_label.place(x=115, y=150)
            password_label.place(x=115, y=215)
            loginprofile_imglb.place(x=200, y=40)
            username_entry.place(x=115, y=175, height=30)
            password_entry.place(x=115, y=240, height=30)
            loginbtn.place(y=280)
            infobtn.place(x=457, y=319)
            settingsbtn.place(x=464, y=0)

            rememberlb.place(x=6, y=328)
            rememberlb.bind("<Enter>", lambda event: rememberlb.config(fg="#0083FF"))
            rememberlb.bind("<Leave>", lambda event: rememberlb.config(fg="#0055FF"))

            # ========== LOAD MAIN WINDOW ========== #
            load_mainlabels()
            load_mainentrys()
            load_maintable()
            load_mainmenubar()
            load_mainrbs()
            load_mainbtns()
            load_mainseparators()

            # ========== LOAD DEFAULT LANGUAGE ========== #
            eng_lang_login()

            # ========== LOAD DEFAULT THEME ========== #
            window_dark()

            # ============================== #
            dynamic_window.deiconify()
            dynamic_window.focus_force()
            username_entry.focus()
            dynamic_window.mainloop()  # ---- END of the Code
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
    tk.messagebox.showerror("OS Version Not supported | Version del S.O No compatible!", "Windows 8 x64 (Build 9200) or Higher is Required to Work!\nPlease Update the O.S, If you still have Problems contact the Developer.\n\nSe Necesita Windows 8 x64 (Compilacion 9200) o Superior para Funcionar!\nPor Favor Actualice el S.O, Si aun tienes Problemas contacta con el Desarrollador.")
    sys.exit(0)
elif res_width < 1024 or res_height < 768: 
    tk.messagebox.showerror("Low Screen Resolution Detected! | Baja Resolución de Pantalla Detectada!", "A Display Resolution of 1024 x 768 or Higher is Required to Work!\nIf you still have Problems contact the Developer.\n\nSe requiere una Resolucion de Pantalla de 1024 x 768 para Funcionar!\nSi aun tienes Problemas contacta con el Desarrollador.")
    sys.exit(0)
else: 
    DWI()