

# 可用用with同时打开多个文件，用逗号分隔开即可
with open('RemoteWorking/a.txt', 'r') as read_f, open('RemoteWorking/b.txt', 'w') as write_f:
    data = read_f.read()
    print(data)
    write_f.write(data)

