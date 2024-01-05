# Example implementation of CrewAI
#
# 1. Install with `pip install crewai`
# 
# 2. Add your OpenAI API key, or update the code with an open source model
#
# 3. Update the contents below (change the roles, goals, backstories, tasks, etc.)
# 
# 4. Run this file from terminal with `python app.py`
#

import os
from crewai import Agent, Task, Crew, Process

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# Define your tools, custom or not.
# Install duckduckgo-search for this example:
#
# !pip install -U duckduckgo-search
from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

company_name = "IBM"

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Research Analyst',
  goal=f'Report on financial trends based on {company_name}\'s financial statements',
  backstory="""You are a Senior Research Analyst at a leading financial firm.
  Your expertise lies in identifying and reporting on financial trends based on
  companys financial statements. You are known for your ability to uncover
  hidden insights and provide actionable recommendations.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
  # llm=OpenAI(temperature=0.7, model_name="gpt-4"). It uses langchain.chat_models, default is GPT4
)
writer = Agent(
  role='Financial Content Strategist',
  goal='Craft compelling content that highlights the latest financial trends',
  backstory="""You are a Financial Content Strategist at a leading financial firm.
  Your expertise lies in crafting compelling content that highlights the latest
  financial trends. You are known for your ability to translate complex financial
  concepts into engaging narratives.""",
  verbose=True,
  allow_delegation=True
)

# Create tasks for your agents
task1 = Task(
  description="""Research the specified companies' financial statements and
  analyze their financial trends. Compile your findings in a detailed report. 
  Your final answer MUST be a full analysis report""",
  agent=researcher
)

task2 = Task(
  description="""Using the insights from the researcher's report, develop an engaging blog
  report that highlights the latest financial trends.
  Your post should be informative yet accessible, catering to a regular audience.
  Your final answer MUST be a full report that breaks down the financial trends.""",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
  process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
