import subprocess

def neo4j_start():
    start_inst = 'neo4j start'
    subprocess.run(start_inst, shell=True, cwd='C:\Environments\\Neo4j\\neo4j-community-5.18.1\\bin')
    print('neo4j started')
def neo4j_stop():
    stop_inst = 'neo4j stop'
    subprocess.run(stop_inst, shell=True)
    print('neo4j closed')

