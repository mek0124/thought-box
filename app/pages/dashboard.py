from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QTextEdit,
    QPushButton, QStatusBar
)

from PySide6.QtCore import Qt, QTimer

from ..models.entry import Entry


class Dashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Dashboard")

        self.db = parent.db
        self.color_theme = parent.color_theme
        self.editing_id = None

        self.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}

                QWidget#row-container {{
                    border: none;
                }}

                QLabel#form-label {{
                    font-weight: bold;
                    font-style: italic;
                    font-size: 12px;
                    color: {self.color_theme['text_primary']}
                }}

                QLineEdit#form-input {{
                    border: 1px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_medium']};
                    font-size: 12px;
                    padding: 6px auto;
                    color: {self.color_theme['text_primary']};
                    background-color: transparent;
                    outline: none;
                }}

                QLineEdit#form-input:hover {{
                    background-color: {self.color_theme['surface_glass_hover']};
                    outline: none;
                }}

                QLineEdit#form-input:focus {{
                    background-color: {self.color_theme["surface_glass"]};
                    outline: none;
                }}

                QTextEdit#form-input {{
                    border-bottom: 1px solid {self.color_theme['primary']};
                    border-left: 1px solid {self.color_theme['primary']};
                    border-right: 1px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_medium']};
                    font-size: 12px;
                    color: {self.color_theme['text_primary']};
                    background-color: transparent;
                    outline: none;
                }}

                QTextEdit#form-input:hover {{
                    background-color: {self.color_theme['surface_glass_hover']};
                    outline: none;
                }}

                QTextEdit#form-input:focus {{
                    background-color: {self.color_theme["surface_glass"]};
                    outline: none;
                }}

                QPushButton#form-button-clear {{
                    border: 2px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_medium']};
                    font-size: 12px;
                    color: {self.color_theme['error']};
                }}

                QPushButton#form-button-clear:hover {{
                    background-color: {self.color_theme['error']};
                    color: black;
                    font-weight: bold;
                    font-style: italic;
                }}

                QPushButton#form-button-submit {{
                    border: 2px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_medium']};
                    font-size: 12px;
                    color: {self.color_theme['success']};
                }}

                QPushButton#form-button-submit:hover {{
                    background-color: {self.color_theme['success']};
                    color: black;
                    font-weight: bold;
                    font-style: italic;
                }}
            """
        )

        self.setup_ui()
        self.title_input.setFocus()

    def handle_error_success(self, msg: str, is_error: bool = True):
        if is_error:
            self.status_bar.setStyleSheet(
                f"""
                    QStatusBar {{
                        color: {self.color_theme['error']};
                    }}
                """
            )
        else:
            self.status_bar.setStyleSheet(
                f"""
                    QStatusBar {{
                        color: {self.color_theme['success']};
                    }}
                """
            )

        self.status_bar.showMessage(msg)

        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.reset_status_bar)
        self.timer.start()

    def reset_status_bar(self):
        self.status_bar.clearMessage()
        self.status_bar.setStyleSheet("")
        self.timer.stop()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignCenter)

        main_container = QWidget()
        main_container.setObjectName("container")

        main_container_layout = QHBoxLayout(main_container)
        main_container_layout.setContentsMargins(0, 0, 0, 0)
        main_container_layout.setSpacing(0)
        main_container_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        self.add_left_side(main_container_layout)
        self.add_right_side(main_container_layout)

        self.status_bar = QStatusBar()

        layout.addWidget(main_container, 2)
        layout.addWidget(self.status_bar)
        layout.addStretch()

    def add_left_side(self, layout):
        left_container = QWidget()
        left_container.setObjectName("container")

        left_container_layout = QVBoxLayout(left_container)
        left_container_layout.setContentsMargins(0, 0, 0, 0)
        left_container_layout.setSpacing(0)
        left_container_layout.setAlignment(Qt.AlignCenter)

        label = QLabel("Undeveloped Portion")
        label.setObjectName("form-label")
        label.setAlignment(Qt.AlignCenter)

        left_container_layout.addWidget(label)

        layout.addWidget(left_container, 1)
        return layout
    
    def add_right_side(self, layout):
        right_container = QWidget()
        right_container.setObjectName("container")
        
        right_container_layout = QVBoxLayout(right_container)
        right_container_layout.setContentsMargins(0, 0, 0, 0)
        right_container_layout.setSpacing(10)
        right_container_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        title_label = QLabel("Title")
        title_label.setObjectName("form-label")
        title_label.setAlignment(Qt.AlignCenter)

        self.title_input = QLineEdit()
        self.title_input.setObjectName("form-input")
        self.title_input.setAlignment(Qt.AlignCenter)

        content_label = QLabel("Content")
        content_label.setObjectName("form-label")
        content_label.setAlignment(Qt.AlignCenter)

        self.content_input = QTextEdit()
        self.content_input.setObjectName("form-input")
        self.content_input.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        btn_row = QWidget()
        btn_row.setObjectName("container")
        
        btn_row_layout = QHBoxLayout(btn_row)
        btn_row_layout.setContentsMargins(0, 0, 0, 0)
        btn_row_layout.setSpacing(0)
        btn_row_layout.setAlignment(Qt.AlignCenter)

        clear_btn = QPushButton("Clear")
        clear_btn.setFixedSize(150, 30)
        clear_btn.setObjectName("form-button-clear")
        clear_btn.clicked.connect(self.clear_form)

        submit_btn = QPushButton(
            "Update" if self.editing_id else "Save"
        )
        submit_btn.setFixedSize(150, 30)
        submit_btn.setObjectName("form-button-submit")
        submit_btn.clicked.connect(self.handle_save)

        btn_row_layout.addWidget(clear_btn)
        btn_row_layout.addWidget(submit_btn)

        right_container_layout.addWidget(title_label)
        right_container_layout.addWidget(self.title_input)
        right_container_layout.addWidget(content_label)
        right_container_layout.addWidget(self.content_input, 2)
        right_container_layout.addWidget(btn_row)

        layout.addWidget(right_container, 1)
        return layout
    
    def clear_form(self):
        self.title_input.clear()
        self.content_input.clear()
        self.title_input.setFocus()

    def handle_save(self):
        new_title = self.title_input.text().strip()
        new_content = self.content_input.toPlainText().strip()

        if not new_title or not new_content:
            return self.handle_error_success("Title & Content Are Required!")
        
        existing_title = self.db.query(Entry).filter(Entry.title == new_title).first()

        if existing_title:
            return self.handle_error_success("Title Already Exist!")
        
        new_entry = Entry(
            title = new_title,
            content = new_content
        )

        self.db.add(new_entry)
        self.db.commit()
        self.clear_form()

        return self.handle_error_success("Entry Saved Successfully!", False)