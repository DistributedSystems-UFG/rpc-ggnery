[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_8sc1GR8)
### Overview

This example illustrates RPC in Python using the RPyC library (https://rpyc.readthedocs.io/).

It consists of a server that exposes remotely accessible procedures to manipulate a list:

**Procedimentos disponíveis:**
- value(), append(data), length(), clear()
- search(data), contains(data), count(data), get(index)
- remove(data), remove_at(index), insert(index, data)
- sort(reverse=False), reverse()

### Before running the example, you need to install the RPyC library:

Do the following on the two machines (AWS EC2 instances) that you will use for this activity:

    sudo apt update
    sudo apt install python3-rpyc

### Then edit the constRPYC.py file to use the IP address of the machine where you will run the server:

Also make sure it is using one of the ports left open for incoming TCP connections on the firewall (security group), such as 5678

### Then run the server on one machine

    python3 server.py

(and leave it running)

### Then run the client on the other machine

    python3 client.py

### Funcionalidades Implementadas

O cliente testa as principais operações: append, insert, search, contains, sort, reverse, remove e length.
