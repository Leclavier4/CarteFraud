import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

class ModernCreditFraudDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de Détection de Fraude")
        self.root.geometry("1000x800")
        
        self.style = ttk.Style("cyborg")
        
        self.main_container = ttk.Frame(root, padding="20")
        self.main_container.pack(fill=BOTH, expand=YES)
        
        self.create_header()
        self.create_main_area()
        self.create_transaction_history()
        self.create_footer()
        
    def analyze_transaction(self):
        """Analyse la transaction avec des validations améliorées"""
        card = self.card_number_field.get()
        amount = self.amount_field.get()
        trans_type = self.type_field.get()
        time = self.time_field.get()
        location = self.location_field.get()
        
        # Validation de base
        if not all([card, amount, trans_type, time, location]):
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
            return

        # Validation du numéro de carte
        card_cleaned = card.replace(" ", "")
        if not card_cleaned.isdigit() or len(card_cleaned) != 16:
            messagebox.showerror("Erreur", "Numéro de carte invalide. La carte doit contenir 16 chiffres.")
            return

        # Validation du montant
        try:
            amount_value = float(amount.replace("FCFA", "").strip())
            if amount_value <= 0:
                messagebox.showerror("Erreur", "Le montant doit être supérieur à 0")
                return
        except ValueError:
            messagebox.showerror("Erreur", "Montant invalide")
            return

        # Validation de l'heure
        try:
            datetime.strptime(time, "%H:%M")
        except ValueError:
            messagebox.showerror("Erreur", "Format d'heure invalide. Utilisez le format HH:MM")
            return

        # Validation de la localisation
        if any(char.isdigit() for char in location):
            messagebox.showerror("Erreur", "La localisation ne doit pas contenir de chiffres")
            return

        # Si toutes les validations sont passées, procéder à l'analyse
        try:
            is_suspicious = amount_value > 1000
            
            status = "Suspect" if is_suspicious else "Légitime"
            score = "45%" if is_suspicious else "98%"
            
            self.tree.insert("", 0, values=(
                datetime.now().strftime("%Y-%m-%d %H:%M"),
                f"{amount_value:.2f} FCFA",
                trans_type,
                status,
                score
            ))
            
            if is_suspicious:
                messagebox.showwarning("Attention", "Transaction suspecte détectée !")
            else:
                messagebox.showinfo("Succès", "Transaction légitime")
                
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {str(e)}")
            
    def create_header(self):
        """Crée l'en-tête de l'application"""
        header_frame = ttk.Frame(self.main_container)
        header_frame.pack(fill=X, pady=(0, 20))
        
        title_frame = ttk.Frame(header_frame)
        title_frame.pack(pady=10)
        
        logo_label = ttk.Label(
            title_frame,
            text="🔒",
            font=("Helvetica", 36)
        )
        logo_label.pack()
        
        title_label = ttk.Label(
            title_frame,
            text="Détection de Fraude",
            font=("Helvetica", 24, "bold"),
            bootstyle="primary"
        )
        title_label.pack(pady=5)
        
        subtitle_label = ttk.Label(
            title_frame,
            text="Système de surveillance en temps réel",
            font=("Helvetica", 12),
            bootstyle="light"
        )
        subtitle_label.pack()
        
    def create_main_area(self):
        """Crée la zone principale avec le formulaire"""
        form_frame = ttk.LabelFrame(
            self.main_container,
            text="Nouvelle Transaction",
            padding="20"
        )
        form_frame.pack(fill=X, pady=20)
        
        form_grid = ttk.Frame(form_frame)
        form_grid.pack(fill=X)
        
        form_grid.columnconfigure(1, weight=1)
        
        fields = [
            ("Numéro de carte", "card_number", "Ex: 1234 5678 9012 3456"),
            ("Montant (FCFA)", "amount", "Montant"),
            ("Type de transaction", "type", None),
            ("Heure", "time", "HH:MM"),
            ("Localisation", "location", "Ville, Pays")
        ]
        
        for i, (label, name, placeholder) in enumerate(fields):
            ttk.Label(
                form_grid,
                text=label,
                font=("Helvetica", 11),
                bootstyle="light"
            ).grid(row=i, column=0, padx=(0, 20), pady=10, sticky=W)
            
            if name == "type":
                field = ttk.Combobox(
                    form_grid,
                    values=["Achat en ligne", "Achat en magasin", "Retrait", "Transfert"],
                    width=30
                )
            else:
                field = ttk.Entry(form_grid, width=30)
                if placeholder:
                    field.insert(0, placeholder)
                    field.bind("<FocusIn>", lambda e, f=field, p=placeholder: self.clear_placeholder(e, f, p))
                    field.bind("<FocusOut>", lambda e, f=field, p=placeholder: self.restore_placeholder(e, f, p))
            
            field.grid(row=i, column=1, sticky=EW)
            setattr(self, f"{name}_field", field)
        
        ttk.Button(
            form_frame,
            text="Analyser la Transaction",
            command=self.analyze_transaction,
            bootstyle="primary",
            width=20
        ).pack(pady=(20, 0))
        
    def create_transaction_history(self):
        """Crée la section historique des transactions"""
        history_frame = ttk.LabelFrame(
            self.main_container,
            text="Historique des Transactions",
            padding="20"
        )
        history_frame.pack(fill=BOTH, expand=YES, pady=20)
        
        columns = ("Date", "Montant", "Type", "Statut", "Score")
        self.tree = ttk.Treeview(history_frame, columns=columns, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        self.tree.pack(fill=BOTH, expand=YES)
        
        sample_data = [
            (datetime.now().strftime("%Y-%m-%d %H:%M"), "150.00 FCFA", "Achat", "Légitime", "98%"),
            (datetime.now().strftime("%Y-%m-%d %H:%M"), "1200.00 FCFA", "Retrait", "Suspect", "45%"),
        ]
        
        for item in sample_data:
            self.tree.insert("", END, values=item)
            
    def create_footer(self):
        """Crée le pied de page avec les statistiques"""
        footer_frame = ttk.Frame(self.main_container)
        footer_frame.pack(fill=X, pady=(0, 20))
        
        stats = [
            ("Transactions aujourd'hui", "127"),
            ("Alertes", "3"),
            ("Score moyen", "96%")
        ]
        
        for text, value in stats:
            stat_frame = ttk.Frame(footer_frame)
            stat_frame.pack(side=LEFT, expand=YES, padx=10)
            
            ttk.Label(
                stat_frame,
                text=text,
                font=("Helvetica", 10),
                bootstyle="secondary"
            ).pack()
            
            ttk.Label(
                stat_frame,
                text=value,
                font=("Helvetica", 16, "bold"),
                bootstyle="primary"
            ).pack()
            
    def clear_placeholder(self, event, field, placeholder):
        """Efface le placeholder quand le champ reçoit le focus"""
        if field.get() == placeholder:
            field.delete(0, END)
            field.configure(foreground="light")
            
    def restore_placeholder(self, event, field, placeholder):
        """Restaure le placeholder si le champ est vide"""
        if not field.get():
            field.insert(0, placeholder)
            field.configure(foreground="gray")

if __name__ == "__main__":
    root = ttk.Window()
    app = ModernCreditFraudDetectionApp(root)
    root.mainloop()