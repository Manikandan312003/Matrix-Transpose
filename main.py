def transpose(arr):
    M,N=len(arr),len(arr[0])
    print(M,N)
    if M!=N:
        arr, ren = [[0 for _ in range(M)] for i in range(N)], arr
        for i in range(M):
            for j in range(N):
                arr[j][i] = ren[i][j]
        return arr
    for i in range(M):
        for j in range(i+1,M):
            arr[i][j],arr[j][i] =arr[j][i] ,arr[i][j]
    return arr

print(transpose([ [1, 2, 3],[4, 5, 6],[7, 8, 9] ]))
print(transpose([ [1, 2],[1, 2],[1, 2] ]))