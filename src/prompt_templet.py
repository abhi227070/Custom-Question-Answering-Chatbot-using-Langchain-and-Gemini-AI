from langchain.prompts import PromptTemplate



def get_prompt():
    
    prompt_templet = """
    Given the following context and a question, generate an answer based on the context only.
    In the answer try to provide as much text as possible from "response" section in the source document.
    If the answer is not found in the context, kindly state that "I don't know.". Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}

    """

    prompt = PromptTemplate(
    template = prompt_templet,
    input_variables = ["context","question"]
    )
    
    return prompt