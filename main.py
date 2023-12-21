import time
def comp(W, orig_W, W_set):
    #check if a W is compound or not
    if W in W_set and W != orig_W:
        return True
    for i in range(1, len(W)):
        P = W[:i]
        S = W[i:]
        if P in W_set and comp(S, orig_W, W_set):
            return True
    return False

def longest_compword(Ws):
    W_set = set(Ws)
    ans = ""
    for W in Ws:
        if comp(W, W, W_set) and len(W) > len(ans):
            ans = W
    return ans

def secon_longcomp(Ws, long_W):
    W_set = set(Ws)
    ans = ""

    for W in Ws:
        if W != long_W and comp(W, W, W_set) and len(ans) < len(W):
            ans = W
    return ans

if __name__ == "__main__":
    #start time
    s_time = time.time()
    with open("Input_02.txt", "r") as file:
        W_list = [line.strip() for line in file]
# longest and second longest compounded Ws
    long_W = longest_compword(W_list)
    second_long_W = secon_longcomp(W_list, long_W)
#Execution time
    #end time
    e_time = time.time()
    execution_time = round((e_time - s_time) * 1000, 2)
#output
    print(f"Longest Compound Word: {long_W}")
    print(f"Second Longest Compound Word: {second_long_W}")
    print(f"Time taken to process input: {execution_time} milliseconds")