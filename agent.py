
from kb_client import read_knowledge_base_async
from llm_hf import call_llm
from prompt import get_custom_prompt


class ChatAgent:

    async def run(self, query: str) -> str:
        """
        Process the user query by:
        1. Reading the knowledge base from knowledge_base.docx
        2. Creating a prompt with the query and knowledge base content
        3. Sending to LLM for response
        4. Returning the LLM response
        """
        # 1. Read the knowledge base content from the docx file
        knowledge_base = await read_knowledge_base_async()

        # 2. Create the prompt with query and knowledge base content
        messages = get_custom_prompt(query, knowledge_base)
        print("Prompt messages:", messages)

        # 3. Send to LLM
        llm_response = await call_llm(messages)
        print("LLM response:", llm_response)

        # 4. Return the LLM response content
        return llm_response.content
