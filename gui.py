import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLineEdit, QPushButton
)
 
from tokenizer import tokenize
from convert_tokens import convert_token
from evaluate import evaluate, CalculatorError
 
 
# ---------------------------------------------------------------
# Themes: every color the UI needs, grouped by theme name.
# Adding a new theme later just means adding a new entry here.
# ---------------------------------------------------------------
THEMES = {
    "dark": {
        "background": "#121212",
        "display_bg": "#1e1e1e",
        "display_text": "#ffffff",
        "number_bg": "#333333",
        "number_text": "#ffffff",
        "operator_bg": "#ff9500",
        "operator_text": "#ffffff",
        "utility_bg": "#4a4a4a",
        "utility_text": "#ffffff",
    },
    "light": {
        "background": "#f0f0f0",
        "display_bg": "#ffffff",
        "display_text": "#000000",
        "number_bg": "#e0e0e0",
        "number_text": "#000000",
        "operator_bg": "#ff9500",
        "operator_text": "#ffffff",
        "utility_bg": "#c9c9c9",
        "utility_text": "#000000",
    },
}
 
OPERATORS = {'+', '-', '*', '/'}
UTILITY_KEYS = {'C', '⌫'}
 
 
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
 
        self.current_theme = "dark"
        self.all_buttons = []  # (button, text) pairs, kept for re-styling on theme switch
 
        self.setWindowTitle("My calculator")
        self.resize(320, 550)
 
        self._build_ui()
        self.apply_theme(self.current_theme)
 
    # -----------------------------------------------------------
    # UI construction
    # -----------------------------------------------------------
    def _build_ui(self):
        main_layout = QVBoxLayout()
 
       # Theme switch row
        theme_row = QHBoxLayout()
        dark_button = QPushButton("Dark")
        light_button = QPushButton("Light")
        dark_button.setStyleSheet("color: white; background-color: #2a2a2a; padding: 8px;")
        light_button.setStyleSheet("color: white; background-color: #2a2a2a; padding: 8px;")
        dark_button.clicked.connect(lambda: self.apply_theme("dark"))
        light_button.clicked.connect(lambda: self.apply_theme("light"))
        theme_row.addWidget(dark_button)
        theme_row.addWidget(light_button)
        main_layout.addLayout(theme_row)
        
        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(60)
        main_layout.addWidget(self.display)
 
        # Buttons grid
        buttons_layout = QGridLayout()
        buttons = [
            ('C', 0, 0), ('⌫', 4, 2), ('/', 3, 3), ('*', 0, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3),
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('=', 4, 3),
            ('0', 4, 1), ('.', 4, 0),
        ]
 
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(65, 65)
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
            buttons_layout.addWidget(button, row, col)
            self.all_buttons.append((button, text))
 
            main_layout.addLayout(buttons_layout)
            self.setLayout(main_layout)
 
    # -----------------------------------------------------------
    # Theming
    # -----------------------------------------------------------
    def apply_theme(self, theme_name):
        self.current_theme = theme_name
        theme = THEMES[theme_name]
 
        self.setStyleSheet(f"background-color: {theme['background']};")
 
        self.display.setStyleSheet(f"""
            font-size: 28px;
            padding: 10px;
            background-color: {theme['display_bg']};
            color: {theme['display_text']};
            border-radius: 8px;
            border: none;
        """)
 
        for button, text in self.all_buttons:
            if text in OPERATORS or text == '=':
                bg, fg = theme['operator_bg'], theme['operator_text']
            elif text in UTILITY_KEYS:
                bg, fg = theme['utility_bg'], theme['utility_text']
            else:
                bg, fg = theme['number_bg'], theme['number_text']
 
            button.setStyleSheet(f"""
                font-size: 20px;
                border-radius: 32px;
                background-color: {bg};
                color: {fg};
                border: none;
            """)
 
    # -----------------------------------------------------------
    # Button behavior
    # -----------------------------------------------------------
    def on_button_click(self, text):
        if text == 'C':
            self.display.setText("")
            return
 
        if text == '⌫':
            current = self.display.text()
            self.display.setText(current[:-1])
            return
 
        if text == '=':
            self.calculate()
            return
 
        current = self.display.text()
        self.display.setText(current + text)
 
    def calculate(self):
        expression = self.display.text()
        try:
            tokens = tokenize(expression)
            converted = convert_token(tokens)
            result = evaluate(converted)
            self.display.setText(str(result))
        except CalculatorError as error:
            self.display.setText(str(error))
        except Exception:
            # Safety net for anything unexpected, so the app never
            # crashes outright from a bad button sequence.
            self.display.setText("Error!")
 
 
def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
 
 
if __name__ == "__main__":
    main()