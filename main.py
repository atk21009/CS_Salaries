import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from functions import main
from pandastable import Table


class App(tk.Tk):
    def __init__(self):
        # main setup
        super().__init__()

        self.geometry("2000x800")
        self.minsize(800, 800)
        self.title("CS Salaries")
        self.iconbitmap("./imgs/cs.ico")

        # widgets

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}

        for F in (Content, ContentData):
            frame = F(container, self)
            self.frames[F] = frame

        self.show_frame(Content)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Content(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets(parent, controller)

    def create_widgets(self, parent, controller):
        Nav(self, controller)

        frame = tk.Frame(self, background="#c5c5c5")
        frame.place(relx=0.1, y=0, relwidth=0.9, relheight=1)

        context = tk.Frame(frame, background="white")
        context.place(
            relwidth=0.7,
            relheight=0.5,
            rely=0.25,
            relx=0.15,
        )

        test = ttk.Label(
            context, text="Dashboard", font=("Arial Bold", 24), background="white"
        )
        test.pack(pady=10)

        desc = ttk.Label(
            context,
            font=("Arial", 10),
            background="white",
            text="This application aims to show real world data of different computer science fields. In this application it allows for filtering data to see different aspects of the computer science field. In this application users can filter work year, experience levels, employment types, job titles, salaries, residence, remote ratio, location, and company size. This aims to give a better understanding of different fields and routes programmers can take. It gives a general idea of how much computer science fields make, their remote availability and locations that are offering these choices. It gives a general size of the company as well to show what size of companies are offering these aspects of the employment.",
        )
        desc.bind(
            "<Configure>",
            lambda e: desc.config(wraplength=(context.winfo_width() - 60)),
        )
        desc.pack(anchor="w", padx=30, fill="x")

        lbal_container = tk.Frame(context, background="white")
        lbal_container.pack(anchor="w", padx=30, pady=30)

        lbal_label = ttk.Label(
            lbal_container,
            font=("Arial Bold", 12),
            text="Filter Fields",
            background="white",
        )
        lbal_label.pack(anchor="w")

        lbal = BLabel(master=lbal_container)
        lbal.add_option("Work Year")
        lbal.add_option("Experience Level")
        lbal.add_option("Employment Type")
        lbal.add_option("Job Title")
        lbal.add_option("Salary")
        lbal.add_option("Employee Residence")
        lbal.add_option("Remote Ratio")
        lbal.add_option("Company Location")
        lbal.add_option("Company Size")
        lbal.l.pack(anchor="w")


class ContentData(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=1)

        s = ttk.Style()
        s.configure("Content.TFrame", background="#c5c5c5")

        self["style"] = "Content.TFrame"
        self.create_widgets(parent, controller)

    def create_widgets(self, parent, controller):
        Nav(self, controller)
        frame = tk.Frame(self, background="red")
        frame.place(relx=0.10, y=0, relwidth=0.9, relheight=1)

        context = tk.Frame(frame, background="white")
        context.place(
            relwidth=1,
            relheight=1,
            rely=0,
            relx=0,
        )

        selection_frame = tk.Frame(context)
        selection_frame.grid(sticky="NSEW", column=0)
        selection_frame.columnconfigure(tuple(range(12)), weight=1)
        selection_frame.place(relwidth=1)

        style = ttk.Style()
        style.configure("TCombobox", foreground="#000000", font=("Arial Bold", 10))

        self.option_add("*TCombobox*Font", ("Arial Bold", 10))
        self.option_add("*TCombobox*Listbox*selectForeground", "#ffffff")
        self.option_add("*TCombobox*Listbox*selectBackground", "#2d2d2d")
        self.option_add("*TCombobox*Listbox*Font", ("Arial Bold", 8))
        self.option_add("*TCombobox*Listbox*Background", "#c5c5c5")

        WY = ttk.Combobox(
            selection_frame,
            state="readonly",
            values=[2023, 2022, 2021, 2020],
            justify="center",
        )
        WY.set("Work Year")
        WY.grid(row=0, column=0, sticky="NSEW")

        EL = ttk.Combobox(
            selection_frame,
            state="readonly",
            values=["EN", "EX", "MI", "SE"],
            justify="center",
        )
        EL.set("Experience Level")
        EL.grid(row=0, column=1, sticky="NSEW")

        ET = ttk.Combobox(
            selection_frame,
            state="readonly",
            values=["FT", "CT", "FL", "PT"],
            justify="center",
        )
        ET.set("Employment Type")
        ET.grid(row=0, column=2, sticky="NSEW")

        jt_values = [
            "Principal Data Scientist",
            "ML Engineer",
            "Data Scientist",
            "Applied Scientist",
            "Data Analyst",
            "Data Modeler",
            "Research Engineer",
            "Analytics Engineer",
            "Business Intelligence Engineer",
            "Machine Learning Engineer",
            "Data Strategist",
            "Data Engineer",
            "Computer Vision Engineer",
            "Data Quality Analyst",
            "Compliance Data Analyst",
            "Data Architect",
            "Applied Machine Learning Engineer",
            "AI Developer",
            "Research Scientist",
            "Data Analytics Manager",
            "Business Data Analyst",
            "Applied Data Scientist",
            "Staff Data Analyst",
            "ETL Engineer",
            "Data DevOps Engineer",
            "Head of Data",
            "Data Science Manager",
            "Data Manager",
            "Machine Learning Researcher",
            "Big Data Engineer",
            "Data Specialist",
            "Lead Data Analyst",
            "BI Data Engineer",
            "Director of Data Science",
            "Machine Learning Scientist",
            "MLOps Engineer",
            "AI Scientist",
            "Autonomous Vehicle Technician",
            "Applied Machine Learning Scientist",
            "Lead Data Scientist",
            "Cloud Database Engineer",
            "Financial Data Analyst",
            "Data Infrastructure Engineer",
            "Software Data Engineer",
            "AI Programmer",
            "Data Operations Engineer",
            "BI Developer",
            "Data Science Lead",
            "Deep Learning Researcher",
            "BI Analyst",
            "Data Science Consultant",
            "Data Analytics Specialist",
            "Machine Learning Infrastructure Engineer",
            "BI Data Analyst",
            "Head of Data Science",
            "Insight Analyst",
            "Deep Learning Engineer",
            "Machine Learning Software Engineer",
            "Big Data Architect",
            "Product Data Analyst",
            "Computer Vision Software Engineer",
            "Azure Data Engineer",
            "Marketing Data Engineer",
            "Data Analytics Lead",
            "Data Lead",
            "Data Science Engineer",
            "Machine Learning Research Engineer",
            "NLP Engineer",
            "Manager Data Management",
            "Machine Learning Developer",
            "3D Computer Vision Researcher",
            "Principal Machine Learning Engineer",
            "Data Analytics Engineer",
            "Data Analytics Consultant",
            "Data Management Specialist",
            "Data Science Tech Lead",
            "Data Scientist Lead",
            "Cloud Data Engineer",
            "Data Operations Analyst",
            "Marketing Data Analyst",
            "Power BI Developer",
            "Product Data Scientist",
            "Principal Data Architect",
            "Machine Learning Manager",
            "Lead Machine Learning Engineer",
            "ETL Developer",
            "Cloud Data Architect",
            "Lead Data Engineer",
            "Head of Machine Learning",
            "Principal Data Analyst",
            "Principal Data Engineer",
            "Staff Data Scientist",
            "Finance Data Analyst",
        ]
        jt_values.sort()
        JT = ttk.Combobox(
            selection_frame, state="readonly", values=jt_values, justify="center"
        )
        JT.set("Job Title")
        JT.grid(row=0, column=3, sticky="NSEW")

        S = ttk.Combobox(
            selection_frame,
            state="readonly",
            values=[25000, 50000, 75000, 100000, 150000, 200000, 250000],
            justify="center",
        )
        S.set("Salary")
        S.grid(row=0, column=4, sticky="NSEW")

        ER_values = [
            "ES",
            "US",
            "CA",
            "DE",
            "GB",
            "NG",
            "IN",
            "HK",
            "PT",
            "NL",
            "CH",
            "CF",
            "FR",
            "AU",
            "FI",
            "UA",
            "IE",
            "IL",
            "GH",
            "AT",
            "CO",
            "SG",
            "SE",
            "SI",
            "MX",
            "UZ",
            "BR",
            "TH",
            "HR",
            "PL",
            "KW",
            "VN",
            "CY",
            "AR",
            "AM",
            "BA",
            "KE",
            "GR",
            "MK",
            "LV",
            "RO",
            "PK",
            "IT",
            "MA",
            "LT",
            "BE",
            "AS",
            "IR",
            "HU",
            "SK",
            "CN",
            "CZ",
            "CR",
            "TR",
            "CL",
            "PR",
            "DK",
            "BO",
            "PH",
            "DO",
            "EG",
            "ID",
            "AE",
            "MY",
            "JP",
            "EE",
            "HN",
            "TN",
            "RU",
            "DZ",
            "IQ",
            "BG",
            "JE",
            "RS",
            "NZ",
            "MD",
            "LU",
            "MT",
        ]
        ER_values.sort()
        ER = ttk.Combobox(
            selection_frame, state="readonly", values=ER_values, justify="center"
        )
        ER.set("Employee Residence")
        ER.grid(row=0, column=5, sticky="NSEW")

        RR = ttk.Combobox(
            selection_frame, state="readonly", values=[0, 50, 100], justify="center"
        )
        RR.set("Remote Ratio")
        RR.grid(row=0, column=6, sticky="NSEW")

        CL_values = [
            "ES",
            "US",
            "CA",
            "DE",
            "GB",
            "NG",
            "IN",
            "HK",
            "NL",
            "CH",
            "CF",
            "FR",
            "FI",
            "UA",
            "IE",
            "IL",
            "GH",
            "CO",
            "SG",
            "AU",
            "SE",
            "SI",
            "MX",
            "BR",
            "PT",
            "RU",
            "TH",
            "HR",
            "VN",
            "EE",
            "AM",
            "BA",
            "KE",
            "GR",
            "MK",
            "LV",
            "RO",
            "PK",
            "IT",
            "MA",
            "PL",
            "AL",
            "AR",
            "LT",
            "AS",
            "CR",
            "IR",
            "BS",
            "HU",
            "AT",
            "SK",
            "CZ",
            "TR",
            "PR",
            "DK",
            "BO",
            "PH",
            "BE",
            "ID",
            "EG",
            "AE",
            "LU",
            "MY",
            "HN",
            "JP",
            "DZ",
            "IQ",
            "CN",
            "NZ",
            "CL",
            "MD",
            "MT",
        ]
        CL_values.sort()
        CL = ttk.Combobox(
            selection_frame, state="readonly", values=CL_values, justify="center"
        )
        CL.set("Company Location")
        CL.grid(row=0, column=7, sticky="NSEW")

        CS = ttk.Combobox(
            selection_frame, state="readonly", values=["L", "S", "M"], justify="center"
        )
        CS.set("Company Size")
        CS.grid(row=0, column=8, sticky="NSEW")

        ROWS = ttk.Combobox(
            selection_frame,
            state="readonly",
            values=[25, 50, 100, 200],
            justify="center",
        )
        ROWS.set("Rows")
        ROWS.grid(row=0, column=9, sticky="NSEW")

        def apply_filter():
            vals = [WY, EL, ET, JT, S, ER, RR, CL, CS, ROWS]
            updateVals = [[], [], [], [], [], [], [], [], [], []]
            count = 0
            for val in vals:
                if val.get() in (val["values"]):
                    updateVals[count] = [val.get()]
                count += 1

            if WY.get() in WY["values"]:
                updateVals[0][0] = int(updateVals[0][0])
            if RR.get() in RR["values"]:
                updateVals[6][0] = int(updateVals[6][0])
            if ROWS.get() in ROWS["values"]:
                updateVals[9] = int(updateVals[9][0])
            else:
                updateVals[9] = 100
            datasetUpdate = main(
                "./datasets/ds_salaries.csv",
                updateVals[0],
                updateVals[1],
                updateVals[2],
                updateVals[3],
                updateVals[4],
                updateVals[5],
                updateVals[6],
                updateVals[7],
                updateVals[8],
                updateVals[9],
            )
            pt.model.df = datasetUpdate
            pt.redraw()

        def clear_filter():
            vals = [WY, EL, ET, JT, S, ER, RR, CL, CS, ROWS]
            vals_txt = [
                "Work Year",
                "Experience Level",
                "Employment Type",
                "Job Title",
                "Salary",
                "Employee Residence",
                "Remote Ratio",
                "Company Location",
                "Company Size",
                "Rows",
            ]
            count = 0
            for val in vals:
                val.set(vals_txt[count])
                count += 1
            dataset = main(
                "./datasets/ds_salaries.csv",
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                100,
            )
            pt.model.df = dataset
            pt.redraw()

        filter_btn = tk.Button(
            selection_frame,
            text="Apply Filter",
            command=apply_filter,
            bg="#2d2d2d",
            fg="white",
            font=("Arial Bold", 10),
            relief="flat",
            justify="center",
        )
        filter_btn.grid(row=0, column=10, sticky="NSEW")

        clear_btn = tk.Button(
            selection_frame,
            text="Clear",
            command=clear_filter,
            bg="#2d2d2d",
            fg="white",
            font=("Arial Bold", 10),
            relief="flat",
            justify="center",
        )
        clear_btn.grid(row=0, column=11, sticky="NSEW")

        dataset = main(
            "./datasets/ds_salaries.csv",
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            100,
        )

        table_frame = tk.Frame(context, pady=10)
        table_frame.place(relwidth=1, y=28, relheight=0.97)

        self.table = pt = Table(
            table_frame, dataframe=dataset, rows=5, editable=False, enable_menus=False
        )

        self.table.showIndex = False
        pt.showIndex = False
        pt.show()
        pt.zoomOut()
        pt.zoomOut()
        pt.autoResizeColumns()
        self.table.autoResizeColumns()


class Nav(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.1, relheight=1)

        s = ttk.Style()
        s.configure("Nav.TFrame", border="none", background="#535353")
        self.config(style="Nav.TFrame")

        def switch(e):
            name = e.widget["text"]
            match name:
                case "Computer Science Salaries":
                    controller.show_frame(ContentData)
                case " Dashboard":
                    controller.show_frame(Content)

        self.create_widgets(switch)

    def create_widgets(self, switch):
        self.homeImg = tk.PhotoImage(
            file="./imgs/house-white-silhouette-without-door.png"
        )

        f = font.Font(family="Arial Bold", size=12)
        fB = font.Font(family="Arial Bold", size=10)

        def on_enter(e):
            e.widget["background"] = "#3a3a3a"

        def on_leave(e):
            e.widget["background"] = "#2d2d2d"

        dashboard = tk.Button(
            self,
            text=" Dashboard",
            bg="#2d2d2d",
            image=self.homeImg,
            font=(f),
            height=30,
            compound="left",
            foreground="white",
            borderwidth=0,
            pady=8,
        )
        dashboard.pack(fill="x")
        dashboard.bind("<Enter>", on_enter)
        dashboard.bind("<Leave>", on_leave)
        dashboard.bind("<Button-1>", switch)

        css = tk.Button(
            self,
            text="Computer Science Salaries",
            bg="#2d2d2d",
            font=(fB),
            foreground="white",
            justify="center",
            borderwidth=0,
            pady=8,
        )
        css.pack(fill="x")
        css.bind("<Enter>", on_enter)
        css.bind("<Leave>", on_leave)
        css.bind("<Button-1>", switch)


class BLabel(object):
    b = "•"

    def __init__(self, master):
        import tkinter as tk

        self.l = tk.Label(
            master,
            anchor="w",
            justify="left",
            padx=30,
            font=("Arial", 10),
            background="white",
        )

    def add_option(self, text):
        if self.l.cget("text") == "":
            self.l.config(text=self.b + " " + text)
        else:
            self.l.config(text=self.l.cget("text") + "\n" + self.b + " " + text)


app = App()
app.mainloop()
