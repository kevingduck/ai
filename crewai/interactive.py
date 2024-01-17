"""
This script lets users create and manage a workflow with a team of virtual agents. 

Users can define agents by specifying their roles, goals, and backstories, and assign them tasks. 

The script confirms each input for accuracy and allows adding multiple agents and tasks. 

To use it: 
- install ollama (https://ollama.ai) 
- from a terminal window run `ollama run mistral:instruct` to download the model
- from a terminal window run `pip install -U crewai duckduckgo-search`
- download and run this script (in terminal, `python interactive.py`
- if you want to use a template, fill out template file and run `python interactive.py --template-file your_filename.json`

Follow the prompts to input agent and task details, and the workflow is executed sequentially, 
displaying the results at the end. Ideal for interactive and customizable task automation.
"""
import os
import json
from argparse import ArgumentParser

from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama

# Define your tools
from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

ollama_mistral = Ollama(model="mixtral")

# Function to create an agent from template
def create_agent_from_template(template):
    return Agent(
        role=template["role"],
        goal=template["goal"],
        backstory=template["backstory"],
        verbose=True,
        allow_delegation=True,
        tools=[search_tool],
        llm=ollama_mistral
    )

# Function to create a task from template
def create_task_from_template(template):
    return Task(
        description=template["description"],
        agent=agents[int(template["agent"])]
    )

# Parse command line arguments
parser = ArgumentParser()
parser.add_argument('--template-file', type=str, 
help='Path to the JSON template file')
args = parser.parse_args()

if args.template_file:
    with open(args.template_file) as f:
        template = json.load(f)

    # Create agents based on template
    agents = [create_agent_from_template(t) for t in 
template["agents"]]

    # Create tasks based on template
    tasks = [create_task_from_template(t) for t in 
template["tasks"]]
else:
    # Function to create an agent
    def create_agent():
        while True:
            role = input("Enter the agent's role: ")
            goal = input("Enter the agent's goal: ")
            backstory = input("Enter the agent's backstory: ")

            # Read back the input and ask for confirmation
            print("\nAgent Details:")
            print(f"Role: {role}\nGoal: {goal}\nBackstory: {backstory}")
            confirm = input("Is this correct? (yes/no):")
            if confirm.lower() == 'yes':
                return Agent(
                    role=role,
                    goal=goal,
                    backstory=backstory,
                    verbose=True,
                    allow_delegation=True,
                    tools=[search_tool],
                    llm=ollama_mistral
                )
            else:
                print("Let's try entering the agent's details again.")

    # Create agents based on user input
    agents = []
    first_agent = create_agent()
    agents.append(first_agent)

    add_more_agents = input("Do you want to add more agents? (yes/no): ")
    while add_more_agents.lower() == 'yes':
        agents.append(create_agent())
        add_more_agents = input("Do you want to add more agents? (yes/no): ")

    # Function to create a task
    def create_task():
        while True:
            description = input("Enter the task description: ")
            print("Available agents:")
            for i, agent in enumerate(agents):
                print(f"{i}: {agent.role}")

            agent_index = int(input("Enter the index of the agent responsible for this task: "))

            # Read back the input and ask for confirmation
            print("\nTask Details:")
            print(f"Description: {description}\nAgent: {agents[agent_index].role}")
            confirm = input("Is this correct? (yes/no):")
            if confirm.lower() == 'yes':
                return Task(
                    description=description,
                    agent=agents[agent_index]
                )
            else:
                print("Let's try entering the task details again.")

    # Create tasks based on user input
    tasks = []
    add_tasks = True
    while add_tasks:
        tasks.append(create_task())
        add_more_tasks = input("Do you want to add more tasks? (yes/no): ")
        add_tasks = add_more_tasks.lower() == 'yes'

# Instantiate your crew with a sequential process
crew = Crew(
    agents=agents,
    tasks=tasks,
    verbose=2,
    process=Process.sequential
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
