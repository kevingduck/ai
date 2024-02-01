# Links
Here are some links to AI tools that I find useful. 

## ChatGPT
- ~Pay $20 for one month of GPT-4. It's worth it for at least one month to see the GPT-4 performance in addition to the other features like custom GPTs. GPT-3.5 is good but GPT-4 is the current best model out there.~ I've changed my tune about this ... I still use ChatGPT occasionally, but I canceled my pro subscription in favor of running local open source models 😮

## Alternatives
- [poe.com](poe.com) has a great web app and [mobile app](https://apps.apple.com/us/app/poe-fast-ai-chat/id1640745955). You can try out different models, and you can create custom GPTs for specific use cases, or try out someone else's GPTs.
- Try this: [tell this bot](https://poe.com/PoeBotCreater) what kind of custom GPT you want to create. It will generate really good custom instructions, which you can use to create a NEW bot. Copy the generated output, create a new bot, and paste the copied output into the new bot. Now you have your own custom GPT in under a minute. 

## Run GPTs locally, free, privately
- [ollama.ai](ollama.ai) is the easiest way to get an open source model running. Download the software, then run it from a Terminal window (e.g., "ollama run mistral") and you can start chatting with a local, offline and free GPT.
- [LM Studio](https://lmstudio.ai/) is a nice interface that lets you download and chat with open source models like Llama2
- [Huggingface.co](Huggingface.co) is where people upload their open source models. Some are trained for specific things like chatting or coding. LM studio and ollama let you download models easily like you would from Huggingface.
- [Glossary of all the terms explained](https://osanseviero.github.io/hackerllama/blog/posts/hitchhiker_guide/) for local LLMs

## Prompting tips
- Prompting (i.e., the instructions you give to the model) determines whether your GPT outputs will be any good. Better prompts = better responses. [This post](https://cloud.google.com/blog/products/application-development/five-best-practices-for-prompt-engineering) has some tips on prompting.
- [Specific tips](https://github.com/kevingduck/ai/blob/main/prompting_tips.md) for prompting from [thepromptindex.com](https://www.thepromptindex.com/the-science-of-prompting-chatgpt:-26-principles-to-unlock-its-potential.html).

## YouTube Channels
- [Matthew Berman](https://www.youtube.com/@matthew_berman) makes lots of videos where he tests new AI apps and models. Good for keeping up with latest trends. 
- [David Shapiro](https://www.youtube.com/@DaveShap) has lots of content discussing the latest AI developments, implications, predictions, etc.

## AI Tools
- [GitHub Copilot](https://github.com/features/copilot) - install it in a code editor like VS Code and start writing ... it will generate the code for you. Must-have for programming now since it speeds up and improves development so dramatically. 
- [Social media automation](https://zapier.com/blog/best-ai-social-media-management/) - apps to help create, schedule social media posts
- [simplfied.ai](simplfied.ai) - Presentation maker
- [invideo.ai](invideo.ai) - Video maker

## Noteworthy Links
- [crewai](https://github.com/joaomdmoura/crewAI) is really impressive. In a few lines of code, you set up a **team** of specialists and give them a goal and they work together to achieve it.
  - Example: you set up a researcher, a writer, and a PowerPoint prentation specialist, then tell them to analyze and report on the latest financial statements from a given company. The researcher finds the information online, the writer generates a report based off of the researcher's analysis, and the PowerPoint specialist creates content for each slide, **including a description of the image in the slide, which can be used to generate an actual image by feeding it into MidJourney, Dall-E, etc.** 
  - Try this out here: https://github.com/kevingduck/ai/blob/main/crewai/app.py
  - ⭐ Try this! [Run CrewAI and create agents/ tasks easily](https://github.com/kevingduck/ai/blob/main/crewai/interactive.py)
- ⭐ **Fine-tune your own model.** Give a bot your docs (emails, chats, whatever) and **train it to sound like you and respond in your own style**. [Instructions here](https://www.youtube.com/watch?v=74NSDMvYZ9Y).
