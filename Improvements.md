# UI 
1. Interface refresh after prompt imput (priority)
2. access to UI files - Path
3. change login name from default 'alice@gmail.com'
4. add thread name automatically, generated from prompt query


# Access to PostgreSQL
sudo -u postgres psql for entering psql
Then \c promptq to connect to the database. 
Then you can do whatever command, like SELECT * FROM users;

# Access Docker folder
ubuntu@vmi794304:~/prompt/client/src$ docker ps
3 containers running


# UI Files change
-Stop docker : 
docker compose -f docker-compose.prod.yml down
-After any UI files change, run:
docker compose -f docker-compose.prod.yml up --build -d

# Using the same 2 files you made to run locally
Docker file and package.json
running docker-compose I should be able to run the app locally, right ?

10.Jan.2025
- Add the Chat UI to a website -> test ai.athenalabo.com
- Add a button to the UI that will allow the upload file to process (embedding and classification)
- Add a app in the backend for add additional files to the database embedding
- Use pgvector as extension pgvectorscale, integrated into Postgresql as embedding vector database alternative to ChromaDB
- Add a backend app to convert pptx, wordx, pdf to markdown file to embed into vector database
- Add a backend app to index multi-modal embedded information
- Add a backend app to process multi-modal, not only text but also pictures, videos, audio, etc.
- Add a button to the UI that will allow the assess correctness of the answer and provide a string of comment if the answer is wrong.
- Add a button to the UI that will allow the user to save the current chat session to a file.
- Add a button to the UI that will allow the user to load a saved chat session from a file.
- Add a button to the UI that will allow the user to delete a saved chat session from a file.
- Add a button to the UI that will allow the user to delete all saved chat sessions from a file.
