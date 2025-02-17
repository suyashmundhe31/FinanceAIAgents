from phi.agent import Agent
from phi.model.groq import Groq
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app


Finance_Agent = Agent(
    name="Finance Agent",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    storage=SqlAgentStorage(table_name="Finance_Agent", db_file="agents.db"),
    add_history_to_messages=True,
)   

News_Agent = Agent(
    name="News Agent",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    show_tool_calls=True,
    markdown=True,
    instructions="You are a helpful assistant that can answer questions and help with tasks.",
    storage=SqlAgentStorage(table_name="News_Agent", db_file="agents.db"),
    add_history_to_messages=True,
)

QandA_Agent = Agent(
    name="QandA Agent",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions="You are a helpful assistant that can answer questions and help with tasks.",
    storage=SqlAgentStorage(table_name="QandA_Agent", db_file="agents.db"),
    add_history_to_messages=True,
)

Portfolio_Agent = Agent(
    name="Portfolio Agent",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    storage=SqlAgentStorage(table_name="Portfolio_Agent", db_file="agents.db"),
    add_history_to_messages=True,
) 

app = Playground(agents=[Finance_Agent, News_Agent, QandA_Agent, Portfolio_Agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)