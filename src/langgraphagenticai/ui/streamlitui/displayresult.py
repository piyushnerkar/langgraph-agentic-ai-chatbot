import streamlit as st


class DisplayResultStreamlit:

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):

        try:
            result = self.graph.invoke(
                {
                    "messages": [
                        ("user", self.user_message)
                    ]
                }
            )

            messages = result.get("messages", [])

            if messages:
                response = messages[-1].content
                st.chat_message("assistant").write(response)

        except Exception as e:
            st.error(f"Error while generating response: {e}")