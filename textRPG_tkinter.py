## Porão Misterioso — Text RPG com interface Tkinter
## Requer apenas Python 3 (Tkinter já vem instalado)
## Para rodar: python textRPG_tkinter.py

import tkinter as tk
from tkinter import font
import time
import threading

# ── Cores do tema ──────────────────────────────────────────────
BG        = "#1a1a2e"
SURFACE   = "#16213e"
CARD      = "#0f3460"
ACCENT    = "#e94560"
GOLD      = "#f5a623"
TEXT      = "#eaeaea"
MUTED     = "#a0a0b0"
GREEN     = "#a8e6a3"
RED       = "#ff8a80"
BLUE      = "#7ec8e3"


class RPGApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⚔  Porão Misterioso")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)
        self.root.geometry("680x560")

        self.inventory = []
        self._build_ui()
        self.start_game()

    # ── Construção da interface ────────────────────────────────
    def _build_ui(self):
        # Cabeçalho
        header = tk.Frame(self.root, bg=SURFACE, height=42)
        header.pack(fill="x")
        header.pack_propagate(False)

        dots = tk.Frame(header, bg=SURFACE)
        dots.pack(side="left", padx=14, pady=12)
        for color in ("#ff5f57", "#ffbd2e", "#28c840"):
            tk.Label(dots, bg=color, width=1, height=1,
                     relief="flat").pack(side="left", padx=3)

        tk.Label(header, text="⚔  PORÃO MISTERIOSO",
                 bg=SURFACE, fg=GOLD,
                 font=("Courier", 11, "bold")).pack(side="left", padx=4)

        self.inv_label = tk.Label(header, text="inventário: vazio",
                                  bg=SURFACE, fg=MUTED,
                                  font=("Courier", 9))
        self.inv_label.pack(side="right", padx=14)

        # Log de texto
        log_frame = tk.Frame(self.root, bg=BG)
        log_frame.pack(fill="both", expand=True, padx=12, pady=(10, 0))

        self.log = tk.Text(log_frame, bg=BG, fg=TEXT,
                           font=("Courier", 11),
                           wrap="word", state="disabled",
                           relief="flat", bd=0,
                           selectbackground=CARD,
                           height=18, cursor="arrow")
        self.log.pack(side="left", fill="both", expand=True)

        scroll = tk.Scrollbar(log_frame, command=self.log.yview,
                              bg=SURFACE, troughcolor=BG, bd=0,
                              activebackground=MUTED)
        scroll.pack(side="right", fill="y")
        self.log.configure(yscrollcommand=scroll.set)

        # Tags de cor
        self.log.tag_configure("narr",   foreground=TEXT,   lmargin1=8, lmargin2=8, spacing3=4)
        self.log.tag_configure("player", foreground=BLUE,   font=("Courier", 11, "italic"), spacing3=4)
        self.log.tag_configure("result", foreground=GREEN,  lmargin1=8, lmargin2=8, spacing3=4)
        self.log.tag_configure("danger", foreground=RED,    lmargin1=8, lmargin2=8, spacing3=4)
        self.log.tag_configure("system", foreground=MUTED,  justify="center", spacing3=6)
        self.log.tag_configure("gold",   foreground=GOLD,   lmargin1=8, lmargin2=8, spacing3=4)

        # Separador
        tk.Frame(self.root, bg=SURFACE, height=1).pack(fill="x", pady=(8, 0))

        # Área de botões
        self.btn_frame = tk.Frame(self.root, bg=BG, height=90)
        self.btn_frame.pack(fill="x", padx=12, pady=10)

    # ── Helpers de UI ─────────────────────────────────────────
    def add_msg(self, text, tag="narr"):
        self.log.configure(state="normal")
        self.log.insert("end", text + "\n", tag)
        self.log.configure(state="disabled")
        self.log.see("end")

    def set_choices(self, options):
        for w in self.btn_frame.winfo_children():
            w.destroy()

        for opt in options:
            btn = tk.Button(
                self.btn_frame,
                text=opt["label"],
                command=lambda o=opt: self._choose(o),
                bg=CARD, fg=TEXT,
                activebackground=ACCENT, activeforeground="white",
                font=("Courier", 10),
                relief="flat", bd=0,
                padx=14, pady=7,
                cursor="hand2"
            )
            btn.pack(side="left", padx=5, pady=8)

            def on_enter(e, b=btn): b.configure(bg=ACCENT, fg="white")
            def on_leave(e, b=btn): b.configure(bg=CARD, fg=TEXT)
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

    def _choose(self, opt):
        self.set_choices([])
        self.add_msg("> " + opt["label"], "player")
        self.root.after(500, opt["action"])

    def update_inv(self):
        text = "inventário: " + ", ".join(self.inventory) if self.inventory else "inventário: vazio"
        self.inv_label.configure(text=text)

    def delay(self, fn, ms=700):
        self.root.after(ms, fn)

    # ── Lógica do jogo ────────────────────────────────────────
    def start_game(self):
        self.inventory = []
        self.update_inv()
        self.add_msg("Você acordou em um porão misterioso.")
        self.add_msg("Não sabe como chegou ali...")
        self.delay(lambda: self.add_msg("Num canto você avista três itens: uma pá, uma tocha e uma espada."))
        self.delay(lambda: self.set_choices([
            {"label": "🪛  Pegar a pá",     "action": lambda: self.pick_item("pá")},
            {"label": "🔦  Pegar a tocha",  "action": lambda: self.pick_item("tocha")},
            {"label": "⚔️  Pegar a espada", "action": lambda: self.pick_item("espada")},
        ]), 1000)

    def pick_item(self, item):
        self.inventory = [item]
        self.update_inv()
        msgs = {
            "pá":     "Você pega a pá. Ela é pesada, mas pode ser útil.",
            "tocha":  "Você pega a tocha. A chama ilumina os cantos escuros do porão.",
            "espada": "Você pega a espada. A lâmina reluz mesmo na escuridão.",
        }
        self.add_msg(msgs[item], "result")
        self.delay(self.door_scene)

    def door_scene(self):
        self.add_msg("Explorando o porão, você encontra uma porta de madeira trancada.")
        self.delay(lambda: self.set_choices([
            {"label": "🪛  Usar a pá",     "action": lambda: self.use_door("pá")},
            {"label": "🔦  Usar a tocha",  "action": lambda: self.use_door("tocha")},
            {"label": "⚔️  Usar a espada", "action": lambda: self.use_door("espada")},
        ]))

    def use_door(self, item):
        msgs = {
            "pá":     "Você arrombra a porta com a pá. Com esforço ela cede — um corredor largo se abre.",
            "tocha":  "Você queima a porta com a tocha. Ela range e desmorona, revelando um corredor escuro.",
            "espada": "Você corta os gonzos com a espada. A porta cai e um corredor largo se abre.",
        }
        self.add_msg(msgs[item], "result")
        self.delay(self.spider_scene)

    def spider_scene(self):
        self.add_msg("Ao avançar pelo corredor...", "narr")
        self.delay(lambda: self.add_msg("Uma ARANHA GIGANTE bloqueia seu caminho!", "danger"))
        self.delay(lambda: self.add_msg("Suas presas gotejam veneno. Ela se prepara para atacar!", "danger"), 1200)
        self.delay(lambda: self.set_choices([
            {"label": "🪛  Usar a pá",     "action": lambda: self.fight_spider("pá")},
            {"label": "🔦  Usar a tocha",  "action": lambda: self.fight_spider("tocha")},
            {"label": "⚔️  Usar a espada", "action": lambda: self.fight_spider("espada")},
        ]), 1800)

    def fight_spider(self, item):
        if item == "pá":
            self.add_msg("Você tenta golpear a aranha — mas a pá se parte no exoesqueleto duro!", "danger")
            self.end_game("A aranha te envolve em teia e morde seu pescoço. Você sucumbe ao veneno.")
            return
        if item == "tocha":
            self.add_msg("Você empurra a tocha contra a aranha. Ela grita e vai se consumindo nas chamas!", "result")
        else:
            self.add_msg("Você gira a espada com precisão e corta a aranha ao meio. Golpe certeiro!", "result")
        self.delay(self.stairs_scene)

    def stairs_scene(self):
        self.add_msg("Com a aranha derrotada, você avista uma escada que sobe para o próximo andar.")
        self.delay(lambda: self.set_choices([
            {"label": "⬆️  Subir a escada",       "action": lambda: self.climb_stairs(True)},
            {"label": "🔍  Continuar explorando",  "action": lambda: self.climb_stairs(False)},
        ]))

    def climb_stairs(self, yes):
        if not yes:
            self.end_game("Você explora mais o porão. Horas depois, perdido e sem água, perece de exaustão.")
            return
        self.add_msg("Você sobe a escada e emerge num salão enorme.")
        self.delay(lambda: self.add_msg("No centro, um DRAGÃO VERMELHO abre os olhos dourados.", "danger"))
        self.delay(lambda: self.add_msg("Seu rugido faz as pedras tremerem. Ele está faminto!", "danger"), 1200)
        self.delay(lambda: self.set_choices([
            {"label": "🔦  Usar a tocha",  "action": lambda: self.fight_dragon("tocha")},
            {"label": "⚔️  Usar a espada", "action": lambda: self.fight_dragon("espada")},
        ]), 1800)

    def fight_dragon(self, item):
        if item == "tocha":
            self.add_msg("Você ergue a tocha... mas o dragão sopra fogo 10x mais forte!", "danger")
            self.end_game("As chamas do dragão te consomem completamente. A tocha não adiantou nada.")
            return
        self.add_msg("Você esquiva do bafo de fogo e crava a espada no coração do dragão!", "result")
        self.delay(lambda: self.add_msg("O dragão ruge pela última vez e desmorona. Silêncio total."))
        self.delay(lambda: self.add_msg("No fundo do salão, um imenso baú de ouro e joias brilha!", "gold"), 1200)
        self.delay(lambda: self.add_msg("🏆  Você escapou do porão com riquezas imensas. VOCÊ VENCEU!", "result"), 1800)
        self.delay(lambda: self.add_msg("—  Vitória!  —", "system"), 2400)
        self.delay(lambda: self.set_choices([
            {"label": "↺  Jogar novamente", "action": self.restart}
        ]), 2800)

    def end_game(self, msg):
        self.add_msg(msg, "danger")
        self.delay(lambda: self.add_msg("—  Fim de jogo  —", "system"))
        self.delay(lambda: self.set_choices([
            {"label": "↺  Jogar novamente", "action": self.restart}
        ]), 1200)

    def restart(self):
        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")
        self.add_msg("══════════════════════════════", "system")
        self.start_game()


# ── Inicialização ──────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = RPGApp(root)
    root.mainloop()
