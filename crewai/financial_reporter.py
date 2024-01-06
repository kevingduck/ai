"""
This script sets up an automated workflow using CrewAI and LangChain libraries to analyze financial trends for a specified company (in this case, Microsoft). It utilizes the following steps:

1. Initializes an Ollama open source language model for processing natural language tasks.
2. Defines a DuckDuckGo search tool for information retrieval.
3. Creates three specialized agents - a Researcher, a Writer, and a Presenter - each with distinct roles and goals related to financial analysis and content creation.
4. Assigns specific tasks to each agent: the Researcher analyzes financial statements, the Writer creates content based on the analysis, and the Presenter designs a PowerPoint presentation.
5. Organizes these agents and their tasks into a Crew, executing the tasks in a sequential process.
6. Finally, the script runs the workflow and prints the results, which include research findings, written content, and presentation details.

This automated system demonstrates the integration of natural language processing, task delegation, and workflow management for efficient business intelligence and content creation.
"""


import os
from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama

ollama_mistral = Ollama(model="mistral")

# Define your tools, custom or not.
# Install duckduckgo-search for this example:
#
# !pip install -U duckduckgo-search
from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

company_name = "Microsoft"

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
  tools=[search_tool],
  # llm=OpenAI(temperature=0.7, model_name="gpt-4"). It uses langchain.chat_models, default is GPT4
  llm=ollama_mistral
)
writer = Agent(
  role='Financial Content Strategist',
  goal='Craft compelling content that highlights the latest financial trends',
  backstory="""You are a Financial Content Strategist at a leading financial firm.
  Your expertise lies in crafting compelling content that highlights the latest
  financial trends. You are known for your ability to translate complex financial
  concepts into engaging narratives.""",
  verbose=True,
  allow_delegation=True,
  llm=ollama_mistral
)

presenter = Agent(
    role='PowerPoint Presentation Specialist',
    goal='Design clean, concise PowerPoint presentations with effective use of images',
    backstory="""You are a PowerPoint Presentation Specialist known for creating 
    outlines for visually appealing and impactful presentations. Your expertise includes 
    synthesizing information into clear, concise slides and selecting or creating 
    images that enhance the message. You have a keen eye for design and layout, 
    ensuring that each slide is both informative and engaging. """,
    verbose=True,
    allow_delegation=True,
    llm=ollama_mistral
)


# Create tasks for your agents
task1 = Task(
  description="""Research the specified companies' most recent financial statements and
  analyze their financial trends. Compile your findings in a detailed report. 
  Make sure to include links to the financial statements you used, when possible.""",
  agent=researcher
)

task2 = Task(
  description="""Using the insights from the researcher's report, craft a
  compelling summary outline with bullet points that highlights the latest 
  financial trends that can be handed to the presentation specialist to create 
  a PowerPoint presentation.""",
  agent=writer
)

task3 = Task(
  description="""Using the insights from the researcher's report and the
  writer's article, create a PowerPoint presentation that highlights the latest
  financial trends. Make sure to include links to the financial statements you
  used. Also make sure to include a description of the images used for each slide. 
  You MUST return the text of the script for the presenter to read, a 
  description of the content on the slides, and a description of the images used 
  in each slide.""",
  agent=presenter
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer, presenter],
  tasks=[task1, task2, task3],
  verbose=2, # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
  process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
