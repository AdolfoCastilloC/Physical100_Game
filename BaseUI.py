import tkinter as tk
from Board import Board
from Board import Zone


class BoardUI:
    def __init__(self, root, board):
        self.root = root
        self.board = board

        self.root.title("Mini Board UI")

        # Frame principal que contiene el "mapa"
        self.map_frame = tk.Frame(root, padx=10, pady=10)
        self.map_frame.pack()

        # Render inicial
        self.render_board()

    def render_board(self):
        """Crea la interfaz grid basada en board.grid."""
        for r in range(self.board.rows):
            for c in range(self.board.cols):

                zone = self.board.get_zone(r, c)

                # Crear marco por celda
                cell_frame = tk.Frame(
                    self.map_frame,
                    width=120,
                    height=80,
                    padx=5,
                    pady=5,
                    relief="solid",
                    borderwidth=1
                )
                cell_frame.grid(row=r, column=c)

                if zone:
                    # Label con nombre y peso
                    label = tk.Label(cell_frame, text=f"{zone.name}\nPeso: {zone.weight}")
                    label.pack()

                else:
                    # Si está vacío
                    empty_label = tk.Label(cell_frame, text="(vacío)")
                    empty_label.pack()


if __name__ == "__main__":
    board = Board(10,10)
    board.place_zone(Zone("Zona A"), 0, 0)
    board.place_zone(Zone("Zona B"), 4, 9)
    board.place_zone(Zone("Zona C"), 9, 5)

    root = tk.Tk()
    app = BoardUI(root, board)
    root.mainloop()