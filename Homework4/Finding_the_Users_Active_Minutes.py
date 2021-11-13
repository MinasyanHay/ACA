def users(logs, k):
        f = {}
        for i in range(len(logs)):
            if logs[i][0] in f:
                f[logs[i][0]] += [logs[i][1]]
            else:
                 f[logs[i][0]] = [logs[i][1]]
        
        a = [0 for _ in range(k)]
        for key in f:
            a[len(set(f[key]))-1] += 1
        return a

logs = [[0,5], [1,2], [0,2], [0,5], [1,3]]
k = 5
print(users(logs,k))
