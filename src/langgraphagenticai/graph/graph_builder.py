from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition

from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.nodes.chatbot_with_Tool_node import ChatbotWithToolNode
from src.langgraphagenticai.tools.search_tool import (
    get_tools,
    create_tool_node
)


class GraphBuilder:

    def __init__(self, model):

        self.llm = model
        self.graph_builder = StateGraph(State)

    # -----------------------------------------
    # Basic Chatbot
    # -----------------------------------------

    def basic_chatbot_build_graph(self):

        chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node(
            "chatbot",
            chatbot_node.process
        )

        self.graph_builder.add_edge(
            START,
            "chatbot"
        )

        self.graph_builder.add_edge(
            "chatbot",
            END
        )

    # -----------------------------------------
    # Chatbot With Tools
    # -----------------------------------------

    def chatbot_with_tools_build_graph(self):

        # Get tools
        tools = get_tools()

        # Create ToolNode
        tool_node = create_tool_node(tools)

        # Create chatbot with tools
        chatbot_with_tools = ChatbotWithToolNode(
            self.llm
        )

        chatbot_node = chatbot_with_tools.create_chatbot(
            tools
        )

        # Add nodes
        self.graph_builder.add_node(
            "chatbot",
            chatbot_node
        )

        self.graph_builder.add_node(
            "tools",
            tool_node
        )

        # Start → Chatbot
        self.graph_builder.add_edge(
            START,
            "chatbot"
        )

        # Chatbot → Tool OR END
        self.graph_builder.add_conditional_edges(
            "chatbot",
            tools_condition
        )

        # Tool → Chatbot
        self.graph_builder.add_edge(
            "tools",
            "chatbot"
        )

    # -----------------------------------------
    # Setup Graph
    # -----------------------------------------

    def setup_graph(self, usecase: str):

        if usecase == "Basic Chatbot":

            self.basic_chatbot_build_graph()

        elif usecase == "Chatbot With Web":

            self.chatbot_with_tools_build_graph()

        else:

            raise ValueError(
                f"Unsupported usecase: {usecase}"
            )

        return self.graph_builder.compile()