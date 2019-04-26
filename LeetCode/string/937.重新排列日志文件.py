
class Solution:
    def reorderLogFiles(self,logs):
              # logs: List[str]) -> List[str]:
              str_logs = []
              num_logs = []
              for log in logs:
                  if log[-1].isdigit():
                      num_logs.append(log)
                  else :
                      str_logs.append(log)
              # word_sort = sorted(str_logs,key = lambda x:x.split()[1:])
              str_logs.sort(key=lambda x: x.split()[1:])
              return str_logs + num_logs
