import re

class Parser:
    def __init__(self, san_text):
        self.san_text = san_text

        # Expresiones regulares basadas en la gramática BNF
        self.pattern_castling = re.compile(r"^O-O(-O)?$")  # Enroque corto o largo
        self.pattern_piece_move = re.compile(r"^[KQRBN][a-h]?[1-8]?x?[a-h][1-8](=[QRBN])?[\+#]?$")
        self.pattern_pawn_advance = re.compile(r"^[a-h][1-8](=[QRBN])?[\+#]?$")
        self.pattern_pawn_capture = re.compile(r"^[a-h]x[a-h][1-8](=[QRBN])?[\+#]?$")

    def is_valid_move(self, move):
        return (
            self.pattern_castling.match(move) or
            self.pattern_piece_move.match(move) or
            self.pattern_pawn_advance.match(move) or
            self.pattern_pawn_capture.match(move)
        )

    def validate(self):
        # Patrón para validar el formato del turno completo: número, jugada blanca y negra
        turn_pattern = re.compile(r"^\d+\.\s+\S+\s+\S+$")
        lines = self.san_text.strip().split('\n')
        errors = []
        valid_turns = []  # Lista de tuplas (turno, jugada blanca, jugada negra)

        for idx, line in enumerate(lines, start=1):
            if not turn_pattern.match(line):
                errors.append(f"Error en la línea {idx}: '{line}' no es un turno válido.")
            else:
                parts = line.split()
                white_move = parts[1]
                black_move = parts[2]

                if not self.is_valid_move(white_move):
                    errors.append(f"Error en la línea {idx}: Jugada de blancas '{white_move}' no es válida.")
                if not self.is_valid_move(black_move):
                    errors.append(f"Error en la línea {idx}: Jugada de negras '{black_move}' no es válida.")

                valid_turns.append((idx, white_move, black_move))

        # RETORNAR SIEMPRE 3 VALORES
        if errors:
            return False, "\n".join(errors), []  # Devuelve lista vacía de turnos si hay errores
        else:
            return True, "La partida es válida según la gramática BNF.", valid_turns
