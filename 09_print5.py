import time
start = time.time()

cnt = 0
while True:
    cnt = cnt + 1
    if cnt>10000000:
        break

end = time.time()
print(cnt)
print(end - start)
