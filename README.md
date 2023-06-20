# TO SET UP AND RUN
  # CREATE A NEW BRANCH TO WORK OFF OF. 
  # Open requirements.txt and click create virtual environment. Follow prompts to create .venv file. 
  # I am using python 3.10 currently in my environment. 
  # open projects folder and copy the " example " folder and paste inside the projects folder. 
  # Open your terminal ( CTRL + ` ) make sure it has the virtual environment loaded. It will have (.venv) somewhere around the terminal line
  # run " gpt-engineer projects/"YOUR PROJECT NAME HERE"
  # when it errors out for no api key follow the code reference and replace the word "key" with your key
  # .venv\Lib\site-packages\openai\api_requestor.py is where that code lives that needs the updated key. 
  # for me it was on line 138 you can search for " self.api_key = key " 
  # Make sure your key is wrapped in '' to make sure that it is read as a string value. 

# TO RUN 
  # run " gpt-engineer projects/"YOUR PROJECT NAME HERE"






# GPT Engineer
[![GitHub Repo stars](https://img.shields.io/github/stars/AntonOsika/gpt-engineer?style=social)](https://github.com/AntonOsika/gpt-engineer)
[![Discord Follow](https://dcbadge.vercel.app/api/server/4t5vXHhu?style=flat)](https://discord.gg/4t5vXHhu)
[![Twitter Follow](https://img.shields.io/twitter/follow/antonosika?style=social)](https://twitter.com/AntonOsika)


**Specify what you want it to build, the AI asks for clarification, and then builds it.**

GPT Engineer is made to be easy to adapt, extend, and make your agent learn how you want your code to look. It generates an entire codebase based on a prompt.

[Demo](https://twitter.com/antonosika/status/1667641038104674306) 👶🤖

## Project philosophy
- Simple to get value
- Flexible and easy to add new own "AI steps". See `steps.py`.
- Incrementally build towards a user experience of:
  1. high level prompting
  2. giving feedback to the AI that it will remember over time
- Fast handovers back and forth between AI and human
- Simplicity, all computation is "resumable" and persisted to the filesystem

## Usage

Choose either **stable** or **development**.

For **stable** release:

- `pip install gpt-engineer`

For **development**:
- `git clone git@github.com:AntonOsika/gpt-engineer.git`
- `cd gpt-engineer`
- `make install`
- `source venv/bin/activate`

**Setup**

With an api key that has GPT4 access run:

- `export OPENAI_API_KEY=[your api key]`


**Run**:
- Create an empty folder. If inside the repo, you can run:
  - `cp -r projects/example/ projects/my-new-project`
- Fill in the `main_prompt` file in your new folder
- Run: `gpt-engineer projects/my-new-project`

**Results**
- Check the generated files in `projects/my-new-project/workspace`

### Limitations
Implementing additional chain of thought prompting, e.g. [Reflexion](https://github.com/noahshinn024/reflexion), should be able to make it more reliable and not miss requested functionality in the main prompt.

Contributors welcome! If you are unsure what to add, check out the ideas listed in the Projects tab in the GitHub repo.


## Features
You can specify the "identity" of the AI agent by editing the files in the `identity` folder.

Editing the identity, and evolving the `main_prompt`, is currently how you make the agent remember things between projects.

Each step in `steps.py` will have its communication history with GPT4 stored in the logs folder, and can be rerun with `scripts/rerun_edited_message_logs.py`.

## Contributing
If you want to contribute, please check out the [projects](https://github.com/AntonOsika/gpt-engineer/projects?query=is%3Aopen) or [issues tab](https://github.com/AntonOsika/gpt-engineer/issues) in the GitHub repo and please read the [contributing document](.github/CONTRIBUTING.md) on how to contribute. Here is our [Discord 💬](https://discord.gg/4t5vXHhu)


## High resolution example

https://github.com/AntonOsika/gpt-engineer/assets/4467025/6e362e45-4a94-4b0d-973d-393a31d92d9b
