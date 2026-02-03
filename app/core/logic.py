from typing import Tuple, Union, Optional, List
from ..models.entry import Entry


class ThoughtBoxLogic:
    def __init__(self, db):
        self.db = db

    def get_all_entries(self) -> Union[List, None]:
        try:
            return self.db.query(Entry).all()
        
        except Exception as e:
            print(f"Unknown Exception Getting All Entries: {e}")
            return "Failed To Load Entries"
        
    def get_entry_by_id(self, entry_id: int) -> Union[Entry, None]:
        if not entry_id:
            return None
        
        try:
            return self.db.query(Entry).filter(Entry.id == entry_id).first()
        
        except Exception as e:
            print(f"Unknown Exception Getting Entry By ID: {entry_id}: {e}")
            return None
        
    def save_entry(self, new_entry: dict) -> Tuple[bool, str]:
        if not new_entry:
            return True, None, "Entry Cannot Be Empty. Title & Content Are Required!"

        found_title = self.db.query(Entry).filter(Entry.title == new_entry["title"]).first()

        if found_title:
            return True, None, "Title Already Exists!"
        
        entry_to_save = Entry(
            title = new_entry["title"],
            content = new_entry["content"]
        )

        try:
            self.db.add(entry_to_save)
            self.db.commit()
            return False, "Entry Saved Successfully"
        
        except Exception as e:
            return True, "Failed To Save Entry"
        
    def update_entry(self, entry_id: int, updated_entry: dict) -> Tuple[bool, Optional[Entry], str]:
        if not entry_id or not updated_entry:
            return True, None, "Entry ID and Updated Details Are Required!"
        
        if not entry_id:
            return True, None, "Entry ID Cannot Be Empty!"
        
        if not updated_entry:
            return True, None, "Title & Content Cannot Be Empty!"
        
        found_entry = self.db.query(Entry).filter(Entry.id == entry_id).first()

        if not found_entry:
            return True, None, f"No Entry Found By ID: {entry_id}"
        
        if found_entry.title == updated_entry["title"] and \
            found_entry.content == updated_entry["content"]:

            return False, None, "No Changes Made"
        
        try:
            updated_entry = self.db.query(Entry).filter(Entry.id == entry_id).udpate(updated_entry)
            return False, updated_entry, "Entry Updated Successfully"
        
        except Exception as e:
            print(f"Unknown Exception Updating Entry: {e}")
            return False, None, "Failed To Update Entry"
        
    def delete_entry(self, entry_id: int) -> Tuple[bool, str]:
        if not entry_id:
            return True, "Entry ID Cannot Be Empty!"
        
        try:
            self.db.query(Entry).filter(Entry.id == entry_id).delete()
            return False, "Entry Deleted Successfully"

        except Exception as e:
            print(f"Unknown Exception Deleting Entry: {e}")
            return True, "Failed To Delete Entry"