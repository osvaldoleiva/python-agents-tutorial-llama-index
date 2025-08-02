from llama_index.core.agent.workflow import FunctionAgent
from llama_index.tools.yahoo_finance import YahooFinanceToolSpec
from llama_index.llms.openai import OpenAI

finance_tool = YahooFinanceToolSpec().to_tool_list()

workflows = FunctionAgent(
    name="Agent",
    description="Useful for performing financial operations.",
    llm=OpenAI(model="gpt-4o-mini"),
    tools=finance_tool,
    system_prompt="You are a helpful assistant."
)

async def main():
    response = await workflows.run(
        user_msg="What's the current stock price of NVIDIA?"
    )
    print(response)

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())