import json
import os

class SessionManager:
    def __init__(self, session_file="session.json"):
        self.session_file = session_file
        # Load session data if file exists, else initialize empty session
        self.session_data = self._load_session()

    def _load_session(self):
        """Load session data from the JSON file."""
        if os.path.exists(self.session_file):
            with open(self.session_file, "r") as file:
                return json.load(file)
        else:
            return {}

    def save_session(self):
        """Save the current session data to the JSON file."""
        with open(self.session_file, "w") as file:
            json.dump(self.session_data, file, indent=4)

    def get(self, key, default=None):
        """Retrieve a value from the session."""
        return self.session_data.get(key, default)

    def set(self, key, value):
        """Set a value in the session."""
        self.session_data[key] = value
        self.save_session()

    def clear_session(self):
        """Clear all session data."""
        self.session_data = {}
        self.save_session()
