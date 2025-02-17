from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    instructions="You are a helpful assistant that can answer questions and help with tasks.",
)

agent.print_response("What is the capital of the moon?")    

