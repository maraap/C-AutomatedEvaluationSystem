import tkinter as tk
import tkinter.ttk as ttk
from tkinter import E, scrolledtext, filedialog, messagebox, simpledialog
import os
import csv
import time
cale_fisier=os.path.join(os.path.dirname(os.path.abspath(__file__)), "1.txt")
detalii_problema=os.path.join(os.path.dirname(os.path.abspath(__file__)), "detalii.txt")

from Eval_std import Eval_std

class GUI:
    
    def setup(self, root):
        self.root=root
        self.root.title("Evaluator automat C++")
        self.root.geometry("600x450")
        self.root.config(bg="#7A94BB")
        style=ttk.Style()
        style.theme_use("clam")
        title=tk.Label(root, text="Evaluator Automat C++", font=("Segoe UI", 18, "bold"),bg="#7A94BB", fg="white")
        title.pack(pady=20)
        self.pagina_principala()
        
    def pagina_principala(self):
        self.bg_img=tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),"gradient.png"))
        self.pagina_principala_frame=tk.Frame(self.root)
        self.pagina_principala_frame.pack(fill="both", expand=True)
        bg_label = tk.Label(self.pagina_principala_frame, image=self.bg_img)
        bg_label.place(relwidth=1, relheight=1)
        card=tk.Frame(self.pagina_principala_frame, bg="#94c2d8", bd=0)
        card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=280)
        titlu_card=tk.Label(card, text="Alege modul de evaluare:", font=("Segoe UI", 16, "bold"), bg="#94c2d8", fg="white").pack(pady=(30,10))

        tema_buton=tk.Button(card, text="Tema Student", bg="#2563eb", fg="white", font=("Segoe UI", 13, "bold"), activebackground="#1d4ed8", relief="flat", padx=20, pady=14, command=self.treci_la_lista_probleme1)
        tema_buton.pack(fill="x", padx=30, pady=10)

        teme_buton=tk.Button(card, text="Teme Multiple Student", bg="#b274be", fg="white", font=("Segoe UI", 13, "bold"), activebackground="#6b7280", relief="flat", padx=20, pady=12,command=self.treci_la_teme_multiple_student)
        teme_buton.pack(fill="x",padx=30, pady=10)

    def teme_multiple_student(self):
        self.teme_multiple_student_frame=tk.Frame(self.root, bg="white")
        self.teme_multiple_student_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.teme_multiple_student_canvas=self.creare_canvas(self.teme_multiple_student_frame)

        self.frame_probleme=tk.LabelFrame(self.teme_multiple_student_canvas, text="Incarca mai multe teme studenti:", bg="white")
        self.frame_probleme.pack(fill="both", padx=10, pady=10)

        self.buton=tk.Button(self.frame_probleme, text="Alege fisier cu probleme", bd=0, relief="flat", command="disabled")
        self.buton.pack(side="left", padx=10, pady=10)

        self.cpp_label=tk.Label(self.frame_probleme, text="Niciun fisier selectat", bg="white")
        self.cpp_label.pack(side="left")
      
        self.buton_evalueaza= tk.Button(self.teme_multiple_student_canvas, text="Evalueaza", bg="#4CAF50", bd=0, relief="flat", height=2, width=9, fg="white", state="disabled")
        self.buton_evalueaza.pack(pady=15)
       
        self.result_box=scrolledtext.ScrolledText(self.teme_multiple_student_canvas, width=10, height=10)
        self.result_box.pack(padx=10, pady=10, fill="both", expand=True)
        
        columns = ("student", "problema", "stare", "scor")
        self.tree = ttk.Treeview(self.result_box, columns=columns, show="headings", height=20)
        self.tree.heading("student", text="Student")
        self.tree.column("student", width=150)
        self.tree.heading("problema", text="Problema")
        self.tree.column("problema", width=80)
        self.tree.heading("stare", text="Stare")
        self.tree.column("stare", width=80)
        self.tree.heading("scor", text="Scor")
        self.tree.column("scor", width=80)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)



        self.buton_back=tk.Button(self.teme_multiple_student_canvas, text="Inapoi", bg="#f44336", fg="white", bd=0, relief="groove", height=2, width=7, command=self.treci_la_meniu2)
        self.buton_back.pack(side="bottom", pady=10)

    def creare_canvas(self, canvas_frame):

        self.canvas=tk.Canvas(canvas_frame, bg="white")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar=tk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        frame=tk.Frame(self.canvas, bg="white")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas_window=self.canvas.create_window((0,0), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas.find_all()[0], width=e.width))

        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.root.bind_all("<MouseWheel>", _on_mousewheel)
        return frame

    def lista_probleme(self):

        self.lista_probleme_frame=tk.Frame(self.root, bg="white")
        self.lista_probleme_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.cards_frame=self.creare_canvas(self.lista_probleme_frame)

        lista_probleme=self.citeste_probleme(cale_fisier)
        for problema in lista_probleme:
         self.card=tk.Frame(self.cards_frame, bg="white", bd=1, relief="solid")
         self.card.pack(padx=40, pady=40, fill="x")

         self.header=tk.Frame(self.card, bg="#b1cbed")
         self.header.pack(fill="x")

         self.title_label=tk.Label(self.header, text=problema['nume'], font=("Segoe UI", 16, "bold"), bg="#b1cbed", fg="#093a7a")
         self.title_label.pack(side="left", padx=10, pady=10)

         self.id_label=tk.Label(self.header, text=problema['id'], font=("Segoe UI", 10, "bold"), bg="#b1cbed", fg="#093a7a")
         self.id_label.pack(side="right", padx=10) 
        
         self.description=tk.Label(self.card, text=problema['descriere'], font=("Segoe UI", 11), bg="white", wraplength=750, justify="left")
         self.description.pack(padx=15, pady=15, anchor="w")
         def actual_wraplength(self,event):
             latime=event.width-40
             self.description.config(wraplength=latime)
         self.card.bind("<Configure>", actual_wraplength)

         self.button_frame=tk.Frame(self.card,bg="white")
         self.button_frame.pack(fill="x", pady=15)

         self.rezolva_btn=tk.Button(self.button_frame, text="Rezolva", bg="#b274be", fg="white", command=lambda p=problema["nume"] :self.treci_la_evaluator(p), font=("Segoe UI", 11, "bold"), padx=20, pady=8, relief="flat")
         self.rezolva_btn.pack(side="right", padx=15)

        self.buton_back=tk.Button(self.cards_frame, text="Inapoi", bg="#f44336", fg="white", bd=0, relief="flat", command=self.treci_la_meniu1, height=2, width=8)
        self.buton_back.pack(side="bottom", pady=5)

    def pagina_evaluator(self, nume_problema):

        self.pagina_evaluator_canvas=tk.Frame(self.root, bg="white")
        self.pagina_evaluator_canvas.pack(fill="both", expand=True, padx=20, pady=10)

        self.pagina_evaluator_frame=self.creare_canvas(self.pagina_evaluator_canvas)

        self.director_proiect=os.path.dirname(os.path.abspath(__file__))
        self.cale_folder_problema=os.path.join(self.director_proiect, "date_probleme", nume_problema, detalii_problema)
        self.date=self.citeste_detalii_problema(self.cale_folder_problema)

        self.titlu_cerinta=tk.Label(self.pagina_evaluator_frame, text="Cerinta:", font=("Segoe UI", 18, "bold"), bg="white", fg="#093a7a")
        self.titlu_cerinta.pack(padx=10, pady=10, anchor="w")

        self.cerinta=tk.Label(self.pagina_evaluator_frame, text=self.date["cerinta"], font=("Segoe UI", 12), bg="white", wraplength=900, justify="left")
        self.cerinta.pack(padx=10, pady=5, anchor="w")

        self.titlu_date_intrare=tk.Label(self.pagina_evaluator_frame, text="Date Intrare:", font=("Segoe UI", 18, "bold"), bg="white", fg="#a83ebd")
        self.titlu_date_intrare.pack(padx=10, pady=10, anchor="w")  

        self.date_intrare=tk.Label(self.pagina_evaluator_frame, text=self.date["date_intrare"], font=("Segoe UI", 12), bg="white", wraplength=750, justify="left")
        self.date_intrare.pack(padx=10, pady=5, anchor="w")

        self.titlu_date_iesire=tk.Label(self.pagina_evaluator_frame, text="Date Iesire:", font=("Segoe UI", 18, "bold"), bg="white", fg="#a83ebd")
        self.titlu_date_iesire.pack(padx=10, pady=10, anchor="w")

        self.date_iesire=tk.Label(self.pagina_evaluator_frame, text=self.date["date_iesire"], font=("Segoe UI", 12), bg="white", justify="left")
        self.date_iesire.pack(padx=10, pady=5, anchor="w")

        self.titlu_restrictii=tk.Label(self.pagina_evaluator_frame, text="Restrictii:", font=("Segoe UI", 18, "bold"), bg="white", fg="#093a7a")
        self.titlu_restrictii.pack(padx=10, pady=10, anchor="w")

        self.restrictii=tk.Label(self.pagina_evaluator_frame, text=self.date["restrictii"], font=("Segoe UI", 12), bg="white", justify="left")
        self.restrictii.pack(padx=10, pady=5, anchor="w")
        self.text_wrap=[self.cerinta, self.date_intrare, self.date_iesire, self.restrictii]

        def actualizeaza_wraplength(self, event):
            latime=event.width-40
            for text in self.text_wrap:
                text.config(wraplength=latime)

        self.pagina_evaluator_frame.bind("<Configure>", actualizeaza_wraplength)

        self.cpp_path=None
        self.probleme_path=None

        frame_cpp=tk.LabelFrame(self.pagina_evaluator_frame, text="Fisier C++", bg="white")
        frame_cpp.pack(fill="x", padx=10, pady=10)

        tk.Button(frame_cpp, text="Alege fisier C++", bd=0, relief="flat", height=1, width=15, command=self.load_cpp).pack(side="left", padx=10)
        self.cpp_label=tk.Label(frame_cpp, text="Niciun fisier selectat", bg="white")
        self.cpp_label.pack(side="left")

        tk.Button(frame_cpp, text="Sterge fisier C++", bg="#f44336", fg="white", bd=0, relief="raised", anchor="e", command=self.sterge_cpp).pack(side="left", padx=5)

        self.buton_eval=tk.Button(self.pagina_evaluator_frame, text="Evalueaza", bg="#4CAF50", fg="white", bd=0, relief="flat", height=2, width=14, command=lambda p=nume_problema :self.evaluare(p))
        self.buton_eval.pack(pady=10)
       
        self.buton_back=tk.Button(self.pagina_evaluator_frame, text="Inapoi", bg="#f44336", fg="white", bd=0, relief="flat", height=2, width=12, command=self.treci_la_lista_probleme2)
        self.buton_back.pack(side="bottom", pady=10)


    def tabel_rezultat(self, numar_teste):
        self.result_box=scrolledtext.ScrolledText(self.pagina_evaluator_frame, width=10, height=10)
        self.result_box.pack(padx=10, pady=10, fill="both", expand=True)

        columns = ("test", "timp", "status", "detalii", "punctaj")
        self.tabel_problema = ttk.Treeview(self.result_box, columns=columns, show="headings", height=numar_teste)
        self.tabel_problema.heading("test", text="Test")
        self.tabel_problema.column("test", width=80, anchor="center")
        self.tabel_problema.heading("timp", text="Timp")
        self.tabel_problema.column("timp", width=50, anchor="center")
        self.tabel_problema.heading("status", text="Status")
        self.tabel_problema.column("status", width=100, anchor="center")
        self.tabel_problema.heading("detalii", text="Detalii")
        self.tabel_problema.column("detalii", width=350, anchor="center")
        self.tabel_problema.heading("punctaj", text="Punctaj")
        self.tabel_problema.column("punctaj", width=80, anchor="center")
        self.tabel_problema.tag_configure('corect', background='#33cc33')
        self.tabel_problema.tag_configure('incorect', background='#ff0000')
        self.tabel_problema.tag_configure('eroare', background='#ff6666')
        self.tabel_problema.pack(fill="both", expand=True, padx=10, pady=10)
    
    def treci_la_lista_probleme1(self):
        self.pagina_principala_frame.pack_forget()
        self.lista_probleme()

    def treci_la_lista_probleme2(self):
        self.pagina_evaluator_canvas.pack_forget()
        self.lista_probleme()

    def treci_la_evaluator(self, nume_problema):
        self.lista_probleme_frame.pack_forget()
        self.pagina_evaluator(nume_problema)

    def treci_la_meniu1(self):
        self.lista_probleme_frame.pack_forget()
        self.pagina_principala()

    def treci_la_meniu2(self):
        self.teme_multiple_student_frame.pack_forget()
        self.pagina_principala()

    def treci_la_teme_multiple_student(self):
        self.pagina_principala_frame.pack_forget()
        self.teme_multiple_student()

    def citeste_probleme(self, cale_fisier):
        lista_probleme=[]
        if not os.path.exists(cale_fisier):
            messagebox.showerror("Eroare", f"Nu am gasit fisierul la calea: {cale_fisier}")
            return []
        try:
             with open(cale_fisier, 'r', encoding='utf-8') as f:
                 campuri=["nume", "id", "descriere"]
                 cititor=csv.DictReader(f, fieldnames=campuri, skipinitialspace=True)
                 for rand in cititor:
                     lista_probleme.append(rand)
             
        except FileNotFoundError as e:
           messagebox.showerror("Eroare", f"Fisierul nu a fost gasit: {e.filename}")
        return lista_probleme

    def load_cpp(self):
         path=filedialog.askopenfilename(title="Alege fisier C++", filetypes=[("Fisiere C++", "*.cpp")])
         if path:
             self.cpp_path=path
             self.cpp_label.config(text=os.path.basename(path))

    def sterge_cpp(self):
        self.cpp_path=None
        self.cpp_label.config(text="Niciun fisier selectat")
        
    def citeste_detalii_problema(self, cale_fisier):
        detalii={
            "cerinta": "",
            "date_intrare": "",
            "date_iesire": "",
            "restrictii": ""
            }
        mapare_sectiuni={
            "Cerinta:": "cerinta",
            "Date Intrare:": "date_intrare",
            "Date Iesire:": "date_iesire",
            "Restrictii:": "restrictii"
            }

        sectiune_curenta=None

        if not os.path.exists(cale_fisier):
            messagebox.showerror("Eroare", f"Nu am gasit fisierul la calea: {cale_fisier}")
            return detalii

        try:
            with open(cale_fisier, 'r', encoding='utf-8') as f:
                for linie in f:
                    linie_curata=linie.strip()
                    if linie_curata in mapare_sectiuni:
                        sectiune_curenta=mapare_sectiuni[linie_curata]
                        continue
                    if sectiune_curenta:
                        detalii[sectiune_curenta]+=linie
        except FileNotFoundError as e:
            messagebox.showerror("Eroare", f"Fisierul nu a fost gasit: {e.filename}")
        return detalii

    def evaluare(self, nume_problema):
            evaluator=Eval_std()
            self.probleme_path=os.path.join(self.director_proiect, "date_probleme", nume_problema ,"teste")
            if not os.path.isdir(self.probleme_path):
                messagebox.showerror("Eroare", f"Folder teste invalid: {self.probleme_path}.")
            if not self.cpp_path:
                messagebox.showwarning("Atentie!", "Selecteaza fisierul C++!")
                return
            fisiere=sorted(os.listdir(self.probleme_path))
            numar_teste=len([f for f in fisiere if f.endswith(".in")])
            punctaj_total=100
            punctaj_test=punctaj_total/numar_teste if numar_teste>0 else 0
            scor_final=0
            self.tabel_rezultat(numar_teste)
            for item in self.tabel_problema.get_children():
                self.tabel_problema.delete(item)
            executabil="student_exec.exe"
            succes_compilare, mesaj=evaluator.rulare_cod_student(self.cpp_path,executabil)

            if not succes_compilare:
                messagebox.showerror("Eroare Compilare", mesaj)
                return
            
            teste_gasite=False
            for fisier in fisiere:
                if fisier.endswith(".in"):
                    teste_gasite=True 
                    cale_in=os.path.join(self.probleme_path,fisier)
                    nume_fara_ext=os.path.splitext(fisier)[0]
                    cale_out=os.path.join(self.probleme_path, nume_fara_ext+".out")
    
                    date_in, date_out, err=evaluator.citeste_teste(cale_in, cale_out)
                    
                    if err:
                        self.tabel_problema.insert("", "end", values=(fisier, "-", "Eroare Fisier", err, "N/A"), tags="eroare")
                   
                    start_time=time.perf_counter() 

                    succes_exec, output_student=evaluator.executa_program(self.cpp_path,executabil, date_in)
                    
                    end_time=time.perf_counter()
                    timp_exec=f"{(end_time - start_time):.4f}secunde"

                    if not succes_exec:
                        self.tabel_problema.insert("", "end", values=(fisier, "-", "Runtime Error", output_student, f"0/{punctaj_test}"), tags="eroare")
                      
                    else:
                        mesaj_eval=evaluator.evalueaza_rezultatul(output_student, date_out)
                        if "Raspuns Corect" in mesaj_eval:
                            status="Corect"
                            self.tabel_problema.insert("", "end", values=(fisier, timp_exec, status, mesaj_eval, f"{punctaj_test}/{punctaj_test}"), tags="corect")
                            scor_final+=punctaj_test
                        else: 
                            status="Incorect"
                            self.tabel_problema.insert("", "end", values=(fisier, timp_exec, status, mesaj_eval, f"0/{punctaj_test}"), tags="incorect")
                        
                self.root.update_idletasks()
            if not teste_gasite:
               messagebox.showinfo("Info", "Nu am gasit fisiere.in in folderul selectat.")

root=tk.Tk()
app=GUI()
app.setup(root)
root.mainloop()


