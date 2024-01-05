import json
from typing import Dict, List

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

from jobs import config
from jobs.models import Job


TEMPLATE = """
    Goal: Given the list of Jobs, return only the jobs that are relevant to Software Testers, QA Engineers, or Test Automation Engineers (SDET). Return ONLY the relevant list in JSON format.

    JSON model format for Job:

    ```json
    [
        {{
            "title": "Junior Software Tester",
            "company": "N-Tierty Inc."
        }},
        {{
            "title": "QA Engineer, Manual Tester",
            "company": "i2e Consulting"
        }},
        ...
    ]
    ```

    List of Jobs:

    ```
    {jobs}
    ```

    List of relevant Jobs in JSON format:
"""
PROMPT = PromptTemplate(template=TEMPLATE, input_variables=["jobs"])


def get_relevant_jobs(jobs: List[Job]) -> str:
    llm = ChatOpenAI(
        openai_api_key=config.OPENAI_API_KEY, temperature=0, model_name="gpt-4"
    ).bind()  # may need "gpt-4-32k"
    llm_chain = LLMChain(prompt=PROMPT, llm=llm)

    dumped_jobs = [job.model_dump() for job in jobs]
    response = llm_chain.run(dumped_jobs)
    return response


def convert_relevant_jobs_to_list(relevant_jobs: str) -> List[Dict]:
    """The response from the AI is a string that contains the JSON data.

    However, the data may be wrapped in a code block (```json ... ```).
    This function will extract the JSON data from the code block and convert it into a list of dictionaries.
    """
    relevant_jobs = relevant_jobs.strip()

    if relevant_jobs.startswith("["):
        # Already in a clean format and ready to convert to JSON
        json_data = relevant_jobs

    else:
        # Extract the JSON data from the code block
        split = relevant_jobs.split("```")
        json_data = split[1].strip()

        if json_data.startswith("json"):
            json_data = json_data[4:].strip()

    return json.loads(json_data)
