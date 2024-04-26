# AI PDF Reader


This project focuses on data extraction from a PDF file with AI. Given a company's proprietary files, we want to have a quick query system from those files. A system similar to having a secretary. The technology we will use is called Retrieval Augmented Generation (RAG). 

RAG is the process of optimizing a large language model (LLM) so that it utilizes user-provided data not present in the model's training data before generating a response. LLMs are trained on large volumes of data and use billions of parameters to produce original outputs in tasks such as answering questions, translating languages, and completing sentences. A RAG extends the already powerful capabilities of LLMs to specific domains or an organization's internal knowledge base, all without the need to retrain the model. This method is a cost-effective way to enhance the results of LLMs so they remain relevant, accurate, and useful across various contexts.

A RAG offers several direct benefits in the development of an artificial intelligence tool:

+ Cost-effectiveness of implementation. AI development typically begins with a basic model. Foundational Models (FMs) are API-accessible LLMs trained on a broad spectrum of generalized and unlabeled data. The computational and financial costs of retraining FMs to include specific organizational or domain-specific information are very high. A RAG is a more cost-effective approach to introducing new data into the LLM.

+ Updated information. Even if the LLM is trained with data that suits a company's needs, maintaining the model's relevance is challenging. A RAG allows developers to provide the latest research, statistics, or news to generative models. A RAG can be used to connect the LLM directly to live social media feeds, news sites, or other frequently updated information sources. This way, an LLM can offer the most up-to-date information.

+ Trust. By feeding the LLM its own data, the data source is well-known, and it avoids the LLM's hallucination.

+ Greater control. RAG enables AI developers to switch information sources to adapt to changing requirements or the company's multiple uses. They can also restrict the retrieval of sensitive information to different levels of authorization and ensure that the LLM generates appropriate responses.

The general RAG scheme is as follows:

![rag](images/rag.png)

1. The company's documents are processed through an embedding model to be stored as vectors in a database.

2. The query made by the user goes through the same model to convert the text into vectors.

3. The most similar vectors to the query are searched for in the database, and the most relevant vectors are extracted.

4. The most relevant documents extracted and the query are input into the LLM to generate the most appropriate response.

### RAG Building

First we need to transform PDF files. 


