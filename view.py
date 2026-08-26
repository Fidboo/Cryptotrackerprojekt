import tkinter as tk
from tkinter import ttk

class CryptoView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Krypto Tracker")
        self.geometry("550x400")

        self._build_ui()

    def _build_ui(self):
        input_frame = ttk.Frame(self)
        input_frame.pack(padx=10, pady=10, fill="x")

        lbl_input = ttk.Label(input_frame, text="Krypto ID:")
        lbl_input.pack(side="left", padx=(0, 5))

        self.entry_crypto = ttk.Entry(input_frame)
        self.entry_crypto.pack(side="left", padx=(0, 5))

        self.btn_add = ttk.Button(input_frame, text="Tilføj")
        self.btn_add.pack(side="left", padx=2)

        self.btn_remove = ttk.Button(input_frame, text="Fjern")
        self.btn_remove.pack(side="left", padx=2)

        self.btn_refresh = ttk.Button(input_frame, text="Opdater")
        self.btn_refresh.pack(side="right")

        table_frame = ttk.Frame(self)
        table_frame.pack(padx=10, pady=5, fill="both", expand=True)

        columns = ("crypto", "price", "change")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        
        self.tree.heading("crypto", text="Kryptovaluta")
        self.tree.heading("price", text="Pris (DKK)")
        self.tree.heading("change", text="24t Ændring")

        self.tree.pack(fill="both", expand=True)

        self.lbl_status = ttk.Label(self, text="Klar")
        self.lbl_status.pack(padx=10, pady=5, fill="x")

    def get_input_name(self) -> str:
        """Henter teksten fra inputfeltet og tømmer feltet."""
        name = self.entry_crypto.get().strip().lower()
        self.entry_crypto.delete(0, tk.END)
        return name

    def display_prices(self, price_data: dict, currency: str = "dkk"):
        """Udfylder tabellen med rå data uden farvekoder."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not price_data:
            return

        for crypto, details in price_data.items():
            price = details.get(currency, 0.0)
            change = details.get(f"{currency}_24h_change", 0.0)
            
            self.tree.insert("", "end", values=(crypto.capitalize(), f"{price} kr.", f"{change:.2f}%"))

    def show_status(self, message: str, is_error: bool = False):
        """Viser statusbesked i bunden."""
        self.lbl_status.config(text=message)