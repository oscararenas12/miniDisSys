
# CECS 327 Group Project 1: A Bite of Distributed Communication

## Preconditions
        - Must run Linux OS
        - Must have Docker installed
        - Must have Docker account

## Compiling and Testing Instructions
    
1. Ensure the following files are located in the same file directory: 
    
            - client.py
            - server.py
            - Dockerfile_client
            - Dockerfile_server
            - docker-compose.yml

    2. Make sure the current working directory of the terminal is set to where all the files are located.

            cd [folder_name]

    3. Login to Docker using the command:

            sudo docker login 

    4. Build the Docker images and run the containers by running the command:

            sudo docker-compose up --build

    5. Terminate and remove the containers and network with the command: 

            sudo docker-compose down
    

