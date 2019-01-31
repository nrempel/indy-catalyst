import logging

from typing import Callable

from ...base_handler import BaseHandler

# from ..messages.connection_invitation import StateRequest


class StateRequestHandler(BaseHandler):
    def __init__(self, message: "StateRequest") -> None:
        self.logger = logging.getLogger(__name__)
        self.message = message

    def handle(self, thread_state):
        self.logger.debug(
            "StateRequestHandler called with thread_state " + f"{thread_state}"
        )
