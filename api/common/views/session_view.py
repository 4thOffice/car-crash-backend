from abc import abstractmethod


class SessionView:
    @abstractmethod
    def get_by_session(self, session_id):
        pass

    def get_queryset(self):
        session_id = self.request.META.get('HTTP_X_SESSION', '').split()

        if session_id and len(session_id) > 1:
            return self.get_by_session(session_id)

        return []