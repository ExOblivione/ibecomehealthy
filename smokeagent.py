from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ListSortOrder
from config import get_config

def smokeagent(calculation_results, age):
    config = get_config()
    project = AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=config["agent"]["endpoint"])

    agent = project.agents.get_agent("asst_7RCA7Mz1A99wtkM5Po2MGpw5")

    thread = project.agents.threads.create()
    # print(f"Created thread, ID: {thread.id}")

    user = "I am {} years old and quit smoking {} years, {} months, {} weeks, {} days, {} hours, and {} minutes ago.".format(
            age, calculation_results[0], calculation_results[1], calculation_results[2], calculation_results[3], calculation_results[4], calculation_results[5]
        )
    
    print(f"User message: {user}")
    message = project.agents.messages.create(
        thread_id=thread.id,
        role="user",
        content=user
    )

    run = project.agents.runs.create_and_process(
        thread_id=thread.id,
        agent_id=agent.id)

    if run.status == "failed":
        print(f"Run failed: {run.last_error}")
    else:
        messages = project.agents.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)

        for message in messages:
            if message.text_messages:
                print(f"{message.role}: {message.text_messages[-1].text.value}")
