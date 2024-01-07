import os
from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama

ollama_mistral = Ollama(model="mistral:instruct")

# Define your tools
from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

# Function to create an agent
def create_agent():
    while True:
        role = input("Enter the agent's role: ")
        goal = input("Enter the agent's goal: ")
        backstory = input("Enter the agent's backstory: ")

        # Read back the input and ask for confirmation
        print("\nAgent Details:")
        print(f"Role: {role}\nGoal: {goal}\nBackstory: {backstory}")
        confirm = input("Is this correct? (yes/no): ")
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
def create_task(agents):
    while True:
        description = input("Enter the task description: ")
        print("Available agents:")
        for i, agent in enumerate(agents):
            print(f"{i}: {agent.role}")

        agent_index = int(input("Choose the agent for this task by entering the corresponding number: "))

        # Read back the input and ask for confirmation
        print("\nTask Details:")
        print(f"Description: {description}\nAssigned to Agent: {agents[agent_index].role}")
        confirm = input("Is this correct? (yes/no): ")
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
    tasks.append(create_task(agents))
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
