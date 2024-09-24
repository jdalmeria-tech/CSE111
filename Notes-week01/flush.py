import time

# Without flushing
for i in range(3):
    print(i, end=" ", flush=True)
    time.sleep(1)

# default nana nga flush=False
# main difference is ang buffer sa pag print