from openbb_agents.agent import openbb_agent
from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Load your OpenAI API key from an environment variable or replace directly
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


query = "perform a foundational analysis of AMZN using the most reecently available data ,what do you find that is interesting?"

result = openbb_agent(query, verbose=False, openbb_pat=OPENBB_PAT)

print(result)



