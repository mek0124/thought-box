from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QTextEdit,
    QPushButton, QStatusBar, QScrollArea
)

from PySide6.QtCore import Qt, QTimer
from qfluentwidgets import FluentIcon as fi

from ..core.logic import ThoughtBoxLogic


class Dashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Dashboard")

        self.db = parent.db
        self.color_theme = parent.color_theme
        self.editing_id = None

        self.logic = ThoughtBoxLogic(self.db)

        self.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}

                QWidget#row-container {{
                    border: none;
                }}

                QWidget#summary-area {{
                    border-right: 2px solid {self.color_theme['primary']};
                    border-top: 2px solid {self.color_theme['primary']};
                    border-bottom: 2px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_small']};
                }}

                                QScrollArea {{
                    border-left: 2px solid {self.color_theme['primary']};
                    border-top: 2px solid {self.color_theme['primary']};
                    border-bottom: 2px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_small']};
                }}

                QScrollArea {{
                    border-left: 2px solid {self.color_theme['primary']};
                    border-top: 2px solid {self.color_theme['primary']};
                    border-bottom: 2px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_small']};
                }}

                QScrollArea > QWidget > QWidget {{
                    background-color: transparent;
                    border: none;
                }}

                QWidget#entry-card {{
                    background-color: {self.color_theme['surface_glass']};
                    border-radius: {self.color_theme['border_radius_small']};
                    border: none;
                }}

                QWidget#entry-card QWidget {{
                    background-color: transparent;
                    border: none;
                }}

                QWidget#entry-card QLabel {{
                    background-color: transparent;
                    border: none;
                }}

                QLabel#entry-title {{
                    font-weight: bold;
                    font-style: italic;
                    font-size: 14px;
                    color: {self.color_theme['primary']};
                    border: none;
                }}

                QLabel#entry-content {{
                    font-size: 12px;
                    color: {self.color_theme['text_primary']};
                    border: none;
                }}

                QLabel#entry-date {{
                    font-size: 10px;
                    color: {self.color_theme['text_secondary']};
                    border: none;
                }}

                QPushButton#entry-button {{
                    font-size: 12px;
                    background-color: {self.color_theme['primary']};
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
        self.load_entries()

    def update_entry(self):
        if not self.editing_id:
            return self.handle_error_success(f"Target Entry ID Not Set!", True)
        
        updated_title = self.title_input.text().strip()
        updated_content = self.content_input.toPlainText().strip()

        if not updated_title and not updated_content:
            return self.handle_error_success("Title & Content Cannot Both Be Empty!", True)
        
        updated_details = {}

        if updated_title:
            updated_details["title"] = updated_title

        if updated_content:
            updated_details["content"] = updated_content

        did_update, response = self.logic.update_entry(self.editing_id, updated_content)
        
        if not did_update:
            return self.handle_error_success(response, did_update)
        
        self.editing_id = None
        self.clear_form()
        self.load_entries()
        
        return self.handle_error_success(response, did_update)

    def save_entry(self):
        new_title = self.title_input.text().strip()
        new_content = self.content_input.toPlainText().strip()

        if not new_title and not new_content:
            return self.handle_error_success(
                "All Inputs Are Requried!",
                True
            )

        if not new_title:
            return self.handle_error_success("Title Cannot Be Empty!", True)

        if not new_content:
            return self.handle_error_success("Content Cannot Be Empty!", True)
        
        new_entry = {
            "title": new_title,
            "content": new_content
        }
        
        did_save, response = self.logic.save_entry(new_entry)

        self.clear_form()
        self.load_entries()
        return self.handle_error_success(response, did_save)

    def handle_entry_delete(self, entry_id):
        did_delete, response = self.logic.delete_entry(entry_id)
        return self.handle_error_success(response, did_delete)

    def handle_entry_edit(self, entry_id):
        if not entry_id:
            return self.handle_error_success("Entry ID Cannot Be Empty", True)
        
        found_entry = self.logic.get_entry_by_id(entry_id)

        if not found_entry:
            return self.handle_error_success(f"No Entry Found By ID: {entry_id}", True)
        
        self.editing_id = found_entry.id
        
        self.title_input.clear()
        self.content_input.clear()
        
        self.title_input.setText(found_entry.title)
        self.content_input.setText(found_entry.content)

    def handle_save(self):
        if self.editing_id:
            self.update_entry()

        else:
            self.save_entry()
    
    def clear_form(self):
        self.title_input.clear()
        self.content_input.clear()
        self.title_input.setFocus()

    def handle_error_success(self, msg: str, is_error: bool):
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
        main_container_layout.setContentsMargins(10, 10, 10, 10)
        main_container_layout.setSpacing(10)
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
        left_container_layout.setContentsMargins(10, 10, 10, 10)
        left_container_layout.setSpacing(10)
        left_container_layout.setAlignment(Qt.AlignCenter)

        top_container = QWidget()
        top_container.setObjectName("summary-area")

        top_container_layout = QVBoxLayout(top_container)
        top_container_layout.setContentsMargins(0, 0, 0, 0)
        top_container_layout.setSpacing(0)
        top_container_layout.setAlignment(Qt.AlignCenter)

        label = QLabel("Undeveloped Area")
        label.setObjectName("form-label")
        label.setAlignment(Qt.AlignCenter)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setContentsMargins(5, 5, 5, 5)

        top_container_layout.addWidget(label)

        left_container_layout.addWidget(top_container, 1)
        left_container_layout.addWidget(self.scroll_area, 1)

        layout.addWidget(left_container, 1)
        return layout
    
    def add_right_side(self, layout):
        right_container = QWidget()
        right_container.setObjectName("container")
        
        right_container_layout = QVBoxLayout(right_container)
        right_container_layout.setContentsMargins(10, 10, 10, 10)
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
        btn_row_layout.setSpacing(150)
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

    def load_entries(self):
        entries = self.logic.get_all_entries()
        
        entries_container = QWidget()
        entries_container.setObjectName("container")
        
        entries_layout = QVBoxLayout(entries_container)
        entries_layout.setContentsMargins(10, 10, 10, 10)
        entries_layout.setSpacing(10)
        entries_layout.setAlignment(Qt.AlignTop)

        for entry in entries:
            entry_card = QWidget()
            entry_card.setObjectName("entry-card")
            
            entry_card_layout = QVBoxLayout(entry_card)
            entry_card_layout.setContentsMargins(5, 5, 5, 5)
            entry_card_layout.setSpacing(5)

            title_container = QWidget()
            title_container.setObjectName("container")

            title_container_layout = QHBoxLayout(title_container)
            title_container_layout.setContentsMargins(10, 0, 0, 0)
            title_container_layout.setSpacing(0)
            title_container_layout.setAlignment(Qt.AlignCenter)

            entry_title = QLabel(entry.title)
            entry_title.setObjectName("entry-title")

            title_container_layout.addWidget(entry_title, 2)

            date_col = QWidget()
            date_col.setObjectName("container")

            date_col_layout = QVBoxLayout(date_col)
            date_col_layout.setContentsMargins(5, 5, 5, 5)
            date_col_layout.setSpacing(10)
            date_col_layout.setAlignment(Qt.AlignCenter | Qt.AlignLeft)

            entry_created = QLabel(f"Created On: {entry.created_at}")
            entry_created.setObjectName("entry-date")
            
            date_col_layout.addWidget(entry_created)

            if entry.updated_at != entry.created_at:
                entry_updated = QLabel(f"Last Updated: {entry.updated_at}")
                entry_updated.setObjectName("entry-date")
                entry_updated.setAlignment(Qt.AlignRight)

                date_col_layout.addWidget(entry_updated)

            title_container_layout.addWidget(date_col)

            body_container = QWidget()
            body_container.setObjectName("container")

            body_container_layout = QHBoxLayout(body_container)
            body_container_layout.setContentsMargins(10, 0, 0, 0)
            body_container_layout.setSpacing(0)
            body_container_layout.setAlignment(Qt.AlignCenter)
            
            content_preview = entry.content[:50] + '...' if len(entry.content) > 50 else entry.content
            entry_content = QLabel(content_preview)
            entry_content.setObjectName("entry-content")

            body_container_layout.addWidget(entry_content, 2)

            entry_btn_container = QWidget()
            entry_btn_container.setObjectName("container")

            entry_btn_container_layout = QVBoxLayout(entry_btn_container)
            entry_btn_container_layout.setContentsMargins(10, 10, 10, 10)
            entry_btn_container_layout.setSpacing(10)
            entry_btn_container_layout.setAlignment(Qt.AlignCenter)

            edit_btn = QPushButton("🖋️")
            edit_btn.setObjectName("entry-button")
            edit_btn.clicked.connect(lambda checked=False, eid=entry.id: self.handle_entry_edit(eid))

            delete_btn = QPushButton("🗑️")
            delete_btn.setObjectName("entry-button")
            delete_btn.clicked.connect(lambda checked=False, eid=entry.id: self.handle_entry_delete(eid))

            entry_btn_container_layout.addWidget(edit_btn)
            entry_btn_container_layout.addWidget(delete_btn)

            body_container_layout.addWidget(entry_btn_container)

            entry_card_layout.addWidget(title_container)
            entry_card_layout.addWidget(body_container)

            entries_layout.addWidget(entry_card)

        self.scroll_area.setWidget(entries_container)