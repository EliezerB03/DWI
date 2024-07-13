import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from ctypes import wintypes
from cryptography.fernet import Fernet
import os, sys, csv, re, random, wmi, datetime, darkdetect, shutil, platform, ctypes, cryptography, webbrowser

if os.path.exists(os.path.join(os.path.dirname(__file__), "DWI.exe")):
    process_query = "SELECT Name, ProcessId FROM Win32_Process WHERE Name = 'DWI.exe'"
    processes = wmi.WMI().query(process_query)
    if len(processes) >= 2:
        sys.exit(0)
else:
    sys.exit(0)

# ============================================== START PROGRAM EXECUTION ============================================== #
key = "7JB92Is8xP8UU002V0x3-3mUkVYdsyJAeYMTqkwKGIQ="
crypt_key = Fernet(key)
if not os.path.exists(os.path.join(os.path.dirname(__file__), "settings.dat")):
    with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
        settingfile.write("")
if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data")):
    os.makedirs(os.path.join(os.path.dirname(__file__), "Data"))
if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data/account_data.csv")):
    with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "w") as accountfile:
        accountfile.write("")
if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv")):
    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "w") as inventoryfile:
        inventoryfile.write("")
    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
        inventory_info = inventoryfile.read()
    encrypt_data = crypt_key.encrypt(inventory_info)
    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
        inventoryfile.write(encrypt_data)

# ============================================== REQUIREMENTS ============================================== #
os_version = int(platform.version().split('.')[2])
recom_req = 19042 
min_req = 14393

display_res = ctypes.windll.user32.GetDesktopWindow()
res = ctypes.wintypes.RECT()
ctypes.windll.user32.GetWindowRect(display_res, ctypes.byref(res))
res_width = res.right - res.left 
res_height = res.bottom - res.top 

# ============================================== LOAD ENCRYPTION SYSTEM ============================================== #
try:
    with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
        account_info = accountfile.read()
    decrypt_data = crypt_key.decrypt(account_info)
except cryptography.fernet.InvalidToken:
    with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "w") as accountfile:
        accountfile.write("")
    if os_version < recom_req and os_version >= min_req:
        with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
            settingfile.write("theme=light_theme\nlanguage=eng_lang\nsetup=unfinished\n")
    else:
        with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
            settingfile.write("theme=system_theme\nlanguage=eng_lang\nsetup=unfinished\n")

# ============================================== LOAD DEPENDENCIES ============================================== #
dynamic_window = tk.Tk() # ----- MAIN WINDOW
dynamic_window.withdraw()
dynamic_window.tk.call('tk', 'scaling', 1.35)
dynamic_window.protocol("WM_DELETE_WINDOW", lambda: close()) 
basic_window = tk.Toplevel(dynamic_window)
basic_window.withdraw()
basic_img = tk.PhotoImage()
basic_imglb = tk.Label(basic_window, image=basic_img)
basic_lb1 = tk.Label(basic_window)
basic_btn_yes = ttk.Button(basic_window, cursor= "hand2")
basic_btn_cleardata = ttk.Button(basic_window, cursor= "hand2")
basic_btn_no = ttk.Button(basic_window, cursor= "hand2")
style_table = ttk.Style()
style_elements = ttk.Style()
errorinfo_window = tk.Toplevel(dynamic_window)
errorinfo_window.withdraw()
errorinfo_window.transient(dynamic_window)
error_close_btn = ttk.Button(errorinfo_window)
errorimg = tk.PhotoImage()
errorimglb = tk.Label(errorinfo_window, image=errorimg)
errorlb = tk.Label(errorinfo_window)
infotxtlb = tk.Label(errorinfo_window, wraplength=520, cursor="hand2", justify="left")
eMenu = Menu(errorinfo_window, tearoff=False)
icons_wm = tk.Label(text="💾📝🔐❓❗👤🔑♻️✔️❌✨💫➕✒️➖🔎📂🔓🔒🔧🌙🔆🌓💡📤📥📄🎨💬⏪⏩◀️▶️👁️📧")

setup_window = tk.Toplevel(dynamic_window)
setup_window.withdraw()
setup_window.transient(dynamic_window)
setup_btn_back = ttk.Button(setup_window, cursor="hand2")
setup_btn_next = ttk.Button(setup_window, cursor="hand2")
setup_btn_done = ttk.Button(setup_window, cursor="hand2")
setup_frame = tk.Frame(setup_window, height=1, bd=0)
setup_lb_title = tk.Label(setup_window)
setup_img = tk.PhotoImage()
setup_imglb = tk.Label(setup_window, image=setup_img)
setup_lb1 = tk.Label(setup_window)
setup_lb2 = tk.Label(setup_window)
setup_languagegroup = tk.IntVar()
setup_eng_langrb = ttk.Radiobutton(setup_window, text="English", cursor="hand2", value=1, variable=setup_languagegroup, takefocus=False)
setup_esp_langrb = ttk.Radiobutton(setup_window, text="Español", cursor="hand2", value=2, variable=setup_languagegroup, takefocus=False)
setup_themegroup = tk.IntVar()
setup_systemthemerb = ttk.Radiobutton(setup_window, value=3, cursor="hand2", variable=setup_themegroup, takefocus=False)
setup_lightthemerb = ttk.Radiobutton(setup_window, value=2, cursor="hand2", variable=setup_themegroup, takefocus=False)
setup_darkthemerb = ttk.Radiobutton(setup_window, value=1, cursor="hand2", variable=setup_themegroup, takefocus=False)
setup_username_lb = tk.Label(setup_window)
setup_password_lb = tk.Label(setup_window)
setup_username = tk.Entry(setup_window)
setup_password = tk.Entry(setup_window, show="*")
showhide_setuppass_btn = ttk.Button(setup_window, takefocus=False, cursor= "hand2")
setup_password.bind('<Control-c>', lambda _:'break')
setup_password.bind('<Control-v>', lambda _:'break')
setup_check1_lb = tk.Label(setup_window)
setup_check2_lb = tk.Label(setup_window)

def close():
    sys.exit(0)

def error_window():
    try:
        def copy_text():
            errorinfo_window.clipboard_clear()
            errorinfo_window.clipboard_append(infotxtlb.cget("text"))

        def e_menu(action):
            eMenu.entryconfigure(0, command=lambda: copy_text())
            eMenu.post(action.x_root, action.y_root)

        def error_light():
            style_elements.theme_use("default")
            eMenu.entryconfigure(0, background="white", foreground="black", activeforeground="black", activebackground="#DADADA")
            errorinfo_window.config(bg="white")
            errorlb.config(bg="white", fg="black")
            errorimglb.config(bg="white")
            infotxtlb.config(background="white", foreground="#9E0000")
            style_elements.map("TButton", background=[('pressed', '#E3E3E3'), ('active', '#DEDEDE'), ("disabled", "#F6F6F6")], foreground=[("disabled", "#888888")], 
                        relief=[('pressed', 'groove'), ('!pressed', 'ridge')])
            style_elements.configure("TButton", background="#ECECEC", foreground="black", font=("Segoe UI", 12), focuscolor="black")
        
        def error_dark():
            style_elements.theme_use("default")
            eMenu.entryconfigure(0, background="#101010", foreground="white", activeforeground="white", activebackground="#404040")
            errorinfo_window.config(bg="#101010")
            errorlb.config(bg="#101010", fg="white")
            errorimglb.config(bg="#101010")
            infotxtlb.config(background="#101010", foreground="#FF9E9E")
            style_elements.map("TButton", background=[('pressed', '#202020'), ('active', '#303030'), ("disabled", "#050505")], foreground=[("disabled", "#777777")], 
                        relief=[('pressed', 'groove'), ('!pressed', 'ridge')])
            style_elements.configure("TButton", background="#151515", foreground="white", font=("Segoe UI", 12), focuscolor='white')

        def load_error_theme():
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            os_themedata = set([row[0]for row in settingdata])
            dynamic_window.after(1000, load_error_theme)
            if not dynamic_window.focus_get():
                if "theme=system_theme" in os_themedata:
                    if darkdetect.isDark():
                        error_dark()
                    else:
                        error_light()

        errorinfo_window.resizable(width=False, height=False)
        errorinfo_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "main.ico"))
        errorinfo_window.grab_set()
        errorinfo_window.focus_set()
        eMenu.add_command(compound=tk.LEFT)
        infotxtlb.bind("<ButtonRelease-1>", e_menu)
        infotxtlb.bind("<ButtonRelease-3>", e_menu)
        errorimg.config(file=os.path.join(os.path.dirname(__file__), "error.png"))
        dynamic_window.bind("<FocusOut>", load_error_theme())
        dynamic_window.attributes('-disabled', 1)
        themedata = set([row[0]for row in settingdata])   
        if "theme=dark_theme" in themedata:                 
            error_dark()
        elif "theme=light_theme" in themedata:
            error_light()
        elif "theme=system_theme" in themedata:
            if darkdetect.isDark():
                error_dark()
            else:
                error_light()
    except (ValueError, FileNotFoundError, IndexError):
        with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
            settingfile.write("theme=system_theme\nlanguage=eng_lang\n")
        error_window()
        datafile_error_msg()

def loadfile_error_msg():
    window_w_total = errorinfo_window.winfo_screenwidth()
    window_h_total = errorinfo_window.winfo_screenheight()
    window_w = 704
    window_h = 320
    error_width = round(window_w_total/2-window_w/2)
    error_height = round(window_h_total/2-window_h/2-30)
    errorinfo_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(error_height))
    errorwm_height = round(window_h_total/2-window_h/2-999999999999999999999999999999999999999)
    dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(errorwm_height))
    errorinfo_window.protocol("WM_DELETE_WINDOW", lambda: close())                
    languagedata = set([row[0]for row in settingdata])
    if "language=eng_lang" in languagedata:
        errorinfo_window.title("An Fatal Error has occurred!")
        eMenu.entryconfigure(0, label="📄  Copy", font=("Segoe UI", 12))
        errorlb.config(justify="left", text="The Program was Closed due to an Error!\n\nThe Required Files Could Not be Loaded!\nReinstall/Restore of the Program is Required!\n\nInformation about the Error:", font=("Segoe UI", 12))
        infotxtlb.config(text=str(sys.exc_info()), font=("Consolas", 11))
        error_close_btn.config(text="❌  Close", cursor="hand2", command=close)
    elif "language=esp_lang" in languagedata:
        errorinfo_window.title("Ha ocurrido un Error Fatal!")
        eMenu.entryconfigure(0, label="📄  Copiar", font=("Segoe UI", 12))
        errorlb.config(justify="left", text="El Programa se Cerro debido a un Error!\n\nNo se han Podido Cargar los Archivos Requeridos!\nSe Requiere Reinstalar/Restaurar el Programa!\n\nInformacion acerca del Error:", font=("Segoe UI", 12))
        infotxtlb.config(text=str(sys.exc_info()), font=("Consolas", 11))
        error_close_btn.config(text="❌  Cerrar", cursor="hand2", command=close)
    errorlb.place(x=110, y=25)
    infotxtlb.place(x=110, y=155)
    error_close_btn.place(x=290, y=270, width=110, height=37)
    errorimglb.place(x=15, y=90)
    dynamic_window.withdraw()
    basic_window.withdraw()
    errorinfo_window.deiconify()
    dynamic_window.mainloop()

def corruptvalues_error_msg():
    window_w_total = errorinfo_window.winfo_screenwidth()
    window_h_total = errorinfo_window.winfo_screenheight()
    window_w = 704
    window_h = 300
    error_width = round(window_w_total/2-window_w/2)
    error_height = round(window_h_total/2-window_h/2-30)
    errorinfo_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(error_height))
    errorwm_height = round(window_h_total/2-window_h/2-999999999999999999999999999999999999999)
    dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(errorwm_height))
    errorinfo_window.protocol("WM_DELETE_WINDOW", lambda: close())
    languagedata = set([row[0]for row in settingdata])
    if "language=eng_lang" in languagedata:
        errorinfo_window.title("An error has occurred!")
        eMenu.entryconfigure(0, label="📄  Copy", font=("Segoe UI", 12))
        errorlb.config(justify="left", text="The Program was Closed due to an Error!\n\nNon Valid Values have been Found in the Program!\n\nInformation about the Error:", font=("Segoe UI", 12))
        infotxtlb.config(text=str(sys.exc_info()), font=("Consolas", 11))
        error_close_btn.config(text="❌  Close", cursor="hand2", command=close)
    elif "language=esp_lang" in languagedata:
        errorinfo_window.title("Ha ocurrido un Error!")
        eMenu.entryconfigure(0, label="📄  Copiar", font=("Segoe UI", 12))
        errorlb.config(justify="left", text="El Programa se Cerro debido a un Error!\n\nSe han Encontrado Valores No Válidos en el Programa!\n\nInformacion acerca del Error:", font=("Segoe UI", 12))
        infotxtlb.config(text=str(sys.exc_info()), font=("Consolas", 11))
        error_close_btn.config(text="❌  Cerrar", cursor="hand2", command=close)
    errorlb.place(x=110, y=25)
    infotxtlb.place(x=110, y=135)
    error_close_btn.place(x=290, y=250, width=110, height=37)
    errorimglb.place(x=15, y=70)
    dynamic_window.withdraw()
    basic_window.withdraw()
    errorinfo_window.deiconify()
    dynamic_window.mainloop()

def datafile_error_msg():
    window_w_total = errorinfo_window.winfo_screenwidth()
    window_h_total = errorinfo_window.winfo_screenheight()
    window_w = 704
    window_h = 300
    error_width = round(window_w_total/2-window_w/2)
    error_height = round(window_h_total/2-window_h/2-30)
    errorinfo_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(error_height))
    errorwm_height = round(window_h_total/2-window_h/2-999999999999999999999999999999999999999)
    dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(errorwm_height))
    errorinfo_window.protocol("WM_DELETE_WINDOW", lambda: close())
    languagedata = set([row[0]for row in settingdata])
    if "language=eng_lang" in languagedata:
        errorinfo_window.title("An error has occurred!")
        eMenu.entryconfigure(0, label="📄  Copy", font=("Segoe UI", 12))
        errorlb.config(justify="left", text="The Program was Closed due to an Error!\n\nFiles contains Non Valid Values/Is Corrupt/Could Not be Found!\n\nInformation about the Error:", font=("Segoe UI", 12))
        infotxtlb.config(text=str(sys.exc_info()), font=("Consolas", 11))
        error_close_btn.config(text="❌  Close", cursor="hand2", command=close)
    elif "language=esp_lang" in languagedata:
        errorinfo_window.title("Ha ocurrido un Error!")
        eMenu.entryconfigure(0, label="📄  Copiar", font=("Segoe UI", 12))
        errorlb.config(justify="left", text="El Programa se Cerro debido a un Error!\n\nLos Archivos contiene Valores No Validos/Esta Corrupto/No se Pudo Encontrar!\n\nInformacion acerca del Error:", font=("Segoe UI", 12))
        infotxtlb.config(text=str(sys.exc_info()), font=("Consolas", 11))
        error_close_btn.config(text="❌  Cerrar", cursor="hand2", command=close)
    errorlb.place(x=110, y=25)
    infotxtlb.place(x=110, y=135)
    error_close_btn.place(x=290, y=250, width=110, height=37)
    errorimglb.place(x=15, y=70)
    dynamic_window.withdraw()
    basic_window.withdraw()
    errorinfo_window.deiconify()
    dynamic_window.mainloop()

def load_csvfile_error_msg():
    errorinfo_window.protocol("WM_DELETE_WINDOW", lambda: close())
    languagedata = set([row[0]for row in settingdata])
    if "language=eng_lang" in languagedata:
        window_w = 673
        window_h = 190
        errorinfo_window.title("An error has occurred!")
        eMenu.entryconfigure(0, label="📄  Copy", font=("Segoe UI", 12))
        errorlb.config(justify="center", text="The Program was Closed due to an Error!\n\nThe Inventory File contains Non Valid Values/Is Corrupt/Could Not be Found!\nThe Content of Inventory Data will be Wiped.", font=("Segoe UI", 12))
        error_close_btn.config(text="❌  Close", cursor="hand2", command=close)
        error_close_btn.place(x=272, y=135, width=110, height=37)
    elif "language=esp_lang" in languagedata:
        window_w = 772
        window_h = 190
        errorinfo_window.title("Ha ocurrido un Error!")
        eMenu.entryconfigure(0, label="📄  Copiar", font=("Segoe UI", 12))
        errorlb.config(justify="center", text="El Programa se Cerro debido a un Error!\n\nEl Archivo de Inventario contiene Valores No Validos/Esta Corrupto/No se Pudo Encontrar!\nSe Borrara el Contenido de los Datos del Inventario.", font=("Segoe UI", 12))
        error_close_btn.config(text="❌  Cerrar", cursor="hand2", command=close)
        error_close_btn.place(x=329, y=135, width=110, height=37)
    errorlb.place(x=110, y=25)
    errorimglb.place(x=15, y=30)
    window_w_total = errorinfo_window.winfo_screenwidth()
    window_h_total = errorinfo_window.winfo_screenheight()
    error_width = round(window_w_total/2-window_w/2)
    error_height = round(window_h_total/2-window_h/2-30)
    errorinfo_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(error_height))
    errorwm_height = round(window_h_total/2-window_h/2-999999999999999999999999999999999999999)
    dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(error_width)+"+"+str(errorwm_height))
    dynamic_window.withdraw()
    basic_window.withdraw()
    errorinfo_window.deiconify()
    dynamic_window.mainloop()

# ========================================================== LOAD PROGRAM =========================================================== #
def DWI():
    try:
        with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
            loadsettings = csv.reader(settingfile)
            settingdata = list(loadsettings)

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
            global ltips_mbtn, ltips_menu, main_mbtn, tips_mbtn, about_mbtn, signout_btn, lmbar_separator, loginprofile_img, loginprofile_imglb, welcome_login
            global username_label, password_label, changeaccountlogin_btn, username_entry, password_entry, loginbtn, settings_btn, changeaccount_btn, showhide_pass_btn
            ltips_mbtn = ttk.Menubutton(dynamic_window)
            ltips_menu = Menu(ltips_mbtn, tearoff=False)
            ltips_mbtn["menu"]= ltips_menu			
            ltips_menu.add_command()
            ltips_menu.add_separator()
            ltips_menu.add_command()
            ltips_mbtn.place(x=0, y=0, height=33, width=130)
            main_mbtn = ttk.Menubutton(dynamic_window)
            tips_mbtn = ttk.Menubutton(dynamic_window)	
            about_mbtn = ttk.Menubutton(dynamic_window)	
            signout_btn = ttk.Button(dynamic_window)
            about_mbtn.place(y=0, height=33, width=130)
            changeaccount_btn = ttk.Button(dynamic_window, cursor= "hand2")
            settings_btn = ttk.Button(dynamic_window, cursor= "hand2")
            lmbar_separator = tk.Frame(dynamic_window)
            loginprofile_img = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/login.png"))
            loginprofile_imglb = tk.Label(dynamic_window, image=loginprofile_img)
            welcome_login = tk.Label(dynamic_window, anchor="center")
            username_label = tk.Label(dynamic_window)
            username_entry = tk.Entry(dynamic_window, width=30, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font=("Segoe UI", 12))
            password_label = tk.Label(dynamic_window)
            password_entry = tk.Entry(dynamic_window, width=30, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font=("Segoe UI", 12), show="*")
            showhide_pass_btn = ttk.Button(dynamic_window, takefocus=False, cursor= "hand2")
            password_entry.bind('<Control-c>', lambda _:'break')
            password_entry.bind('<Control-v>', lambda _:'break')
            username_entry.bind("<Return>", main_window)
            password_entry.bind("<Return>", main_window)
            loginbtn = ttk.Button(dynamic_window, cursor= "hand2", command=main_window)
            changeaccountlogin_btn = ttk.Button(dynamic_window, cursor= "hand2", takefocus=False, command=changeaccount)

        def showpass(show):
            password_entry.config(show="")
        def hidepass(hide):
            password_entry.config(show="*")
        def showpassbutton(show):
            showhide_pass_btn.place(x=418, y=274, width=33, height=31)
        def hidepassbutton(hide):
            showhide_pass_btn.place_forget()

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
            def validate_value_text(text):
                pattern = re.compile(r"^[a-zA-Z0-9-_.]+$")
                if pattern.match(text) is not None and len(text) <= 28:
                    return True
                elif text == "":
                    return True
                else:
                    return False

            global main_menu, tips_menu, about_menu, idlb, brandlb, modellb, colorlb, datelb, inventorylb, searchlb, device_img, device_imglb, reflesh_inventory
            global id_entry, brand_entry, model_entry, color_entry, date_entry, search_entry, inventory_table, table_scrollbar, addrb, editrb, deleterb, modes_group
            global addbtn, checkbtn, editbtn, cancelbtn, deletebtn, clearbtn, separator1, separator2, separator3, foundlb, username_logged_lb, search_focusin, search_focusout
            main_menu = Menu(main_mbtn, tearoff=False)
            main_mbtn["menu"]= main_menu
            main_menu.add_command()
            main_menu.add_separator()
            main_menu.add_command()
            main_menu.add_command()
            main_menu.add_separator()
            main_menu.add_command()	
            tips_menu = Menu(tips_mbtn, tearoff=False)
            tips_mbtn["menu"]= tips_menu			
            tips_menu.add_command()
            tips_menu.add_separator()
            tips_menu.add_command()
            tips_menu.add_command()
            tips_menu.add_command()
            tips_menu.add_command()
            about_menu = Menu(about_mbtn, tearoff=False)
            about_mbtn["menu"]= about_menu				
            about_menu.add_command()
            about_menu.add_command()
            separator1 = tk.Frame(dynamic_window)
            username_logged_lb = tk.Label(dynamic_window, width=28, wraplength=280, anchor="e")
            modes_group = tk.IntVar()
            addrb = ttk.Radiobutton(dynamic_window, value=1, variable=modes_group, cursor="hand2", takefocus=False)
            editrb = ttk.Radiobutton(dynamic_window, value=2, variable=modes_group, cursor="hand2", takefocus=False)
            deleterb = ttk.Radiobutton(dynamic_window, value=3, variable=modes_group, cursor="hand2", takefocus=False)
            separator2 = tk.Frame(dynamic_window)
            inventorylb = tk.Label(dynamic_window)
            searchlb = tk.Label(dynamic_window)
            search_entry = tk.Entry(dynamic_window, width=30, font=("Segoe UI", 12))
            inventory_table = ttk.Treeview(dynamic_window, selectmode="browse", takefocus=False)
            inventory_table['show']='headings'
            inventory_table["columns"]=("id", "brand", "model", "color", "date")
            inventory_table.column("id", width=85, minwidth=85, anchor=tk.W)
            inventory_table.column("brand", width=160, minwidth=160, anchor=tk.W)
            inventory_table.column("model", width=300, minwidth=300, anchor=tk.W)
            inventory_table.column("color", width=150, minwidth=150, anchor=tk.W)
            inventory_table.column("date", width=185, minwidth=185, anchor=tk.W)
            table_scrollbar = ttk.Scrollbar(dynamic_window, orient="vertical", command=inventory_table.yview)
            inventory_table.configure(yscrollcommand=table_scrollbar.set)
            foundlb = tk.Label(dynamic_window)
            separator3 = tk.Frame(dynamic_window)
            device_img = tk.PhotoImage()
            device_imglb = tk.Label(dynamic_window)
            idlb = tk.Label(dynamic_window)
            brandlb = tk.Label(dynamic_window)
            modellb = tk.Label(dynamic_window)
            colorlb = tk.Label(dynamic_window)
            datelb = tk.Label(dynamic_window)
            id_entry =tk.Entry(dynamic_window, width=31, validate="key", validatecommand=(dynamic_window.register(validate_value_id), "%P"), cursor= "xterm", font=("Segoe UI", 12))
            brand_entry =tk.Entry(dynamic_window, width=31, validate="key", validatecommand=(dynamic_window.register(validate_value_brand), "%P"), cursor= "xterm", font=("Segoe UI", 12))
            model_entry =tk.Entry(dynamic_window, width=31, validate="key", validatecommand=(dynamic_window.register(validate_value_model), "%P"), cursor= "xterm", font=("Segoe UI", 12))
            color_entry =tk.Entry(dynamic_window, width=31, validate="key", validatecommand=(dynamic_window.register(validate_value_color), "%P"), cursor= "xterm", font=("Segoe UI", 12))
            date_entry =tk.Entry(dynamic_window, width=31, validate="key", validatecommand=(dynamic_window.register(validate_value_date), "%P"), cursor= "xterm", font=("Segoe UI", 12))
            addbtn = ttk.Button(dynamic_window, cursor= "hand2")
            checkbtn = ttk.Button(dynamic_window, cursor= "hand2")
            editbtn = ttk.Button(dynamic_window, cursor= "hand2")
            cancelbtn = ttk.Button(dynamic_window, cursor= "hand2")
            deletebtn = ttk.Button(dynamic_window, cursor= "hand2")
            clearbtn = ttk.Button(dynamic_window, cursor= "hand2")
            def search_focusin():
                lang_value = languagegroup.get()
                if lang_value == 1:
                    if search_entry.get() == "Search by ID...":
                        search_entry.delete(0, tk.END)
                elif lang_value == 2:
                    if search_entry.get() == "Buscar por ID...":
                        search_entry.delete(0, tk.END)
                search_entry.config(validate="key", validatecommand=(dynamic_window.register(validate_value_id), "%P"))
            def search_focusout():
                search_entry.config(validate="focusout", validatecommand=(dynamic_window.register(validate_value_text), "%P"))
                lang_value = languagegroup.get()
                if search_entry.get() == "":
                    if lang_value == 1:
                        search_entry.insert(0, "Search by ID...")
                    elif lang_value == 2:
                        search_entry.insert(0, "Buscar por ID...")

            def reflesh_inventory():
                try:
                    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                        inventory_info = inventoryfile.read()
                    decrypt_data = crypt_key.decrypt(inventory_info)
                    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                        inventoryfile.write(decrypt_data)
                    inventory_table.delete(*inventory_table.get_children())
                    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r") as refleshfile:
                        data = refleshfile.readlines()
                    if len(data) > 10:
                        table_scrollbar.place(x=885, y=153, height=225, width=17)
                    else:
                        table_scrollbar.place_forget()
                    for row in data:
                        id, brand, model, color, date = row.strip().split(",")
                        inventory_table.insert("", "end", values=(id, brand, model, color, date))
                    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                        inventory_info = inventoryfile.read()
                    encrypt_data = crypt_key.encrypt(inventory_info)
                    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                        inventoryfile.write(encrypt_data)
                except (UnicodeDecodeError, ValueError, FileNotFoundError, IndexError, cryptography.fernet.InvalidToken):
                    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "w") as inventoryfile:
                        inventoryfile.write("")
                    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                        inventory_info = inventoryfile.read()
                    encrypt_data = crypt_key.encrypt(inventory_info)
                    with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                        inventoryfile.write(encrypt_data)
                    error_window()
                    load_csvfile_error_msg()

        # ============================================== LANGUAGES ============================================== #
        def eng_lang_login():
            setting_btn_apply.config(command=apply_settings_login)
            dynamic_window.title("Device Warehouse Inventory (Sign-In)")
            ltips_mbtn.config(text="💡  Tips")
            ltips_menu.entryconfigure(0, label="💡  Open Tips", font=("Segoe UI", 12), command=tips)
            ltips_menu.entryconfigure(2, label="❓  How to Sign-In?", font=("Segoe UI", 12), command=login_help)             
            about_mbtn.config(text = "❗  About") 
            about_menu.entryconfigure(0, label="📝  ChangeLog", font=("Segoe UI", 12), command=changelog)
            about_menu.entryconfigure(1, label="❗  About the Program", font=("Segoe UI", 12), command=about)
            about_mbtn.place(x=130)
            welcome_login.config(text="Login with your Account", font=("Segoe UI", 17))
            welcome_login.place(x=0, width=550)
            username_label.config(text="Username:", font=("Segoe UI", 12))
            password_label.config(text="Password:", font=("Segoe UI", 12))
            changeaccountlogin_btn.config(text="👤 Account Settings")
            loginbtn.config(text="🔓 Sign-In")
            loginbtn.place(x=221, width=100, height=38)
            settings_btn.config(text="🔧", command=settings)
            showhide_pass_btn.config(text="👁️")
            settings_eng()

        def esp_lang_login():
            setting_btn_apply.config(command=apply_settings_login)
            dynamic_window.title("Device Warehouse Inventory (Inicia Sesion)")
            ltips_mbtn.config(text="💡  Consejos")
            ltips_menu.entryconfigure(0, label="💡  Abrir Consejos", font=("Segoe UI", 12), command=tips)
            ltips_menu.entryconfigure(2, label="❓  Como Iniciar Sesion?", font=("Segoe UI", 12), command=login_help)
            about_mbtn.config(text = "❗  Acerca de") 
            about_menu.entryconfigure(0, label="📝  Registro de Cambios", font=("Segoe UI", 12), command=changelog)
            about_menu.entryconfigure(1, label="❗  Acerca del Programa", font=("Segoe UI", 12), command=about)
            about_mbtn.place(x=130)
            welcome_login.config(text="Inicia Sesion con tu Cuenta", font=("Segoe UI", 17))
            welcome_login.place(x=0, width=550)
            username_label.config(text="Nombre de Usuario:", font=("Segoe UI", 12))
            password_label.config(text="Contraseña:", font=("Segoe UI", 12))
            changeaccountlogin_btn.config(text="👤 Configuracion de Cuenta")
            loginbtn.config(text="🔓 Iniciar Sesion")
            loginbtn.place(x=199, width=145, height=38)
            settings_btn.config(text="🔧", command=settings)
            showhide_pass_btn.config(text="👁️")
            settings_esp()

        def eng_lang_mainwindow(): 
            try:           
                dynamic_window.protocol("WM_DELETE_WINDOW", lambda: signout_ask())
                main_mbtn.config(text = "💫  Utilities")
                main_menu.entryconfigure(0, label="📂  Open Data Folder", font=("Segoe UI", 12))		
                main_menu.entryconfigure(2, label="📥  Import Inventory from CSV File", font=("Segoe UI", 12))
                main_menu.entryconfigure(3, label="📤  Export Inventory to CSV File", font=("Segoe UI", 12))
                main_menu.entryconfigure(5, label="💾  Save Inventory to Text File", font=("Segoe UI", 12))		
                tips_mbtn.config(text="💡  Tips")
                tips_mbtn.place(x=130)
                tips_menu.entryconfigure(0, label="💡  Open Tips", font=("Segoe UI", 12), command=tips)
                tips_menu.entryconfigure(2, label="❓  How to use This Program?", font=("Segoe UI", 12), command=main_help)
                tips_menu.entryconfigure(3, label="➕  How to use Add Mode?", font=("Segoe UI", 12), command=addmode_help)
                tips_menu.entryconfigure(4, label="✒️  How to use Edit Mode?", font=("Segoe UI", 12), command=editmode_help)
                tips_menu.entryconfigure(5, label="➖  How to use Delete Mode?", font=("Segoe UI", 12), command=deletemode_help)    
                about_mbtn.config(text = "❗  About") 
                about_mbtn.place(x=260)	
                about_menu.entryconfigure(0, label="📝  ChangeLog", font=("Segoe UI", 12), command=changelog)
                about_menu.entryconfigure(1, label="❗  About the Program", font=("Segoe UI", 12), command=about)
                signout_btn.config(text="🔐  Sign-Out", command=signout_ask)
                signout_btn.place(x=390)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                decrypt_data = crypt_key.decrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(decrypt_data)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "r") as accountfile:
                    accountreader = csv.reader(accountfile, delimiter=",")
                    accountdata = list(accountreader)
                username_logged_lb.config(text="Welcome "+str(accountdata[0][0].upper()), font=("Segoe UI", 12, "bold"))
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                encrypt_data = crypt_key.encrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(encrypt_data)
                addrb.config(text="➕\nAdd Mode")
                editrb.config(text="✒️\nEdit Mode")
                deleterb.config(text="➖\nDelete Mode")
                search_entry.delete(0, tk.END)
                search_entry.insert(0, "Search by ID...")
                search_entry.bind("<FocusIn>", lambda event: search_focusin()) 
                search_entry.bind("<FocusOut>", lambda event: search_focusout()) 
                foundlb.config(text="Not Found", font=("Segoe UI", 12))
                foundlb.place_forget()
                reflesh_inventory()
                inventory_table.heading("id", text= " ID", anchor=tk.W)
                inventory_table.heading("brand", text= " Brand", anchor=tk.W)
                inventory_table.heading("model", text= " Model", anchor=tk.W)
                inventory_table.heading("color", text= " Color", anchor=tk.W)
                inventory_table.heading("date", text= " Registered Date", anchor=tk.W)
                idlb.config(text="ID", font=("Segoe UI", 12))
                brandlb.config(text="Brand", font=("Segoe UI", 12))
                modellb.config(text="Model", font=("Segoe UI", 12))
                colorlb.config(text="Color", font=("Segoe UI", 12))
                datelb.config(text="Date", font=("Segoe UI", 12))
                inventorylb.config(text="Inventory Information", font=("Segoe UI", 15))
                addbtn.config(text=" ➕  Add")
                checkbtn.config(text=" 🔎  Check")
                cancelbtn.config(text=" ❌  Cancel")
                editbtn.config(text=" ✒️  Edit")
                deletebtn.config(text=" ➖  Delete")
                clearbtn.config(text=" ✨  Clear")
                changeaccount_btn.config(text="👤", command=changeaccount)
                settings_btn.config(text="🔧", command=settings)
                settings_eng()
            except cryptography.fernet.InvalidToken:
                error_window()
                datafile_error_msg()  

        def esp_lang_mainwindow():    
            try:                
                dynamic_window.protocol("WM_DELETE_WINDOW", lambda: signout_ask())
                main_mbtn.config(text = "💫  Utilidades")
                main_menu.entryconfigure(0, label="📂  Abrir Carpeta Data", font=("Segoe UI", 12))	
                main_menu.entryconfigure(2, label="📥  Importar Inventario desde Archivo CSV", font=("Segoe UI", 12))
                main_menu.entryconfigure(3, label="📤  Exportar Inventario en Archivo CSV", font=("Segoe UI", 12))
                main_menu.entryconfigure(5, label="💾  Guardar Inventario en Archivo de Texto", font=("Segoe UI", 12))
                tips_mbtn.config(text="💡  Consejos")
                tips_mbtn.place(x=130) 
                tips_menu.entryconfigure(0, label="💡  Abrir Consejos", font=("Segoe UI", 12), command=tips)
                tips_menu.entryconfigure(2, label="❓  Como usar Este Programa?", font=("Segoe UI", 12), command=main_help)
                tips_menu.entryconfigure(3, label="➕  Como usar el Modo Agregar?", font=("Segoe UI", 12), command=addmode_help)
                tips_menu.entryconfigure(4, label="✒️  Como usar el Modo Editar?", font=("Segoe UI", 12), command=editmode_help)
                tips_menu.entryconfigure(5, label="➖  Como usar el Modo Eliminar?", font=("Segoe UI", 12), command=deletemode_help)
                about_mbtn.config(text = "❗  Acerca de")	
                about_mbtn.place(x=260)	
                about_menu.entryconfigure(0, label="📝  Registro de Cambios", font=("Segoe UI", 12), command=changelog)
                about_menu.entryconfigure(1, label="❗  Acerca del Programa", font=("Segoe UI", 12), command=about)
                signout_btn.config(text="🔐  Cerrar Sesion", command=signout_ask)
                signout_btn.place(x=390)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                decrypt_data = crypt_key.decrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(decrypt_data)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "r") as accountfile:
                    accountreader = csv.reader(accountfile, delimiter=",")
                    accountdata = list(accountreader)
                username_logged_lb.config(text="Bienvenido "+str(accountdata[0][0].upper()), font=("Segoe UI", 12, "bold"))
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                encrypt_data = crypt_key.encrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(encrypt_data)
                addrb.config(text="➕\nModo Agregar")
                editrb.config(text="✒️\nModo Editar")
                deleterb.config(text="➖\nModo Eliminar")
                search_entry.delete(0, tk.END)
                search_entry.insert(0, "Buscar por ID...")
                search_entry.bind("<FocusIn>", lambda event: search_focusin()) 
                search_entry.bind("<FocusOut>", lambda event: search_focusout()) 
                foundlb.config(text="No Encontrado", font=("Segoe UI", 12))
                foundlb.place_forget()
                reflesh_inventory()
                inventory_table.heading("id", text= " ID", anchor=tk.W)
                inventory_table.heading("brand", text= " Marca", anchor=tk.W)
                inventory_table.heading("model", text= " Modelo", anchor=tk.W)
                inventory_table.heading("color", text= " Color", anchor=tk.W)
                inventory_table.heading("date", text= " Fecha de Registro", anchor=tk.W)
                idlb.config(text="ID", font=("Segoe UI", 12))
                brandlb.config(text="Marca", font=("Segoe UI", 12))
                modellb.config(text="Modelo", font=("Segoe UI", 12))
                colorlb.config(text="Color", font=("Segoe UI", 12))
                datelb.config(text="Fecha", font=("Segoe UI", 12))
                inventorylb.config(text="Informacion del Inventario", font=("Segoe UI", 15))
                addbtn.config(text=" ➕  Agregar")
                checkbtn.config(text=" 🔎  Comprobar ")
                cancelbtn.config(text=" ❌  Cancelar")
                editbtn.config(text=" ✒️  Editar")
                deletebtn.config(text=" ➖  Eliminar")
                clearbtn.config(text=" ✨  Limpiar")
                changeaccount_btn.config(text="👤", command=changeaccount)
                settings_btn.config(text="🔧", command=settings)
                settings_esp()
            except cryptography.fernet.InvalidToken:
                error_window()
                datafile_error_msg() 

        def settings_eng():
            settings_window.title("Settings")
            themelb.config(text="🎨  Themes", font=("Segoe UI", 12))
            languagelb.config(text="💬  Languages", font=("Segoe UI", 12))
            systemthemerb.config(text="🌓  System", cursor="hand2") 
            lightthemerb.config(text="🔆  Light", cursor="hand2") 
            darkthemerb.config(text="🌙  Dark", cursor="hand2")
            setting_btn_cleardata.config(text="✨  Delete Program Data")
            setting_btn_close.config(text="❌ Close")
            setting_btn_apply.config(text="✔️ Apply") 

        def settings_esp():
            settings_window.title("Configuracion")
            themelb.config(text="🎨  Temas", font=("Segoe UI", 12))
            languagelb.config(text="💬  Idiomas", font=("Segoe UI", 12))
            systemthemerb.config(text="🌓  Sistema", cursor="hand2")
            lightthemerb.config(text="🔆  Claro", cursor="hand2") 
            darkthemerb.config(text="🌙  Oscuro", cursor="hand2") 
            setting_btn_cleardata.config(text="✨  Borrar Datos del Programa")
            setting_btn_close.config(text="❌ Cerrar") 
            setting_btn_apply.config(text="✔️ Aplicar")

        # ============================================== LIGHT\DARK THEME ============================================== #
        def window_light():
            dynamic_window.config(bg="white")
            settings_light()
            changeaccount_light()
            tips_light()

            # ====== STYLES ====== #
            style_elements.theme_use("default")
            style_elements.map("TMenubutton", background=[('active', '#DADADA')], relief=[('pressed', 'ridge'), ('!pressed', 'flat')])
            style_elements.configure("TMenubutton", anchor="w", background="white", foreground="black", font=("Segoe UI", 12), focuscolor="black")
            style_elements.layout('TMenubutton', [('Menubutton.border', {'sticky': 'nswe','children': [('Menubutton.focus', {'sticky': 'nswe','children': [('Menubutton.padding', 
                {'expand': '1', 'sticky': 'we', 'children': [('Menubutton.label',{'side': 'left', 'sticky': ''})]})]})]})])
            style_elements.map("TButton", background=[('pressed', '#E3E3E3'), ('active', '#DADADA'), ("disabled", "#F6F6F6")], foreground=[("disabled", "#888888")], 
                                relief=[('pressed', 'groove'), ('!pressed', 'ridge')])
            style_elements.configure("TButton", background="#ECECEC", foreground="black", font=("Segoe UI", 12), focuscolor="black", justify=tk.CENTER, anchor=tk.CENTER)
            style_elements.map("Info.TButton", background=[('pressed', 'white'), ('active', 'white')], 
                                foreground=[('pressed', '#003FD1'), ('active', '#55AAFF'), ("disabled", "#888888")], relief=[('pressed', 'flat'), ('!pressed', 'flat')])
            style_elements.configure('Info.TButton', foreground='#0047ED', background="white", justify=tk.CENTER, anchor=tk.CENTER)
            contact_info.config(style='Info.TButton')
            github_project.config(style='Info.TButton')
            style_elements.configure('signin.TButton', foreground='#AC8300', focuscolor='#AC8300')
            loginbtn.config(style='signin.TButton')
            style_elements.configure('reset.TButton', foreground='#B35A00', focuscolor='#B35A00')
            style_elements.map('reset.TButton', foreground=[("disabled", "#006C04")])
            changeaccount_btn_reset.config(style='reset.TButton') 
            style_elements.configure('resetaccount.TButton', foreground='#B35A00', focuscolor='#B35A00', justify=tk.W, anchor=tk.W)
            style_elements.map('resetaccount.TButton', foreground=[("disabled", "#006C04")])
            resetaccount_btn.config(style='resetaccount.TButton')
            style_elements.map("signout_mbtn.TButton", background=[('pressed', '#B18700'), ('active', '#B18700')], foreground=[('pressed', 'white'), ('active', 'white')], relief=[('pressed', 'ridge'), ('!pressed', 'flat')])
            style_elements.configure('signout_mbtn.TButton', anchor="w", background="white", foreground="#AC8300", focuscolor='#AC8300')
            signout_btn.config(style='signout_mbtn.TButton')
            style_elements.configure('Add.TButton', foreground='#009003', focuscolor='#009003', justify=tk.W, anchor=tk.W)
            style_elements.configure('Edit.TButton', foreground='#0049DE', focuscolor='#0049DE', justify=tk.W, anchor=tk.W)
            style_elements.configure('Delete.TButton', foreground='#CE0000', focuscolor='#CE0000', justify=tk.W, anchor=tk.W)
            style_elements.configure('miscs.TButton', justify=tk.W, anchor=tk.W)
            addbtn.config(style='Add.TButton')
            checkbtn.config(style='Edit.TButton')
            editbtn.config(style='Edit.TButton')
            cancelbtn.config(style='Delete.TButton')
            deletebtn.config(style='Delete.TButton')
            clearbtn.config(style='miscs.TButton')
            changeusername_btn.config(style='miscs.TButton')
            changepassword_btn.config(style='miscs.TButton')
            style_elements.configure('ClearData.TButton', foreground='#CE0000', focuscolor='#CE0000')
            setting_btn_cleardata.config(style='ClearData.TButton')
            style_elements.map("pass.TButton", background=[('pressed', 'white'), ('active', 'white')], 
                                foreground=[('pressed', '#737373'), ('active', 'black')], relief=[('pressed', 'flat'), ('!pressed', 'flat')])
            style_elements.configure('pass.TButton', foreground='black', background="white", justify=tk.CENTER, anchor=tk.CENTER)
            showhide_pass_btn.config(style='pass.TButton')
            showhide_cleardata_pass_btn.config(style='pass.TButton')
            showhide_actualpass_btn.config(style='pass.TButton')
            showhide_newpass_btn.config(style='pass.TButton')
            style_elements.configure('Tip.TButton', justify=tk.CENTER, anchor=tk.CENTER)
            style_elements.map("TipArrows.TButton", background=[('pressed', 'white'), ('active', 'white')], 
                                foreground=[('pressed', '#737373'), ('active', '#535353'), ("disabled", "#888888")], relief=[('pressed', 'flat'), ('!pressed', 'flat')])
            style_elements.configure('TipArrows.TButton', foreground='black', background="white", justify=tk.CENTER, anchor=tk.CENTER)
            tip1_btn.config(style='Tip.TButton')
            tip2_btn.config(style='Tip.TButton')
            tip3_btn.config(style='Tip.TButton')
            tip4_btn.config(style='Tip.TButton')
            tip5_btn.config(style='Tip.TButton')
            tip6_btn.config(style='Tip.TButton')
            tip7_btn.config(style='Tip.TButton')
            tip8_btn.config(style='Tip.TButton')
            tip9_btn.config(style='Tip.TButton')
            tip_before.config(style='TipArrows.TButton')
            tip_after.config(style='TipArrows.TButton')
            style_elements.map("Toolbutton", background=[('pressed', '#E3E3E3'), ('active', '#DADADA'), ('selected', '#C3C3C3')], 
                                indicatorcolor=[('selected', 'black')], relief=[('selected', 'groove')])
            style_elements.configure("Toolbutton", background="#ECECEC", foreground="black", font=("Segoe UI", 12), focuscolor="black", indicatorcolor="#999999", 
                                        justify=tk.CENTER, anchor=tk.CENTER, relief=tk.RIDGE)
            systemthemerb.config(style='Toolbutton')
            lightthemerb.config(style='Toolbutton')
            darkthemerb.config(style='Toolbutton')
            eng_langrb.config(style='Toolbutton')
            esp_langrb.config(style='Toolbutton')
            style_elements.configure('AddMode.Toolbutton', foreground='#009003', focuscolor='#009003')
            style_elements.configure('EditMode.Toolbutton', foreground='#0049DE', focuscolor='#0049DE')
            style_elements.configure('DeleteMode.Toolbutton', foreground='#CE0000', focuscolor='#CE0000')
            addrb.config(style='AddMode.Toolbutton')
            editrb.config(style='EditMode.Toolbutton')
            deleterb.config(style='DeleteMode.Toolbutton')

            # ====== LOGIN ====== #
            loginmenubar_light()
            loginlabels_light()
            loginentrys_light()    
            style_elements.map("changeaccount.TButton", background=[('pressed', 'white'), ('active', 'white')], 
                                foreground=[('pressed', '#003FD1'), ('active', '#55AAFF'), ("disabled", "#888888")], relief=[('pressed', 'flat'), ('!pressed', 'flat')])
            style_elements.configure('changeaccount.TButton', foreground='#0047ED', background="white", justify=tk.CENTER, anchor=tk.CENTER)
            changeaccountlogin_btn.config(style='changeaccount.TButton')

            # ====== MAINWINDOW ====== #
            mainmenubar_mw_light()
            mainseparators_light()
            labels_main_light()
            entrys_mw_light()
            table_light()

            # ====== MISC ====== #
            basic_window_light()
            if inventory_table.winfo_ismapped():
                info_af()
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
            dynamic_window.config(bg="#101010")
            settings_dark()
            changeaccount_dark()
            tips_dark()

            # ====== STYLES ====== #
            style_elements.theme_use("default")
            style_elements.map("TMenubutton", background=[('active', '#303030')], relief=[('pressed', 'groove'), ('!pressed', 'flat')])
            style_elements.configure("TMenubutton", anchor="w", background="#101010", foreground="white", font=("Segoe UI", 12), focuscolor='white')
            style_elements.layout('TMenubutton', [('Menubutton.border', {'sticky': 'nswe','children': [('Menubutton.focus', {'sticky': 'nswe','children': [('Menubutton.padding', 
                {'expand': '1', 'sticky': 'we', 'children': [('Menubutton.label',{'side': 'left', 'sticky': ''})]})]})]})])
            style_elements.map("TButton", background=[('pressed', '#252525'), ('active', '#303030'), ("disabled", "#101010")], foreground=[("disabled", "#777777")], 
                                relief=[('pressed', 'groove'), ('!pressed', 'ridge')])
            style_elements.configure("TButton", background="#171717", foreground="white", font=("Segoe UI", 12), focuscolor='white', justify=tk.CENTER, anchor=tk.CENTER)
            style_elements.map("Info.TButton", background=[('pressed', '#101010'), ('active', '#101010')], 
                                foreground=[('pressed', '#0076EC'), ('active', '#55AAFF'), ("disabled", "#777777")], relief=[('pressed', 'flat'), ('!pressed', 'flat')])
            style_elements.configure('Info.TButton', foreground='#0083FF', background="#101010", justify=tk.CENTER, anchor=tk.CENTER)
            contact_info.config(style='Info.TButton')
            github_project.config(style='Info.TButton')
            style_elements.configure('signin.TButton', foreground='#C19300', focuscolor='#C19300')
            loginbtn.config(style='signin.TButton')
            style_elements.configure('reset.TButton', foreground='#E37200', focuscolor='#E37200')
            style_elements.map('reset.TButton', foreground=[("disabled", "#00A006")])
            changeaccount_btn_reset.config(style='reset.TButton')
            style_elements.configure('resetaccount.TButton', foreground='#E37200', focuscolor='#E37200', justify=tk.W, anchor=tk.W)
            style_elements.map('resetaccount.TButton', foreground=[("disabled", "#00A006")])
            resetaccount_btn.config(style='resetaccount.TButton')
            style_elements.map("signout_mbtn.TButton", background=[('pressed', '#C19300'), ('active', '#C19300')], foreground=[('pressed', 'white'), ('active', 'white')], 
                                relief=[('pressed', 'ridge'), ('!pressed', 'flat')])
            style_elements.configure('signout_mbtn.TButton', anchor="w", background="#101010", foreground="#C19300", focuscolor='#C19300')
            signout_btn.config(style='signout_mbtn.TButton')
            style_elements.configure('Add.TButton', foreground='#00C300', focuscolor='#00C300', justify=tk.W, anchor=tk.W)
            style_elements.configure('Edit.TButton', foreground='#0078FF', focuscolor='#0078FF', justify=tk.W, anchor=tk.W)
            style_elements.configure('Delete.TButton', foreground='#FF2A2A', focuscolor='#FF2A2A', justify=tk.W, anchor=tk.W)
            style_elements.configure('miscs.TButton', justify=tk.W, anchor=tk.W)
            addbtn.config(style='Add.TButton')
            checkbtn.config(style='Edit.TButton')
            editbtn.config(style='Edit.TButton')
            cancelbtn.config(style='Delete.TButton')
            deletebtn.config(style='Delete.TButton')
            clearbtn.config(style='miscs.TButton')
            changeusername_btn.config(style='miscs.TButton')
            changepassword_btn.config(style='miscs.TButton')
            style_elements.configure('ClearData.TButton', foreground='#CE0000', focuscolor='#CE0000')
            setting_btn_cleardata.config(style='ClearData.TButton')
            style_elements.map("pass.TButton", background=[('pressed', '#101010'), ('active', '#101010')], 
                                foreground=[('pressed', '#AAAAAA'), ('active', 'white')], relief=[('pressed', 'flat'), ('!pressed', 'flat')])
            style_elements.configure('pass.TButton', foreground='white', background="#101010", justify=tk.CENTER, anchor=tk.CENTER)
            showhide_pass_btn.config(style='pass.TButton')
            showhide_cleardata_pass_btn.config(style='pass.TButton')
            showhide_actualpass_btn.config(style='pass.TButton')
            showhide_newpass_btn.config(style='pass.TButton')
            style_elements.map("TipArrows.TButton", background=[('pressed', '#101010'), ('active', '#101010')], 
                                foreground=[('pressed', '#AAAAAA'), ('active', '#DADADA'), ("disabled", "#777777")], relief=[('pressed', 'flat'), ('!pressed', 'flat')])
            style_elements.configure('TipArrows.TButton', foreground='white', background="#101010", justify=tk.CENTER, anchor=tk.CENTER)
            style_elements.configure('Tip.TButton', justify=tk.CENTER, anchor=tk.CENTER)
            tip1_btn.config(style='Tip.TButton')
            tip2_btn.config(style='Tip.TButton')
            tip3_btn.config(style='Tip.TButton')
            tip4_btn.config(style='Tip.TButton')
            tip5_btn.config(style='Tip.TButton')
            tip6_btn.config(style='Tip.TButton')
            tip7_btn.config(style='Tip.TButton')
            tip8_btn.config(style='Tip.TButton')
            tip9_btn.config(style='Tip.TButton')
            tip_before.config(style='TipArrows.TButton')
            tip_after.config(style='TipArrows.TButton')
            style_elements.map("Toolbutton", background=[('pressed', '#252525'), ('active', '#303030'), ('selected', '#252525')], 
                                indicatorcolor=[('selected', '#707070')], relief=[('selected', 'groove')])
            style_elements.configure("Toolbutton", background="#171717", foreground="white", font=("Segoe UI", 12), focuscolor="white", indicatorcolor="white", 
                                        justify=tk.CENTER, anchor=tk.CENTER, relief=tk.RIDGE)
            systemthemerb.config(style='Toolbutton')
            lightthemerb.config(style='Toolbutton')
            darkthemerb.config(style='Toolbutton')
            eng_langrb.config(style='Toolbutton')
            esp_langrb.config(style='Toolbutton')
            style_elements.configure('AddMode.Toolbutton', foreground='#00C300', focuscolor='#00C300')
            style_elements.configure('EditMode.Toolbutton', foreground='#0078FF', focuscolor='#0078FF')
            style_elements.configure('DeleteMode.Toolbutton', foreground='#FF2A2A', focuscolor='#FF2A2A')
            addrb.config(style='AddMode.Toolbutton')
            editrb.config(style='EditMode.Toolbutton')
            deleterb.config(style='DeleteMode.Toolbutton')

            # ====== LOGIN ====== #
            loginmenubar_dark()
            loginlabels_dark()
            loginentrys_dark()    
            style_elements.map("changeaccount.TButton", background=[('pressed', '#101010'), ('active', '#101010')], 
                                foreground=[('pressed', '#0076EC'), ('active', '#55AAFF'), ("disabled", "#777777")], relief=[('pressed', 'flat'), ('!pressed', 'flat')])
            style_elements.configure('changeaccount.TButton', foreground='#0083FF', background="#101010", justify=tk.CENTER, anchor=tk.CENTER)
            changeaccountlogin_btn.config(style='changeaccount.TButton')

            # ====== MAINWINDOW ====== #
            mainmenubar_mw_dark()
            mainseparators_dark()
            labels_main_dark()
            entrys_mw_dark()
            table_dark()

            # ====== MISC ====== #
            basic_window_dark()
            if inventory_table.winfo_ismapped():
                info_af()
            modes_value = modes_group.get()
            if modes_value == 2:
                if editbtn.winfo_ismapped():
                    brandlb.config(fg="#0078FF")
                    modellb.config(fg="#0078FF")
                    colorlb.config(fg="#0078FF")
                    datelb.config(fg="#0078FF")
                    id_entry.config(foreground="white", insertbackground="white", disabledforeground="#0078FF", disabledbackground="#101010")
                    brand_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2)
                    model_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2)
                    color_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2)
                    date_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2)
                else:
                    id_entry.config(foreground="white", insertbackground="white", background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", highlightthickness=2)
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
            window_h = 425
            window_width = round(window_w_total/2-window_w/2)
            window_height = round(window_h_total/2-window_h/2-30)
            dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))

        def main_window_place():
            window_w_total = dynamic_window.winfo_screenwidth()
            window_h_total = dynamic_window.winfo_screenheight()
            window_w = 923
            window_h = 585
            window_width = round(window_w_total/2-window_w/2)
            window_height = round(window_h_total/2-window_h/2-30)
            dynamic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
    
        # =================================================================================================================== #
        # ========== LOAD BASIC WINDOW ELEMENTS ========== #
        basic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))
        basic_btn_ok = ttk.Button(basic_window, text="✔️  OK", cursor= "hand2")  
        info_bf_lb = tk.Label(basic_window)
        info_af_lb = tk.Label(basic_window)
        id_inf = tk.Label(basic_window, font=("Segoe UI", 11, "bold"), anchor="w", justify="left")
        brand_bf = tk.Label(basic_window, font=("Segoe UI", 11), anchor="w", justify="left")
        model_bf = tk.Label(basic_window, font=("Segoe UI", 11), anchor="w", justify="left")
        color_bf = tk.Label(basic_window, font=("Segoe UI", 11), anchor="w", justify="left")
        date_bf = tk.Label(basic_window, font=("Segoe UI", 11), anchor="w", justify="left")
        brand_af = tk.Label(basic_window, font=("Segoe UI", 11), anchor="w", justify="left")
        model_af = tk.Label(basic_window, font=("Segoe UI", 11), anchor="w", justify="left")
        color_af = tk.Label(basic_window, font=("Segoe UI", 11), anchor="w", justify="left")
        date_af = tk.Label(basic_window, font=("Segoe UI", 11), anchor="w", justify="left") 
        infobf_frame = tk.Frame(basic_window, height=1, bd=0)
        infoaf_frame = tk.Frame(basic_window, height=1, bd=0)
        show_csvfilelb = tk.Label(basic_window, cursor='hand2', font=("Segoe UI", 12)) 
        passwordlb_cleardata = tk.Label(basic_window)
        password_cleardata = tk.Entry(basic_window, width=20, show="*")
        showhide_cleardata_pass_btn = ttk.Button(basic_window, takefocus=False, cursor= "hand2")
        passwordcheck_cleardata = tk.Label(basic_window)
        contact_info = ttk.Button(basic_window, takefocus=False, cursor= "hand2")
        github_project = ttk.Button(basic_window, takefocus=False, cursor= "hand2")

        # ========== LOAD SETTINGS WINDOW ELEMENTS ========== #
        settings_window = tk.Toplevel(dynamic_window)                               
        settings_window.withdraw()
        themeframe = tk.Frame(settings_window, height=1, bd=0)
        themelb = tk.Label(settings_window)
        themegroup = tk.IntVar()
        systemthemerb = ttk.Radiobutton(settings_window, value=3, variable=themegroup, takefocus=False) 
        lightthemerb = ttk.Radiobutton(settings_window, value=2, variable=themegroup, takefocus=False)
        darkthemerb = ttk.Radiobutton(settings_window, value=1, variable=themegroup, takefocus=False)
        languageframe = tk.Frame(settings_window, height=1, bd=0)
        languagelb = tk.Label(settings_window)
        languagegroup = tk.IntVar()
        eng_langrb = ttk.Radiobutton(settings_window, text="English", cursor="hand2", value=1, variable=languagegroup, takefocus=False)
        esp_langrb = ttk.Radiobutton(settings_window, text="Español", cursor="hand2", value=2, variable=languagegroup, takefocus=False)
        setting_btn_cleardata = ttk.Button(settings_window, cursor="hand2")
        setting_btn_close = ttk.Button(settings_window, cursor="hand2")
        setting_btn_apply = ttk.Button(settings_window)

        # ========== LOAD CHANGEACCOUNT WINDOW ELEMENTS ========== #
        changeaccount_window = tk.Toplevel(dynamic_window)
        changeaccount_window.withdraw()
        changeaccount_btn_back = ttk.Button(changeaccount_window)
        changeaccount_frame = tk.Frame(changeaccount_window, height=1, bd=0)
        changeaccount_lb_title = tk.Label(changeaccount_window, anchor="center")
        changeaccount_lb1 = tk.Label(changeaccount_window)
        changeaccount_lb2 = tk.Label(changeaccount_window)
        changeaccount_lb3 = tk.Label(changeaccount_window)
        changeaccount_lb4 = tk.Label(changeaccount_window)
        changeaccount_check1_lb = tk.Label(changeaccount_window)
        changeaccount_check2_lb = tk.Label(changeaccount_window)
        changeaccount_check3_lb = tk.Label(changeaccount_window)
        changeaccount_imglb = tk.Label(changeaccount_window, image=basic_img)
        changeusername_btn = ttk.Button(changeaccount_window)
        changepassword_btn = ttk.Button(changeaccount_window)
        resetaccount_btn = ttk.Button(changeaccount_window)
        actual_username = tk.Entry(changeaccount_window)
        new_username = tk.Entry(changeaccount_window)
        actual_password = tk.Entry(changeaccount_window, show="*")
        showhide_actualpass_btn = ttk.Button(changeaccount_window, takefocus=False, cursor= "hand2")
        actual_password.bind('<Control-c>', lambda _:'break')
        actual_password.bind('<Control-v>', lambda _:'break')
        new_password = tk.Entry(changeaccount_window, show="*")
        showhide_newpass_btn = ttk.Button(changeaccount_window, takefocus=False, cursor= "hand2")
        new_password.bind('<Control-c>', lambda _:'break')
        new_password.bind('<Control-v>', lambda _:'break')
        changeaccount_btn_reset = ttk.Button(changeaccount_window)
        changeaccount_btn_close = ttk.Button(changeaccount_window)
        changeaccount_btn_change = ttk.Button(changeaccount_window)
        
        def showactualpass(show):
            actual_password.config(show="")
        def hideactualpass(hide):
            actual_password.config(show="*")
        def showactualpassbutton(show):
            if new_password.winfo_ismapped():
                showhide_actualpass_btn.place(x=344, y=180, width=33, height=31)
            else:
                showhide_actualpass_btn.place(x=344, y=268, width=33, height=31)
        def hideactualpassbutton(hide):
            showhide_actualpass_btn.place_forget()
        def shownewpass(show):
            new_password.config(show="")
        def hidenewpass(hide):
            new_password.config(show="*")
        def shownewpassbutton(show):
            showhide_newpass_btn.place(x=344, y=268, width=33, height=31)
        def hidenewpassbutton(hide):
            showhide_newpass_btn.place_forget()

        # ========== LOAD TIPS WINDOW ELEMENTS ========== #
        tips_window = tk.Toplevel(dynamic_window)
        tips_window.withdraw()
        tips_btn_back = ttk.Button(tips_window)
        tips_frame = tk.Frame(tips_window, height=1, bd=0)
        maintips_lb_title = tk.Label(tips_window, anchor="center")
        tips_lb_title = tk.Label(tips_window)
        tips_imglb = tk.Label(tips_window, image=basic_img)
        tips_lb1 = tk.Label(tips_window)
        tips_urllb = tk.Label(tips_window, border=0)
        tip1_btn = ttk.Button(tips_window)
        tip2_btn = ttk.Button(tips_window)
        tip3_btn = ttk.Button(tips_window)
        tip4_btn = ttk.Button(tips_window)
        tip5_btn = ttk.Button(tips_window)
        tip6_btn = ttk.Button(tips_window)
        tip7_btn = ttk.Button(tips_window)
        tip8_btn = ttk.Button(tips_window)
        tip9_btn = ttk.Button(tips_window)
        tip_before = ttk.Button(tips_window, takefocus=False)
        tip_pagelb = tk.Label(tips_window)
        tip_after = ttk.Button(tips_window, takefocus=False)
        tip_btn_close = ttk.Button(tips_window)

        # ============================================== LOAD BASIC FUNCTIONS ============================================== #
        def apply_settings_login():
            lang_value = languagegroup.get()
            if lang_value == 1:
                eng_langrb.invoke()
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
                eng_lang_login()
            elif lang_value == 2: 
                esp_langrb.invoke()
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
                esp_lang_login()
            theme_value = themegroup.get()
            if theme_value == 1:
                darkthemerb.invoke()
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                for row in settingdata:
                    if row[0] == "theme=light_theme" or row[0] == "theme=system_theme":
                        row[0] = "theme=dark_theme"
                        break 
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                    writer = csv.writer(settingfile)
                    writer.writerows(settingdata)
                    settingfile.seek(0, 2) 
                window_dark()
            elif theme_value == 2:
                lightthemerb.invoke()
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                for row in settingdata:
                    if row[0] == "theme=dark_theme" or row[0] == "theme=system_theme":
                        row[0] = "theme=light_theme"
                        break 
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                    writer = csv.writer(settingfile)
                    writer.writerows(settingdata)
                    settingfile.seek(0, 2)
                window_light()
            elif theme_value == 3:
                systemthemerb.invoke()
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                for row in settingdata:
                    if row[0] == "theme=light_theme" or row[0] == "theme=dark_theme":
                        row[0] = "theme=system_theme"
                        break 
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                    writer = csv.writer(settingfile)
                    writer.writerows(settingdata)
                    settingfile.seek(0, 2)
                if darkdetect.isDark():
                    window_dark()
                else:
                    window_light()
            setting_btn_apply.config(state="disabled", cursor="arrow", takefocus=False)
            settings_window.focus()

        def apply_settings_main():
            lang_value = languagegroup.get()
            if lang_value == 1:
                eng_langrb.invoke()
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
                eng_lang_mainwindow()
            elif lang_value == 2:
                esp_langrb.invoke()
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
                esp_lang_mainwindow()
            theme_value = themegroup.get()
            if theme_value == 1:
                darkthemerb.invoke()
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                for row in settingdata:
                    if row[0] == "theme=light_theme" or row[0] == "theme=system_theme":
                        row[0] = "theme=dark_theme"
                        break 
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                    writer = csv.writer(settingfile)
                    writer.writerows(settingdata)
                    settingfile.seek(0, 2)   
                window_dark()
            elif theme_value == 2:
                lightthemerb.invoke()
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                for row in settingdata:
                    if row[0] == "theme=dark_theme" or row[0] == "theme=system_theme":
                        row[0] = "theme=light_theme"
                        break 
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                    writer = csv.writer(settingfile)
                    writer.writerows(settingdata)
                    settingfile.seek(0, 2)  
                window_light()
            elif theme_value == 3:
                systemthemerb.invoke()
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                for row in settingdata:
                    if row[0] == "theme=light_theme" or row[0] == "theme=dark_theme":
                        row[0] = "theme=system_theme"
                        break 
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                    writer = csv.writer(settingfile)
                    writer.writerows(settingdata)
                    settingfile.seek(0, 2) 
                if darkdetect.isDark():
                    window_dark()
                else:
                    window_light()
            setting_btn_apply.config(state="disabled", cursor="arrow", takefocus=False) 
            settings_window.focus()

        def cleardata_settings():
            try:
                dynamic_window.attributes('-disabled', 0)
                basic_window.grab_release()
                basic_window.transient(None)
                basic_window.withdraw()
                basic_lb1.place_forget()
                basic_imglb.place_forget()
                basic_btn_ok.place_forget()
                basic_btn_yes.place_forget()
                basic_btn_no.place_forget()
                show_csvfilelb.place_forget()
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
                    settingfile.write("")
                if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data")):
                    os.makedirs(os.path.join(os.path.dirname(__file__), "Data"))
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "w") as accountfile:
                    accountfile.write("")
                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "w") as inventoryfile:
                    inventoryfile.write("")
                cleardata_success_msg()
            except TclError:
                error_window()
                loadfile_error_msg()
            except (ValueError, FileNotFoundError, IndexError):
                error_window()
                datafile_error_msg()

        # ============================================== LOAD/HIDE MSG FUNCTIONS ============================================== #            
        def hide_basic_window():
            dynamic_window.attributes('-disabled', 0)
            restore_elements()
            basic_window.grab_release()
            basic_window.transient(None)
            basic_window.withdraw()
            basic_lb1.place_forget()
            basic_imglb.place_forget()
            basic_btn_ok.place_forget()
            basic_btn_yes.place_forget()
            basic_btn_no.place_forget()
            show_csvfilelb.place_forget()
            contact_info.place_forget()
            github_project.place_forget()

        def hide_settings():
            try:
                dynamic_window.attributes('-disabled', 0)
                restore_elements()
                settings_window.grab_release()
                settings_window.transient(None)
                settings_window.withdraw()    
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                languagedata = set([row[0]for row in settingdata])
                if "language=eng_lang" in languagedata:
                    eng_langrb.invoke()
                elif "language=esp_lang" in languagedata:
                    esp_langrb.invoke()
                themedata = set([row[0]for row in settingdata])
                if "theme=dark_theme" in themedata:                     
                    darkthemerb.invoke()
                elif "theme=light_theme" in themedata:
                    lightthemerb.invoke()
                elif "theme=system_theme" in themedata:
                    systemthemerb.invoke()
            except TclError:
                error_window()
                loadfile_error_msg()
            except (ValueError, FileNotFoundError, IndexError):
                error_window()
                datafile_error_msg()
        
        def hide_cleardata_settings():
            settings_window.attributes('-disabled', 0)
            restore_elements()
            basic_window.grab_release()
            basic_window.transient(None)
            basic_window.withdraw()
            basic_lb1.place_forget()
            basic_imglb.place_forget()
            basic_btn_ok.place_forget()
            basic_btn_cleardata.place_forget()
            basic_btn_yes.place_forget()
            basic_btn_no.place_forget()
            show_csvfilelb.place_forget()
            password_cleardata.delete(0, tk.END)
            showhide_cleardata_pass_btn.place_forget()
            passwordlb_cleardata.place_forget()
            password_cleardata.place_forget()
            passwordcheck_cleardata.place_forget()
            
        def hide_importcsv_window():
            dynamic_window.attributes('-disabled', 0)
            restore_elements()
            basic_window.grab_release()
            basic_window.transient(None)
            basic_window.withdraw()
            basic_lb1.place_forget()
            basic_imglb.place_forget()
            basic_btn_ok.place_forget()
            basic_btn_yes.place_forget()
            basic_btn_no.place_forget()
            show_csvfilelb.place_forget()
            reflesh_inventory()

        def change_setting():
            setting_btn_apply.config(state="normal", cursor="hand2", takefocus=True)

        def hide_changeaccount_window():
            dynamic_window.attributes('-disabled', 0)
            restore_elements()
            changeaccount_window.grab_release()
            changeaccount_window.transient(None)
            changeaccount_window.withdraw()
            changeaccount_back()

        def changeaccount_back():
            changeaccount_btn_back.place_forget()
            changeaccount_lb1.place_forget()
            changeaccount_lb2.place_forget()
            changeaccount_lb3.place_forget()
            changeaccount_lb4.place_forget()
            changeaccount_check1_lb.place_forget()
            changeaccount_check2_lb.place_forget()
            changeaccount_check3_lb.place_forget()
            changeaccount_imglb.place_forget()
            changeaccount_btn_reset.place_forget()
            changeaccount_frame.place_forget()
            actual_username.place_forget()
            showhide_actualpass_btn.place_forget()
            showhide_newpass_btn.place_forget()
            new_username.place_forget()
            actual_password.place_forget()
            new_password.place_forget()
            actual_username.delete(0, tk.END)
            new_username.delete(0, tk.END)
            actual_password.delete(0, tk.END)
            new_password.delete(0, tk.END)
            lang_value = languagegroup.get()
            if lang_value == 1:
                changeaccount_lb_title.place(x=0, y=24, width=420)
            elif lang_value == 2:
                changeaccount_lb_title.place(x=0, y=24, width=420)
            if loginprofile_imglb.winfo_ismapped():
                if lang_value == 1:
                    changeusername_btn.place(x=89, y=97, width=242, height=35)
                    changepassword_btn.place(x=89, y=175, width=242, height=35)
                    resetaccount_btn.place(x=89, y=253, width=242, height=35)
                elif lang_value == 2:
                    changeusername_btn.place(x=41, y=97, width=341, height=35)
                    changepassword_btn.place(x=41, y=175, width=341, height=35)
                    resetaccount_btn.place(x=41, y=253, width=341, height=35)
            else:
                if lang_value == 1:
                    changeusername_btn.place(x=89, y=130, width=242, height=50)
                    changepassword_btn.place(x=89, y=230, width=242, height=50)
                    resetaccount_btn.place_forget()
                elif lang_value == 2:
                    changeusername_btn.place(x=41, y=130, width=341, height=50)
                    changepassword_btn.place(x=41, y=230, width=341, height=50)
                    resetaccount_btn.place_forget()
            changeaccount_btn_close.place(x=153, y=350, width=110, height=37)
            changeaccount_btn_change.place_forget()

        def hide_changeaccount_msg():
            changeaccount_window.attributes('-disabled', 0)
            restore_elements()
            basic_window.grab_release()
            basic_window.transient(None)
            basic_window.withdraw()
            basic_btn_ok.place_forget()
            basic_btn_ok.config(text="✔️ OK")
            changeaccount_btn_reset.place_forget()
            changeaccount_window.grab_set()
            changeaccount_window.focus_set()

        def hide_tips_window():
            dynamic_window.attributes('-disabled', 0)
            restore_elements()
            tips_window.grab_release()
            tips_window.transient(None)
            tips_window.withdraw()
            tips_back()

        def tips_back():
            tips_lb_title.place_forget()
            tips_btn_back.place_forget()
            tips_frame.place_forget()
            tips_lb1.place_forget()
            tips_urllb.place_forget()
            tips_imglb.place_forget()
            tip_before.place_forget()
            tip_pagelb.place_forget()
            tip_after.place_forget()
            maintips_lb_title.place(x=0, y=18, width=560)
            tip1_btn.place(x=17, y=100, width=170, height=75)
            tip2_btn.place(x=194, y=100, width=170, height=75)
            tip3_btn.place(x=371, y=100, width=170, height=75)
            tip7_btn.place(x=17, y=187, width=170, height=75)
            tip8_btn.place(x=194, y=187, width=170, height=75)
            tip9_btn.place(x=371, y=187, width=170, height=75)
            tip4_btn.place(x=17, y=274, width=170, height=75)
            tip5_btn.place(x=194, y=274, width=170, height=75)
            tip6_btn.place(x=371, y=274, width=170, height=75)
            tip_btn_close.place(x=221, y=360, width=110, height=37)

        def reset_account():
            try:
                if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data")):
                    os.makedirs(os.path.join(os.path.dirname(__file__), "Data"))
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "w") as accountfile:
                    accountfile.write("admin,12345678\n")
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                encrypt_data = crypt_key.encrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(encrypt_data)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    changeaccount_btn_reset.config(text="✔️ Restored!", cursor="arrow", state="disabled")
                    changeaccount_window.focus()
                elif lang_value == 2:
                    changeaccount_btn_reset.config(text="✔️ Restablecido!", cursor="arrow", state="disabled")
                    changeaccount_window.focus()
            except cryptography.fernet.InvalidToken:
                error_window()
                datafile_error_msg()

        def enable_change_userdata():
            try:
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                decrypt_data = crypt_key.decrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(decrypt_data)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "r") as accountfile:
                    accountreader = csv.reader(accountfile, delimiter=",")
                    accountdata = list(accountreader)
                if actual_username.get() == "":
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check1_lb.config(text="Empty Text Field.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check1_lb.config(text="Campo de Texto Vacio.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check1_lb.place(x=75, y=117)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow") 
                elif not accountdata[0][0] == actual_username.get():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check1_lb.config(text="Username Incorrect.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check1_lb.config(text="Nombre de Usuario Incorrecto.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check1_lb.place(x=75, y=117)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow") 
                elif accountdata[0][0] == actual_username.get():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check1_lb.config(text="Username Verified.", font=("Segoe UI", 12), fg="#009E00")
                    elif lang_value == 2:
                        changeaccount_check1_lb.config(text="Nombre de Usuario Verificado.", font=("Segoe UI", 12), fg="#009E00")
                    changeaccount_check1_lb.place(x=75, y=117)
                if new_username.get() == "":
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check3_lb.config(text="Empty Text Field.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check3_lb.config(text="Campo de Texto Vacio.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check3_lb.place(x=75, y=207)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow") 
                elif len(new_username.get()) < 4:
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check3_lb.config(text="Must be at Least 4 Letters/Numbers.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check3_lb.config(text="Debe tener al menos 4 Letras/Numeros.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check3_lb.place(x=75, y=207)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow") 
                elif len(new_username.get()) >= 4:
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check3_lb.config(text="Valid Username.", font=("Segoe UI", 12), fg="#009E00")
                    elif lang_value == 2:
                        changeaccount_check3_lb.config(text="Nombre de usuario Valido.", font=("Segoe UI", 12), fg="#009E00")
                    changeaccount_check3_lb.place(x=75, y=207)
                if actual_password.get() == "":
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check2_lb.config(text="Empty Text Field.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check2_lb.config(text="Campo de Texto Vacio.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check2_lb.place(x=75, y=295)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow") 
                elif not accountdata[0][1] == actual_password.get():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check2_lb.config(text="Password Incorrect.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check2_lb.config(text="Contreseña Incorrecta.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check2_lb.place(x=75, y=295)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow")
                elif accountdata[0][1] == actual_password.get():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check2_lb.config(text="Password Verified.", font=("Segoe UI", 12), fg="#009E00")
                    elif lang_value == 2:
                        changeaccount_check2_lb.config(text="Contreseña Verificada.", font=("Segoe UI", 12), fg="#009E00")
                    changeaccount_check2_lb.place(x=75, y=295)
                if accountdata[0][0] == actual_username.get() and accountdata[0][1] == actual_password.get() and len(new_username.get()) >= 4:
                    changeaccount_btn_change.config(state="normal", cursor="hand2", command=change_userdata)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                encrypt_data = crypt_key.encrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(encrypt_data)
            except cryptography.fernet.InvalidToken:
                error_window()
                datafile_error_msg()

        def enable_change_password():
            try:
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                decrypt_data = crypt_key.decrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(decrypt_data)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "r") as accountfile:
                    accountreader = csv.reader(accountfile, delimiter=",")
                    accountdata = list(accountreader)
                if actual_username.get() == "":
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check1_lb.config(text="Empty Text Field.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check1_lb.config(text="Campo de Texto Vacio.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check1_lb.place(x=75, y=117)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow") 
                elif not accountdata[0][0] == actual_username.get():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check1_lb.config(text="Username Incorrect.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check1_lb.config(text="Nombre de Usuario Incorrecto.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check1_lb.place(x=75, y=117)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow") 
                elif accountdata[0][0] == actual_username.get():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check1_lb.config(text="Username Verified.", font=("Segoe UI", 12), fg="#009E00")
                    elif lang_value == 2:
                        changeaccount_check1_lb.config(text="Nombre de Usuario Verificado.", font=("Segoe UI", 12), fg="#009E00")
                    changeaccount_check1_lb.place(x=75, y=117)
                if actual_password.get() == "":
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check2_lb.config(text="Empty Text Field.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check2_lb.config(text="Campo de Texto Vacio.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check2_lb.place(x=75, y=207)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow") 
                elif not accountdata[0][1] == actual_password.get():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check2_lb.config(text="Password Incorrect.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check2_lb.config(text="Contreseña Incorrecta.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check2_lb.place(x=75, y=207)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow")
                elif accountdata[0][1] == actual_password.get():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check2_lb.config(text="Password Verified.", font=("Segoe UI", 12), fg="#009E00")
                    elif lang_value == 2:
                        changeaccount_check2_lb.config(text="Contreseña Verificada.", font=("Segoe UI", 12), fg="#009E00")
                    changeaccount_check2_lb.place(x=75, y=207)
                if new_password.get() == "":
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check3_lb.config(text="Empty Text Field.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check3_lb.config(text="Campo de Texto Vacio.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check3_lb.place(x=75, y=295)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow") 
                elif len(new_password.get()) < 8:
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check3_lb.config(text="Security Level: Weak.", font=("Segoe UI", 12), fg="#CE0000")
                    elif lang_value == 2:
                        changeaccount_check3_lb.config(text="Nivel de Seguridad: Debil.", font=("Segoe UI", 12), fg="#CE0000")
                    changeaccount_check3_lb.place(x=75, y=295)
                    changeaccount_btn_change.config(state="disabled", cursor="arrow") 
                elif len(new_password.get()) >= 8:
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        changeaccount_check3_lb.config(text="Security Level: Safe.", font=("Segoe UI", 12), fg="#009E00")
                    elif lang_value == 2:
                        changeaccount_check3_lb.config(text="Nivel de Seguridad: Segura.", font=("Segoe UI", 12), fg="#009E00")
                    changeaccount_check3_lb.place(x=75, y=295)
                if accountdata[0][0] == actual_username.get() and accountdata[0][1] == actual_password.get() and len(new_password.get()) >= 8:
                    changeaccount_btn_change.config(state="normal", cursor="hand2", command=change_passworddata)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                encrypt_data = crypt_key.encrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(encrypt_data)
            except cryptography.fernet.InvalidToken:
                error_window()
                datafile_error_msg()
        
        def enable_cleardata():
            try:
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                decrypt_data = crypt_key.decrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(decrypt_data)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "r") as accountfile:
                    accountreader = csv.reader(accountfile, delimiter=",")
                    accountdata = list(accountreader)
                if password_cleardata.get() == "":
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        passwordcheck_cleardata.config(text="Empty Text Field.", font=("Segoe UI", 12), fg="#CE0000")
                        passwordcheck_cleardata.place(x=295, y=105)
                    elif lang_value == 2:
                        passwordcheck_cleardata.config(text="Campo de Texto Vacio.", font=("Segoe UI", 12), fg="#CE0000")
                        passwordcheck_cleardata.place(x=353, y=105)
                    basic_btn_cleardata.config(state="disabled", cursor="arrow") 
                elif not accountdata[0][1] == password_cleardata.get():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        passwordcheck_cleardata.config(text="Password Incorrect.", font=("Segoe UI", 12), fg="#CE0000")
                        passwordcheck_cleardata.place(x=295, y=105)
                    elif lang_value == 2:
                        passwordcheck_cleardata.config(text="Contreseña Incorrecta.", font=("Segoe UI", 12), fg="#CE0000")
                        passwordcheck_cleardata.place(x=353, y=105)
                    basic_btn_cleardata.config(state="disabled", cursor="arrow") 
                elif accountdata[0][1] == password_cleardata.get():
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        passwordcheck_cleardata.config(text="Password Verified.", font=("Segoe UI", 12), fg="#009E00")
                        passwordcheck_cleardata.place(x=295, y=105)
                    elif lang_value == 2:
                        passwordcheck_cleardata.config(text="Contreseña Verificada.", font=("Segoe UI", 12), fg="#009E00")
                        passwordcheck_cleardata.place(x=353, y=105)
                    basic_btn_cleardata.config(state="normal", cursor="hand2", command=cleardata_settings)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                encrypt_data = crypt_key.encrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(encrypt_data)
            except cryptography.fernet.InvalidToken:
                error_window()
                datafile_error_msg()

        def change_userdata():
            try:
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                decrypt_data = crypt_key.decrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(decrypt_data)
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
                        lang_value = languagegroup.get()
                        if lang_value == 1:
                            username_logged_lb.config(text="Welcome "+str(accountdata[0][0].upper()), font=("Segoe UI", 12, "bold"))
                        elif lang_value == 2:
                            username_logged_lb.config(text="Bienvenido "+str(accountdata[0][0].upper()), font=("Segoe UI", 12, "bold"))
                    with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                        account_info = accountfile.read()
                    encrypt_data = crypt_key.encrypt(account_info)
                    with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                        accountfile.write(encrypt_data)
                    changeusername_correct_msg()
            except (FileNotFoundError, cryptography.fernet.InvalidToken):
                error_window()
                datafile_error_msg()

        def change_passworddata():
            try:
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                decrypt_data = crypt_key.decrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(decrypt_data)
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
                    with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                        account_info = accountfile.read()
                    encrypt_data = crypt_key.encrypt(account_info)
                    with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                        accountfile.write(encrypt_data)
                    changeaccount_back()
                    changepassword_correct_msg()
            except (FileNotFoundError, cryptography.fernet.InvalidToken):
                error_window()
                datafile_error_msg()
           
        # ============================================== LOAD WINDOW FUNCTIONS ============================================== #
        # ========== SETTINGS WINDOW ========== #
        def settings():
            try:
                setting_w_total = dynamic_window.winfo_screenwidth()
                setting_h_total = dynamic_window.winfo_screenheight()
                if os_version < recom_req and os_version >= min_req:
                    setting_w = 338
                    setting_h = 360
                    themeframe.place(x=26, y=33, width=287, height=75)
                    languageframe.place(x=26, y=145, width=287, height=75)
                    themelb.place(x=41, y=19)
                    languagelb.place(x=41, y=131)
                    lightthemerb.place(x=47, y=51, width=110, height=40)
                    darkthemerb.place(x=179, y=51, width=110, height=40)
                    eng_langrb.place(x=47, y=164, width=110, height=40)
                    esp_langrb.place(x=179,y=164, width=110, height=40)
                    setting_btn_cleardata.place(x=93, y=245, width=250, height=45)
                    setting_btn_close.place(x=47, y=310, width=110, height=37)
                    setting_btn_apply.place(x=179, y=310, width=110, height=37)
                else:
                    setting_w = 439
                    setting_h = 360
                    themeframe.place(x=26, y=33, width=385, height=75)
                    languageframe.place(x=26, y=145, width=385, height=75)
                    themelb.place(x=41, y=19)
                    languagelb.place(x=41, y=131)
                    lightthemerb.place(x=162, y=51, width=110, height=40)
                    darkthemerb.place(x=285, y=51, width=110, height=40)
                    systemthemerb.place(x=39, y=51, width=110, height=40)
                    eng_langrb.place(x=75, y=165, width=110, height=40)
                    esp_langrb.place(x=245, y=165, width=110, height=40)
                    setting_btn_cleardata.place(x=93, y=245, width=250, height=45)
                    setting_btn_close.place(x=98, y=310, width=110, height=37)
                    setting_btn_apply.place(x=230, y=310, width=110, height=37)
                
                setting_width = round(setting_w_total/2-setting_w/2)
                setting_height = round(setting_h_total/2-setting_h/2-30)
                settings_window.geometry(str(setting_w)+"x"+str(setting_h)+"+"+str(setting_width)+"+"+str(setting_height))
                off_elements_msg()
                settings_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/settings.ico"))
                settings_window.protocol("WM_DELETE_WINDOW", lambda: hide_settings())
                settings_window.resizable(width=False, height=False)
                settings_window.grab_set()
                settings_window.focus_set()
                lightthemerb.config(command=change_setting)
                darkthemerb.config(command=change_setting)
                systemthemerb.config(command=change_setting)
                eng_langrb.config(command=change_setting)
                esp_langrb.config(command=change_setting)
                setting_btn_close.config(command=hide_settings)
                setting_btn_cleardata.config(command=cleardata_ask)
                setting_btn_apply.config(state="disabled", cursor="arrow", takefocus=False)
                settings_window.transient(dynamic_window)
                settings_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except NameError:
                error_window()
                corruptvalues_error_msg()
            except TclError:
                error_window()
                loadfile_error_msg()
            except (ValueError, FileNotFoundError, IndexError):
                error_window()
                datafile_error_msg()

        # ========== CHANGEACCOUNT WINDOW ========== #
        def changeaccount():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 420
                window_h = 400
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                changeaccount_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                changeaccount_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/changeaccount.ico"))
                changeaccount_window.protocol("WM_DELETE_WINDOW", lambda: hide_changeaccount_window())
                changeaccount_window.resizable(width=False, height=False)
                changeaccount_window.grab_set()
                changeaccount_window.focus_set()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    changeaccount_window.title("Account Settings")
                    changeaccount_lb_title.config(text="Select one of the options\nto change your account information.", font=("Segoe UI", 12))
                    changeusername_btn.config(text=" 👤  Change Username", cursor="hand2", command=changeusername) 
                    changepassword_btn.config(text=" 🔑  Change Password", cursor="hand2", command=changepassword)
                    resetaccount_btn.config(text=" ♻️  Reset Default Account", cursor="hand2", command=resetaccount)
                    changeaccount_btn_close.config(text="❌  Close") 
                    changeaccount_btn_change.config(text="✔️  Change")   
                elif lang_value == 2:
                    changeaccount_window.title("Configuracion de Cuenta")
                    changeaccount_lb_title.config(text="Selecciona una de las opciones\npara cambiar información de tu cuenta.", font=("Segoe UI", 12))
                    changeusername_btn.config(text=" 👤  Cambiar Nombre de Usuario", cursor="hand2", command=changeusername) 
                    changepassword_btn.config(text=" 🔑  Cambiar Contraseña", cursor="hand2", command=changepassword)
                    resetaccount_btn.config(text=" ♻️  Restablecer Cuenta Predeterminada", cursor="hand2", command=resetaccount)
                    changeaccount_btn_close.config(text="❌  Cerrar") 
                    changeaccount_btn_change.config(text="✔️  Cambiar") 
                if loginprofile_imglb.winfo_ismapped():
                    if lang_value == 1:
                        changeusername_btn.place(x=89, y=97, width=242, height=35)
                        changepassword_btn.place(x=89, y=175, width=242, height=35)
                        resetaccount_btn.place(x=89, y=253, width=242, height=35)
                    elif lang_value == 2:
                        changeusername_btn.place(x=41, y=97, width=341, height=35)
                        changepassword_btn.place(x=41, y=175, width=341, height=35)
                        resetaccount_btn.place(x=41, y=253, width=341, height=35)
                else:
                    if lang_value == 1:
                        changeusername_btn.place(x=89, y=130, width=242, height=50)
                        changepassword_btn.place(x=89, y=230, width=242, height=50)
                        resetaccount_btn.place_forget()
                    elif lang_value == 2:
                        changeusername_btn.place(x=41, y=130, width=341, height=50)
                        changepassword_btn.place(x=41, y=230, width=341, height=50)
                        resetaccount_btn.place_forget()
                changeaccount_lb_title.place(x=0, y=24, width=420)
                changeaccount_btn_close.config(cursor="hand2", command=hide_changeaccount_window)
                changeaccount_btn_close.place(x=153, y=350, width=110, height=37)
                changeaccount_btn_change.config(state="disabled", cursor="arrow")
                changeaccount_window.transient(dynamic_window)
                changeaccount_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()        

        # ========== CHANGE USERNAME WINDOW ========== #
        def changeusername():
            def validate_value_account(text):
                pattern = re.compile(r"^[a-zA-Z0-9]+$")
                if pattern.match(text) is not None:
                    return True and len(text) <= 20
                elif text == "":
                    return True and len(text) <= 20
                else:
                    return False
            changeaccount_lb_title.place_forget()
            changeusername_btn.place_forget()
            changepassword_btn.place_forget()
            resetaccount_btn.place_forget()
            changeaccount_frame.place(x=40, y=45, width=340, height=285) 
            actual_username.focus()
            actual_username.config(width=29, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font=("Segoe UI", 12))
            new_username.config(width=29, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font=("Segoe UI", 12))
            actual_password.config(width=29, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font=("Segoe UI", 12)) 
            actual_username.bind("<KeyRelease>", lambda event: enable_change_userdata())
            new_username.bind("<KeyRelease>", lambda event: enable_change_userdata())
            actual_password.bind("<KeyRelease>", lambda event: enable_change_userdata())
            showhide_actualpass_btn.bind("<ButtonPress-1>", showactualpass)
            showhide_actualpass_btn.bind("<ButtonRelease-1>", hideactualpass)
            actual_password.bind("<FocusIn>", showactualpassbutton)
            actual_password.bind("<FocusOut>", hideactualpassbutton)
            lang_value = languagegroup.get()
            if lang_value == 1:
                changeaccount_lb1.config(text="👤 Change Username", font=("Segoe UI", 12))
                changeaccount_lb2.config(text="Actual Username:", font=("Segoe UI", 12))
                changeaccount_lb3.config(text="New Username:", font=("Segoe UI", 12))
                changeaccount_lb4.config(text="Password to Confirm:", font=("Segoe UI", 12))
            elif lang_value == 2:
                changeaccount_lb1.config(text="👤 Cambiar Nombre de Usuario", font=("Segoe UI", 12))
                changeaccount_lb2.config(text="Nombre de Usuario Actual:", font=("Segoe UI", 12))
                changeaccount_lb3.config(text="Nuevo Nombre de Usuario:", font=("Segoe UI", 12))
                changeaccount_lb4.config(text="Contraseña para Confirmar:", font=("Segoe UI", 12))
            actual_username.place(x=75, y=92, height=30)
            new_username.place(x=75, y=181, height=30)
            actual_password.place(x=75, y=269, height=30)
            showhide_actualpass_btn.config(text="👁️")
            changeaccount_lb1.place(x=55, y=31)
            changeaccount_lb2.place(x=75, y=66)
            changeaccount_lb3.place(x=75, y=156)
            changeaccount_lb4.place(x=75, y=243)
            changeaccount_btn_back.config(text="⏪", cursor="hand2", command=changeaccount_back)
            changeaccount_btn_back.place(x=0, width=37, height=33)
            changeaccount_btn_close.config(cursor="hand2", command=hide_changeaccount_window)
            changeaccount_btn_change.config(state="disabled", cursor="arrow") 
            changeaccount_btn_close.place(x=90, y=350, width=110, height=37)
            changeaccount_btn_change.place(x=220, y=350, width=110, height=37)

        # ========== CHANGE PASSWORD WINDOW ========== #
        def changepassword():
            def validate_value_account(text):
                pattern = re.compile(r"^[a-zA-Z0-9]+$")
                if pattern.match(text) is not None:
                    return True and len(text) <= 20
                elif text == "":
                    return True and len(text) <= 20
                else:
                    return False
            changeaccount_lb_title.place_forget()
            changeusername_btn.place_forget()
            changepassword_btn.place_forget()
            resetaccount_btn.place_forget()
            changeaccount_frame.place(x=40, y=45, width=340, height=285)
            actual_username.focus()
            actual_username.config(width=29, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font=("Segoe UI", 12))
            actual_password.config(width=29, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font=("Segoe UI", 12))
            new_password.config(width=29, validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font=("Segoe UI", 12)) 
            actual_username.bind("<KeyRelease>", lambda event: enable_change_password())
            actual_password.bind("<KeyRelease>", lambda event: enable_change_password())
            new_password.bind("<KeyRelease>", lambda event: enable_change_password()) 
            showhide_actualpass_btn.bind("<ButtonPress-1>", showactualpass)
            showhide_actualpass_btn.bind("<ButtonRelease-1>", hideactualpass)
            showhide_newpass_btn.bind("<ButtonPress-1>", shownewpass)
            showhide_newpass_btn.bind("<ButtonRelease-1>", hidenewpass)
            actual_password.bind("<FocusIn>", showactualpassbutton)
            actual_password.bind("<FocusOut>", hideactualpassbutton)
            new_password.bind("<FocusIn>", shownewpassbutton)
            new_password.bind("<FocusOut>", hidenewpassbutton)
            lang_value = languagegroup.get()
            if lang_value == 1:
                changeaccount_lb1.config(text="🔑 Change Password", font=("Segoe UI", 12))
                changeaccount_lb2.config(text="Actual Username:", font=("Segoe UI", 12))
                changeaccount_lb3.config(text="Actual Password:", font=("Segoe UI", 12))
                changeaccount_lb4.config(text="New Password:", font=("Segoe UI", 12))
            elif lang_value == 2:
                changeaccount_lb1.config(text="🔑 Cambiar Contraseña", font=("Segoe UI", 12))
                changeaccount_lb2.config(text="Nombre de Usuario Actual:", font=("Segoe UI", 12))
                changeaccount_lb3.config(text="Contraseña Actual:", font=("Segoe UI", 12))
                changeaccount_lb4.config(text="Nueva Contraseña:", font=("Segoe UI", 12))
            actual_username.place(x=75, y=92, height=30)
            actual_password.place(x=75, y=181, height=30)
            new_password.place(x=75, y=269, height=30)
            showhide_actualpass_btn.config(text="👁️")
            showhide_newpass_btn.config(text="👁️")
            changeaccount_lb1.place(x=55, y=31)
            changeaccount_lb2.place(x=75, y=66)
            changeaccount_lb3.place(x=75, y=156)
            changeaccount_lb4.place(x=75, y=243)
            changeaccount_btn_back.config(text="⏪", cursor="hand2", command=changeaccount_back) 
            changeaccount_btn_back.place(x=0, width=37, height=33)
            changeaccount_btn_close.config(cursor="hand2", command=hide_changeaccount_window)
            changeaccount_btn_change.config(state="disabled", cursor="arrow")
            changeaccount_btn_close.place(x=90, y=350, width=110, height=37)
            changeaccount_btn_change.place(x=220, y=350, width=110, height=37)
        
        # ========== RESET DEFAULT ACCOUNT WINDOW ========== #
        def resetaccount():
            try:
                changeaccount_lb_title.place_forget()
                changeusername_btn.place_forget()
                changepassword_btn.place_forget()
                resetaccount_btn.place_forget()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/remember.png"))
                changeaccount_frame.place(x=40, y=45, width=340, height=285)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    changeaccount_lb1.config(text="♻️ Reset Default Account", font=("Segoe UI", 12))
                    changeaccount_lb2.config(justify="center", text="Default Account:\n\nUsername:  >   admin\nPassword:  >   12345678", font=("Segoe UI", 12))
                    changeaccount_lb2.place(x=160, y=84)
                    changeaccount_btn_reset.config(text="♻️ Reset to Default", cursor="hand2", state="normal", command=reset_account) 
                    changeaccount_lb3.config(justify="left", text="*You can change the Username/Password \nagain after resetting it.", font=("Segoe UI", 12))
                    changeaccount_btn_reset.place(x=125, y=204, height=50, width=160)
                elif lang_value == 2:
                    changeaccount_lb1.config(text="♻️ Restablecer Cuenta Predeterminada", font=("Segoe UI", 12))
                    changeaccount_lb2.config(justify="center", text="Cuenta Predeterminada:\n\nNombre de Usuario: > admin\nContraseña: > 12345678", font=("Segoe UI", 12))
                    changeaccount_lb2.place(x=140, y=84)
                    changeaccount_btn_reset.config(text="♻️ Restablecer a Predeterminado", cursor="hand2", state="normal", command=reset_account) 
                    changeaccount_lb3.config(justify="left", text="*Puedes volver a cambiar el Nombre de \nusuario/Contraseña luego de restablecerlo.", font=("Segoe UI", 12))
                    changeaccount_btn_reset.place(x=78, y=204, height=50, width=260)
                changeaccount_lb1.place(x=55, y=31)
                changeaccount_lb3.place(x=45, y=275)
                changeaccount_imglb.place(x=45, y=85)
                changeaccount_btn_back.config(text="⏪", cursor="hand2", command=changeaccount_back) 
                changeaccount_btn_back.place(x=0, width=37, height=33)
                changeaccount_btn_close.config(cursor="hand2", command=hide_changeaccount_window) 
                changeaccount_btn_close.place(x=153, y=350, width=110, height=37)
            except TclError:
                error_window()
                loadfile_error_msg()  

        # ========== TIPS WINDOW ========== #
        def tips():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 560
                window_h = 410
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                tips_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                tips_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/tips.ico"))
                tips_window.protocol("WM_DELETE_WINDOW", lambda: hide_tips_window())                              
                tips_window.resizable(width=False, height=False)
                tips_window.grab_set()
                tips_window.focus_set()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    tips_window.title("Tips")
                    maintips_lb_title.config(text="Welcome to Tips\nHere you will find all Information\nyou need to know About this Program and its Use.", font=("Segoe UI", 12))
                    tip1_btn.config(text="💡\nWhat is the Purpose\nof this Program?", cursor="hand2", command=tip_1)
                    tip2_btn.config(text="❓\nHow to\nSign-In?", cursor="hand2", command=tip_2)
                    tip3_btn.config(text="❓\nHow to use\nThis Program?", cursor="hand2", command=tip_3)
                    tip4_btn.config(text="➕\nHow to use\nAdd Mode?", cursor="hand2", command=tip_4)
                    tip5_btn.config(text="✒️\nHow to use\nEdit Mode?", cursor="hand2", command=tip_5)
                    tip6_btn.config(text="➖\nHow to use\nDelete Mode?", cursor="hand2", command=tip_6)
                    tip7_btn.config(text="🔒\nIs my\nData Safe?", cursor="hand2", command=tip_7)
                    tip8_btn.config(text="❓\nHow to change the\nTheme/Language?", cursor="hand2", command=tip_8)
                    tip9_btn.config(text="👤\nHow to change the\nUsername/Password?", cursor="hand2", command=tip_9)
                    tip_btn_close.config(text="❌ Close")   
                elif lang_value == 2:
                    tips_window.title("Consejos")
                    maintips_lb_title.config(text="Bienvenido a Consejos\nAqui encontraras toda la Informacion que necesitas\nsaber Acerca de este Programa y su Uso.", font=("Segoe UI", 12))
                    tip1_btn.config(text="💡\nCual es el Proposito\nde este Programa?", cursor="hand2", command=tip_1)
                    tip2_btn.config(text="❓\nComo\nIniciar Sesion?", cursor="hand2", command=tip_2)
                    tip3_btn.config(text="❓\nComo usar\nEste Programa?", cursor="hand2", command=tip_3)
                    tip4_btn.config(text="➕\nComo usar\nel Modo Agregar?", cursor="hand2", command=tip_4)
                    tip5_btn.config(text="✒️\nComo usar\nel Modo Editar?", cursor="hand2", command=tip_5)
                    tip6_btn.config(text="➖\nComo usar\nel Modo Eliminar?", cursor="hand2", command=tip_6)
                    tip7_btn.config(text="🔒\nMis Datos\nestan Seguros?", cursor="hand2", command=tip_7)
                    tip8_btn.config(text="❓\nComo cambiar el\nTema/Idioma?", cursor="hand2", command=tip_8)
                    tip9_btn.config(text="👤\nComo cambiar el\nUsuario/Contraseña?", cursor="hand2", command=tip_9)
                    tip_btn_close.config(text="❌ Cerrar")
                maintips_lb_title.place(x=0, y=18, width=560) 
                tip1_btn.place(x=17, y=100, width=170, height=75)
                tip2_btn.place(x=194, y=100, width=170, height=75)
                tip3_btn.place(x=371, y=100, width=170, height=75)
                tip7_btn.place(x=17, y=187, width=170, height=75)
                tip8_btn.place(x=194, y=187, width=170, height=75)
                tip9_btn.place(x=371, y=187, width=170, height=75)
                tip4_btn.place(x=17, y=274, width=170, height=75)
                tip5_btn.place(x=194, y=274, width=170, height=75)
                tip6_btn.place(x=371, y=274, width=170, height=75)
                tip_btn_close.config(cursor="hand2", command=hide_tips_window)
                tip_btn_close.place(x=221, y=360, width=110, height=37)
                tips_window.transient(dynamic_window)
                tips_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()        
                
        # ========== TIP-1 WINDOW ========== #
        def tip_1(): 
            try:
                maintips_lb_title.place_forget()
                tip1_btn.place_forget()
                tip2_btn.place_forget()
                tip3_btn.place_forget()
                tip4_btn.place_forget()
                tip5_btn.place_forget()
                tip6_btn.place_forget()
                tip7_btn.place_forget()
                tip8_btn.place_forget()
                tip9_btn.place_forget()
                tips_urllb.place_forget()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip1.png"))
                tips_frame.place(x=40, y=45, width=480, height=295)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    tips_lb_title.config(text="💡 What is the Purpose of this Program?", font=("Segoe UI", 12))
                    tips_lb1.config(justify="center", text="Its purpose is to offer options to easily\nmanage device information\nfrom an inventory list.\n\nTo learn more about the program,\ncheck the other questions of Tips.", font=("Segoe UI", 12))
                    tips_lb1.place(x=180, y=125)
                elif lang_value == 2:
                    tips_lb_title.config(text="💡 Cual es el Proposito de este Programa?", font=("Segoe UI", 12))
                    tips_lb1.config(justify="center", text="Su propósito es ofrecer opciones\npara administrar fácilmente\nla información de los dispositivos desde\nuna lista de inventario.\n\nPara saber mas acerca del programa, consulta\nlas demas preguntas de Consejos.", font=("Segoe UI", 12))
                    tips_lb1.place(x=160, y=115)
                tip_before.config(text="◀️", cursor="arrow", state="disabled")
                tip_pagelb.config(text="1/9", font=("Segoe UI", 12))
                tip_after.config(text="▶️", cursor="hand2", state="normal", command=tip_2) 
                tips_lb_title.place(x=55, y=31)
                tips_imglb.place(x=45, y=130)
                tips_btn_back.config(text="⏪", cursor="hand2", command=tips_back) 
                tips_btn_back.place(x=0, width=37, height=33)
                tip_before.place(x=229, y=322, width=33, height=31)
                tip_pagelb.place(x=262, y=322, width=33, height=31)
                tip_after.place(x=295, y=322, width=33, height=31)
                tip_btn_close.config(cursor="hand2", command=hide_tips_window) 
                tip_btn_close.place(x=221, y=360, width=110, height=37) 
            except TclError:
                error_window()
                loadfile_error_msg()  

        # ========== TIP-2 WINDOW ========== #
        def tip_2():
            try:
                maintips_lb_title.place_forget()
                tip1_btn.place_forget()
                tip2_btn.place_forget()
                tip3_btn.place_forget()
                tip4_btn.place_forget()
                tip5_btn.place_forget()
                tip6_btn.place_forget()
                tip7_btn.place_forget()
                tip8_btn.place_forget()
                tip9_btn.place_forget()
                tips_urllb.place_forget()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip2.png"))
                tips_frame.place(x=40, y=45, width=480, height=295)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    tips_lb_title.config(text="❓ How to Sign-In?", font=("Segoe UI", 12)) 
                    tips_lb1.config(justify="center", text="To begin, enter your Username and Password,\nand press the [🔓 Sign-In] button.\nif the data is correct the program\nwill start, otherwise you will receive\nan error message.\n\nIf you still have problems logging in, you can\nreset your account from [👤Account Settings],\nif you still have problems logging in\nthen contact the Developer [Here].", font=("Segoe UI", 12))
                    tips_lb1.place(x=150, y=80)
                    tips_urllb.config(justify="center", text="[Here].", cursor="hand2", font=("Segoe UI", 12))
                    tips_urllb.bind("<Button-1>", lambda event: webbrowser.open_new_tab("mailto:el.elie03@gmail.com"))
                    tips_urllb.place(x=384, y=272, height=20)
                elif lang_value == 2:
                    tips_lb_title.config(text="❓ Como Iniciar Sesion?", font=("Segoe UI", 12))
                    tips_lb1.config(justify="center", text="Para empezar, escriba su\nNombre de Usuario y Contraseña\ny presione el boton [🔓 Iniciar Sesion]\nsi los datos son correcto el programa iniciara,\nde lo contrario recibiras un mensaje de error.\n\nSi aun tienes problemas para iniciar sesion,\npuedes restablecer la cuenta\ndesde la [👤 Configuracion de Cuenta],\nsi aun asi tienes problemas para iniciar sesion\nentonces, contacta al Desarrollador [Aqui].", font=("Segoe UI", 12))
                    tips_lb1.place(x=160, y=70)
                    tips_urllb.config(justify="center", text="[Aqui].", cursor="hand2", font=("Segoe UI", 12))
                    tips_urllb.bind("<Button-1>", lambda event: webbrowser.open_new_tab("mailto:el.elie03@gmail.com"))
                    tips_urllb.place(x=420, y=283, height=21)  
                tip_before.config(text="◀️", cursor="hand2", state="normal", command=tip_1)
                tip_pagelb.config(text="2/9", font=("Segoe UI", 12))
                tip_after.config(text="▶️", cursor="hand2", state="normal", command=tip_3)  
                tips_lb_title.place(x=55, y=31)
                tips_imglb.place(x=45, y=140)
                tips_btn_back.config(text="⏪", cursor="hand2", command=tips_back) 
                tips_btn_back.place(x=0, width=37, height=33)
                tip_before.place(x=229, y=322, width=33, height=31)
                tip_pagelb.place(x=262, y=322, width=33, height=31)
                tip_after.place(x=295, y=322, width=33, height=31)
                tip_btn_close.config(cursor="hand2", command=hide_tips_window) 
                tip_btn_close.place(x=221, y=360, width=110, height=37) 
            except TclError:
                error_window()
                loadfile_error_msg()  

        # ========== TIP-3 WINDOW ========== #
        def tip_3():
            try:
                maintips_lb_title.place_forget()
                tip1_btn.place_forget()
                tip2_btn.place_forget()
                tip3_btn.place_forget()
                tip4_btn.place_forget()
                tip5_btn.place_forget()
                tip6_btn.place_forget()
                tip7_btn.place_forget()
                tip8_btn.place_forget()
                tip9_btn.place_forget()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip3.png"))
                tips_frame.place(x=40, y=45, width=480, height=295)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    tips_lb_title.config(text="❓ How to use This Program?", font=("Segoe UI", 12)) 
                    tips_lb1.config(justify="center", text="To begin, select one of the available options\nlocated at the top to open each option,\namong those available are:\n➕ Add Mode, ✒️ Edit Mode and ➖ Delete Mode.\n\nIf you have problems accessing the options,\nplease contact the Developer [Here].", font=("Segoe UI", 12))
                    tips_lb1.place(x=145, y=115) 
                    tips_urllb.config(justify="center", text="[Here].", cursor="hand2", font=("Segoe UI", 12))
                    tips_urllb.bind("<Button-1>", lambda event: webbrowser.open_new_tab("mailto:el.elie03@gmail.com"))
                    tips_urllb.place(x=401, y=244, height=20) 
                elif lang_value == 2:
                    tips_lb_title.config(text="❓ Como usar Este Programa?", font=("Segoe UI", 12))
                    tips_lb1.config(justify="center", text="Para comenzar, seleccione una de las opciones\ndisponibles ubicadas en la parte superior\npara abrir cada opcion, entre las disponibles\nestan: ➕ Modo Agregar, ✒️ Modo Editar y\n➖ Modo Eliminar.\n\nSi tiene problemas al acceder con las opciones,\ncontacta con el Desarrollador [Aqui].", font=("Segoe UI", 12))
                    tips_lb1.place(x=160, y=105) 
                    tips_urllb.config(justify="center", text="[Aqui].", cursor="hand2", font=("Segoe UI", 12))
                    tips_urllb.bind("<Button-1>", lambda event: webbrowser.open_new_tab("mailto:el.elie03@gmail.com"))
                    tips_urllb.place(x=404, y=255, height=21)  
                tip_before.config(text="◀️", cursor="hand2", state="normal", command=tip_2)
                tip_pagelb.config(text="3/9", font=("Segoe UI", 12))
                tip_after.config(text="▶️", cursor="hand2", state="normal", command=tip_7) 
                tips_lb_title.place(x=55, y=31)
                tips_imglb.place(x=45, y=130)
                tips_btn_back.config(text="⏪", cursor="hand2", command=tips_back) 
                tips_btn_back.place(x=0, width=37, height=33)
                tip_before.place(x=229, y=322, width=33, height=31)
                tip_pagelb.place(x=262, y=322, width=33, height=31)
                tip_after.place(x=295, y=322, width=33, height=31)
                tip_btn_close.config(cursor="hand2", command=hide_tips_window) 
                tip_btn_close.place(x=221, y=360, width=110, height=37) 
            except TclError:
                error_window()
                loadfile_error_msg()  
            
        # ========== TIP-4 WINDOW ========== #
        def tip_4():
            try:
                maintips_lb_title.place_forget()
                tip1_btn.place_forget()
                tip2_btn.place_forget()
                tip3_btn.place_forget()
                tip4_btn.place_forget()
                tip5_btn.place_forget()
                tip6_btn.place_forget()
                tip7_btn.place_forget()
                tip8_btn.place_forget()
                tip9_btn.place_forget()
                tips_urllb.place_forget()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip4.png"))
                tips_frame.place(x=40, y=45, width=480, height=295)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    tips_lb_title.config(text="➕ How to use Add Mode?", font=("Segoe UI", 12)) 
                    tips_lb1.config(justify="center", text="To begin, fill out the text fields and\npress the [➕ Add] Button, When you press\nthe button, a message will\nappear to confirm, Press [✔️ Yes] to Add,\nthe data entered will be\nsaved in the inventory, with a Unique ID.", font=("Segoe UI", 12))
                    tips_lb1.place(x=165, y=125)  
                elif lang_value == 2:
                    tips_lb_title.config(text="➕ Como usar el Modo Agregar?", font=("Segoe UI", 12))
                    tips_lb1.config(justify="center", text="Para empezar, llena los campos de texto y\npresiona el Boton [➕ Agregar], al presionar\nel boton, aparecera un mensaje para confirmar,\nPresiona [✔️ Si] para Agregar,\nlos datos introducidos se guardaran\nen el inventario, con un ID Unico.", font=("Segoe UI", 12))
                    tips_lb1.place(x=155, y=127) 
                tip_before.config(text="◀️", cursor="hand2", state="normal", command=tip_9)
                tip_pagelb.config(text="7/9", font=("Segoe UI", 12))
                tip_after.config(text="▶️", cursor="hand2", state="normal", command=tip_5) 
                tips_lb_title.place(x=55, y=31)
                tips_imglb.place(x=45, y=130)
                tips_btn_back.config(text="⏪", cursor="hand2", command=tips_back) 
                tips_btn_back.place(x=0, width=37, height=33)
                tip_before.place(x=229, y=322, width=33, height=31)
                tip_pagelb.place(x=262, y=322, width=33, height=31)
                tip_after.place(x=295, y=322, width=33, height=31)
                tip_btn_close.config(cursor="hand2", command=hide_tips_window) 
                tip_btn_close.place(x=221, y=360, width=110, height=37)
            except TclError:
                error_window()
                loadfile_error_msg()   

        # ========== TIP-5 WINDOW ========== #
        def tip_5():
            try:
                maintips_lb_title.place_forget()
                tip1_btn.place_forget()
                tip2_btn.place_forget()
                tip3_btn.place_forget()
                tip4_btn.place_forget()
                tip5_btn.place_forget()
                tip6_btn.place_forget()
                tip7_btn.place_forget()
                tip8_btn.place_forget()
                tip9_btn.place_forget()
                tips_urllb.place_forget()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip5.png"))
                tips_frame.place(x=40, y=45, width=480, height=295)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    tips_lb_title.config(text="✒️ How to use Edit Mode?", font=("Segoe UI", 12)) 
                    tips_lb1.config(justify="center", text="To begin, write a ID from Inventory\nthen press the [🔎 Check] Button,\nwill enable the other fields to edit,\nchoose the text field(s) to edit and\npress the [✒️ Edit] Button, a message will\nappear to confirm, Press [✔️ Yes] to Edit.\n\nNOTE: once changes are made\nthey cannot be undone.", font=("Segoe UI", 12))
                    tips_lb1.place(x=185, y=95) 
                elif lang_value == 2:
                    tips_lb_title.config(text="✒️ Como usar el Modo Editar?", font=("Segoe UI", 12))
                    tips_lb1.config(justify="center", text="Para empezar, escribe un ID del inventario,\nluego presiona el Boton [🔎 Comprobar],\nse habilitaran los demas campos para editar,\nelige el/los campos de texto a editar\ny presiona el Boton [✒️ Editar],\naparecera un mensaje para confirmar,\nPresiona [✔️ Si] para Editar.\n\nNOTA: una vez hecho los cambios\nno se pueden deshacer.", font=("Segoe UI", 12))
                    tips_lb1.place(x=165, y=80)
                tip_before.config(text="◀️", cursor="hand2", state="normal", command=tip_4)
                tip_pagelb.config(text="8/9", font=("Segoe UI", 12))
                tip_after.config(text="▶️", cursor="hand2", state="normal", command=tip_6)  
                tips_lb_title.place(x=55, y=31)
                tips_imglb.place(x=45, y=130)
                tips_btn_back.config(text="⏪", cursor="hand2", command=tips_back) 
                tips_btn_back.place(x=0, width=37, height=33)
                tip_before.place(x=229, y=322, width=33, height=31)
                tip_pagelb.place(x=262, y=322, width=33, height=31)
                tip_after.place(x=295, y=322, width=33, height=31)
                tip_btn_close.config(cursor="hand2", command=hide_tips_window) 
                tip_btn_close.place(x=221, y=360, width=110, height=37)
            except TclError:
                error_window()
                loadfile_error_msg()   

        # ========== TIP-6 WINDOW ========== #
        def tip_6():
            try:
                maintips_lb_title.place_forget()
                tip1_btn.place_forget()
                tip2_btn.place_forget()
                tip3_btn.place_forget()
                tip4_btn.place_forget()
                tip5_btn.place_forget()
                tip6_btn.place_forget()
                tip7_btn.place_forget()
                tip8_btn.place_forget()
                tip9_btn.place_forget()
                tips_urllb.place_forget()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip6.png"))
                tips_frame.place(x=40, y=45, width=480, height=295)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    tips_lb_title.config(text="➖ How to use Delete Mode?", font=("Segoe UI", 12)) 
                    tips_lb1.config(justify="center", text="To begin, write a ID from Inventory and\npress the [➖ Delete] Button\na message will appear to confirm,\nPress [✔️ Yes] to Delete.\n\nNOTE: once changes are made\nthey cannot be undone.", font=("Segoe UI", 12))
                    tips_lb1.place(x=175, y=115)  
                elif lang_value == 2:
                    tips_lb_title.config(text="➖ Como usar el Modo Eliminar?", font=("Segoe UI", 12))
                    tips_lb1.config(justify="center", text="Para empezar, escribe un ID del Inventario y\npresiona el Boton [➖ Eliminar],\naparecera un mensaje para confirmar,\nPresiona [✔️ Si] para Eliminar.\n\nNOTA: una vez hecho los cambios\nno se pueden deshacer.", font=("Segoe UI", 12))
                    tips_lb1.place(x=160, y=115) 
                tip_before.config(text="◀️", cursor="hand2", state="normal", command=tip_5)
                tip_pagelb.config(text="9/9", font=("Segoe UI", 12))
                tip_after.config(text="▶️", cursor="arrow", state="disabled") 
                tips_lb_title.place(x=55, y=31)
                tips_imglb.place(x=45, y=130)
                tips_btn_back.config(text="⏪", cursor="hand2", command=tips_back) 
                tips_btn_back.place(x=0, width=37, height=33)
                tip_before.place(x=229, y=322, width=33, height=31)
                tip_pagelb.place(x=262, y=322, width=33, height=31)
                tip_after.place(x=295, y=322, width=33, height=31)
                tip_btn_close.config(cursor="hand2", command=hide_tips_window) 
                tip_btn_close.place(x=221, y=360, width=110, height=37)
            except TclError:
                error_window()
                loadfile_error_msg()   

        # ========== TIP-7 WINDOW ========== #
        def tip_7():
            try:
                maintips_lb_title.place_forget()
                tip1_btn.place_forget()
                tip2_btn.place_forget()
                tip3_btn.place_forget()
                tip4_btn.place_forget()
                tip5_btn.place_forget()
                tip6_btn.place_forget()
                tip7_btn.place_forget()
                tip8_btn.place_forget()
                tip9_btn.place_forget()
                tips_urllb.place_forget()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip7.png"))
                tips_frame.place(x=40, y=45, width=480, height=295)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    tips_lb_title.config(text="🔒 Is my Data Safe?", font=("Segoe UI", 12)) 
                    tips_lb1.config(justify="center", text="Both Account Data and Inventory are secure,\nthey are Encrypted with a unique key generated\nto prevent other programs\nfrom accesing them.", font=("Segoe UI", 12))
                    tips_lb1.place(x=155, y=140)  
                elif lang_value == 2:
                    tips_lb_title.config(text="🔒 Mis Datos estan Seguros?", font=("Segoe UI", 12))
                    tips_lb1.config(justify="center", text="Tanto los Datos de la Cuenta como el Inventario\nestan seguros, estos estan Encriptados\ncon una clave unica generada\npara impedir que otros programas\npuedan acceder a ellos.", font=("Segoe UI", 12))
                    tips_lb1.place(x=155, y=135) 
                tip_before.config(text="◀️", cursor="hand2", state="normal", command=tip_3)
                tip_pagelb.config(text="4/9", font=("Segoe UI", 12))
                tip_after.config(text="▶️", cursor="hand2", state="normal", command=tip_8) 
                tips_lb_title.place(x=55, y=31)
                tips_imglb.place(x=45, y=135)
                tips_btn_back.config(text="⏪", cursor="hand2", command=tips_back) 
                tips_btn_back.place(x=0, width=37, height=33)
                tip_before.place(x=229, y=322, width=33, height=31)
                tip_pagelb.place(x=262, y=322, width=33, height=31)
                tip_after.place(x=295, y=322, width=33, height=31)
                tip_btn_close.config(cursor="hand2", command=hide_tips_window) 
                tip_btn_close.place(x=221, y=360, width=110, height=37)
            except TclError:
                error_window()
                loadfile_error_msg()   

        # ========== TIP-8 WINDOW ========== #
        def tip_8():
            try:
                maintips_lb_title.place_forget()
                tip1_btn.place_forget()
                tip2_btn.place_forget()
                tip3_btn.place_forget()
                tip4_btn.place_forget()
                tip5_btn.place_forget()
                tip6_btn.place_forget()
                tip7_btn.place_forget()
                tip8_btn.place_forget()
                tip9_btn.place_forget()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip8.png"))
                tips_frame.place(x=40, y=45, width=480, height=295)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    tips_lb_title.config(text="❓ How to change the Theme/Language?", font=("Segoe UI", 12)) 
                    tips_lb1.config(justify="center", text="To begin, press the Button with the Icon [🔧],\nwhic is located in the upper right corner,\nthe Settings Window will open,\nthe available Themes are: [System, Light, Dark] and\nthe available Languages are: [English, Español],\nSelect the Theme/Language of your Preference\nand press the [✔️ Apply] Button\nto Save the Changes.\n\nNOTE: some Options may not be available\nin certain Windows Versions.\nFor more information see the Requirements [Here].", font=("Segoe UI", 12))
                    tips_lb1.place(x=145, y=60)
                    tips_urllb.config(justify="center", text="[Here].", cursor="hand2", font=("Segoe UI", 12))
                    tips_urllb.bind("<Button-1>", lambda event: webbrowser.open_new_tab("https://github.com/EliezerB03/DWI?tab=readme-ov-file#requirements-for-some-features"))
                    tips_urllb.place(x=455, y=294, height=20)   
                elif lang_value == 2:
                    tips_lb_title.config(text="❓ Como cambiar el Tema/Idioma?", font=("Segoe UI", 12))
                    tips_lb1.config(justify="center", text="Para empezar, presiona el Boton con el Icono [🔧],\nque esta ubicado en la esquina superior derecha,\nse abrira la Ventana de Configuracion,\nlos Temas disponibles son: [Sistema, Claro, Oscuro]\ny los Idiomas disponibles son: [English, Español],\nSeleciona el Tema/Idioma de tu Preferencia\ny presiona el Boton [✔️ Aplicar]\npara Guardar los Cambios.\n\nNOTA: algunas Opciones pueden no estar\ndisponibles en ciertas Versiones de Windows\nPara mas Informacion consulte los Requisitos [Aqui].", font=("Segoe UI", 12))
                    tips_lb1.place(x=145, y=60)
                    tips_urllb.config(justify="center", text="[Aqui].", cursor="hand2", font=("Segoe UI", 12))
                    tips_urllb.bind("<Button-1>", lambda event: webbrowser.open_new_tab("https://github.com/EliezerB03/DWI/blob/master/README_ES.md#requisitos-para-algunas-caracter%C3%ADsticas"))
                    tips_urllb.place(x=465, y=294, height=21)
                tip_before.config(text="◀️", cursor="hand2", state="normal", command=tip_7)
                tip_pagelb.config(text="5/9", font=("Segoe UI", 12))
                tip_after.config(text="▶️", cursor="hand2", state="normal", command=tip_9) 
                tips_lb_title.place(x=55, y=31)
                tips_imglb.place(x=45, y=145)
                tips_btn_back.config(text="⏪", cursor="hand2", command=tips_back) 
                tips_btn_back.place(x=0, width=37, height=33)
                tip_before.place(x=229, y=322, width=33, height=31)
                tip_pagelb.place(x=262, y=322, width=33, height=31)
                tip_after.place(x=295, y=322, width=33, height=31)
                tip_btn_close.config(cursor="hand2", command=hide_tips_window) 
                tip_btn_close.place(x=221, y=360, width=110, height=37)
            except TclError:
                error_window()
                loadfile_error_msg()   

        # ========== TIP-9 WINDOW ========== #
        def tip_9():
            try:
                maintips_lb_title.place_forget()
                tip1_btn.place_forget()
                tip2_btn.place_forget()
                tip3_btn.place_forget()
                tip4_btn.place_forget()
                tip5_btn.place_forget()
                tip6_btn.place_forget()
                tip7_btn.place_forget()
                tip8_btn.place_forget()
                tip9_btn.place_forget()
                tips_urllb.place_forget()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip9.png"))
                tips_frame.place(x=40, y=45, width=480, height=295)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    tips_lb_title.config(text="👤 How to change the Username/Password?", font=("Segoe UI", 12)) 
                    tips_lb1.config(justify="center", text="To begin, press the [👤 Account Settings] Button\nto change the Username/Paswword, press the\n[👤 Change Username]/[🔑 Change Password]\nButton Fill in the Text Fields\nwith information requested, and\npress the [✔️ Change] Button\nto Save the Changes.\n\nNOTE: Your Username/Password\nis Required to confirm Changes.", font=("Segoe UI", 12))
                    tips_lb1.place(x=150, y=80)  
                elif lang_value == 2:
                    tips_lb_title.config(text="👤 Como cambiar el Usuario/Contraseña?", font=("Segoe UI", 12))
                    tips_lb1.config(justify="center", text="Para empezar, presiona el Boton\n[👤 Configuracion de Cuenta],\npara cambiar el Nombre de Usuario/\nContraseña, presiona el\nBoton [👤 Cambiar Nombre de Usuario]/\n[🔑 Cambiar Contraseña], Rellena\nlos Campos de Texto con la informacion\nque le pide y presione el boton [✔️ Cambiar]\npara Guardar los Cambios.\n\nNOTA: Se Requiere su Nombre de Usuario/\nContraseña para confirmar los Cambios.", font=("Segoe UI", 12))
                    tips_lb1.place(x=170, y=60) 
                tip_before.config(text="◀️", cursor="hand2", state="normal", command=tip_8)
                tip_pagelb.config(text="6/9", font=("Segoe UI", 12))
                tip_after.config(text="▶️", cursor="hand2", state="normal", command=tip_4) 
                tips_lb_title.place(x=55, y=31)
                tips_imglb.place(x=45, y=120)
                tips_btn_back.config(text="⏪", cursor="hand2", command=tips_back) 
                tips_btn_back.place(x=0, width=37, height=33)
                tip_before.place(x=229, y=322, width=33, height=31)
                tip_pagelb.place(x=262, y=322, width=33, height=31)
                tip_after.place(x=295, y=322, width=33, height=31)
                tip_btn_close.config(cursor="hand2", command=hide_tips_window) 
                tip_btn_close.place(x=221, y=360, width=110, height=37)
            except TclError:
                error_window()
                loadfile_error_msg()   

        # ============================================== LOAD MSG WINDOWS ============================================== #
        # ========== CHANGE USERNAME CORRECT MSG ========== #
        def changeusername_correct_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 417
                    basic_window.title("Change Username")
                    basic_lb1.config(justify="center", text="Your Username has been CHANGED!", font=("Segoe UI", 12))
                    basic_btn_ok.place(x=172, y=125, width=80, height=37)
                elif lang_value == 2:
                    window_w = 447
                    basic_window.title("Cambiar Nombre de Usuario")  
                    basic_lb1.config(justify="center", text="Tu Nombre de Usuario se ha CAMBIADO!", font=("Segoe UI", 12))
                    basic_btn_ok.place(x=179, y=125, width=80, height=37)
                window_h = 175
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_changeaccount_msg())  
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                basic_imglb.place(x=15, y=30)
                basic_lb1.place(x=120, y=56)
                basic_btn_ok.config(command=hide_changeaccount_msg)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
                changeaccount_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== CHANGE PASSWORD CORRECT MSG ========== #
        def changepassword_correct_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 417 
                    basic_window.title("Change Password")
                    basic_lb1.config(justify="center", text="Your Password has been CHANGED!", font=("Segoe UI", 12))
                    basic_btn_ok.place(x=172, y=125, width=80, height=37)
                elif lang_value == 2:
                    window_w = 393 
                    basic_window.title("Cambiar Contraseña") 
                    basic_lb1.config(justify="center", text="Tu Contraseña se ha CAMBIADO!", font=("Segoe UI", 12)) 
                    basic_btn_ok.place(x=152, y=125, width=80, height=37)
                window_h = 175
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_changeaccount_msg())   
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                basic_imglb.place(x=15, y=30)
                basic_lb1.place(x=120, y=56)
                basic_btn_ok.config(command=hide_changeaccount_msg)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
                changeaccount_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== CHANGELOG MSG ========== #
        def changelog():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 495 
                    window_h = 565 
                    basic_window.title("Changelog in this Version")
                    basic_imglb.place(x=178, y=5)
                    basic_lb1.config(justify="left", text="================ CHANGELOG ===============\n\n  <<<<<                  VERSION 3.2 (13-JUL-2024)              >>>>>\n\n- Encryption System has been Improved.\n- More FAQs Added to 'Tips'.\n- Added Developer Contact Information to 'About the Program'.\n- Added 'Clear Data Program' Option in Settings.\n- Various UI Improvements.\n- Improved Language Translations.\n- Some Functionality Improvements.\n- In-Code Optimizations.\n- Various Bugs Fixes.\n\n                               Developed By Eliezer Brito\n                                      © Elie-Dev (2024)\n                                      All rights reserved", font=("Segoe UI", 12))
                    basic_lb1.place(x=17, y=140)
                    basic_btn_ok.place(x=198, y=520, width=80, height=37)
                elif lang_value == 2:
                    window_w = 605 
                    window_h = 565
                    basic_window.title("Registro de Cambios en esta Version")
                    basic_imglb.place(x=239, y=5)
                    basic_lb1.config(justify="left", text="================== REGISTRO DE CAMBIOS ==================\n\n  <<<<<                               VERSION 3.2 (13-JUL-2024)                               >>>>>\n\n- Se ha Mejorado el Sistema de Encryptacion.\n- Se Agregaron mas Preguntas Frecuentes a 'Consejos'.\n- Se Agrego Informacion de Contacto del Desarrollador en 'Acerca del Programa'.\n- Se Agrego la Opcion 'Borrar Datos del Programa' en Configuracion.\n- Varias Mejoras en la Interfaz de Usuario.\n- Se Mejoraron las Traducciones de los Idiomas.\n- Algunas Mejoras en la Funcionalidad.\n- Optimizaciones en el Codigo.\n- Varias Correcciones de Errores.\n\n                                             Desarrollado por Eliezer Brito\n                                                      © Elie-Dev (2024)\n                                           Todos los Derechos Reservados", font=("Segoe UI", 12))
                    basic_lb1.place(x=17, y=140)
                    basic_btn_ok.place(x=260, y=515, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/changelog.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== ABOUT MSG ========== #
        def about():
            try:
                def contact():
                    webbrowser.open_new_tab("mailto:el.elie03@gmail.com")
                def projectpage():
                    webbrowser.open_new_tab("https://github.com/EliezerB03/DWI")
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 348
                    window_h = 460
                    basic_window.title("About the Program")
                    basic_imglb.place(x=112, y=5)
                    basic_lb1.config(justify="center", text="Device Warehouse Inventory\nVersion: 3.2\n\nA Program that Facilitates the Management\nof Inventory Device Information\nfrom a Local Database.\n\nDeveloped By Eliezer Brito\n© Elie-Dev (2024)\nAll rights reserved", font=("Segoe UI", 12))
                    basic_lb1.place(x=19, y=140)
                    contact_info.config(text="📧  Contact", command=contact)
                    github_project.config(text="🌐  Project Page", command=projectpage) 
                    contact_info.place(x=51, y=360, width=103, height=30)
                    github_project.place(x=169, y=360, width=130, height=30)
                    basic_btn_ok.place(x=131, y=410, width=80, height=37)
                elif lang_value == 2:
                    window_w = 368
                    window_h = 460
                    basic_window.title("Acerca del Programa")
                    basic_imglb.place(x=119, y=5)
                    basic_lb1.config(justify="center", text="Device Warehouse Inventory\nVersion: 3.2\n\nUn Programa que Facilita el\nManejo de informacion de los Dispositivos\ndel Inventario desde una Base de Datos Local.\n\nDesarrollado por Eliezer Brito\n© Elie-Dev (2024)\nTodos los Derechos Reservados", font=("Segoe UI", 12))
                    basic_lb1.place(x=21, y=140)
                    contact_info.config(text="📧  Contacto", command=contact)
                    github_project.config(text="🌐  Pagina del Projecto", command=projectpage) 
                    contact_info.place(x=33, y=360, width=110, height=30)
                    github_project.place(x=151, y=360, width=180, height=30)
                    basic_btn_ok.place(x=137, y=410, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/about.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== HELP LOGIN MSG ========== #
        def login_help(): 
            try: 
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 460
                    window_h = 235
                    basic_window.title("How to Sign-In?")
                    basic_imglb.place(x=15, y=40)
                    basic_lb1.config(justify="center", text="To begin, enter your Username and Password,\nand press the [🔓 Sign-In] button.\nif the data is correct the program\nwill start, otherwise you will receive\nan error message.\n\nFor more information, consult Tips.", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=20)                        
                    basic_btn_ok.place(x=193, y=185, width=80, height=37)
                elif lang_value == 2:
                    window_w = 475
                    window_h = 235
                    basic_window.title("Como Iniciar Sesion?") 
                    basic_imglb.place(x=15, y=40)
                    basic_lb1.config(justify="center", text="Para empezar, escriba su\nNombre de Usuario y Contraseña\ny presione el boton [🔓 Iniciar Sesion]\nsi los datos son correcto el programa iniciara,\nde lo contrario recibiras un mensaje de error.\n\nPara mas informacion, consulte Consejos.", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=20) 
                    basic_btn_ok.place(x=195, y=185, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))           
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip2.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()
                
        # ========== LOGIN ERROR MSG ========== #
        def login_error(): 
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 393
                    window_h = 175
                    basic_window.title("Failed to Login")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Your Account is incorrect or invalid!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=160, y=125, width=80, height=37)
                elif lang_value == 2:
                    window_w = 393
                    window_h = 175
                    basic_window.title("Error al Iniciar Sesion")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Tu Cuenta es Incorrecta o Invalida!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=152, y=125, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== HELP MAIN MSG ========== #
        def main_help():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 455
                    window_h = 200
                    basic_window.title("How to use This Program?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="To begin, select one of the available options\nlocated at the top to open each option.\n\nFor more information, consult Tips.", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=40)                  
                    basic_btn_ok.place(x=185, y=150, width=80, height=37)
                elif lang_value == 2:
                    window_w = 510
                    window_h = 200
                    basic_window.title("Como usar Este Programa?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Para comenzar, seleccione una de las\nopciones disponibles ubicadas en la parte superior\npara abrir cada opcion.\n\nPara mas informacion, consulte Consejos.", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=20)
                    basic_btn_ok.place(x=212, y=150, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip3.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== ADD MODE HELP MSG ========== #
        def addmode_help(): 
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 438
                    window_h = 220
                    basic_window.title("How to use Add Mode?") 
                    basic_imglb.place(x=15, y=35)
                    basic_lb1.config(justify="center", text="To begin, fill out the text fields and\npress the [➕ Add] Button, When you press\nthe button, a message will\nappear to confirm.\n\nFor more information, consult Tips.", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=20)                
                    basic_btn_ok.place(x=183, y=170, width=80, height=37)
                elif lang_value == 2:
                    window_w = 480
                    window_h = 210
                    basic_window.title("Como usar el Modo Agregar?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Para empezar, llena los campos de texto y\npresiona el Boton [➕ Agregar], al presionar\nel boton, aparecera un mensaje para confirmar.\n\nPara mas informacion, consulte Consejos.", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=30)
                    basic_btn_ok.place(x=195, y=160, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip4.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== EDIT MODE HELP MSG ========== #
        def editmode_help():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 387
                    window_h = 240
                    basic_window.title("How to use Edit Mode?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="To begin, write the ID,\npress the [🔎 Check] Button,\npressing the button if the\nID is correct will enable\nthe other fields to edit.\n\nFor more information, consult Tips.", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=20)              
                    basic_btn_ok.place(x=149, y=190, width=80, height=37)
                elif lang_value == 2:
                    window_w = 444
                    window_h = 240
                    basic_window.title("Como usar el Modo Editar?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Para empezar, escribe el ID,\npresiona el Boton [🔎 Comprobar],\nal presionar el boton si el ID\nes correcto se habilitaran los\ndemas campos para editar.\n\nPara mas informacion, consulte Consejos.", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=20)
                    basic_btn_ok.place(x=177, y=190, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()                   
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip5.png"))                    
                basic_btn_ok.config(command=hide_basic_window)                    
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== DELETE MODE HELP MSG ========== #
        def deletemode_help(): 
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 385
                    window_h = 240
                    basic_window.title("How to use Delete Mode?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="To begin, write the\nID and press the \n[➖ Delete] Button, if the\nID is correct a message\nwill appear to confirm.\n\nFor more information, consult Tips.", font=("Segoe UI", 12))
                    basic_lb1.place(x=115, y=20)          
                    basic_btn_ok.place(x=156, y=190, width=80, height=37)
                elif lang_value == 2:
                    window_w = 444
                    window_h = 240
                    basic_window.title("Como usar el Modo Eliminar?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Para empezar, escribe el\nID  y presiona el\nBoton [➖ Eliminar], si\nel ID es correcto te aparecera\nun mensaje para confirmar.\n\nPara mas informacion, consulte Consejos.", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=20)
                    basic_btn_ok.place(x=177, y=190, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())                        
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()                    
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/tip6.png"))                    
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== ADD PRODUCT SAVE MSG ========== #
        def add_prod_save():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 450
                    window_h = 165
                    basic_window.title("Adding to Inventory...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Your Product has been ADDED to Inventory!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=188, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 465
                    window_h = 165
                    basic_window.title("Agregando al Inventario...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Tu Producto se ha AGREGADO al Inventario!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=188, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== ADD PRODUCT EMPTY MSG ========== #
        def add_prod_empty():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 393
                    window_h = 165
                    basic_window.title("Adding to Inventory...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="You can't leave EMPTY Text Fields!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=160, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 490
                    window_h = 165
                    basic_window.title("Agregando al Inventario...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="No Puedes dejar VACIOS los Campos de Texto!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=202, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== ADD PRODUCT ASK MSG ========== #
        def add_prod_ask():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 732 
                window_h = 210
                lang_value = languagegroup.get()
                if lang_value == 1: 
                    basic_window.title("Adding in the Inventory...")
                    basic_imglb.place(x=15, y=50) 
                    basic_lb1.config(justify="center", text="A Unique ID will be generated and Saved in the Inventory with the following Information.\nDo you Want to Add it to your Inventory?", font=("Segoe UI", 12))
                    basic_lb1.place(x=95, y=15)
                    info_bf_lb.config(justify="center", text="Info:", font=("Segoe UI", 12, "bold"))
                    info_bf_lb.place(x=115, y=70)
                    brand_bf.place(x=115, y=95, width=192)
                    model_bf.place(x=305, y=95, width=247)
                    color_bf.place(x=550, y=95, width=167)
                    infobf_frame.place(x=115, y=120, width=602, height=2)
                    style_elements.configure("yesadd.TButton", foreground="#009003", focuscolor='#009003')
                    basic_btn_yes.config(text="✔️  Yes", style="yesadd.TButton")
                    basic_btn_yes.place(x=281, y=160, width=80, height=37)
                    basic_btn_no.config(text="❌  No")
                    basic_btn_no.place(x=376, y=160, width=80, height=37)
                elif lang_value == 2:
                    basic_window.title("Agregando en el Inventario...")
                    basic_imglb.place(x=15, y=50) 
                    basic_lb1.config(justify="center", text="Se generara un ID Unico y se Guardara en el Inventario con la siguiente Informacion.\nQuieres Agregarlo al Inventario?", font=("Segoe UI", 12))
                    basic_lb1.place(x=115, y=15) 
                    info_bf_lb.config(justify="center", text="Info:", font=("Segoe UI", 12, "bold"))
                    info_bf_lb.place(x=115, y=70)
                    brand_bf.place(x=115, y=95, width=192)
                    model_bf.place(x=305, y=95, width=247)
                    color_bf.place(x=550, y=95, width=167)
                    infobf_frame.place(x=115, y=120, width=602, height=2)
                    style_elements.configure("yesadd.TButton", foreground="#009003", focuscolor='#009003')
                    basic_btn_yes.config(text="✔️  Si", style="yesadd.TButton")
                    basic_btn_yes.place(x=281, y=160, width=80, height=37)
                    basic_btn_no.config(text="❌  No")
                    basic_btn_no.place(x=376, y=160, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: add_no())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/ask.png"))
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== EDIT PRODUCT SAVE MSG ========== #
        def edit_prod_save():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 478
                    window_h = 165
                    basic_window.title("Editing in the Inventory...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Your Product has been EDITED in the Inventory!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=200, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 465
                    window_h = 165
                    basic_window.title("Editando en el Inventario...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Tu Producto se ha EDITADO en el Inventario!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=188, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== EDIT PRODUCT NOTFOUND MSG ========== #
        def edit_prod_notfound():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 320
                    window_h = 165
                    basic_window.title("Editing in the Inventory...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="This ID does not EXIST!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=117, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 315
                    window_h = 165
                    basic_window.title("Editando en el Inventario...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Este ID no Existe!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=115, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()                   
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== EDIT PRODUCT EMPTY MSG ========== #
        def edit_prod_empty():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 393
                    window_h = 165
                    basic_window.title("Editing in the Inventory...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="You can't leave EMPTY Text Fields!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=160, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 490
                    window_h = 165
                    basic_window.title("Editando en el Inventario...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="No Puedes dejar VACIOS los Campos de Texto!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=210, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()                  
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== EDIT PRODUCT ASK MSG ========== #
        def edit_prod_ask():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 890 
                window_h = 290
                lang_value = languagegroup.get()
                if lang_value == 1: 
                    basic_window.title("Editing in the Inventory...")
                    basic_imglb.place(x=15, y=90) 
                    basic_lb1.config(justify="center", text="Are you sure you want to EDIT it from inventory?\nThis action is IRREVERSIBLE!", font=("Segoe UI", 12))
                    basic_lb1.place(x=270, y=15) 
                    info_bf_lb.config(justify="center", text="Now:", font=("Segoe UI", 12, "bold"))
                    info_bf_lb.place(x=115, y=70)
                    id_inf.place(x=115, y=250)
                    brand_bf.place(x=115, y=95, width=192)
                    model_bf.place(x=305, y=95, width=247)
                    color_bf.place(x=550, y=95, width=167)
                    date_bf.place(x=715, y=95, width=160)
                    infobf_frame.place(x=115, y=120, width=760, height=2)
                    info_af_lb.config(justify="center", text="After:", font=("Segoe UI", 12, "bold"))
                    info_af_lb.place(x=115, y=150)
                    brand_af.place(x=115, y=175, width=192)
                    model_af.place(x=305, y=175, width=247)
                    color_af.place(x=550, y=175, width=167)
                    date_af.place(x=715, y=175, width=160)
                    infoaf_frame.place(x=115, y=200, width=760, height=2)
                    style_elements.configure("yesedit.TButton", foreground="#0078FF", focuscolor='#0078FF')
                    basic_btn_yes.config(text="✔️  Yes", style="yesedit.TButton")
                    basic_btn_yes.place(x=352, y=240, width=80, height=37)
                    basic_btn_no.config(text="❌  No")
                    basic_btn_no.place(x=447, y=240, width=80, height=37)
                elif lang_value == 2:
                    basic_window.title("Editando en el Inventario...")
                    basic_imglb.place(x=15, y=90) 
                    basic_lb1.config(justify="center", text="Estas Seguro que quieres EDITARLO del Inventario?\nEsta accion es INRREVERSIBLE!", font=("Segoe UI", 12))
                    basic_lb1.place(x=255, y=15) 
                    info_bf_lb.config(justify="center", text="Ahora:", font=("Segoe UI", 12, "bold"))
                    info_bf_lb.place(x=115, y=70)
                    id_inf.place(x=115, y=250)
                    brand_bf.place(x=115, y=95, width=192)
                    model_bf.place(x=305, y=95, width=247)
                    color_bf.place(x=550, y=95, width=167)
                    date_bf.place(x=715, y=95, width=160)
                    infobf_frame.place(x=115, y=120, width=760, height=2)
                    info_af_lb.config(justify="center", text="Despues:", font=("Segoe UI", 12, "bold"))
                    info_af_lb.place(x=115, y=150)
                    brand_af.place(x=115, y=175, width=192)
                    model_af.place(x=305, y=175, width=247)
                    color_af.place(x=550, y=175, width=167)
                    date_af.place(x=715, y=175, width=160)
                    infoaf_frame.place(x=115, y=200, width=760, height=2)
                    style_elements.configure("yesedit.TButton", foreground="#0078FF", focuscolor='#0078FF')
                    basic_btn_yes.config(text="✔️  Si", style="yesedit.TButton")
                    basic_btn_yes.place(x=352, y=240, width=80, height=37)
                    basic_btn_no.config(text="❌  No")
                    basic_btn_no.place(x=447, y=240, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: edit_no())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()                   
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/ask.png"))
                id_inf.config(fg="#0078FF")
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== DELETE PRODUCT DEL MSG ========== #
        def delete_prod_del():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 495
                    window_h = 165
                    basic_window.title("Deleting in the Inventory...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Your Product has been DELETED in the Inventory!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=205, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 470
                    window_h = 165 
                    basic_window.title("Eliminando en el Inventario...")                        
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Tu Profucto ha sido ELIMINADO del Inventario!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=190, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== DELETE PRODUCT NOTFOUND MSG ========== #
        def delete_prod_notfound():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 325
                    window_h = 165
                    basic_window.title("Deleting in the Inventory...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="This ID does not EXIST!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=120, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 315
                    window_h = 165
                    basic_window.title("Eliminando en el Inventario...")                        
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Este ID no Existe!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=115, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== DELETE PRODUCT EMPTY MSG ========== #
        def delete_prod_empty():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 393
                    window_h = 165
                    basic_window.title("Deleting in the Inventory...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="You can't leave EMPTY Text Fields!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=160, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 490
                    window_h = 165
                    basic_window.title("Eliminando en el Inventario...")                        
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="No Puedes dejar VACIOS los Campos de Texto!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=56)
                    basic_btn_ok.place(x=202, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()                    
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basic_btn_ok.config(command=hide_basic_window)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== DELETE PRODUCT ASK MSG ========== #
        def delete_prod_ask():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                window_w = 890 
                window_h = 210
                lang_value = languagegroup.get()
                if lang_value == 1: 
                    basic_window.title("Deleting in the Inventory...")
                    basic_imglb.place(x=15, y=50) 
                    basic_lb1.config(justify="center", text="Are you sure you want to DELETE it from inventory?\nThis action is IRREVERSIBLE!", font=("Segoe UI", 12))
                    basic_lb1.place(x=270, y=15) 
                    info_bf_lb.config(justify="center", text="Info:", font=("Segoe UI", 12, "bold"))
                    info_bf_lb.place(x=115, y=70)
                    id_inf.place(x=115, y=170)
                    brand_bf.place(x=115, y=95, width=192)
                    model_bf.place(x=305, y=95, width=247)
                    color_bf.place(x=550, y=95, width=167)
                    date_bf.place(x=715, y=95, width=160)
                    infobf_frame.place(x=115, y=120, width=760, height=2)
                    style_elements.configure("yesdel.TButton", foreground="#EB0000", focuscolor='#EB0000')
                    basic_btn_yes.config(text="✔️  Yes", style="yesdel.TButton")
                    basic_btn_yes.place(x=360, y=160, width=80, height=37)
                    basic_btn_no.config(text="❌  No")
                    basic_btn_no.place(x=455, y=160, width=80, height=37)
                elif lang_value == 2:
                    basic_window.title("Eliminando en el Inventario...")
                    basic_imglb.place(x=15, y=50) 
                    basic_lb1.config(justify="center", text="Estas Seguro que quieres ELIMINARLO del Inventario?\nEsta accion es INRREVERSIBLE!", font=("Segoe UI", 12))
                    basic_lb1.place(x=255, y=15) 
                    info_bf_lb.config(justify="center", text="Info:", font=("Segoe UI", 12, "bold"))
                    info_bf_lb.place(x=115, y=70)
                    id_inf.place(x=115, y=170)
                    brand_bf.place(x=115, y=95, width=192)
                    model_bf.place(x=305, y=95, width=247)
                    color_bf.place(x=550, y=95, width=167)
                    date_bf.place(x=715, y=95, width=160)
                    infobf_frame.place(x=115, y=120, width=760, height=2)
                    style_elements.configure("yesdel.TButton", foreground="#EB0000", focuscolor='#EB0000')
                    basic_btn_yes.config(text="✔️  Si", style="yesdel.TButton")
                    basic_btn_yes.place(x=360, y=160, width=80, height=37)
                    basic_btn_no.config(text="❌  No")
                    basic_btn_no.place(x=455, y=160, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: del_no())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/ask.png"))
                id_inf.config(fg="#EB0000")
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== SAVE TXT FILE SUCCESS MSG ========== #
        def save_txtfile_success_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                theme_value = themegroup.get()   
                if theme_value == 1:
                    show_csvfilelb.config(bg="#101010", fg="white")
                    show_csvfilelb.bind("<Enter>", lambda event: show_csvfilelb.config(fg="#CECECE"))
                    show_csvfilelb.bind("<Leave>", lambda event: show_csvfilelb.config(fg="white"))
                    style_elements.configure("export.TButton", foreground="white", focuscolor='white')
                    basic_btn_yes.config(style="export.TButton")
                elif theme_value == 2:
                    show_csvfilelb.config(bg="white", fg="black")
                    show_csvfilelb.bind("<Enter>", lambda event: show_csvfilelb.config(fg="#777777"))
                    show_csvfilelb.bind("<Leave>", lambda event: show_csvfilelb.config(fg="black"))
                    style_elements.configure("export.TButton", foreground="black", focuscolor='black')
                    basic_btn_yes.config(style="export.TButton")
                elif theme_value == 3:
                    if darkdetect.isDark():
                        show_csvfilelb.config(bg="#101010", fg="white")
                        show_csvfilelb.bind("<Enter>", lambda event: show_csvfilelb.config(fg="#CECECE"))
                        show_csvfilelb.bind("<Leave>", lambda event: show_csvfilelb.config(fg="white"))
                        style_elements.configure("export.TButton", foreground="white", focuscolor='white')
                        basic_btn_yes.config(style="export.TButton")
                    else:
                        show_csvfilelb.config(bg="white", fg="black")
                        show_csvfilelb.bind("<Enter>", lambda event: show_csvfilelb.config(fg="#777777"))
                        show_csvfilelb.bind("<Leave>", lambda event: show_csvfilelb.config(fg="black"))
                        style_elements.configure("export.TButton", foreground="black", focuscolor='black')
                        basic_btn_yes.config(style="export.TButton")
                show_csvfilelb.bind("<Button-1>", lambda event: show_txtfile())
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 513
                    window_h = 165
                    basic_window.title("Saving Content to Text File...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="The contents of the inventory have been SAVED\nto Text File successfully!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=44)
                    basic_btn_ok.place(x=218, y=115, width=80, height=37)
                    show_csvfilelb.config(text="📂 Show File")
                    show_csvfilelb.place(x=403, y=134)
                elif lang_value == 2:
                    window_w = 496
                    window_h = 165
                    basic_window.title("Guardando Contenido al Archivo de Texto...")                      
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="El contenido del Inventario ha sido GUARDADO\nal Archivo de Texto Exitosamente!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=44)
                    show_csvfilelb.config(text="📂 Mostrar Archivo")
                    show_csvfilelb.place(x=346, y=134)
                    basic_btn_ok.place(x=198, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                basic_btn_ok.config(command=hide_basic_window) 
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== SAVE TXT FILE ERROR MSG ========== #
        def save_txtfile_error_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 525 
                    window_h = 155
                    basic_window.title("Saving Content to Text File...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="The Text File contains Non Valid Values or Is Corrupt!\nThe Content of Inventory Data will be Not Saved!", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=34)
                    basic_btn_ok.place(x=228, y=105, width=80, height=37)
                elif lang_value == 2:
                    window_w = 608
                    window_h = 155
                    basic_window.title("Guardando Contenido al Archivo de Texto...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="El Archivo de Texto contiene Valores No Validos o Esta Corrupto!\nNo Se Guardara el Contenido de los Datos del Inventario!", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=34)
                    basic_btn_ok.place(x=259, y=105, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basic_btn_ok.config(command=hide_basic_window) 
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== SAVE TXT FILE CANCELED MSG ========== #
        def save_txtfile_canceled_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 505
                    window_h = 155
                    basic_window.title("Saving Content to Text File...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="The User has Canceled the Save of the Text File.\nNo Changes Have Been Made.", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=34)
                    basic_btn_ok.place(x=214, y=105, width=80, height=37)
                elif lang_value == 2:
                    window_w = 566
                    window_h = 155
                    basic_window.title("Guardando Contenido al Archivo de Texto...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="El Usuario ha Cancelado el Guardado del Archivo de Texto.\nNo se han Hecho Cambios.", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=34)
                    basic_btn_ok.place(x=238, y=105, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basic_btn_ok.config(command=hide_basic_window) 
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()
        
        # ========== SAVE TXT FILE ASK MSG ========== #
        def save_txtfile_ask():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                theme_value = themegroup.get()   
                if theme_value == 1:
                    style_elements.configure("export.TButton", foreground="white", focuscolor='white')
                    basic_btn_yes.config(style="export.TButton")
                elif theme_value == 2:
                    style_elements.configure("export.TButton", foreground="black", focuscolor='black')
                    basic_btn_yes.config(style="export.TButton")
                elif theme_value == 3:
                    if darkdetect.isDark():
                        style_elements.configure("export.TButton", foreground="white", focuscolor='white')
                        basic_btn_yes.config(style="export.TButton")
                    else:
                        style_elements.configure("export.TButton", foreground="black", focuscolor='black')
                        basic_btn_yes.config(style="export.TButton")
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 615
                    window_h = 165
                    basic_window.title("Save Content to Text File?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="WARNING: When you Save the Text file it will be decrypted,\nso any program will be able to access it.", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=44)
                    basic_btn_yes.config(text="💾  Save", command=save_txtfile)
                    basic_btn_yes.place(x=185, y=115, width=110, height=37)
                    basic_btn_no.config(text="❌  Cancel", command=hide_basic_window)
                    basic_btn_no.place(x=322, y=115, width=110, height=37)
                elif lang_value == 2:
                    window_w = 726
                    window_h = 165
                    basic_window.title("Guardar Contenido al Archivo de Texto?")                 
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="ADVERTENCIA: Al Guardar el Archivo de Texto sera Desencriptado,\npor lo que cualquier Programa podra Acceder a el.", font=("Segoe UI", 12))
                    basic_lb1.place(x=150, y=44)
                    basic_btn_yes.config(text="💾  Guardar", command=save_txtfile)
                    basic_btn_yes.place(x=238, y=115, width=110, height=37)
                    basic_btn_no.config(text="❌  Cancelar", command=hide_basic_window)
                    basic_btn_no.place(x=373, y=115, width=110, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== SIGN-OUT ASK MSG ========== #
        def signout_ask():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 395
                    window_h = 165
                    basic_window.title("Sign-Out?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Are you sure you want to Sign-Out?", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=54)
                    theme_value = themegroup.get()
                    if theme_value == 1:
                        style_elements.configure("signout.TButton", foreground="#C19300", focuscolor='#C19300')
                        basic_btn_yes.config(text="✔️  Yes", command=signout, style="signout.TButton")
                    if theme_value == 2:
                        style_elements.configure("signout.TButton", foreground="#AC8300", focuscolor='#AC8300')
                        basic_btn_yes.config(text="✔️  Yes", command=signout, style="signout.TButton")
                    elif theme_value == 3:
                        if darkdetect.isDark():
                            style_elements.configure("signout.TButton", foreground="#C19300", focuscolor='#C19300')
                            basic_btn_yes.config(text="✔️  Yes", command=signout, style="signout.TButton")
                        else:
                            style_elements.configure("signout.TButton", foreground="#AC8300", focuscolor='#AC8300')
                            basic_btn_yes.config(text="✔️  Yes", command=signout, style="signout.TButton")
                    basic_btn_yes.place(x=108, y=115, width=80, height=37)
                    basic_btn_no.config(text="❌  No", command=hide_basic_window)
                    basic_btn_no.place(x=205, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 440
                    window_h = 165
                    basic_window.title("Cerrar Sesion?")                 
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Estas Seguro que quieres Cerrar Sesion?", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=54)
                    theme_value = themegroup.get()
                    if theme_value == 1:
                        style_elements.configure("signout.TButton", foreground="#C19300", focuscolor='#C19300')
                        basic_btn_yes.config(text="✔️  Si", command=signout, style="signout.TButton")
                    if theme_value == 2:
                        style_elements.configure("signout.TButton", foreground="#AC8300", focuscolor='#AC8300')
                        basic_btn_yes.config(text="✔️  Si", command=signout, style="signout.TButton")
                    elif theme_value == 3:
                        if darkdetect.isDark():
                            style_elements.configure("signout.TButton", foreground="#C19300", focuscolor='#C19300')
                            basic_btn_yes.config(text="✔️  Si", command=signout, style="signout.TButton")
                        else:
                            style_elements.configure("signout.TButton", foreground="#AC8300", focuscolor='#AC8300')
                            basic_btn_yes.config(text="✔️  Si", command=signout, style="signout.TButton")
                    basic_btn_yes.place(x=130, y=115, width=80, height=37)
                    basic_btn_no.config(text="❌ No", command=hide_basic_window)
                    basic_btn_no.place(x=225, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/ask.png"))
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== IMPORT CSV FILE SUCCESS MSG ========== #
        def import_csvfile_success_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 473 
                    window_h = 165
                    basic_window.title("Importing CSV File...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="The CSV File has been imported successfully!\nThe Content will Load!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=44)           
                    basic_btn_ok.place(x=198, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 490
                    window_h = 165
                    basic_window.title("Importando Archivo CSV...")                      
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="El Archivo CSV se ha Importado Correctamente!\nEl Contenido se Cargara!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=44)
                    basic_btn_ok.place(x=200, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: None)    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                basic_btn_ok.config(command=hide_importcsv_window) 
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== IMPORT CSV FILE ERROR MSG ========== #
        def import_csvfile_error_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 653 
                    window_h = 155
                    basic_window.title("Importing CSV File...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="The CSV File is Encrypted/Is Corrupt/Could Not be Found!\nThe Content of Inventory Data will be Not Loaded!", font=("Segoe UI", 12))
                    basic_lb1.place(x=150, y=34)
                    basic_btn_ok.place(x=288, y=105, width=80, height=37)
                elif lang_value == 2:
                    window_w = 718
                    window_h = 155
                    basic_window.title("Importando Archivo CSV...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="El Archivo CSV esta Encriptado/Esta Corrupto/No se Pudo Encontrar!\nNo Se Cargara el Contenido de los Datos del Inventario!", font=("Segoe UI", 12))
                    basic_lb1.place(x=150, y=34)
                    basic_btn_ok.place(x=316, y=105, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basic_btn_ok.config(command=hide_basic_window) 
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== IMPORT CSV FILE CANCELED MSG ========== #
        def import_csvfile_canceled_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 503
                    window_h = 155
                    basic_window.title("Importing CSV File...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="The User has Canceled the Import of the CSV File.\nNo Changes Have Been Made.", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=34)
                    basic_btn_ok.place(x=213, y=105, width=80, height=37)
                elif lang_value == 2:
                    window_w = 558
                    window_h = 155
                    basic_window.title("Importando Archivo CSV...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="El Usuario ha Cancelado la Importación del Archivo CSV.\nNo se han Hecho Cambios.", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=34)
                    basic_btn_ok.place(x=236, y=105, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basic_btn_ok.config(command=hide_basic_window) 
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== IMPORT CSV FILE ASK MSG ========== #
        def import_csvfile_ask():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                theme_value = themegroup.get()   
                if theme_value == 1:
                    style_elements.configure("import.TButton", foreground="white", focuscolor='white')
                    basic_btn_yes.config(style="import.TButton")
                elif theme_value == 2:
                    style_elements.configure("import.TButton", foreground="black", focuscolor='black')
                    basic_btn_yes.config(style="import.TButton")
                elif theme_value == 3:
                    if darkdetect.isDark():
                        style_elements.configure("import.TButton", foreground="white", focuscolor='white')
                        basic_btn_yes.config(style="import.TButton")
                    else:
                        style_elements.configure("import.TButton", foreground="black", focuscolor='black')
                        basic_btn_yes.config(style="import.TButton")
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 615
                    window_h = 165
                    basic_window.title("Import Inventory from CSV File?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Once the File has been Imported you CANNOT undo the Changes.\nMake Sure you Have a Copy of the File before Importing!\n\nNOTE: The CSV File must not be Encrypted or you will get an Error!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=12)
                    basic_btn_yes.config(text="📥  Import", command=import_csvfile)
                    basic_btn_yes.place(x=185, y=115, width=110, height=37)
                    basic_btn_no.config(text="❌  Cancel", command=hide_basic_window)
                    basic_btn_no.place(x=322, y=115, width=110, height=37)
                elif lang_value == 2:
                    window_w = 726
                    window_h = 165
                    basic_window.title("Importar Inventario desde Archivo CSV?")                 
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Una Vez que el Archivo se haya Importado NO SE PODRA deshacer los Cambios.\nAsegurece de Tener una Copia del Archivo antes de Importar!\n\nNOTA: el Archivo CSV no debe estar Encriptado o tendras un Error!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=12)
                    basic_btn_yes.config(text="📥  Importar", command=import_csvfile)
                    basic_btn_yes.place(x=238, y=115, width=110, height=37)
                    basic_btn_no.config(text="❌  Cancelar", command=hide_basic_window)
                    basic_btn_no.place(x=373, y=115, width=110, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== EXPORT CSV FILE SUCCESS MSG ========== #
        def export_csvfile_success_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                theme_value = themegroup.get()   
                if theme_value == 1:
                    show_csvfilelb.config(bg="#101010", fg="white")
                    show_csvfilelb.bind("<Enter>", lambda event: show_csvfilelb.config(fg="#CECECE"))
                    show_csvfilelb.bind("<Leave>", lambda event: show_csvfilelb.config(fg="white"))
                    style_elements.configure("export.TButton", foreground="white", focuscolor='white')
                    basic_btn_yes.config(style="export.TButton")
                elif theme_value == 2:
                    show_csvfilelb.config(bg="white", fg="black")
                    show_csvfilelb.bind("<Enter>", lambda event: show_csvfilelb.config(fg="#777777"))
                    show_csvfilelb.bind("<Leave>", lambda event: show_csvfilelb.config(fg="black"))
                    style_elements.configure("export.TButton", foreground="black", focuscolor='black')
                    basic_btn_yes.config(style="export.TButton")
                elif theme_value == 3:
                    if darkdetect.isDark():
                        show_csvfilelb.config(bg="#101010", fg="white")
                        show_csvfilelb.bind("<Enter>", lambda event: show_csvfilelb.config(fg="#CECECE"))
                        show_csvfilelb.bind("<Leave>", lambda event: show_csvfilelb.config(fg="white"))
                        style_elements.configure("export.TButton", foreground="white", focuscolor='white')
                        basic_btn_yes.config(style="export.TButton")
                    else:
                        show_csvfilelb.config(bg="white", fg="black")
                        show_csvfilelb.bind("<Enter>", lambda event: show_csvfilelb.config(fg="#777777"))
                        show_csvfilelb.bind("<Leave>", lambda event: show_csvfilelb.config(fg="black"))
                        style_elements.configure("export.TButton", foreground="black", focuscolor='black')
                        basic_btn_yes.config(style="export.TButton")
                show_csvfilelb.bind("<Button-1>", lambda event: show_csvfile())
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 500  
                    window_h = 165
                    basic_window.title("Exporting Content to CSV File...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="The CSV File has been Exported successfully!", font=("Segoe UI", 12))
                    basic_lb1.place(x=125, y=54)
                    show_csvfilelb.config(text="📂 Show File")
                    show_csvfilelb.place(x=390, y=134)
                    basic_btn_ok.place(x=213, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 520
                    window_h = 165
                    basic_window.title("Exportando Contenido al Archivo CSV...")                 
                    basic_imglb.place(x=25, y=30)
                    basic_lb1.config(justify="center", text="El Archivo CSV se ha Exportado Correctamente!", font=("Segoe UI", 12))
                    basic_lb1.place(x=135, y=54)
                    show_csvfilelb.config(text="📂 Mostrar Archivo")
                    show_csvfilelb.place(x=370, y=134)
                    basic_btn_ok.place(x=215, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/check.png"))
                basic_btn_ok.config(command=hide_basic_window) 
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== EXPORT CSV FILE ERROR MSG ========== #
        def export_csvfile_error_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 525 
                    window_h = 155
                    basic_window.title("Exporting Content to CSV File...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="The CSV File contains Non Valid Values or Is Corrupt!\nThe Content of Inventory Data will be Not Saved!", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=34)
                    basic_btn_ok.place(x=228, y=105, width=80, height=37)
                elif lang_value == 2:
                    window_w = 578
                    window_h = 155
                    basic_window.title("Exportando Contenido al Archivo CSV...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="El Archivo CSV contiene Valores No Validos o Esta Corrupto!\nNo Se Guardara el Contenido de los Datos del Inventario!", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=34)
                    basic_btn_ok.place(x=246, y=105, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basic_btn_ok.config(command=hide_basic_window) 
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== EXPORT CSV FILE CANCELED MSG ========== #
        def export_csvfile_canceled_msg():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 503
                    window_h = 155
                    basic_window.title("Exporting Content to CSV File...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="The User has Canceled the Export of the CSV File.\nNo Changes Have Been Made.", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=34)
                    basic_btn_ok.place(x=213, y=105, width=80, height=37)
                elif lang_value == 2:
                    window_w = 558
                    window_h = 155
                    basic_window.title("Exportando Contenido al Archivo CSV...")
                    basic_imglb.place(x=15, y=20)
                    basic_lb1.config(justify="center", text="El Usuario ha Cancelado la Exportación del Archivo CSV.\nNo se han Hecho Cambios.", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=34)
                    basic_btn_ok.place(x=236, y=105, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/error.png"))
                basic_btn_ok.config(command=hide_basic_window) 
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== EXPORT CSV FILE ASK MSG ========== #
        def export_csvfile_ask():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                theme_value = themegroup.get()   
                if theme_value == 1:
                    style_elements.configure("import.TButton", foreground="white", focuscolor='white')
                    basic_btn_yes.config(style="import.TButton")
                elif theme_value == 2:
                    style_elements.configure("import.TButton", foreground="black", focuscolor='black')
                    basic_btn_yes.config(style="import.TButton")
                elif theme_value == 3:
                    if darkdetect.isDark():
                        style_elements.configure("import.TButton", foreground="white", focuscolor='white')
                        basic_btn_yes.config(style="import.TButton")
                    else:
                        style_elements.configure("import.TButton", foreground="black", focuscolor='black')
                        basic_btn_yes.config(style="import.TButton")
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 615
                    window_h = 165
                    basic_window.title("Export Inventory to CSV File?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="WARNING: When you Export the CSV file it will be decrypted,\nso any program will be able to access it.", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=44)
                    basic_btn_yes.config(text="📤  Export", command=export_csvfile)
                    basic_btn_yes.place(x=185, y=115, width=110, height=37)
                    basic_btn_no.config(text="❌  Cancel", command=hide_basic_window)
                    basic_btn_no.place(x=322, y=115, width=110, height=37)
                elif lang_value == 2:
                    window_w = 726
                    window_h = 165
                    basic_window.title("Exportar Inventario en Archivo CSV?")                 
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="ADVERTENCIA: Al Exportar el Archivo CSV sera Desencriptado,\npor lo que cualquier Programa podra Acceder a el.", font=("Segoe UI", 12))
                    basic_lb1.place(x=155, y=44)
                    basic_btn_yes.config(text="📤  Exportar", command=export_csvfile)
                    basic_btn_yes.place(x=238, y=115, width=110, height=37)
                    basic_btn_no.config(text="❌  Cancelar", command=hide_basic_window)
                    basic_btn_no.place(x=373, y=115, width=110, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_basic_window())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()
        
        # ========== DELETE PROGRAM DATA SUCCESS MSG ========== #
        def cleardata_success_msg():
            try:
                dynamic_window.withdraw()
                settings_window.withdraw()
                basic_btn_cleardata.place_forget()
                password_cleardata.delete(0, tk.END)
                showhide_cleardata_pass_btn.place_forget()
                passwordlb_cleardata.place_forget()
                password_cleardata.place_forget()
                passwordcheck_cleardata.place_forget()
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 393
                    window_h = 165
                    basic_window.title("Deleting Program Data...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="All Program Data Has Been Deleted!\nThe Program will Close!", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=40)
                    basic_btn_ok.place(x=160, y=115, width=80, height=37)
                elif lang_value == 2:
                    window_w = 490
                    window_h = 165
                    basic_window.title("Borrando Datos del Programa...")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Se han Borrado todos los Datos del Programa!\nEl Programa se Cerrara!", font=("Segoe UI", 12))
                    basic_lb1.place(x=110, y=40)
                    basic_btn_ok.place(x=210, y=115, width=80, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: close())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()                  
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/info.png"))
                basic_btn_ok.config(command=close)
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()
        
        # ========== DELETE PROGRAM DATA ASK MSG ========== #
        def cleardata_ask():
            try:
                def validate_value_account(text):
                    pattern = re.compile(r"^[a-zA-Z0-9]+$")
                    if pattern.match(text) is not None:
                        return True and len(text) <= 20
                    elif text == "":
                        return True and len(text) <= 20
                    else:
                        return False
                def showpass_cleardata(show):
                    password_cleardata.config(show="")
                def hidepass_cleardata(hide):
                    password_cleardata.config(show="*")
                def showpassbutton_cleardata(show):
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        showhide_cleardata_pass_btn.place(x=486, y=75, width=33, height=31)
                    elif lang_value == 2:
                        showhide_cleardata_pass_btn.place(x=544, y=75, width=33, height=31)
                def hidepassbutton_cleardata(hide):
                    showhide_cleardata_pass_btn.place_forget()
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                languagedata = set([row[0]for row in settingdata])
                if "language=eng_lang" in languagedata:
                    eng_langrb.invoke()
                elif "language=esp_lang" in languagedata:
                    esp_langrb.invoke()
                themedata = set([row[0]for row in settingdata])
                if "theme=dark_theme" in themedata:                     
                    darkthemerb.invoke()
                elif "theme=light_theme" in themedata:
                    lightthemerb.invoke()
                elif "theme=system_theme" in themedata:
                    systemthemerb.invoke()
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                theme_value = themegroup.get()   
                if theme_value == 1:
                    style_elements.configure("cleardata.TButton", foreground="#CE0000", focuscolor='#CE0000')
                    style_elements.map('cleardata.TButton', foreground=[("disabled", "#900000")])
                    basic_btn_cleardata.config(style="cleardata.TButton")
                elif theme_value == 2:
                    style_elements.configure("cleardata.TButton", foreground="#CE0000", focuscolor='#CE0000')
                    style_elements.map('cleardata.TButton', foreground=[("disabled", "#FF6060")])
                    basic_btn_cleardata.config(style="cleardata.TButton")
                elif theme_value == 3:
                    if darkdetect.isDark():
                        style_elements.configure("cleardata.TButton", foreground="#CE0000", focuscolor='#CE0000')
                        style_elements.map('cleardata.TButton', foreground=[("disabled", "#900000")])
                        basic_btn_cleardata.config(style="cleardata.TButton")
                    else:
                        style_elements.configure("cleardata.TButton", foreground="#CE0000", focuscolor='#CE0000')
                        style_elements.map('cleardata.TButton', foreground=[("disabled", "#FF6060")])
                        basic_btn_cleardata.config(style="cleardata.TButton")
                basic_btn_cleardata.config(state="disabled", cursor="arrow") 
                password_cleardata.bind("<KeyRelease>", lambda event: enable_cleardata())
                showhide_cleardata_pass_btn.bind("<ButtonPress-1>", showpass_cleardata)
                showhide_cleardata_pass_btn.bind("<ButtonRelease-1>", hidepass_cleardata)
                password_cleardata.config(validate="key", validatecommand=(dynamic_window.register(validate_value_account), "%P"), font=("Segoe UI", 12))
                password_cleardata.bind("<FocusIn>", showpassbutton_cleardata)
                password_cleardata.bind("<FocusOut>", hidepassbutton_cleardata)
                password_cleardata.bind('<Control-c>', lambda _:'break')
                password_cleardata.bind('<Control-v>', lambda _:'break')
                lang_value = languagegroup.get()
                if lang_value == 1:
                    window_w = 615
                    window_h = 200
                    basic_window.title("Delete Program Data?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="All Program Data will be Deleted, including the Inventory.\nWARNING: This action is UNRREVERSIBLE!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=12)
                    passwordlb_cleardata.config(justify="left", text="Password to Confirm:", font=("Segoe UI", 12))                    
                    passwordlb_cleardata.place(x=140, y=75, height=30)
                    showhide_cleardata_pass_btn.config(text="👁️")
                    password_cleardata.place(x=295, y=75, height=30)
                    basic_btn_cleardata.config(text="✨  Delete Data", command=cleardata_settings)
                    basic_btn_cleardata.place(x=165, y=150, width=140, height=37)
                    basic_btn_no.config(text="❌  Cancel", command=hide_cleardata_settings)
                    basic_btn_no.place(x=322, y=150, width=140, height=37)
                elif lang_value == 2:
                    window_w = 726
                    window_h = 200
                    basic_window.title("Borrar Datos del Programa?")                 
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="Se Borraran todos los Datos del Programa incluyendo el Inventario.\nADVERTENCIA: Esta accion es INRREVERSIBLE!", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=12)
                    passwordlb_cleardata.config(justify="left", text="Contraseña para Confirmar:", font=("Segoe UI", 12))
                    passwordlb_cleardata.place(x=153, y=75, height=30)
                    showhide_cleardata_pass_btn.config(text="👁️")
                    password_cleardata.place(x=353, y=75, height=30)
                    basic_btn_cleardata.config(text="✨  Borrar Datos", command=cleardata_settings)
                    basic_btn_cleardata.place(x=198, y=150, width=140, height=37)
                    basic_btn_no.config(text="❌ Cancelar", command=hide_cleardata_settings)
                    basic_btn_no.place(x=363, y=150, width=140, height=37)
                window_width = round(window_w_total/2-window_w/2)
                window_height = round(window_h_total/2-window_h/2-30)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(window_width)+"+"+str(window_height))
                off_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_cleardata_settings())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/warning.png"))
                basic_window.transient(dynamic_window)
                basic_window.deiconify()
                password_cleardata.focus()
                dynamic_window.attributes('-disabled', 1)
                settings_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()
            except (ValueError, FileNotFoundError, IndexError):
                error_window()
                datafile_error_msg()

         # ============================================== LOAD MISC FUNCTIONS ============================================== #
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
            addrb.config(cursor="arrow")
            editrb.config(cursor="arrow")
            deleterb.config(cursor="arrow")
            settings_btn.config(cursor="arrow")
            username_entry.config(cursor="arrow")
            password_entry.config(cursor="arrow")
            loginbtn.config(cursor="arrow")
            changeaccountlogin_btn.config(cursor="arrow")

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
            addrb.config(cursor="hand2")
            editrb.config(cursor="hand2")
            deleterb.config(cursor="hand2")
            settings_btn.config(cursor="hand2")
            username_entry.config(cursor="xterm")
            password_entry.config(cursor="xterm")
            loginbtn.config(cursor="hand2")
            changeaccountlogin_btn.config(cursor="hand2")

        def signout():
            try:
                dynamic_window.attributes('-disabled', 0)
                dynamic_window.withdraw()
                hide_basic_window()
                separator1.place_forget()
                separator3.place_forget()
                separator2.place_forget()
                main_mbtn.place_forget()
                tips_mbtn.place_forget()
                about_mbtn.place_forget()
                signout_btn.place_forget()
                idlb.place_forget()
                brandlb.place_forget()
                modellb.place_forget()
                colorlb.place_forget()
                datelb.place_forget()
                username_logged_lb.place_forget()
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
                device_imglb.place_forget()
                addrb.place_forget()
                editrb.place_forget()
                deleterb.place_forget()
                show_csvfilelb.place_forget()
                setting_btn_apply.config(command=apply_settings_login)
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)                   
                dynamic_window.protocol("WM_DELETE_WINDOW", lambda: close())
                dynamic_window.resizable(width=False, height=False)
                login_window_place()
                dynamic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))
                ltips_mbtn.place(x=0, y=0, height=33, width=130)
                about_mbtn.place(x=130, height=33, width=130)
                lmbar_separator.place(x=0, y=32, width=550, height=1)
                loginprofile_imglb.place(x=220, y=35)
                welcome_login.place(y=140)
                username_label.place(x=135, y=185)
                password_label.place(x=135, y=250)
                changeaccountlogin_btn.place(x=6, y=392)
                lang_value = languagegroup.get()
                if lang_value == 1:
                    eng_lang_login()
                    resetaccount_btn.place(x=87, y=213, width=242, height=35)
                elif lang_value == 2:
                    esp_lang_login()
                    resetaccount_btn.place(x=40, y=213, width=341, height=35)
                username_entry.place(x=136, y=210, height=30)
                password_entry.place(x=136, y=275, height=30)
                loginbtn.place(y=320)
                settings_btn.place(x=513, y=0, width=37)
                basic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))
                dynamic_window.deiconify()
                dynamic_window.focus_force()
                username_entry.focus()
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========================================================================================================= #
        def main_window(event=None):
            try:
                global username_entry, password_entry, dynamic_window, info_bf, info_af, import_csvfile, export_csvfile, save_txtfile, show_csvfile, show_txtfile
                username_get = username_entry.get()
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                decrypt_data = crypt_key.decrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(decrypt_data)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "r") as accountfile:
                    accountreader = csv.reader(accountfile, delimiter=",")
                    accountdata = list(accountreader)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                    account_info = accountfile.read()
                encrypt_data = crypt_key.encrypt(account_info)
                with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                    accountfile.write(encrypt_data)
                if accountdata[0][0] == username_get.lower() and accountdata[0][1] == password_entry.get():
                    dynamic_window.withdraw()
                    ltips_mbtn.place_forget()
                    lmbar_separator.place_forget()
                    loginprofile_imglb.place_forget()
                    welcome_login.place_forget()
                    username_label.place_forget()
                    password_label.place_forget()
                    changeaccountlogin_btn.place_forget()
                    resetaccount_btn.place_forget()
                    username_entry.place_forget()
                    password_entry.place_forget()
                    loginbtn.place_forget()
                    showhide_pass_btn.place_forget()
                    settings_btn.place_forget()
                    setting_btn_apply.config(command=apply_settings_main)
                    lang_value = languagegroup.get()
                    if lang_value == 1:
                        eng_lang_mainwindow()
                    elif lang_value == 2:
                        esp_lang_mainwindow()

                    # ============================================== LOAD MAIN WINDOW FUNCTIONS ============================================== #  
                    def mainmenubar_mw():
                        main_mbtn.place(x=0, y=0, height=33, width=130)
                        tips_mbtn.place(y=0, height=33, width=130)
                        about_mbtn.place(y=0, height=33, width=130)
                        signout_btn.place(y=0, height=33, width=141)

                    def labels_mw():
                        brandlb.place(x=388, y=403)
                        modellb.place(x=388, y=443)
                        colorlb.place(x=388, y=483)
                        inventorylb.place(x=18, y=116)
                        searchlb.place(x=596, y=114)
                        username_logged_lb.place(x=550, y=3)

                    def separators_mw():
                        separator1.place(x=0, y=32, width=924, height=1)
                        separator2.place(x=0, y=108, width=924, height=1)
                        separator3.place(x=0, y=385, width=924, height=1)
            
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
                        addbtn.place(x=763, y=399, width=139, height=31)
                        clearbtn.place(x=763, y=439, width=139, height=31)
                        changeaccount_btn.place(x=849, y=0, width=37, height=33)
                        settings_btn.place(x=886, y=0, width=37, height=33)
 
                    def search_byid():
                        try:
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                inventory_info = inventoryfile.read()
                            decrypt_data = crypt_key.decrypt(inventory_info)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                inventoryfile.write(decrypt_data)
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
                                    table_scrollbar.place(x=885, y=153, height=225, width=17)
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
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                inventory_info = inventoryfile.read()
                            encrypt_data = crypt_key.encrypt(inventory_info)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                inventoryfile.write(encrypt_data)
                        except cryptography.fernet.InvalidToken:
                            error_window()
                            datafile_error_msg() 
                            
                    def optionselected_mode(action):
                        global rb_selected
                        rb_selected = action.widget
                        if rb_selected.cget("value") == 1:
                            try:
                                addrb.invoke()
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
                                addbtn.place(x=763, y=399, width=139, height=31)
                                clearbtn.place(x=763, y=439, width=139, height=31)
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Search by ID...")
                                elif lang_value == 2:
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Buscar por ID...")
                                idlb.place_forget()
                                id_entry.place_forget()
                                datelb.place_forget()
                                date_entry.place_forget()
                                brandlb.config(fg="#00C300")
                                modellb.config(fg="#00C300")
                                colorlb.config(fg="#00C300")
                                brand_entry.config(cursor= "xterm", highlightcolor="#00C300", highlightbackground="#00C300", highlightthickness=2)
                                model_entry.config(cursor= "xterm", highlightcolor="#00C300", highlightbackground="#00C300", highlightthickness=2)
                                color_entry.config(cursor= "xterm", highlightcolor="#00C300", highlightbackground="#00C300", highlightthickness=2) 
                                brand_entry.focus()
                                brand_entry.bind("<Return>", add_inventory)
                                model_entry.bind("<Return>", add_inventory)
                                color_entry.bind("<Return>", add_inventory)
                                brandlb.place(x=388, y=403)
                                modellb.place(x=388, y=443)
                                colorlb.place(x=388, y=483)
                                brand_entry.place(x=457, y=400, height=30)
                                model_entry.place(x=457, y=439, height=30)
                                color_entry.place(x=457, y=479, height=30)
                                reflesh_inventory()
                            except (ValueError, FileNotFoundError, IndexError):
                                error_window()
                                datafile_error_msg()
                            except TclError:
                                error_window()
                                loadfile_error_msg()

                        elif rb_selected.cget("value") == 2:
                            try:
                                editrb.invoke()
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
                                checkbtn.place(x=763, y=399, width=139, height=31)
                                clearbtn.place(x=763, y=439, width=139, height=31)
                                editbtn.place_forget()
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Search by ID...")
                                elif lang_value == 2:
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Buscar por ID...")
                                theme_value = themegroup.get()
                                if theme_value == 1:
                                    id_entry.config(fg="white", insertbackground="white", highlightcolor="#0078FF", highlightbackground="#0078FF", highlightthickness=2, cursor="xterm", state="normal")
                                    brand_entry.config(background="#191919", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                    model_entry.config(background="#191919", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                    color_entry.config(background="#191919", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                    date_entry.config(background="#191919", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                elif theme_value == 2:
                                    id_entry.config(fg="black", insertbackground="black", highlightcolor="#0078FF", highlightbackground="#0078FF", highlightthickness=2, cursor="xterm", state="normal")
                                    brand_entry.config(background="#F9F9F9", highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, state="disabled")
                                    model_entry.config(background="#F9F9F9", highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, state="disabled")
                                    color_entry.config(background="#F9F9F9", highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, state="disabled")
                                    date_entry.config(background="#F9F9F9", highlightcolor="#C9C9C9", highlightbackground="#C9C9C9", highlightthickness=2, state="disabled")
                                elif theme_value == 3:
                                    if darkdetect.isDark():
                                        id_entry.config(fg="white", insertbackground="white", highlightcolor="#0078FF", highlightbackground="#0078FF", highlightthickness=2, cursor="xterm", state="normal")
                                        brand_entry.config(background="#191919", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                        model_entry.config(background="#191919", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                        color_entry.config(background="#191919", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                        date_entry.config(background="#191919", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, state="disabled")
                                    else:
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
                                id_entry.bind("<Return>", edit_check_inventory)
                                brandlb.place(x=388, y=443)
                                modellb.place(x=388, y=483)
                                colorlb.place(x=388, y=523)
                                datelb.place(x=388, y=563)
                                brand_entry.place(x=457, y=439, height=30)
                                model_entry.place(x=457, y=479, height=30)
                                color_entry.place(x=457, y=519, height=30)
                                date_entry.place(x=457, y=559, height=30)
                                reflesh_inventory()
                            except (ValueError, FileNotFoundError, IndexError):
                                error_window()
                                datafile_error_msg()
                            except TclError:
                                error_window()
                                loadfile_error_msg()

                        elif rb_selected.cget("value") == 3:
                            try:
                                deleterb.invoke()
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
                                deletebtn.place(x=763, y=399, width=139, height=31)
                                clearbtn.place(x=763, y=439, width=139, height=31)                                
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
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Search by ID...")
                                elif lang_value == 2:
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Buscar por ID...")
                                idlb.place(x=388, y=403)
                                id_entry.place(x=457, y=400, height=30)
                                idlb.config(fg="#FE2727")
                                id_entry.config(fg="#FE2727", insertbackground="#FE2727", highlightcolor="#FE2727", highlightbackground="#FE2727", highlightthickness=2, cursor="xterm", state="normal")
                                clear_mw()
                                id_entry.focus()
                                id_entry.bind("<Return>", del_inventory)
                                reflesh_inventory()
                            except (ValueError, FileNotFoundError, IndexError):
                                error_window()
                                datafile_error_msg()
                            except TclError:
                                error_window()
                                loadfile_error_msg()
                    
                    def add_inventory(event=None):
                        global add_no
                        id_get = id_entry.get()
                        brand_get = brand_entry.get()
                        model_get = model_entry.get()
                        color_get = color_entry.get()
                        id_upper = id_get.upper()
                        brand_upper = brand_get.upper()
                        model_upper = model_get.upper()
                        color_upper = color_get.upper()
                        info_add()
                        def add_no():
                            dynamic_window.attributes('-disabled', 0)
                            info_bf_lb.place_forget()
                            id_inf.place_forget()
                            brand_bf.place_forget()
                            model_bf.place_forget()
                            color_bf.place_forget()
                            date_bf.place_forget()
                            infobf_frame.place_forget()
                            restore_elements()
                            basic_window.withdraw()
                            basic_btn_yes.place_forget()
                            basic_btn_no.place_forget()
                            basic_window.grab_release()
                            basic_window.transient(None)
                        def add_yes():
                            try:
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                    inventory_info = inventoryfile.read()
                                decrypt_data = crypt_key.decrypt(inventory_info)
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                    inventoryfile.write(decrypt_data)
                                date_os = datetime.datetime.now()
                                date_format = date_os.strftime("%d-%m-%Y %I:%M %p") 
                                dynamic_window.attributes('-disabled', 0)
                                basic_window.withdraw()
                                info_bf_lb.place_forget()
                                id_inf.place_forget()
                                brand_bf.place_forget()
                                model_bf.place_forget()
                                color_bf.place_forget()
                                date_bf.place_forget()
                                infobf_frame.place_forget()
                                basic_btn_yes.place_forget()
                                basic_btn_no.place_forget() 
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
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                    inventory_info = inventoryfile.read()
                                encrypt_data = crypt_key.encrypt(inventory_info)
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                    inventoryfile.write(encrypt_data)
                                clear_mw()         
                                lang_value = languagegroup.get()
                                if lang_value == 1:
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Search by ID...")
                                elif lang_value == 2:
                                    search_entry.delete(0, tk.END)
                                    search_entry.insert(0, "Buscar por ID...")
                                reflesh_inventory() 
                                add_prod_save()
                            except (ValueError, FileNotFoundError, IndexError, cryptography.fernet.InvalidToken):
                                error_window()
                                datafile_error_msg()
                            except TclError:
                                error_window()
                                loadfile_error_msg()   
                        basic_btn_yes.config(command=add_yes)
                        basic_btn_no.config(command=add_no)    
                        if "" in id_upper and brand_upper and model_upper and color_upper:
                            basic_btn_ok.place_forget()
                            add_prod_ask() 
                        else:
                            add_prod_empty()

                    def edit_check_inventory(event=None):
                        try:
                            brand_entry.bind("<Return>", edit_inventory)
                            model_entry.bind("<Return>", edit_inventory)
                            color_entry.bind("<Return>", edit_inventory)
                            date_entry.bind("<Return>", edit_inventory)
                            id_get = id_entry.get()
                            id_upper = id_get.upper()
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                inventory_info = inventoryfile.read()
                            decrypt_data = crypt_key.decrypt(inventory_info)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                inventoryfile.write(decrypt_data)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r", newline="") as file:
                                    reader = csv.reader(file)
                                    data = list(reader)
                            ids = set([row[0].upper() for row in data])
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                inventory_info = inventoryfile.read()
                            encrypt_data = crypt_key.encrypt(inventory_info)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                inventoryfile.write(encrypt_data)
                            if not id_upper in ids:
                                if id_upper == "":
                                    edit_prod_empty()
                                else:
                                    edit_prod_notfound()
                            elif id_upper in ids:
                                clearbtn.place_forget()
                                cancelbtn.place(x=763, y=439, width=139, height=31)
                                editbtn.place(x=763, y=399, width=139, height=31)
                                theme_value = themegroup.get()
                                if theme_value == 1:
                                    brandlb.config(fg="#0078FF", state="normal")
                                    modellb.config(fg="#0078FF", state="normal")
                                    colorlb.config(fg="#0078FF", state="normal")
                                    datelb.config(fg="#0078FF", state="normal")
                                    id_entry.config(disabledforeground="#0078FF", disabledbackground="#101010", cursor="arrow", state="disabled")
                                    brand_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                                    model_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                                    color_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                                    date_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
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
                                elif theme_value == 3:
                                    if darkdetect.isDark():
                                        brandlb.config(fg="#0078FF", state="normal")
                                        modellb.config(fg="#0078FF", state="normal")
                                        colorlb.config(fg="#0078FF", state="normal")
                                        datelb.config(fg="#0078FF", state="normal")
                                        id_entry.config(disabledforeground="#0078FF", disabledbackground="#101010", cursor="arrow", state="disabled")
                                        brand_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                                        model_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                                        color_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                                        date_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                                    else:
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
                        except cryptography.fernet.InvalidToken:
                            error_window()
                            datafile_error_msg()  
                    
                    def edit_cancel_inventory():
                        brand_entry.unbind("<Return>")
                        model_entry.unbind("<Return>")
                        color_entry.unbind("<Return>")
                        date_entry.unbind("<Return>")
                        clear_mw()
                        checkbtn.place(x=763, y=399, width=139, height=31)
                        clearbtn.place(x=763, y=439, width=139, height=31)
                        editbtn.place_forget()
                        cancelbtn.place_forget()
                        theme_value = themegroup.get()
                        if theme_value == 1:
                            brandlb.config(fg="#0078FF", state="disabled")
                            modellb.config(fg="#0078FF", state="disabled")
                            colorlb.config(fg="#0078FF", state="disabled")
                            datelb.config(fg="#0078FF", state="disabled")
                            id_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
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
                        elif theme_value == 3:
                            if darkdetect.isDark():
                                brandlb.config(fg="#0078FF", state="disabled")
                                modellb.config(fg="#0078FF", state="disabled")
                                colorlb.config(fg="#0078FF", state="disabled")
                                datelb.config(fg="#0078FF", state="disabled")
                                id_entry.config(background="#191919", highlightcolor="#0078FF", highlightbackground="#0078FF", foreground="white", insertbackground="white", highlightthickness=2, cursor="xterm", state="normal")
                                brand_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, cursor="arrow", state="disabled")
                                model_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, cursor="arrow", state="disabled")
                                color_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, cursor="arrow", state="disabled")
                                date_entry.config(highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2, cursor="arrow", state="disabled")
                            else:
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

                    def edit_inventory(event=None):
                        try:
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
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                    inventory_info = inventoryfile.read()
                                decrypt_data = crypt_key.decrypt(inventory_info)
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                    inventoryfile.write(decrypt_data)
                                info_bf()
                                info_af()
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r", newline="") as file:
                                    reader = csv.reader(file)
                                    data = list(reader)
                                ids = set([row[0].upper() for row in data])
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                    inventory_info = inventoryfile.read()
                                encrypt_data = crypt_key.encrypt(inventory_info)
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                    inventoryfile.write(encrypt_data)
                                if id_upper in ids:                     
                                    basic_btn_ok.place_forget()
                                    edit_prod_ask()
                                def edit_yes():
                                    try:
                                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                            inventory_info = inventoryfile.read()
                                        decrypt_data = crypt_key.decrypt(inventory_info)
                                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                            inventoryfile.write(decrypt_data)
                                        dynamic_window.attributes('-disabled', 0)
                                        basic_window.withdraw()
                                        basic_btn_yes.place_forget()
                                        basic_btn_no.place_forget()
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
                                        infobf_frame.place_forget()
                                        infoaf_frame.place_forget()
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
                                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                            inventory_info = inventoryfile.read()
                                        encrypt_data = crypt_key.encrypt(inventory_info)
                                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                            inventoryfile.write(encrypt_data)
                                        clear_mw()
                                        edit_cancel_inventory()
                                        id_entry.delete(0, tk.END)
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            search_entry.delete(0, tk.END)
                                            search_entry.insert(0, "Search by ID...")
                                        elif lang_value == 2:
                                            search_entry.delete(0, tk.END)
                                            search_entry.insert(0, "Buscar por ID...")
                                        reflesh_inventory()
                                        edit_prod_save()
                                    except (ValueError, FileNotFoundError, IndexError, cryptography.fernet.InvalidToken):
                                        error_window()
                                        datafile_error_msg()
                                    except TclError:
                                        error_window()
                                        loadfile_error_msg() 
                                def edit_no():
                                    dynamic_window.attributes('-disabled', 0)
                                    restore_elements()
                                    basic_window.withdraw()
                                    basic_btn_yes.place_forget()
                                    basic_btn_no.place_forget()
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
                                    infobf_frame.place_forget()
                                    infoaf_frame.place_forget()
                                    basic_window.grab_release()
                                    basic_window.transient(None)
                                basic_btn_yes.config(command=edit_yes)
                                basic_btn_no.config(command=edit_no)  
                            elif brand_upper == "" or model_upper == "" or color_upper == "" or date_upper == "":
                                edit_prod_empty() 
                        except cryptography.fernet.InvalidToken:
                            error_window()
                            datafile_error_msg()  

                    def info_add():
                        lang_value = languagegroup.get()
                        if lang_value == 1:
                            brand_bf.config(text="Brand:\n"+str(brand_entry.get().upper()))
                            model_bf.config(text="Model:\n"+str(model_entry.get().upper()))
                            color_bf.config(text="Color:\n"+str(color_entry.get().upper()))
                        elif lang_value == 2:
                            brand_bf.config(text="Marca:\n"+str(brand_entry.get().upper()))
                            model_bf.config(text="Modelo:\n"+str(model_entry.get().upper()))
                            color_bf.config(text="Color:\n"+str(color_entry.get().upper()))

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
                        brand_get = brand_entry.get()
                        brand_upper = brand_get.upper()
                        model_get = model_entry.get()
                        model_upper = model_get.upper()
                        color_get = color_entry.get()
                        color_upper = color_get.upper()
                        date_get = date_entry.get()
                        date_upper = date_get.upper()
                        lang_value = languagegroup.get()
                        if lang_value == 1:
                            brand_af.config(text="Brand:\n"+str(brand_upper))
                            model_af.config(text="Model:\n"+str(model_upper))
                            color_af.config(text="Color:\n"+str(color_upper))
                            date_af.config(text="Registered Date:\n"+str(date_upper))
                            theme_value = themegroup.get()
                            if brand_bf.cget("text") != brand_af.cget("text"):
                                brand_af.config(fg="#0078FF")
                            else:
                                if theme_value == 1:
                                    brand_af.config(fg="white")
                                elif theme_value == 2:
                                    brand_af.config(fg="black")
                                elif theme_value == 3:
                                    if darkdetect.isDark():
                                        brand_af.config(fg="white")
                                    else:
                                        brand_af.config(fg="black")
                            if model_bf.cget("text") != model_af.cget("text"):
                                model_af.config(fg="#0078FF")
                            else:
                                if theme_value == 1:
                                    model_af.config(fg="white")
                                elif theme_value == 2:
                                    model_af.config(fg="black")
                                elif theme_value == 3:
                                    if darkdetect.isDark():
                                        model_af.config(fg="white")
                                    else:
                                        model_af.config(fg="black")
                            if color_bf.cget("text") != color_af.cget("text"):
                                color_af.config(fg="#0078FF")
                            else:
                                if theme_value == 1:
                                    color_af.config(fg="white")
                                elif theme_value == 2:
                                    color_af.config(fg="black")
                                elif theme_value == 3:
                                    if darkdetect.isDark():
                                        color_af.config(fg="white")
                                    else:
                                        color_af.config(fg="black")
                            if date_bf.cget("text") != date_af.cget("text"):
                                date_af.config(fg="#0078FF")
                            else:
                                if theme_value == 1:
                                    date_af.config(fg="white")
                                elif theme_value == 2:
                                    date_af.config(fg="black")
                                elif theme_value == 3:
                                    if darkdetect.isDark():
                                        date_af.config(fg="white")
                                    else:
                                        date_af.config(fg="black")
                        elif lang_value == 2:
                            brand_af.config(text="Marca:\n"+str(brand_upper))
                            model_af.config(text="Modelo:\n"+str(model_upper))
                            color_af.config(text="Color:\n"+str(color_upper))
                            date_af.config(text="Fecha de Registro:\n"+str(date_upper))
                            theme_value = themegroup.get()
                            if brand_bf.cget("text") != brand_af.cget("text"):
                                brand_af.config(fg="#0078FF")
                            else:
                                if theme_value == 1:
                                    brand_af.config(fg="white")
                                elif theme_value == 2:
                                    brand_af.config(fg="black")
                                elif theme_value == 3:
                                    if darkdetect.isDark():
                                        brand_af.config(fg="white")
                                    else:
                                        brand_af.config(fg="black")
                            if model_bf.cget("text") != model_af.cget("text"):
                                model_af.config(fg="#0078FF")
                            else:
                                if theme_value == 1:
                                    model_af.config(fg="white")
                                elif theme_value == 2:
                                    model_af.config(fg="black")
                                elif theme_value == 3:
                                    if darkdetect.isDark():
                                        model_af.config(fg="white")
                                    else:
                                        model_af.config(fg="black")
                            if color_bf.cget("text") != color_af.cget("text"):
                                color_af.config(fg="#0078FF")
                            else:
                                if theme_value == 1:
                                    color_af.config(fg="white")
                                elif theme_value == 2:
                                    color_af.config(fg="black")
                                elif theme_value == 3:
                                    if darkdetect.isDark():
                                        color_af.config(fg="white")
                                    else:
                                        color_af.config(fg="black")
                            if date_bf.cget("text") != date_af.cget("text"):
                                date_af.config(fg="#0078FF")
                            else:
                                if theme_value == 1:
                                    date_af.config(fg="white")
                                elif theme_value == 2:
                                    date_af.config(fg="black")
                                elif theme_value == 3:
                                    if darkdetect.isDark():
                                        date_af.config(fg="white")
                                    else:
                                        date_af.config(fg="black")

                    def del_inventory(event=None):
                        try:
                            global del_no
                            id_get = id_entry.get()
                            id_upper = id_get.upper()
                            if "" in id_upper:
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                    inventory_info = inventoryfile.read()
                                decrypt_data = crypt_key.decrypt(inventory_info)
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                    inventoryfile.write(decrypt_data)
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r", newline="") as file:
                                    reader = csv.reader(file)
                                    data = list(reader)
                                ids = set([row[0].upper() for row in data])
                                info_bf()
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                    inventory_info = inventoryfile.read()
                                encrypt_data = crypt_key.encrypt(inventory_info)
                                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                    inventoryfile.write(encrypt_data)
                                if id_upper in ids:                     
                                    basic_btn_ok.place_forget()
                                    delete_prod_ask()
                                elif not id_upper in ids:
                                    if id_upper == "":
                                        delete_prod_empty()
                                    else:
                                        delete_prod_notfound()
                                def del_yes():
                                    try:
                                        info_bf_lb.place_forget()
                                        id_inf.place_forget()
                                        brand_bf.place_forget()
                                        model_bf.place_forget()
                                        color_bf.place_forget()
                                        date_bf.place_forget()
                                        infobf_frame.place_forget()
                                        dynamic_window.attributes('-disabled', 0)
                                        basic_window.withdraw()
                                        basic_btn_yes.place_forget()
                                        basic_btn_no.place_forget() 
                                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                            inventory_info = inventoryfile.read()
                                        decrypt_data = crypt_key.decrypt(inventory_info)
                                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                            inventoryfile.write(decrypt_data)
                                        for row in data:
                                            if row[0].upper() == id_upper:
                                                data.remove(row)
                                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "w", newline="") as file:
                                            writer = csv.writer(file)
                                            writer.writerows(data)
                                            file.seek(0, 2)
                                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                            inventory_info = inventoryfile.read()
                                        encrypt_data = crypt_key.encrypt(inventory_info)
                                        with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                            inventoryfile.write(encrypt_data)
                                        clear_mw()
                                        reflesh_inventory()
                                        lang_value = languagegroup.get()
                                        if lang_value == 1:
                                            search_entry.delete(0, tk.END)
                                            search_entry.insert(0, "Search by ID...")                            
                                        elif lang_value == 2:
                                            search_entry.delete(0, tk.END)
                                            search_entry.insert(0, "Buscar por ID...")
                                        delete_prod_del()
                                    except (ValueError, FileNotFoundError, IndexError, cryptography.fernet.InvalidToken):
                                        error_window()
                                        datafile_error_msg()
                                    except TclError:
                                        error_window()
                                        loadfile_error_msg() 
                                def del_no():
                                    dynamic_window.attributes('-disabled', 0)
                                    info_bf_lb.place_forget()
                                    id_inf.place_forget()
                                    brand_bf.place_forget()
                                    model_bf.place_forget()
                                    color_bf.place_forget()
                                    date_bf.place_forget()
                                    infobf_frame.place_forget()
                                    restore_elements()
                                    basic_window.withdraw()
                                    basic_btn_yes.place_forget()
                                    basic_btn_no.place_forget()
                                    basic_window.grab_release()
                                    basic_window.transient(None)
                                basic_btn_yes.config(command=del_yes)
                                basic_btn_no.config(command=del_no) 
                        except cryptography.fernet.InvalidToken:
                            error_window()
                            datafile_error_msg() 
                
                    def showdatafolder():
                        if not os.path.exists(os.path.join(os.path.dirname(__file__), "Data")):   
                            os.makedirs(os.path.join(os.path.dirname(__file__), "Data"))
                        os.startfile(os.path.join(os.path.dirname(__file__), "Data"))
                    
                    def show_txtfile():
                        os.startfile(os.path.dirname(save_txt))
                        hide_basic_window()

                    def show_csvfile():
                        os.startfile(os.path.dirname(export_csv))
                        hide_basic_window()

                    def save_txtfile():
                        global save_txt
                        try:
                            dynamic_window.attributes('-disabled', 0)
                            basic_window.withdraw()
                            hide_basic_window()
                            lang_value = languagegroup.get()
                            if lang_value == 1:
                                save_txt = filedialog.asksaveasfilename(title="Save to Text File...", parent=dynamic_window, defaultextension=".txt", filetypes=(("Text File", "*.txt"),))
                            elif lang_value == 2:
                                save_txt = filedialog.asksaveasfilename(title="Guardar a Archivo de Texto...", parent=dynamic_window, defaultextension=".txt", filetypes=(("Archivo de Texto", "*.txt"),))
                            if not save_txt:
                                hide_basic_window()
                                return save_txtfile_canceled_msg()
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                inventory_info = inventoryfile.read()
                            decrypt_data = crypt_key.decrypt(inventory_info)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                inventoryfile.write(decrypt_data)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "r", newline="") as file:
                                reader = csv.reader(file)
                                data = list(reader)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                inventory_info = inventoryfile.read()
                            encrypt_data = crypt_key.encrypt(inventory_info)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                inventoryfile.write(encrypt_data)
                            if lang_value == 1:
                                with open(os.path.join(os.path.dirname(__file__), save_txt), 'w') as save_inventory:
                                    save_inventory.write('ID            Brand                 Model                                  Color                  Registered Date\n-------------------------------------------------------------------------------------------------------------------------\n')
                                    for row in data:
                                        save_inventory.write('{:<10}    {:<15}       {:<28}           {:<18}     {:<20}\n'.format(row[0], row[1], row[2], row[3], row[4]))
                            elif lang_value == 2:
                                with open(os.path.join(os.path.dirname(__file__), save_txt), 'w') as save_inventory:
                                    save_inventory.write('ID            Marca                 Modelo                                 Color                  Fecha de Registro\n-------------------------------------------------------------------------------------------------------------------------\n')
                                    for row in data:
                                        save_inventory.write('{:<10}    {:<15}       {:<28}           {:<18}     {:<20}\n'.format(row[0], row[1], row[2], row[3], row[4]))
                            save_txtfile_success_msg()
                        except (UnicodeDecodeError, ValueError, FileNotFoundError, IndexError, cryptography.fernet.InvalidToken):
                            hide_basic_window()
                            save_txtfile_error_msg()
                    
                    def import_csvfile():
                        try:
                            dynamic_window.attributes('-disabled', 0)
                            basic_window.withdraw()
                            lang_value = languagegroup.get()
                            if lang_value == 1:
                                import_csv = filedialog.askopenfilename(title="Import CSV File", parent=dynamic_window, filetypes=(("CSV File", "*.csv"),))    
                                if not import_csv:
                                    hide_basic_window()
                                    return import_csvfile_canceled_msg() 
                            elif lang_value == 2:
                                import_csv = filedialog.askopenfilename(title="Importar Archivo CSV", parent=dynamic_window, filetypes=(("Archivo CSV", "*.csv"),))
                                if not import_csv:
                                    hide_basic_window()
                                    return import_csvfile_canceled_msg()
                            with open(os.path.join(os.path.dirname(__file__), import_csv), "r") as refleshfile:
                                data = refleshfile.readlines()
                                for row in data:
                                    id, brand, model, color, date = row.strip().split(",")
                            hide_basic_window()
                            name_csv = "inventory_list.csv"
                            file_path = os.path.join((os.path.dirname(__file__)), "Data", name_csv)
                            shutil.copyfile(import_csv, file_path)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                inventory_info = inventoryfile.read()
                            encrypt_data = crypt_key.encrypt(inventory_info)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                inventoryfile.write(encrypt_data)
                            import_csvfile_success_msg()
                        except (UnicodeDecodeError, ValueError, FileNotFoundError, IndexError):
                            hide_basic_window()
                            import_csvfile_error_msg()

                    def export_csvfile():
                        global export_csv
                        try:
                            dynamic_window.attributes('-disabled', 0)
                            basic_window.withdraw()
                            lang_value = languagegroup.get()
                            if lang_value == 1:
                                export_csv = filedialog.asksaveasfilename(title="Export CSV File", parent=dynamic_window, defaultextension=".csv", filetypes=(("CSV File", "*.csv"),))
                                if not export_csv:
                                    hide_basic_window()
                                    return export_csvfile_canceled_msg() 
                            elif lang_value == 2:
                                export_csv = filedialog.asksaveasfilename(title="Exportar Archivo CSV", parent=dynamic_window, defaultextension=".csv", filetypes=(("Archivo CSV", "*.csv"),))
                                if not export_csv:
                                    hide_basic_window()
                                    return export_csvfile_canceled_msg()
                            hide_basic_window()
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                inventory_info = inventoryfile.read()
                            decrypt_data = crypt_key.decrypt(inventory_info)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                inventoryfile.write(decrypt_data)
                            name_csv = "inventory_list.csv"
                            file_path = os.path.join((os.path.dirname(__file__)), "Data", name_csv)
                            shutil.copyfile(file_path, export_csv)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                                inventory_info = inventoryfile.read()
                            encrypt_data = crypt_key.encrypt(inventory_info)
                            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                                inventoryfile.write(encrypt_data)
                            export_csvfile_success_msg() 
                        except (UnicodeDecodeError, ValueError, FileNotFoundError, IndexError, cryptography.fernet.InvalidToken):
                            hide_basic_window()
                            export_csvfile_error_msg()

                    # ========================================================================================================= #
                    dynamic_window.title("Device Warehouse Inventory")
                    dynamic_window.resizable(width=False, height=False)
                    main_window_place()
                    dynamic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/main.ico"))
                    basic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/main.ico"))
                        
                    # ========== DEVICE IMAGE ========== #
                    device_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/devices1.png"))
                    device_imglb.config(image=device_img)
                    device_imglb.place(x=15, y=396)

                    # ========== DATA BASE TABLE ========== #
                    reflesh_inventory()
                    inventory_table.place(x=20, y=153)
                    
                    # ========== RADIO BUTTONS ========== #
                    addrb.bind("<ButtonRelease-1>", optionselected_mode)
                    addrb.bind("<KeyRelease-space>", optionselected_mode)
                    addrb.place(x=65, y=42, width=120, height=55)
                    addrb.invoke()
                    editrb.bind("<ButtonRelease-1>", optionselected_mode)
                    editrb.bind("<KeyRelease-space>", optionselected_mode)
                    editrb.place(x=401, y=42, width=120, height=55) 
                    deleterb.bind("<ButtonRelease-1>", optionselected_mode)
                    deleterb.bind("<KeyRelease-space>", optionselected_mode)
                    deleterb.place(x=738, y=42, width=120, height=55)
                    
                    # ========== LABELS ========== #
                    brandlb.config(fg="#00C300", state="normal")
                    modellb.config(fg="#00C300", state="normal")
                    colorlb.config(fg="#00C300", state="normal")
                    searchlb.config(text="🔍", font=("Segoe UI", 15))
                    labels_mw()
                
                    # ========== TEXT ENTRIES ========== #
                    brand_entry.config(cursor="xterm", highlightcolor="#00C300", highlightbackground="#00C300", highlightthickness=2)
                    model_entry.config(cursor="xterm", highlightcolor="#00C300", highlightbackground="#00C300", highlightthickness=2)
                    color_entry.config(cursor="xterm", highlightcolor="#00C300", highlightbackground="#00C300", highlightthickness=2)
                    brand_entry.delete(0, tk.END)
                    model_entry.delete(0, tk.END)
                    color_entry.delete(0, tk.END)
                    search_entry.bind("<KeyRelease>", lambda event: search_byid())         
                    entrys_mw()

                    # ========== BUTTONS ========== #
                    addbtn.config(cursor="hand2", command=add_inventory)
                    brand_entry.bind("<Return>", add_inventory)
                    model_entry.bind("<Return>", add_inventory)
                    color_entry.bind("<Return>", add_inventory)
                    checkbtn.config(cursor="hand2",)
                    cancelbtn.config(cursor="hand2")
                    editbtn.config(cursor="hand2")
                    deletebtn.config(cursor="hand2")
                    clearbtn.config(cursor="hand2", command=clear_mw)
                    buttons_mw()
                    
                    # ========== SEPARATORS ========== #
                    separators_mw()

                    # ========== MENU BARS ========== #
                    main_menu.entryconfigure(0, command=showdatafolder)
                    main_menu.entryconfigure(2, command=import_csvfile_ask)
                    main_menu.entryconfigure(3, command=export_csvfile_ask)
                    main_menu.entryconfigure(5, command=save_txtfile_ask)
                    mainmenubar_mw()
                    dynamic_window.deiconify()
                    brand_entry.focus()
                else:
                    login_error()
            except UnicodeDecodeError:
                with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "w") as inventoryfile:
                    inventoryfile.write("")
                error_window()
                load_csvfile_error_msg()
            except NameError:
                error_window()
                corruptvalues_error_msg()
            except TclError:
                error_window()
                loadfile_error_msg()
            except (ValueError, FileNotFoundError, IndexError, cryptography.fernet.InvalidToken):
                error_window()
                datafile_error_msg()
        
        # ============================================== LIGHT/DARK WINDOWS THEME ============================================== #
        def settings_light():
            settings_window.config(bg="white")
            themelb.config(bg="white", fg="black")
            languagelb.config(bg="white", fg="black")
            themeframe.config(highlightbackground="#C0C0C0", highlightthickness=2, bg="white")
            languageframe.config(highlightbackground="#C0C0C0", highlightthickness=2, bg="white")
            passwordlb_cleardata.config(bg="white", fg="black") 
            password_cleardata.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#AAAAAA", highlightbackground="#DADADA", highlightthickness=2)
            passwordcheck_cleardata.config(bg="white")
            
        def settings_dark():
            settings_window.config(bg="#101010")
            themelb.config(bg="#101010", fg="white")
            languagelb.config(bg="#101010", fg="white")
            themeframe.config(highlightbackground="#404040", highlightthickness=2, bg="#101010")
            languageframe.config(highlightbackground="#404040", highlightthickness=2, bg="#101010")
            passwordlb_cleardata.config(bg="#101010", fg="white")
            password_cleardata.config(fg="white", bg="#191919", insertbackground="white", highlightcolor="#636363", highlightbackground="#292929", highlightthickness=2)
            passwordcheck_cleardata.config(bg="#101010")

        def changeaccount_light():
            changeaccount_window.config(bg="white")
            changeaccount_lb_title.config(bg="white", fg="black")
            changeaccount_lb1.config(bg="white", fg="black")
            changeaccount_lb2.config(bg="white", fg="black")
            changeaccount_lb3.config(bg="white", fg="black")
            changeaccount_lb4.config(bg="white", fg="black")
            changeaccount_check1_lb.config(bg="white")
            changeaccount_check2_lb.config(bg="white")
            changeaccount_check3_lb.config(bg="white")
            changeaccount_imglb.config(bg="white")
            changeaccount_frame.config(highlightbackground="#C0C0C0", highlightthickness=2, bg="white")
            actual_username.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
            actual_password.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
            new_username.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)
            new_password.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#DADADA", highlightbackground="#DADADA", highlightthickness=2)

        def changeaccount_dark():
            changeaccount_window.config(bg="#101010")
            changeaccount_lb_title.config(bg="#101010", fg="white")
            changeaccount_lb1.config(bg="#101010", fg="white")
            changeaccount_lb2.config(bg="#101010", fg="white")
            changeaccount_lb3.config(bg="#101010", fg="white")
            changeaccount_lb4.config(bg="#101010", fg="white")
            changeaccount_check1_lb.config(bg="#101010")
            changeaccount_check2_lb.config(bg="#101010")
            changeaccount_check3_lb.config(bg="#101010")
            changeaccount_imglb.config(bg="#101010")
            changeaccount_frame.config(highlightbackground="#404040", highlightthickness=2, bg="#101010")
            actual_username.config(fg="white", bg="#191919", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
            actual_password.config(fg="white", bg="#191919", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
            new_username.config(fg="white", bg="#191919", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)
            new_password.config(fg="white", bg="#191919", insertbackground="white", highlightcolor="#292929", highlightbackground="#292929", highlightthickness=2)

        def tips_light():
            tips_window.config(bg="white")
            maintips_lb_title.config(bg="white", fg="black")
            tips_lb_title.config(bg="white", fg="black")
            tips_lb1.config(bg="white", fg="black")
            tips_urllb.config(bg="white", fg="#0047ED")
            tips_urllb.bind("<Enter>", lambda event: tips_urllb.config(fg="#55AAFF"))
            tips_urllb.bind("<Leave>", lambda event: tips_urllb.config(fg="#0047ED"))
            tips_imglb.config(bg="white")
            tips_frame.config(highlightbackground="#C0C0C0", highlightthickness=2, bg="white")
            tip_pagelb.config(bg="white", fg="black")
        
        def tips_dark():
            tips_window.config(bg="#101010")
            maintips_lb_title.config(bg="#101010", fg="white")
            tips_lb_title.config(bg="#101010", fg="white")
            tips_lb1.config(bg="#101010", fg="white")
            tips_urllb.config(bg="#101010", fg="#0083FF")
            tips_urllb.bind("<Enter>", lambda event: tips_urllb.config(fg="#55AAFF"))
            tips_urllb.bind("<Leave>", lambda event: tips_urllb.config(fg="#0083FF"))
            tips_imglb.config(bg="#101010")
            tips_frame.config(highlightbackground="#404040", highlightthickness=2, bg="#101010")
            tip_pagelb.config(bg="#101010", fg="white")

        # ========== LIGHT/DARK LOGIN WINDOW THEME ========== #
        def loginmenubar_dark():
            lmbar_separator.config(bg="#404040")
            ltips_menu.config(background="#101010", foreground="white", activeforeground="white", activebackground="#404040")
            about_menu.config(background="#101010", foreground="white", activeforeground="white", activebackground="#404040")
            
        def loginmenubar_light():
            lmbar_separator.config(bg="#C0C0C0")
            ltips_menu.config(background="white", foreground="black", activeforeground="black", activebackground="#DADADA")
            about_menu.config(background="white", foreground="black", activeforeground="black", activebackground="#DADADA")

        def loginlabels_light():
            loginprofile_imglb.config(bg="white")
            welcome_login.config(fg="black", bg="white")
            username_label.config(fg="black", bg="white")
            password_label.config(fg="black", bg="white")

        def loginlabels_dark():
            loginprofile_imglb.config(bg="#101010")
            welcome_login.config(fg="white", bg="#101010")
            username_label.config(fg="white", bg="#101010")
            password_label.config(fg="white", bg="#101010")

        def loginentrys_light():    
            username_entry.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#AAAAAA", highlightbackground="#DADADA", highlightthickness=2)
            password_entry.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#AAAAAA", highlightbackground="#DADADA", highlightthickness=2)

        def loginentrys_dark():
            username_entry.config(fg="white", bg="#191919", insertbackground="white", highlightcolor="#636363", highlightbackground="#292929", highlightthickness=2)
            password_entry.config(fg="white", bg="#191919", insertbackground="white", highlightcolor="#636363", highlightbackground="#292929", highlightthickness=2)

        # ========== LIGHT/DARK MAIN WINDOW THEME ========== #
        def mainmenubar_mw_dark():
            main_menu.config(background="#101010", foreground="white", activeforeground="white", activebackground="#404040")
            tips_menu.config(background="#101010", foreground="white", activeforeground="white", activebackground="#404040")
            about_menu.config(background="#101010", foreground="white", activeforeground="white", activebackground="#404040")

        def mainmenubar_mw_light():
            main_menu.config(background="white", foreground="black", activeforeground="black", activebackground="#DADADA")
            tips_menu.config(background="white", foreground="black", activeforeground="black", activebackground="#DADADA")
            about_menu.config(background="white", foreground="black", activeforeground="black", activebackground="#DADADA")

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
            username_logged_lb.config(background="white", foreground="black")

        def labels_main_dark():
            device_imglb.config(background="#101010", foreground="white")
            idlb.config(background="#101010")
            brandlb.config(background="#101010", disabledforeground="#696969")
            modellb.config(background="#101010", disabledforeground="#696969")
            colorlb.config(background="#101010", disabledforeground="#696969")
            datelb.config(background="#101010", disabledforeground="#696969")
            inventorylb.config(background="#101010", foreground="white")
            searchlb.config(background="#101010", foreground="white")
            device_imglb.config(background="#101010")
            foundlb.config(background="#101010", foreground="white")
            username_logged_lb.config(background="#101010", foreground="white")

        def entrys_mw_light():
            id_entry.config(fg="black", insertbackground="black", bg="#F9F9F9")
            brand_entry.config(fg="black", insertbackground="black", bg="#F9F9F9", disabledforeground="black", disabledbackground="white")
            model_entry.config(fg="black", insertbackground="black", bg="#F9F9F9", disabledforeground="black", disabledbackground="white")
            color_entry.config(fg="black", insertbackground="black", bg="#F9F9F9", disabledforeground="black", disabledbackground="white")
            date_entry.config(fg="black", insertbackground="black", bg="#F9F9F9", disabledforeground="black", disabledbackground="white")
            search_entry.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#AAAAAA", highlightbackground="#DADADA", highlightthickness=2)
            
        def entrys_mw_dark():
            id_entry.config(fg="white", insertbackground="white", bg="#191919")
            brand_entry.config(fg="white", insertbackground="white", bg="#191919", disabledforeground="white", disabledbackground="#101010")
            model_entry.config(fg="white", insertbackground="white", bg="#191919", disabledforeground="white", disabledbackground="#101010")
            color_entry.config(fg="white", insertbackground="white", bg="#191919", disabledforeground="white", disabledbackground="#101010")
            date_entry.config(fg="white", insertbackground="white",bg="#191919", disabledforeground="white", disabledbackground="#101010")
            search_entry.config(fg="white", bg="#191919", insertbackground="white", highlightcolor="#636363", highlightbackground="#292929", highlightthickness=2)           
                
        def table_light():
            style_table.configure("light.Treeview", fieldbackground="white", background="white", foreground="black", font=("Segoe UI", 11))
            style_table.configure("Treeview.Heading", background="white", foreground="black", relief="ridge", font=("Segoe UI", 12))
            style_table.map("Treeview.Heading", background=[('active', 'white')])
            style_table.map("light.Treeview", background=[('selected', '#C3C3C3')], foreground=[('selected', 'black')])
            inventory_table.config(style="light.Treeview")
            style_table.map("Vertical.TScrollbar", background=[('active', '#DADADA')])
            style_table.configure("Vertical.TScrollbar", background="#EFEFEF", arrowcolor="black", troughcolor="white", arrowsize=32)

        def table_dark():
            style_table.configure("dark.Treeview", fieldbackground="#101010", background="#101010", foreground="white", font=("Segoe UI", 11))
            style_table.configure("Treeview.Heading", background="#101010", foreground="white", relief="ridge", font=("Segoe UI", 12))
            style_table.map("Treeview.Heading", background=[('active', '#101010')])
            style_table.map("dark.Treeview", background=[('selected', '#303030')], foreground=[('selected', 'white')])
            inventory_table.config(style="dark.Treeview")
            style_table.map("Vertical.TScrollbar", background=[('active', '#404040')])
            style_table.configure("Vertical.TScrollbar", background="#191919", arrowcolor="white", troughcolor="black", arrowsize=32)

        def mainseparators_light():
            separator1.config(bg="#C0C0C0")
            separator3.config(bg="#C0C0C0")
            separator2.config(bg="#C0C0C0")

        def mainseparators_dark():
            separator1.config(bg="#404040")
            separator3.config(bg="#404040")
            separator2.config(bg="#404040")

        def basic_window_light():
            basic_window.config(bg="white")
            basic_imglb.config(bg="white")
            basic_lb1.config(bg="white", fg="black")
            info_bf_lb.config(bg="white", fg="black")
            info_af_lb.config(bg="white", fg="black")
            id_inf.config(bg="white")
            brand_bf.config(bg="white", fg="black", highlightbackground="#C0C0C0", highlightthickness=2)
            model_bf.config(bg="white", fg="black", highlightbackground="#C0C0C0", highlightthickness=2)
            color_bf.config(bg="white", fg="black", highlightbackground="#C0C0C0", highlightthickness=2)
            date_bf.config(bg="white", fg="black", highlightbackground="#C0C0C0", highlightthickness=2)
            brand_af.config(bg="white", fg="black", highlightbackground="#C0C0C0", highlightthickness=2)
            model_af.config(bg="white", fg="black", highlightbackground="#C0C0C0", highlightthickness=2)
            color_af.config(bg="white", fg="black", highlightbackground="#C0C0C0", highlightthickness=2)
            date_af.config(bg="white", fg="black", highlightbackground="#C0C0C0", highlightthickness=2)
            infobf_frame.config(highlightbackground="#C0C0C0", highlightthickness=2, bg="white")
            infoaf_frame.config(highlightbackground="#C0C0C0", highlightthickness=2, bg="white")

        def basic_window_dark():
            basic_window.config(bg="#101010")
            basic_imglb.config(bg="#101010")
            basic_lb1.config(bg="#101010", fg="white")
            info_bf_lb.config(bg="#101010", fg="white")
            info_af_lb.config(bg="#101010", fg="white")
            id_inf.config(bg="#101010")
            brand_bf.config(bg="#101010", fg="white", highlightbackground="#404040", highlightthickness=2)
            model_bf.config(bg="#101010", fg="white", highlightbackground="#404040", highlightthickness=2)
            color_bf.config(bg="#101010", fg="white", highlightbackground="#404040", highlightthickness=2)
            date_bf.config(bg="#101010", fg="white", highlightbackground="#404040", highlightthickness=2)
            brand_af.config(bg="#101010", fg="white", highlightbackground="#404040", highlightthickness=2)
            model_af.config(bg="#101010", fg="white", highlightbackground="#404040", highlightthickness=2)
            color_af.config(bg="#101010", fg="white", highlightbackground="#404040", highlightthickness=2)
            date_af.config(bg="#101010", fg="white", highlightbackground="#404040", highlightthickness=2)
            infobf_frame.config(highlightbackground="#404040", highlightthickness=2, bg="#101010")
            infoaf_frame.config(highlightbackground="#404040", highlightthickness=2, bg="#101010")
        
        # ============================================== LOAD ELEMENTS ============================================== #
        # ========== LOAD LOGIN WINDOW ========== #
        login_window_place()
        dynamic_window.resizable(width=False, height=False)
        dynamic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/login.ico"))
        load_loginwindow()
        lmbar_separator.place(x=0, y=32, width=550, height=1)
        loginprofile_imglb.place(x=220, y=35)
        welcome_login.place(y=139)
        username_label.place(x=135, y=184)
        password_label.place(x=135, y=249)
        username_entry.place(x=136, y=210, height=30)
        password_entry.place(x=136, y=275, height=30)
        showhide_pass_btn.bind("<ButtonPress-1>", showpass)
        showhide_pass_btn.bind("<ButtonRelease-1>", hidepass)
        password_entry.bind("<FocusIn>", showpassbutton)
        password_entry.bind("<FocusOut>", hidepassbutton)
        loginbtn.place(y=320)
        settings_btn.place(x=513, y=0, width=37, height=33)
        changeaccountlogin_btn.place(x=6, y=391)

        # ========== LOAD INVENTORY WINDOW ========== #
        load_inventory_window()

        # ========== LOAD LANGUAGE ========== #
        languagedata = set([row[0]for row in settingdata])
        if "language=eng_lang" in languagedata:
            eng_langrb.invoke()
            eng_lang_login()
        elif "language=esp_lang" in languagedata:
            esp_langrb.invoke()
            esp_lang_login()
        
        # ========== LOAD THEME ========== #  
        def load_theme():
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            os_themedata = set([row[0]for row in settingdata])
            dynamic_window.after(500, load_theme)
            if not dynamic_window.focus_get():
                if "theme=system_theme" in os_themedata:
                    if darkdetect.isDark():
                        window_dark()
                    else:
                        window_light()
        dynamic_window.bind("<FocusOut>", load_theme())
        themedata = set([row[0]for row in settingdata])   
        if "theme=dark_theme" in themedata: 
            darkthemerb.invoke()                 
            window_dark()
        elif "theme=light_theme" in themedata:
            lightthemerb.invoke()
            window_light()
        elif "theme=system_theme" in themedata:
            systemthemerb.invoke()
            if darkdetect.isDark():
                window_dark()
            else:
                window_light()

        # ============================== #
        dynamic_window.deiconify()
        dynamic_window.focus_force()
        username_entry.focus()
        dynamic_window.mainloop()  # ---- END of the Main Code

    # ============================================== MAINEXCEPTIONS ============================================== #
    except NameError:
        error_window()
        corruptvalues_error_msg()
    except TclError:
        error_window()
        loadfile_error_msg()
    except (ValueError, FileNotFoundError, IndexError):
        error_window()
        datafile_error_msg()

# ========== RESTORE DEFAULT SETTINGS (IF THE SETTINGS FILE IS CORRUPT) ========== #
with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
    loadsettings = csv.reader(settingfile)
    settingdata = list(loadsettings)
settingsdata = set([row[0]for row in settingdata])
if os_version < recom_req and os_version >= min_req:
    if not set(["theme=dark_theme", "theme=light_theme"]).intersection(set(settingsdata)) or not set(["language=eng_lang", "language=esp_lang"]).intersection(set(settingsdata)) or not set(["setup=unfinished", "setup=finished"]).intersection(set(settingsdata)):
        with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
            settingfile.write("theme=light_theme\nlanguage=eng_lang\nsetup=unfinished\n")
    else:
        with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
            loadsettings = csv.reader(settingfile)
            settingdata = list(loadsettings)
else:
    if not set(["theme=dark_theme", "theme=light_theme", "theme=system_theme"]).intersection(set(settingsdata)) or not set(["language=eng_lang", "language=esp_lang"]).intersection(set(settingsdata)) or not set(["setup=unfinished", "setup=finished"]).intersection(set(settingsdata)):
        with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w") as settingfile:
            settingfile.write("theme=system_theme\nlanguage=eng_lang\nsetup=unfinished\n")
    else:
        with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
            loadsettings = csv.reader(settingfile)
            settingdata = list(loadsettings)
with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as setupfile:
    loadsetup = csv.reader(setupfile)
    setupdata = list(loadsetup)
    
# ============================================== LOAD SETUP PROGRAM (ONLY IN FIRST RUN) ============================================== #
def setup_program(): 
    try:   
        with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
            loadsettings = csv.reader(settingfile)
            settingdata = list(loadsettings)
            
        def setup_finish():
            setup_window.destroy()
            setup_btn_back.destroy()
            setup_btn_next.destroy()
            setup_btn_done.destroy()
            setup_frame.destroy()
            setup_lb_title.destroy()
            setup_lb1.destroy()
            setup_lb2.destroy()
            setup_eng_langrb.destroy()
            setup_esp_langrb.destroy()
            setup_systemthemerb.destroy()
            setup_lightthemerb.destroy()
            setup_darkthemerb.destroy()
            setup_username_lb.destroy()
            setup_password_lb.destroy()
            setup_username.destroy()
            setup_password.destroy()
            showhide_setuppass_btn.destroy()
            setup_check1_lb.destroy()
            setup_check2_lb.destroy()
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            for row in settingdata:
                if row[0] == "setup=unfinished":
                    row[0] = "setup=finished"
                    break 
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                writer = csv.writer(settingfile)
                writer.writerows(settingdata)
                settingfile.seek(0, 2)
            DWI()
        
        def setup_light():
            style_elements.theme_use("default")
            setup_window.config(bg="white")
            setup_lb_title.config(bg="white", fg="black")
            setup_lb1.config(bg="white", fg="black")
            setup_lb2.config(bg="white", fg="black")
            setup_frame.config(highlightbackground="#C0C0C0", highlightthickness=2, bg="white")
            setup_username.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#AAAAAA", highlightbackground="#DADADA", highlightthickness=2)
            setup_password.config(fg="black", bg="#F9F9F9", insertbackground="black", highlightcolor="#AAAAAA", highlightbackground="#DADADA", highlightthickness=2)
            setup_username_lb.config(bg="white", fg="black")
            setup_password_lb.config(bg="white", fg="black")
            setup_check1_lb.config(bg="white")
            setup_check2_lb.config(bg="white")
            style_elements.map("TButton", background=[('pressed', '#E3E3E3'), ('active', '#DADADA'), ("disabled", "#F6F6F6")], foreground=[("disabled", "#888888")], 
                                   relief=[('pressed', 'groove'), ('!pressed', 'ridge')])
            style_elements.configure("TButton", background="#ECECEC", foreground="black", font=("Segoe UI", 12), focuscolor="black", justify=tk.CENTER, anchor=tk.CENTER)
            style_elements.configure("done.TButton", foreground='#009003', focuscolor='#009003')
            setup_btn_done.config(style='done.TButton')
            style_elements.map("pass.TButton", background=[('pressed', 'white'), ('active', 'white')], 
                                   foreground=[('pressed', '#737373'), ('active', 'black')], relief=[('pressed', 'flat'), ('!pressed', 'flat')])
            style_elements.configure('pass.TButton', foreground='black', background="white", justify=tk.CENTER, anchor=tk.CENTER)
            showhide_setuppass_btn.config(style='pass.TButton')
            style_elements.map("Toolbutton", background=[('pressed', '#E3E3E3'), ('active', '#DADADA'), ('selected', '#C3C3C3')], 
                                indicatorcolor=[('selected', 'black')], relief=[('selected', 'groove')])
            style_elements.configure("Toolbutton", background="#ECECEC", foreground="black", font=("Segoe UI", 12), focuscolor="black", indicatorcolor="#999999", 
                                        justify=tk.CENTER, anchor=tk.CENTER, relief=tk.RIDGE)
            setup_eng_langrb.config(style='Toolbutton')
            setup_esp_langrb.config(style='Toolbutton')
            setup_systemthemerb.config(style='Toolbutton')
            setup_lightthemerb.config(style='Toolbutton')
            setup_darkthemerb.config(style='Toolbutton')
            basic_window.config(bg="white")
            basic_imglb.config(bg="white")
            basic_lb1.config(bg="white", fg="black")
            setup_imglb.config(bg="white")
            
        def setup_dark():
            style_elements.theme_use("default")
            setup_window.config(bg="#101010")
            setup_lb_title.config(bg="#101010", fg="white")
            setup_lb1.config(bg="#101010", fg="white")
            setup_lb2.config(bg="#101010", fg="white")
            setup_frame.config(highlightbackground="#404040", highlightthickness=2, bg="#101010")
            setup_username.config(fg="white", bg="#191919", insertbackground="white", highlightcolor="#636363", highlightbackground="#292929", highlightthickness=2)
            setup_password.config(fg="white", bg="#191919", insertbackground="white", highlightcolor="#636363", highlightbackground="#292929", highlightthickness=2)
            setup_username_lb.config(bg="#101010", fg="white")
            setup_password_lb.config(bg="#101010", fg="white")
            setup_check1_lb.config(bg="#101010")
            setup_check2_lb.config(bg="#101010")
            style_elements.map("TButton", background=[('pressed', '#252525'), ('active', '#303030'), ("disabled", "#101010")], foreground=[("disabled", "#777777")], 
                                   relief=[('pressed', 'groove'), ('!pressed', 'ridge')])
            style_elements.configure("TButton", background="#171717", foreground="white", font=("Segoe UI", 12), focuscolor='white', justify=tk.CENTER, anchor=tk.CENTER)
            style_elements.configure("done.TButton", foreground='#00C300', focuscolor='#00C300')
            setup_btn_done.config(style='done.TButton')
            style_elements.map("pass.TButton", background=[('pressed', '#101010'), ('active', '#101010')], 
                                   foreground=[('pressed', '#AAAAAA'), ('active', 'white')], relief=[('pressed', 'flat'), ('!pressed', 'flat')])
            style_elements.configure('pass.TButton', foreground='white', background="#101010", justify=tk.CENTER, anchor=tk.CENTER)
            showhide_setuppass_btn.config(style='pass.TButton')
            style_elements.map("Toolbutton", background=[('pressed', '#252525'), ('active', '#303030'), ('selected', '#252525')], 
                                indicatorcolor=[('selected', '#707070')], relief=[('selected', 'groove')])
            style_elements.configure("Toolbutton", background="#171717", foreground="white", font=("Segoe UI", 12), focuscolor="white", indicatorcolor="white", 
                                        justify=tk.CENTER, anchor=tk.CENTER, relief=tk.RIDGE)
            setup_eng_langrb.config(style='Toolbutton')
            setup_esp_langrb.config(style='Toolbutton')
            setup_systemthemerb.config(style='Toolbutton')
            setup_lightthemerb.config(style='Toolbutton')
            setup_darkthemerb.config(style='Toolbutton') 
            basic_window.config(bg="#101010")
            basic_imglb.config(bg="#101010")
            basic_lb1.config(bg="#101010", fg="white")
            setup_imglb.config(bg="#101010")

        def apply_setup_theme():
            setup_theme_value = setup_themegroup.get()
            if setup_theme_value == 1:               
                setup_dark()
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                for row in settingdata:
                    if row[0] == "theme=light_theme" or row[0] == "theme=system_theme":
                        row[0] = "theme=dark_theme"
                        break 
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                    writer = csv.writer(settingfile)
                    writer.writerows(settingdata)
                    settingfile.seek(0, 2) 
            elif setup_theme_value == 2:
                setup_light()
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                for row in settingdata:
                    if row[0] == "theme=dark_theme" or row[0] == "theme=system_theme":
                        row[0] = "theme=light_theme"
                        break 
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                    writer = csv.writer(settingfile)
                    writer.writerows(settingdata)
                    settingfile.seek(0, 2)
            elif setup_theme_value == 3:
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                    loadsettings = csv.reader(settingfile)
                    settingdata = list(loadsettings)
                for row in settingdata:
                    if row[0] == "theme=light_theme" or row[0] == "theme=dark_theme":
                        row[0] = "theme=system_theme"
                        break 
                with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
                    writer = csv.writer(settingfile)
                    writer.writerows(settingdata)
                    settingfile.seek(0, 2)
                if darkdetect.isDark():
                    setup_dark()
                else:
                    setup_light()

        def loadsetup_theme():
            with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
                loadsettings = csv.reader(settingfile)
                settingdata = list(loadsettings)
            os_themedata = set([row[0]for row in settingdata])
            setup_window.after(500, loadsetup_theme)
            if not setup_window.focus_get():
                if "theme=system_theme" in os_themedata:
                    if darkdetect.isDark():
                        setup_dark()
                    else:
                        setup_light()
        setup_window.bind("<FocusOut>", loadsetup_theme())
        themedata = set([row[0]for row in settingdata])   
        if "theme=dark_theme" in themedata: 
            setup_darkthemerb.invoke()                 
            setup_dark()
        elif "theme=light_theme" in themedata:
            setup_lightthemerb.invoke()
            setup_light()
        elif "theme=system_theme" in themedata:
            setup_systemthemerb.invoke()
            if darkdetect.isDark():
                setup_dark()
            else:
                setup_light()

        def offsetup_elements_msg():
            setup_btn_back.config(cursor="arrow")
            setup_btn_next.config(cursor="arrow")
            setup_btn_done.config(cursor="arrow")
            setup_eng_langrb.config(cursor="arrow")
            setup_esp_langrb.config(cursor="arrow")
            setup_systemthemerb.config(cursor="arrow")
            setup_lightthemerb.config(cursor="arrow")
            setup_darkthemerb.config(cursor="arrow")
            setup_username.config(cursor="arrow")
            setup_password.config(cursor="arrow")

        def hide_cancelsetup():
            setup_window.attributes('-disabled', 0)
            dynamic_window.attributes('-disabled', 0)
            setup_btn_back.config(cursor="hand2")
            setup_btn_next.config(cursor="hand2")
            setup_btn_done.config(cursor="hand2")
            setup_eng_langrb.config(cursor="hand2")
            setup_esp_langrb.config(cursor="hand2")
            setup_systemthemerb.config(cursor="hand2")
            setup_lightthemerb.config(cursor="hand2")
            setup_darkthemerb.config(cursor="hand2")
            setup_username.config(cursor="xterm")
            setup_password.config(cursor="xterm")
            basic_window.grab_release()
            basic_window.transient(None)
            basic_window.withdraw()
            basic_lb1.place_forget()
            basic_imglb.place_forget()
            basic_btn_yes.place_forget()
            basic_btn_no.place_forget()
        
        def showsetuppass(show):
            setup_password.config(show="")
        def hidesetuppass(hide):
            setup_password.config(show="*")
        def showsetuppassbutton(show):
            showhide_setuppass_btn.place(x=344, y=301, width=33, height=31)
        def hidesetuppassbutton(hide):
            showhide_setuppass_btn.place_forget()

        def enable_newaccount():
            if setup_username.get() == "":
                setup_lang_value = setup_languagegroup.get()
                if setup_lang_value == 1:
                    setup_check1_lb.config(text="Empty Text Field.", font=("Segoe UI", 12), fg="#CE0000")
                elif setup_lang_value == 2:
                    setup_check1_lb.config(text="Campo de Texto Vacio.", font=("Segoe UI", 12), fg="#CE0000")
                setup_check1_lb.place(x=75, y=235)
                setup_btn_next.config(state="disabled", cursor="arrow") 
            elif len(setup_username.get()) < 4:
                setup_lang_value = setup_languagegroup.get()
                if setup_lang_value == 1:
                    setup_check1_lb.config(text="Must be at Least 4 Letters/Numbers.", font=("Segoe UI", 12), fg="#CE0000")
                elif setup_lang_value == 2:
                    setup_check1_lb.config(text="Debe tener al menos 4 Letras/Numeros.", font=("Segoe UI", 12), fg="#CE0000")
                setup_check1_lb.place(x=75, y=235)
                setup_btn_next.config(state="disabled", cursor="arrow") 
            elif len(setup_username.get()) >= 4:
                setup_lang_value = setup_languagegroup.get()
                if setup_lang_value == 1:
                    setup_check1_lb.config(text="Valid Username.", font=("Segoe UI", 12), fg="#009E00")
                elif setup_lang_value == 2:
                    setup_check1_lb.config(text="Nombre de usuario Valido.", font=("Segoe UI", 12), fg="#009E00")
                setup_check1_lb.place(x=75, y=235)
            if setup_password.get() == "":
                setup_lang_value = setup_languagegroup.get()
                if setup_lang_value == 1:
                    setup_check2_lb.config(text="Empty Text Field.", font=("Segoe UI", 12), fg="#CE0000")
                elif setup_lang_value == 2:
                    setup_check2_lb.config(text="Campo de Texto Vacio.", font=("Segoe UI", 12), fg="#CE0000")
                setup_check2_lb.place(x=75, y=332)
                setup_btn_next.config(state="disabled", cursor="arrow") 
            elif len(setup_password.get()) < 8:
                setup_lang_value = setup_languagegroup.get()
                if setup_lang_value == 1:
                    setup_check2_lb.config(text="Security Level: Weak.", font=("Segoe UI", 12), fg="#CE0000")
                elif setup_lang_value == 2:
                    setup_check2_lb.config(text="Nivel de Seguridad: Debil.", font=("Segoe UI", 12), fg="#CE0000")
                setup_check2_lb.place(x=75, y=332)
                setup_btn_next.config(state="disabled", cursor="arrow") 
            elif len(setup_password.get()) >= 8:
                setup_lang_value = setup_languagegroup.get()
                if setup_lang_value == 1:
                    setup_check2_lb.config(text="Security Level: Safe.", font=("Segoe UI", 12), fg="#009E00")
                elif setup_lang_value == 2:
                    setup_check2_lb.config(text="Nivel de Seguridad: Segura.", font=("Segoe UI", 12), fg="#009E00")
                setup_check2_lb.place(x=75, y=332)
            if len(setup_username.get()) >= 4 and len(setup_password.get()) >= 8:
                setup_btn_next.config(state="normal", cursor="hand2", command=step_4)
        
        # ========== CANCEL SETUP ASK MSG ========== #
        def cancelsetup_ask():
            try:
                window_w_total = dynamic_window.winfo_screenwidth()
                window_h_total = dynamic_window.winfo_screenheight()
                basic_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/setup.ico"))
                setup_lang_value = setup_languagegroup.get()
                if setup_lang_value == 1:
                    window_w = 465
                    window_h = 175
                    basic_window.title("Exit Setup?")
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="The Setup is not Finished yet and if it Close\nyou will have to start again.\nAre you sure you want to Exit?", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=34)
                    basic_btn_yes.config(text="✔️  Yes", command=close)
                    basic_btn_yes.place(x=140, y=125, width=80, height=37)
                    basic_btn_no.config(text="❌  No", command=hide_cancelsetup)
                    basic_btn_no.place(x=237, y=125, width=80, height=37)
                elif setup_lang_value == 2:
                    window_w = 510 
                    window_h = 175 
                    basic_window.title("Salir de la Configuracion?")                 
                    basic_imglb.place(x=15, y=30)
                    basic_lb1.config(justify="center", text="La Configuracion aun no esta Terminada y si Cierra\ndebera empezar de nuevo.\nEstas seguro que quieres Salir?", font=("Segoe UI", 12))
                    basic_lb1.place(x=120, y=34)
                    basic_btn_yes.config(text="✔️  Si", command=close)
                    basic_btn_yes.place(x=162, y=125, width=80, height=37)
                    basic_btn_no.config(text="❌  No", command=hide_cancelsetup)
                    basic_btn_no.place(x=257, y=125, width=80, height=37)
                setup_width = round(window_w_total/2-window_w/2)
                setup_height = round(window_h_total/2-window_h/2-100)
                basic_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(setup_width)+"+"+str(setup_height))
                offsetup_elements_msg()
                basic_window.protocol("WM_DELETE_WINDOW", lambda: hide_cancelsetup())    
                basic_window.resizable(width=False, height=False)
                basic_window.grab_set()
                basic_window.focus_set()
                basic_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/ask.png"))
                basic_window.transient(setup_window)
                basic_window.deiconify()
                setup_window.attributes('-disabled', 1)
                dynamic_window.attributes('-disabled', 1)
            except TclError:
                error_window()
                loadfile_error_msg()

        # ========== FISRT STEP WINDOW ========== #        
        def first_step_eng():
            setup_btn_back.place_forget() 
            setup_systemthemerb.place_forget() 
            setup_lightthemerb.place_forget() 
            setup_darkthemerb.place_forget() 
            setup_eng_langrb.place_forget()
            setup_esp_langrb.place_forget()
            setup_username.place_forget()
            setup_password.place_forget()
            showhide_setuppass_btn.place_forget()
            setup_username_lb.place_forget()
            setup_password_lb.place_forget()
            setup_check1_lb.place_forget()
            setup_check2_lb.place_forget()
            setup_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/setup.png"))
            setup_window.title("Device Warehouse Inventory Setup")
            setup_lb_title.config(text="Welcome to Device Warehouse Inventory\nBefore we start,\nlet's configure a few things.", font=("Segoe UI", 14))
            setup_lb_title.place(x=0, y=99, width=420)
            setup_lb1.config(text="💬  Select a Language", font=("Segoe UI", 12))
            setup_lb1.place(x=65, y=196)
            setup_eng_langrb.place(x=81, y=277, width=110, height=40)
            setup_esp_langrb.place(x=228, y=277, width=110, height=40)
            setup_btn_next.config(text="⏩")
            setup_btn_next.config(state="normal", cursor="hand2")
            setup_btn_next.place(x=373, y=400, width=37, height=37)
            setup_btn_next.config(command=step_2) 
            setup_frame.place(x=40, y=210, width=340, height=165) 
            setup_imglb.place(x=165, y=5)
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

        def first_step_esp():
            setup_btn_back.place_forget() 
            setup_systemthemerb.place_forget() 
            setup_lightthemerb.place_forget() 
            setup_darkthemerb.place_forget()
            setup_eng_langrb.place_forget()
            setup_esp_langrb.place_forget()
            setup_username.place_forget()
            setup_password.place_forget()
            showhide_setuppass_btn.place_forget()
            setup_username_lb.place_forget()
            setup_password_lb.place_forget()
            setup_check1_lb.place_forget()
            setup_check2_lb.place_forget()
            setup_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/setup.png"))
            setup_window.title("Configuracion de Device Warehouse Inventory")
            setup_lb_title.config(text="Bienvenido a Device Warehouse Inventory\nAntes de comenzar,\nvamos a configurar algunas cosas.", font=("Segoe UI", 14))
            setup_lb_title.place(x=0, y=99, width=420)
            setup_lb1.config(text="💬  Selecciona un Idioma", font=("Segoe UI", 12))
            setup_lb1.place(x=65, y=196)
            setup_eng_langrb.place(x=81, y=277, width=110, height=40)
            setup_esp_langrb.place(x=228, y=277,width=110, height=40)
            setup_btn_next.config(text="⏩")
            setup_btn_next.config(state="normal", cursor="hand2")
            setup_btn_next.place(x=373, y=400, width=37, height=37)
            setup_btn_next.config(command=step_2)
            setup_frame.place(x=40, y=210, width=340, height=165) 
            setup_imglb.place(x=165, y=5)
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

        def first_step():
            window_w_total = dynamic_window.winfo_screenwidth()
            window_h_total = dynamic_window.winfo_screenheight()
            window_w = 420
            window_h = 450
            setup_width = round(window_w_total/2-window_w/2)
            setup_height = round(window_h_total/2-window_h/2-100)
            setup_window.geometry(str(window_w)+"x"+str(window_h)+"+"+str(setup_width)+"+"+str(setup_height))
            errorwm_height = round(window_h_total/2-window_h/2-999999999999999999999999999999999999999)
            dynamic_window.geometry(str(1)+"x"+str(1)+"+"+str(setup_width)+"+"+str(errorwm_height))
            setup_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/setup.ico"))
            setup_window.protocol("WM_DELETE_WINDOW", lambda: cancelsetup_ask())
            setup_window.resizable(width=False, height=False)
            setup_eng_langrb.config(command=first_step_eng)
            setup_esp_langrb.config(command=first_step_esp)
            dynamic_window.withdraw()
            basic_window.withdraw()
            setup_window.deiconify()
            setup_window.focus_force()

        # ========== STEP-2 WINDOW ========== #
        def step_2():
            setup_systemthemerb.place_forget()
            setup_lightthemerb.place_forget()
            setup_darkthemerb.place_forget()
            setup_eng_langrb.place_forget()
            setup_esp_langrb.place_forget()
            setup_username.place_forget()
            setup_password.place_forget()
            showhide_setuppass_btn.place_forget()
            setup_username_lb.place_forget()
            setup_password_lb.place_forget()
            setup_check1_lb.place_forget()
            setup_check2_lb.place_forget()
            setup_lang_value = setup_languagegroup.get()
            if os_version < recom_req and os_version >= min_req:
                if setup_lang_value == 1:
                    setup_lb_title.config(text="Choose the Theme to use in the Program.\n*You Can change it in Settings.", font=("Segoe UI", 12))
                    setup_lb_title.place(x=0, y=79, width=420)
                    setup_lb1.config(text="🎨  Select a Theme", font=("Segoe UI", 12))
                    setup_lb1.place(x=65, y=146)
                    setup_lightthemerb.config(text="🔆      Light", cursor="hand2") 
                    setup_darkthemerb.config(text="🌙      Dark", cursor="hand2") 
                    setup_btn_next.config(text="⏩")
                    setup_btn_back.config(text="⏪") 
                    setup_btn_back.config(command=first_step_eng)
                elif setup_lang_value == 2:
                    setup_lb_title.config(text="Elige el Tema para usar en el Programa.\n*Puedes cambiarlo en Configuracion.", font=("Segoe UI", 12))
                    setup_lb_title.place(x=0, y=79, width=420)
                    setup_lb1.config(text="🎨  Selecciona un Tema", font=("Segoe UI", 12))
                    setup_lb1.place(x=62, y=146)
                    setup_lightthemerb.config(text="🔆       Claro", cursor="hand2") 
                    setup_darkthemerb.config(text="🌙    Oscuro", cursor="hand2") 
                    setup_btn_next.config(text="⏩")
                    setup_btn_back.config(text="⏪") 
                    setup_btn_back.config(command=first_step_esp)
                setup_lightthemerb.place(x=152, y=210, width=110, height=40)
                setup_darkthemerb.place(x=152, y=286, width=110, height=40)
                setup_btn_next.place(x=373, y=400, width=37, height=37)
                setup_btn_back.place(x=10, y=400, width=37, height=37) 
            else:
                if setup_lang_value == 1:
                    setup_lb_title.config(text="Choose the Theme to use in the Program.\n*You Can change it in Settings.", font=("Segoe UI", 12))
                    setup_lb_title.place(x=0, y=79, width=420)
                    setup_lb1.config(text="🎨  Select a Theme", font=("Segoe UI", 12))
                    setup_lb1.place(x=65, y=146)
                    setup_systemthemerb.config(text="🌓  System", cursor="hand2") 
                    setup_lightthemerb.config(text="🔆      Light", cursor="hand2") 
                    setup_darkthemerb.config(text="🌙      Dark", cursor="hand2") 
                    setup_btn_next.config(text="⏩")
                    setup_btn_back.config(text="⏪") 
                    setup_btn_back.config(command=first_step_eng)
                elif setup_lang_value == 2:
                    setup_lb_title.config(text="Elige el Tema para usar en el Programa.\n*Puedes cambiarlo en Configuracion.", font=("Segoe UI", 12))
                    setup_lb_title.place(x=0, y=79, width=420)
                    setup_lb1.config(text="🎨  Selecciona un Tema", font=("Segoe UI", 12))
                    setup_lb1.place(x=62, y=146)
                    setup_systemthemerb.config(text="🌓  Sistema", cursor="hand2")
                    setup_lightthemerb.config(text="🔆       Claro", cursor="hand2") 
                    setup_darkthemerb.config(text="🌙    Oscuro", cursor="hand2") 
                    setup_btn_next.config(text="⏩")
                    setup_btn_back.config(text="⏪") 
                    setup_btn_back.config(command=first_step_esp)
                setup_systemthemerb.place(x=152, y=185, width=110, height=40)
                setup_lightthemerb.place(x=152, y=250, width=110, height=40)
                setup_darkthemerb.place(x=152, y=311, width=110, height=40)
                setup_btn_next.place(x=373, y=400, width=37, height=37) 
                setup_btn_back.place(x=10, y=400, width=37, height=37)
            setup_btn_next.config(command=step_3)
            setup_btn_next.config(state="normal", cursor="hand2")
            setup_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/setup.ico"))
            setup_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/setuptheme.png"))
            setup_window.protocol("WM_DELETE_WINDOW", lambda: cancelsetup_ask())
            setup_systemthemerb.config(command=apply_setup_theme)
            setup_lightthemerb.config(command=apply_setup_theme)
            setup_darkthemerb.config(command=apply_setup_theme)
            setup_frame.place(x=40, y=160, width=340, height=215) 
            setup_imglb.place(x=165, y=5)
            
        # ========== STEP-3 WINDOW ========== #
        def step_3():
            def validate_setupvalue_account(text):
                pattern = re.compile(r"^[a-zA-Z0-9]+$")
                if pattern.match(text) is not None:
                    return True and len(text) <= 20
                elif text == "":
                    return True and len(text) <= 20
                else:
                    return False
            setup_systemthemerb.place_forget() 
            setup_lightthemerb.place_forget() 
            setup_darkthemerb.place_forget() 
            setup_eng_langrb.place_forget()
            setup_esp_langrb.place_forget()
            setup_username.place_forget()
            setup_password.place_forget()
            showhide_setuppass_btn.place_forget()
            setup_username_lb.place_forget()
            setup_password_lb.place_forget()
            setup_check1_lb.place_forget()
            setup_check2_lb.place_forget()
            setup_username.delete(0, tk.END)
            setup_password.delete(0, tk.END)
            setup_lang_value = setup_languagegroup.get()
            if setup_lang_value == 1:
                setup_lb_title.config(text="Type your New Username and Password to Login.\n*You Can change it in [👤 Account Settings].", font=("Segoe UI", 12))
                setup_lb_title.place(x=0, y=79, width=420)
                setup_lb1.config(text="👤  Your New Account", font=("Segoe UI", 12))
                setup_username_lb.config(text="New Username", font=("Segoe UI", 12))
                setup_password_lb.config(text="New Password", font=("Segoe UI", 12))
                setup_btn_next.config(text="⏩")
                setup_btn_back.config(text="⏪") 
            elif setup_lang_value == 2:
                setup_lb_title.config(text="Escribe tu Nuevo Nombre de Usuario y\nContraseña para Iniciar Sesion.\n*Puedes cambiarlo en [👤 Configuracion de Cuenta].", font=("Segoe UI", 12))
                setup_lb_title.place(x=0, y=80, width=420)
                setup_lb1.config(text="👤  Tu Nueva Cuenta", font=("Segoe UI", 12))
                setup_username_lb.config(text="Nuevo Nombre de Usuario", font=("Segoe UI", 12))
                setup_password_lb.config(text="Nueva Contraseña", font=("Segoe UI", 12))
                setup_btn_next.config(text="⏩")
                setup_btn_back.config(text="⏪")
            setup_lb1.place(x=65, y=146)
            setup_btn_next.place(x=373, y=400, width=37, height=37) 
            setup_btn_back.place(x=10, y=400, width=37, height=37) 
            setup_username.config(width=29, validate="key", validatecommand=(dynamic_window.register(validate_setupvalue_account), "%P"), font=("Segoe UI", 12))
            setup_password.config(width=29, validate="key", validatecommand=(dynamic_window.register(validate_setupvalue_account), "%P"), font=("Segoe UI", 12))
            setup_username.bind("<KeyRelease>", lambda event: enable_newaccount())
            setup_password.bind("<KeyRelease>", lambda event: enable_newaccount())
            setup_password.bind("<FocusIn>", showsetuppassbutton)
            setup_password.bind("<FocusOut>", hidesetuppassbutton)
            showhide_setuppass_btn.bind("<ButtonPress-1>", showsetuppass)
            showhide_setuppass_btn.bind("<ButtonRelease-1>", hidesetuppass)
            setup_username_lb.place(x=74, y=180)
            setup_username.place(x=75, y=205, height=30)
            setup_password_lb.place(x=74, y=277)
            setup_password.place(x=75, y=302, height=30)
            showhide_setuppass_btn.config(text="👁️")
            setup_username.focus()
            setup_btn_back.config(command=step_2)
            setup_btn_next.config(state="disabled", cursor="arrow") 
            setup_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/setup.ico"))
            setup_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/setupaccount.png"))
            setup_window.protocol("WM_DELETE_WINDOW", lambda: cancelsetup_ask())
            setup_frame.place(x=40, y=160, width=340, height=215) 
            setup_imglb.place(x=165, y=5)

        def step_4():
            setup_window.resizable(width=False, height=False)
            setupusername = setup_username.get()
            with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "w", newline="") as setupaccountfile:
                setupwriter = csv.writer(setupaccountfile)
                setupwriter.writerow([setupusername.lower(), setup_password.get()])
            with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "rb") as accountfile:
                account_info = accountfile.read()
            encrypt_data = crypt_key.encrypt(account_info)
            with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "wb") as accountfile:
                accountfile.write(encrypt_data)
            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "w") as inventoryfile:
                inventoryfile.write("")
            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "rb") as inventoryfile:
                inventory_info = inventoryfile.read()
            encrypt_data = crypt_key.encrypt(inventory_info)
            with open(os.path.join(os.path.dirname(__file__), "Data/inventory_list.csv"), "wb") as inventoryfile:
                inventoryfile.write(encrypt_data)
            setup_systemthemerb.place_forget() 
            setup_lightthemerb.place_forget() 
            setup_darkthemerb.place_forget() 
            setup_eng_langrb.place_forget()
            setup_esp_langrb.place_forget()
            setup_username.place_forget()
            setup_password.place_forget()
            showhide_setuppass_btn.place_forget()
            setup_username_lb.place_forget()
            setup_password_lb.place_forget()
            setup_check1_lb.place_forget()
            setup_check2_lb.place_forget()
            setup_frame.place_forget()
            setup_lb1.place_forget()
            setup_btn_next.place_forget()
            setup_btn_back.place_forget()
            setup_username.delete(0, tk.END)
            setup_password.delete(0, tk.END)
            setup_imglb.place(x=105, y=25)
            setup_lang_value = setup_languagegroup.get()
            if setup_lang_value == 1:
                setup_lb_title.config(text="Device Warehouse Inventory Setup\nis completed, press the [✅] button\nto close this Window and Start.", font=("Segoe UI", 14))
                setup_lb_title.place(x=0, y=250, width=420)
            elif setup_lang_value == 2:
                setup_lb_title.config(text="Se ha completado la\nConfiguracion de Device Warehouse Inventory,\npresione el boton [✅] para cerrar\nesta Ventana y Empezar.", font=("Segoe UI", 14))
                setup_lb_title.place(x=0, y=250, width=420)
            setup_btn_done.config(text="✅", command=setup_finish)
            setup_btn_done.place(x=173, y=400, width=70, height=37) 
            setup_window.wm_iconbitmap(os.path.join(os.path.dirname(__file__), "Sources/Icons/setup.ico"))
            setup_img.config(file=os.path.join(os.path.dirname(__file__), "Sources/Imgs/setupcomplete.png"))
            setup_window.protocol("WM_DELETE_WINDOW", lambda: setup_finish())

        languagedata = set([row[0]for row in settingdata])
        if "language=eng_lang" in languagedata:
            setup_eng_langrb.invoke()
            first_step_eng()
        elif "language=esp_lang" in languagedata:
            setup_esp_langrb.invoke()
            first_step_esp()
        first_step()

        # ===================================== #   
        dynamic_window.mainloop() 

    # ========== SETUP EXCEPTIONS ========== #
    except NameError:
        error_window()
        corruptvalues_error_msg()
    except TclError:
        error_window()
        loadfile_error_msg()
    except (ValueError, FileNotFoundError, IndexError):
        error_window()
        datafile_error_msg()   

# ========== SETUP MISC ========== #
setup_data = set([row[0]for row in setupdata])
with open(os.path.join(os.path.dirname(__file__), "Data/account_data.csv"), "r") as setupaccountfile:
    setupaccountdata = setupaccountfile.read()
if len(setupaccountdata) < 99 or set(["setup=unfinished"]).intersection(set(setup_data)) or len(setupaccountdata) > 140:
    with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "r", newline="") as settingfile:
        loadsettings = csv.reader(settingfile)
        settingdata = list(loadsettings)
    for row in settingdata:
        if row[0] == "setup=unfinished" or row[0] == "setup=finished":
            row[0] = "setup=unfinished"
            break 
    with open(os.path.join(os.path.dirname(__file__), "settings.dat"), "w", newline="") as settingfile:
        writer = csv.writer(settingfile)
        writer.writerows(settingdata)
        settingfile.seek(0, 2) 
    setup_program()

if os_version < min_req:
    tk.messagebox.showerror("OS Version Not supported! | Version del S.O No compatible!", "Windows 10 x64 (Build 14393) or Higher is Required to Work!\nPlease Update the O.S, If you still have Problems contact the Developer.\n\nSe Necesita Windows 10 x64 (Compilacion 14393) o Superior para Funcionar!\nPor Favor Actualice el S.O, Si aun tienes Problemas contacta con el Desarrollador.")
    sys.exit(0)
elif res_width < 1024 or res_height < 768: 
    tk.messagebox.showerror("Low Screen Resolution Detected! | Baja Resolución de Pantalla Detectada!", "A Display Resolution of 1024 x 768 or Higher is Required to Work!\nIf you still have Problems contact the Developer.\n\nSe requiere una Resolucion de Pantalla de 1024 x 768 para Funcionar!\nSi aun tienes Problemas contacta con el Desarrollador.")
    sys.exit(0)
else: 
    DWI()