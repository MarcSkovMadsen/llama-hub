"""Provides the PanelChatPack"""
from typing import Dict, Any
import os
from llama_index.llama_pack.base import BaseLlamaPack

ENVIRONMENT_VARIABLES = [
    "GITHUB_TOKEN",
    "OPENAI_API_KEY",
]


class PanelChatPack(BaseLlamaPack):
    """Panel chatbot pack."""

    def get_modules(self) -> Dict[str, Any]:
        """Get modules."""
        return {}

    def run(self, *args: Any, **kwargs: Any) -> Any:
        """Run the pipeline."""
        for variable in ENVIRONMENT_VARIABLES:
            if variable not in os.environ:
                raise ValueError(f"{variable} is not set")

        import panel as pn

        if __name__ == "__main__":
            # 'pytest tests' will fail if app is imported elsewhere
            from app import create_chat_ui

            pn.serve(create_chat_ui)
        elif __name__.startswith("bokeh"):
            from app import create_chat_ui

            create_chat_ui().servable()
        else:
            print(
                "To serve the Panel ChatBot please run this file with 'panel serve' or 'python'"
            )


PanelChatPack().run()