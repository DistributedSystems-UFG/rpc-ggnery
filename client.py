import rpyc
from constRPYC import * #-

if __name__ == "__main__":
  conn = rpyc.connect(SERVER, PORT)
  
  conn.root.exposed_clear()
  print("Lista inicial:", conn.root.exposed_value())
  
  conn.root.exposed_append(5)
  conn.root.exposed_append(3)
  conn.root.exposed_append(8)
  conn.root.exposed_append(1)
  print("Após append:", conn.root.exposed_value())
  
  conn.root.exposed_insert(2, 10)
  print("Após insert(2, 10):", conn.root.exposed_value())
  
  print("Índice do 8:", conn.root.exposed_search(8))
  print("Contém 10?", conn.root.exposed_contains(10))
  
  conn.root.exposed_sort()
  print("Após sort:", conn.root.exposed_value())
  
  conn.root.exposed_reverse()
  print("Após reverse:", conn.root.exposed_value())
  
  conn.root.exposed_remove(10)
  print("Após remove(10):", conn.root.exposed_value())
  
  print("Tamanho:", conn.root.exposed_length())
  
  conn.close()
