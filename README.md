
# CECS 327 Group Project 2: Voting Poll Distributed System

## Preconditions
            - Must run Linux OS
            - Must have Docker installed
            - Must have Docker account

## Compiling and Testing Instructions
    
1. Ensure the following files are located in the same file directory: 
    
            - node.py
            - poll1.py
            - poll2.py
            - Dockerfile_node
            - Dockerfile_poll1
            - Dockerfile_poll2
            - docker-compose.yml

(Note: Files must be named exactly as seen above.)

2. Make sure the current working directory of the terminal is set to where all the files are located.

            cd [folder_name]

3. Login to Docker using the command:

            sudo docker login 

4. Build the Docker images and run the containers by running the command:

            sudo docker-compose up --build

5. Terminate and remove the containers and network with the command: 

            sudo docker-compose down

Link to live demo: https://youtu.be/mLWoa8rA8sw 

