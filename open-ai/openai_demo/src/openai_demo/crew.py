import os
from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class OpenaiDemo():
	"""OpenaiDemo crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	anthropic_model_haiku = f"anthropic/{os.getenv('ANTHROPIC_MODEL_HAIKU', 'claude-3-5-haiku-latest')}"
	anthropic_model_sonnet = f"anthropic/{os.getenv('ANTHROPIC_MODEL_SONNET', 'claude-3-7-sonnet-latest')}"

	@agent
	def researcher(self) -> Agent:
		researcher_llm = LLM(model=self.anthropic_model_haiku, temperature=0.5)
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			llm=researcher_llm
		)

	@agent
	def reporting_analyst(self) -> Agent:
		reporting_analyst_llm = LLM(model=self.anthropic_model_haiku, temperature=0.5)
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm=reporting_analyst_llm
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the OpenaiDemo crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
