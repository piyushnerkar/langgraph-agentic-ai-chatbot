from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools():
    """
    Returns the list of tools used by the chatbot.
    """

    tools = [
        TavilySearchResults(
            max_results=3
        )
    ]

    return tools


def create_tool_node(tools):
    """
    Creates and returns a LangGraph ToolNode.
    """

    return ToolNode(
        tools=tools
    )