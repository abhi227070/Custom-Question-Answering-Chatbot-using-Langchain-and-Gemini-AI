# Custom Question Answering Chatbot using Langchain and Gemini LLM

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Tools Used](#tools-used)
- [Getting Started](#getting-started)
- [Screenshot](#screenshot)
- [Use Case](#use-case)
- [Future Improvements](#future-improvements)
- [Contributors](#contributors)
- [License](#license)

## Introduction

This project implements a custom question answering chatbot using Langchain and Google Gemini Language Model (LLM). The chatbot is trained on industrial data from an online learning platform, consisting of questions and corresponding answers.

## Project Overview

The project workflow involves the following steps:

1. **Data Fine-Tuning**: The Google Gemini LLM is fine-tuned with the industrial data, ensuring that the model can accurately answer questions based on the provided context.

2. **Embedding and Vector Database**: HuggingFace sentence embedding is utilized to convert questions and answers into vectors, which are stored in a vector database.

3. **Retriever Implementation**: A retriever component is developed to retrieve similar-looking vectors from the vector database based on the user's query.

4. **Integration with Langchain RetrivalQA Chain**: The components are integrated into a chain using Langchain RetrivalQA chain, which processes incoming queries and retrieves relevant answers.

5. **User Interface**: Streamlit is used to create a simple user interface, allowing users to input their questions and receive answers from the chatbot.

## Tools Used

- [Google Gemini LLM](https://link-to-gemini-llm): Language model fine-tuned with industrial data.
- [HuggingFace](https://link-to-huggingface): Library used for sentence embedding.
- [Langchain](https://link-to-langchain): Framework for building conversational AI systems.
- [Streamlit](https://link-to-streamlit): Library for building web-based user interfaces.

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies listed in the `requirements.txt` file.
3. Run the Streamlit application by executing `streamlit run app.py` in your terminal.

## Screenshot

![Screenshot of Chatbot Interface](screenshot.png)

## Use Case

The custom question answering chatbot serves various purposes, including:

- Providing quick and accurate responses to user queries related to the topic covered by the industrial data.
- Enhancing user experience on online learning platforms by offering immediate assistance.
- Streamlining customer support processes by automating responses to frequently asked questions.

## Future Improvements

- Incorporate additional pre-processing techniques to handle a wider range of user queries.
- Implement advanced language models for more accurate responses.
- Enhance the user interface with additional features for a better user experience.

## Contributors

- [Your Name](link-to-your-profile)

## License

This project is licensed under the [MIT License](link-to-license-file).
