from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.workflow import Context
from llama_index.tools.yahoo_finance import YahooFinanceToolSpec
from llama_index.core.workflow import JsonPickleSerializer, JsonSerializer
import json

finance_tool = YahooFinanceToolSpec().to_tool_list()

workflow = FunctionAgent(
    name="Agent",
    description="Useful for performing financial operations.",
    llm=OpenAI(model="gpt-4o-mini"),
    tools=finance_tool,
    system_prompt="You are a helpful assistant."
)

ctx = Context(workflow)

async def main():
    #response = await workflow.run(
    #    user_msg="Hello, my name is Osvaldo!",
    #    ctx=ctx,
    #)
    #print(response)

    #response2 = await workflow.run(user_msg="What's my name?", ctx=ctx)
    #print(response2)

    #with open('./ctx.json', 'w') as output:
    #    # convert our Context to a dictionary object
    #    ctx_dict = ctx.to_dict(serializer=JsonSerializer())
    #    json.dump(ctx_dict, output)

    with open('./ctx.json', 'r') as inputContext:
        ctx_dict = json.load(inputContext)

    # Create a new context from the dic
    restored_context = Context.from_dict(
        workflow,
        ctx_dict,
        serializer=JsonSerializer()
    )

    print("Now we are using a context restored from a dict which can be a file")

    response3 = await workflow.run(user_msg="What's my name?", ctx=restored_context)
    print(response3)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())