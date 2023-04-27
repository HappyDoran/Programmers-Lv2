def solution(n):
    answer = 0
    bin_n = bin(n)[2:]
    print(bin_n)
    bin_n = str(bin_n)
    n_cnt = bin_n.count("1")      
    while True:
        n+=1
        bin_n = bin(n)[2:]
        print(bin_n)
        bin_n = str(bin_n)
        if bin_n.count("1") == n_cnt:
            break
    return n