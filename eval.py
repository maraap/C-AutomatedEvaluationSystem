class Eval_std:
    def citeste_teste(file_in, file_out):
        try:
             with open(file_in, 'r') as f_in:
                 data_in=f_in.read()
             with open(file_out, 'r') as f_out:
                 data_out=f_out.read()
             return data_in, data_out, None
        except FileNotFoundError as e:
             return None, None, f"Eroare: Fișierul nu a fost găsit: {e.filename}"

    def rulare_cod_student(student_cpp, fisier_exec):
        try:
          rezultat = subprocess.run(
              ['clang++', student_cpp, 
               '-o', fisier_exec,
               '-std=c++20',
               '-Wall'
               ],
              check=True,
              capture_output=True,
              text=True
          )
          if os.path.exists(fisier_exec):
            os.chmod(fisier_exec, 0o755)
        except subprocess.CalledProcessError as e:
          return False, f"Eroare de compilare:\n{e.stderr}"
        except FileNotFoundError:
          return "Error: Compilatorul clang++ nu a fost găsit."
        if rezultat.returncode != 0:
            return False, f"Eroare de compilare:\n{rezultat.stderr}"
        return True, "Compilare reușită."

    def executa_program(fisier_exec, date_intrare, timeout_secunde=30):
   
        if not os.path.isfile(fisier_exec) or not os.access(fisier_exec, os.X_OK):
            return False, "Eroare: Executabilul nu a fost găsit sau nu are permisiuni de rulare."

        try:
            rezultat=subprocess.run(
                ['./' + fisier_exec],
                input=date_intrare,
                capture_output=True,
                text=True,
                timeout=timeout_secunde
                )
            iesire_program = rezultat.stdout.strip()
            return True, iesire_program
        except subprocess.TimeoutExpired:
            return False, "Eroare: Timpul de execuție a fost depășit."
        except Exception as e:
            return False, f"Eroare la rularea programului: {str(e)}"

    def evalueaza_rezultatul(iesire_obtinuta, iesire_asteptata):
        if iesire_obtinuta == iesire_asteptata:
            return "Raspuns Corect."
        else:
            return (
                "Răspuns Incorect."
                f"\n--- Asteptat ---\n{iesire_asteptata}"
                f"\n--- Obtinut ---\n{iesire_obtinuta}"
            )
