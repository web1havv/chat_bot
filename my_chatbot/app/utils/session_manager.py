class SessionManager:
    def __init__(self):
        # Initialize a dictionary to store session data
        self.sessions = {}

    def start_session(self, user_id, session_id):
        """
        Start a new session for a user.

        Args:
            user_id (str): The ID of the user.
            session_id (str): The session ID for the user.

        Returns:
            None
        """
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "user_id": user_id,
                "chat_history": []
            }

    def add_message_to_session(self, session_id, role, content):
        """
        Add a message to the session's chat history.

        Args:
            session_id (str): The session ID.
            role (str): The role of the message sender ('user' or 'assistant').
            content (str): The content of the message.

        Returns:
            None
        """
        if session_id in self.sessions:
            self.sessions[session_id]["chat_history"].append({
                "role": role,
                "content": content
            })

    def get_chat_history(self, session_id):
        """
        Retrieve the chat history for a session.

        Args:
            session_id (str): The session ID.

        Returns:
            list: The chat history for the session.
        """
        return self.sessions.get(session_id, {}).get("chat_history", [])

    def end_session(self, session_id):
        """
        End a session and remove it from the session manager.

        Args:
            session_id (str): The session ID.

        Returns:
            None
        """
        if session_id in self.sessions:
            del self.sessions[session_id]