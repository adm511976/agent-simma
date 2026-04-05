from extractor import extract_text
from simma_api import SimmaAPI
from executor import Executor
from agent import Agent

def main():
    text = extract_text("passport.pdf")

    api = SimmaAPI(
        base_url="http://your-simma-api",
        sid="YOUR_SESSION_ID"
    )

    executor = Executor(api)
    agent = Agent(executor)

    result = agent.run(text)
    print(result)

if __name__ == "__main__":
    main()