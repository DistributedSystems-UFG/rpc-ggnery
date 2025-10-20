import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

  def exposed_search(self, data):
    try:
      return self.value.index(data)
    except ValueError:
      return -1

  def exposed_remove(self, data):
    try:
      self.value.remove(data)
      return True
    except ValueError:
      return False

  def exposed_remove_at(self, index):
    try:
      return self.value.pop(index)
    except IndexError:
      return None

  def exposed_insert(self, index, data):
    try:
      self.value.insert(index, data)
      return True
    except Exception:
      return False

  def exposed_sort(self, reverse=False):
    self.value.sort(reverse=reverse)
    return self.value

  def exposed_clear(self):
    self.value = []
    return True

  def exposed_length(self):
    return len(self.value)

  def exposed_contains(self, data):
    return data in self.value

  def exposed_count(self, data):
    return self.value.count(data)

  def exposed_reverse(self):
    self.value.reverse()
    return self.value

  def exposed_get(self, index):
    try:
      return self.value[index]
    except IndexError:
      return None

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

