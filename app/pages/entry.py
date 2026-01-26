from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLabel, QPushButton,
    QLineEdit, QStatusBar, QScrollArea
)

from PySide6.QtCore import Qt, QTimer

from ..models.entry import EntryModel
from ..utils.color_theme import COLOR_THEME


class Entry(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Entry")

        self.parent_obj = parent
        self.db = self.parent_obj.db
        self.navigation = self.parent_obj.navigationInterface
        self.editing_id = None

        self.setup_ui()

    def setup_ui(self):
        if self.layout() is None:
            layout = QHBoxLayout(self)

        else:
            layout = self.layout()

            while layout.count():
                item = layout.takeAt(0)

                if item.widget():
                    item.widget().deleteLater()

        self.add_goals_column(layout)
        self.add_form_column(layout)

        layout.addStretch()
        return layout

    def add_goals_column(self, layout):
        goals_container = QScrollArea()
        goals_container.setStyleSheet(
            f"""
                QScrollArea {{
                    border-top: 2px solid {COLOR_THEME['primary']};
                    border-bottom: 2px solid {COLOR_THEME['primary']};
                    border-radius: {COLOR_THEME['border_radius_small']};
                }}
            """
        )

        goals_container_layout = QVBoxLayout(goals_container)
        goals_container_layout.setContentsMargins(0, 0, 0, 0)
        goals_container_layout.setSpacing(0)
        goals_container_layout.setAlignment(Qt.AlignCenter)

        title_label = QLabel("Goals Coming Soon!")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(
            f"""
                QLabel {{
                    font-weight: bold;
                    font-style: italic;
                    font-size: 14px;
                    color: {COLOR_THEME['text_primary']};
                }}
            """
        )

        goals_container_layout.addWidget(title_label)

        layout.addWidget(goals_container, 1)

        return layout
    
    def add_form_column(self, layout):
        form_container = QWidget()

        form_container_layout = QVBoxLayout(form_container)
        form_container_layout.setContentsMargins(0, 0, 0, 0)
        form_container_layout.setSpacing(10)
        form_container_layout.setAlignment(Qt.AlignCenter | Qt.AlignLeft)

        form_body = QWidget()

        form_body_layout = QVBoxLayout(form_body)
        form_body_layout.setContentsMargins(0, 0, 0, 0)
        form_body_layout.setSpacing(10)
        form_body_layout.setAlignment(Qt.AlignCenter)

        title_label = QLabel("Title")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(
            f"""
                QLabel {{
                    font-weight: bold; 
                    font-size: 12px; 
                    color: {COLOR_THEME['text_primary']};
                    letter-spacing: 0.5em;
                }}
            """
        )

        self.title_input = QLineEdit()
        self.title_input.setAlignment(Qt.AlignCenter)
        self.title_input.setStyleSheet(
            f"""
                QLineEdit {{
                    border-bottom: 2px solid {COLOR_THEME['primary']};
                    border-radius: {COLOR_THEME['border_radius_small']};
                    height: 30px;
                    color: {COLOR_THEME['primary']};
                    background-color: transparent;
                    font-size: 16px;
                    font-style: normal;
                    letter-spacing: 0.5em;
                }}

                QLineEdit::hover {{
                    background-color: {COLOR_THEME['secondary']};
                    color: {COLOR_THEME['text_primary']};
                    font-style: italic;
                }}

                QLineEdit::focus {{
                    background-color: {COLOR_THEME['secondary']};
                    color: {COLOR_THEME['primary']};
                    font-style: italic;
                }}
            """
        )

        content_label = QLabel("Content")
        content_label.setAlignment(Qt.AlignCenter)
        content_label.setStyleSheet(
            f"""
                QLabel {{
                    font-weight: bold; 
                    font-size: 12px; 
                    color: {COLOR_THEME['text_primary']};
                    letter-spacing: 0.5em;
                }}
            """
        )

        self.content_input = QTextEdit()
        self.content_input.setStyleSheet(
            f"""
                QTextEdit {{
                    border-left: 2px solid {COLOR_THEME['primary']};
                    border-right: 2px solid {COLOR_THEME['primary']};
                    border-radius: {COLOR_THEME['border_radius_small']}; 
                    font-style: italic; 
                    font-size: 16px; 
                    color: {COLOR_THEME['primary']}; 
                    background-color: transparent;
                    letter-spacing: 0.1em;
                }}

                QTextEdit::hover {{
                    background-color: {COLOR_THEME['secondary']};
                    color: {COLOR_THEME['text_primary']};
                    font-style: italic;
                }}

                QTextEdit::focus {{
                    background-color: {COLOR_THEME['secondary']};
                    color: {COLOR_THEME['primary']};
                    font-style: italic;
                }}
            """
        )

        status_bar_container = QWidget()
        status_bar_container.setStyleSheet("border: none;")

        status_bar_container_layout = QHBoxLayout(status_bar_container)
        status_bar_container_layout.setContentsMargins(0, 0, 0, 0)
        status_bar_container_layout.setSpacing(0)
        status_bar_container_layout.setAlignment(Qt.AlignCenter)

        self.status_bar = QStatusBar()
        self.status_bar.setStyleSheet("border: none; height: 30px;")

        form_buttons = QWidget()

        form_buttons_layout = QHBoxLayout(form_buttons)
        form_buttons_layout.setContentsMargins(0, 0, 0, 0)
        form_buttons_layout.setSpacing(150)
        form_buttons_layout.setAlignment(Qt.AlignCenter)

        clear_btn = QPushButton("Reset Form")
        clear_btn.clicked.connect(self.reset_form)
        clear_btn.setFixedSize(120, 30)
        clear_btn.setStyleSheet(
            f"""
                QPushButton {{
                    border: 2px solid {COLOR_THEME['primary']};
                    border-radius: {COLOR_THEME['border_radius_medium']}; 
                    background-color: transparent; 
                    font-size: 10px;
                }}

                QPushButton::hover {{
                    background-color: {COLOR_THEME['secondary']};
                }}
            """
        )

        submit_btn = QPushButton("Update" if self.editing_id else "Create")
        submit_btn.clicked.connect(self.handle_submit)
        submit_btn.setFixedSize(120, 30)
        submit_btn.setStyleSheet(
            f"""
                QPushButton {{
                    border: 2px solid {COLOR_THEME['primary']};
                    border-radius: {COLOR_THEME['border_radius_medium']}; 
                    background-color: transparent; 
                    font-size: 10px;
                }}

                QPushButton::hover {{
                    background-color: {COLOR_THEME['secondary']};
                }}
            """
        )

        form_body_layout.addWidget(title_label)
        form_body_layout.addWidget(self.title_input)
        form_body_layout.addWidget(content_label)
        form_body_layout.addWidget(self.content_input)

        status_bar_container_layout.addWidget(self.status_bar)

        form_buttons_layout.addWidget(clear_btn)
        form_buttons_layout.addWidget(submit_btn)

        form_container_layout.addWidget(form_body)
        form_container_layout.addWidget(status_bar_container)
        form_container_layout.addWidget(form_buttons)

        layout.addWidget(form_container, 3)

        return layout
    
    def handle_error_success(self, msg: str, is_error: bool = True):
        if is_error:
            self.status_bar.setStyleSheet(
                f"background-color: {COLOR_THEME['error']}; color: black;"
            )
        
        else:
            self.status_bar.setStyleSheet(
                f"background-color: {COLOR_THEME['success']}; color: black;"
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
    
    def reset_form(self):
        self.title_input.clear()
        self.content_input.clear()
        self.title_input.setFocus()

    def handle_submit(self):
        if self.editing_id:
            self.update_entry()
        else:
            self.save_entry()

    def save_entry(self):
        new_title = self.title_input.text().strip()
        new_content = self.content_input.toPlainText().strip()

        if not new_title:
            return self.handle_error_success("Title Is Required")
        
        if not new_content:
            return self.handle_error_success("Content Is Required")
        
        title_exists = self.db.query(EntryModel).filter(EntryModel.title == new_title).first()

        if title_exists:
            return self.handle_error_success("Title Already Exists")
        
        new_entry = EntryModel(
            title = new_title,
            content = new_content
        )

        try:
            self.db.add(new_entry)
            self.db.commit()
            self.parent_obj.switchTo(self.parent_obj.dashboard)

        except Exception as e:
            print(f"Unknown Exception Saving Entry: {e}")
            return self.handle_error_success("Error Saving Entry. Try Again Later")

    def update_entry(self):
        pass