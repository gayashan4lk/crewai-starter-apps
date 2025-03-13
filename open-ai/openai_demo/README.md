# Setup `crewAI` with `pip`

Welcome to the OpenaiDemo Crew project, powered by [crewAI](https://crewai.com).
This project is setup using `pip` instead of `uv` which is recommened in the [official crewAI documentation](https://docs.crewai.com/installation).

visit [pip page for crewAI package](https://pypi.org/project/crewai/) for more info.

> **Important Notice:** Before beginning, ensure you have Python >=3.10 <3.13 installed on your system. (I used Python 3.12.9)

## Create a virtual environment

Create a python virtual environment at the root directory of the project:

your current dir: crewai-starter-apps/openai
```bash
python -m venv .venv
```

## Install dependencies

Install the dependencies:

your current dir: crewai-starter-apps/openai
```bash
pip install -r requirements.txt
```

### Create .env file.

copy `.env-example` file and rename to `.env`
add your api keys.

## Running the Project

To run your crew, you need to go into the `openai_demo` directory, which include the crewAI files:

your current dir: crewai-starter-apps/openai
```bash
$ cd openai_demo
```

Execute `main.py` file.
your current dir: crewai-starter-apps/openai/openai_demo
```bash
$ python src/openai_demo/main.py
```

This command initializes the openai-demo Crew, assembling the agents and assigning them tasks as defined in your configuration.

After a successfull run a `report.md` file with the output of a research on LLMs will be created in the project folder `crewai-starter-apps/openai/openai_demo/report.md`.

## Understanding Your Crew

The openai-demo Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
