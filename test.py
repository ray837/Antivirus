import psutil

new_set = set(list(psutil.process_iter()))
for i in new_set:
    print(i.name())
