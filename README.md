# Text-To-Sql-Translator
 This django web app is generated using T5 large language model to translate text to sql.
 # ** You have to add trained model to this project. You can find traind model codes from my repositories.

# Project Description
This project aims to enable users to perform database queries using simple English expressions by leveraging natural language processing (NLP) and machine learning techniques. Specifically, a fine-tuned T5 language model trained on a dataset from Hugging Face converts input natural language queries (e.g., "How many heads of the departments are older than 56 ?") into accurate SQL queries (e.g., "SELECT COUNT(*) FROM head WHERE age > 56"). This allows even users without SQL knowledge to easily perform complex database queries. The project's web interface is developed using the Django web framework, facilitating users to easily input their queries and view the results.

# Technologies Used
The project primarily utilizes the following technologies:

T5 Language Model: A fine-tuned language model trained on a dataset from Hugging Face, used to convert natural language queries into SQL queries.
Django: A high-level Python web framework used to provide a user-friendly web interface.
Hugging Face: A widely used platform in the field of machine learning that provides access to pre-trained language models and datasets.

This project aims to simplify database interaction and streamline user access to data.
