# Day 11, input: 
# aaa: you hhh
# ccc: ddd eee fff
# First is the current device, after : are the path's the device is connected to
# need to find every path from YOU -> OUT
# find and calculate every path

import time
from collections import deque
from functools import lru_cache
starttime = time.time()
debug = False

def load_data(filename):
    connection_graph = {};
    with open(filename) as file:
        for line in file:
            node, neighbours = line.strip().split(":");
            connection_graph[node] = neighbours.strip().split()
    return connection_graph;

def process_data(connection_map, start_loc, mid1, mid2,end_loc):
    # we currently do not care about joltage so let's ignore it for a bit
    local_total_P1 = 0;
    local_total_P2 = 0;
    partTwo = True;
    if partTwo == False: # part One
        local_total_P1 = BFS(connection_map, start_loc, end_loc);

    if partTwo == True:
        dac_out = BFS_2(connection_map, "dac", "out")
        # print(dac_out)
        fft_dac = BFS_2(connection_map, "fft", "dac")
        # print(fft_dac)
        svr_fft = BFS_2(connection_map, "svr", "fft")
        # print(svr_fft)
        fft_out = BFS_2(connection_map, "fft", "out")
        # print(fft_out)
        dac_fft = BFS_2(connection_map, "dac", "fft")
        # print(dac_fft)
        svr_dac = BFS_2(connection_map, "svr", "dac")
        # print(svr_dac)
        local_total_P2 = ((svr_dac * dac_fft * fft_out) + (svr_fft * fft_dac * dac_out))
        # print(local_total_P2)
    
    return local_total_P1, local_total_P2;

def BFS(connected, start, end):
    # https://www.geeksforgeeks.org/python/python-program-for-breadth-first-search-or-bfs-for-a-graph/
    all_visited = []
    queue = []
    def BFS_LOOP(state):
        queue.append(state)
        # base case
        if state == end:
            all_visited.append(queue.copy());
        else:
            for neighbour in connected.get(state, []):
                if neighbour not in queue:
                    BFS_LOOP(neighbour)
        queue.pop();
    BFS_LOOP(start)
    return len(all_visited);

def BFS_2(connected, start, end):
    # https://www.geeksforgeeks.org/python/python-program-for-breadth-first-search-or-bfs-for-a-graph/
    # all_visited = []
    @lru_cache(maxsize=None) #taaadaaaaa
    # queue = []
    def BFS_LOOP(state):
        # queue.append(state)
        # base case
        if state == end:
            # queue.pop()
            return 1
            # all_visited.append(queue.copy());
        total = 0;
        for neighbour in connected.get(state, []):
            # if neighbour not in queue:
            total += BFS_LOOP(neighbour)
        # queue.pop();
        return total;
    return BFS_LOOP(start);

def main():
    starttime = time.time();
    totalP1 = 0;
    totalP2 = 0;
    filename = "input.txt"; #P1: , P2: ?
    # filename = "input_test.txt"; # P1: 5
    # filename = "input_test_2.txt"; # P1: 2
    connection_map = load_data(filename);
    start_loc = "you"; #P1
    start_loc = "svr"; #P2
    end_loc   = "out";
    mid1      = "fft";
    mid2      = "dac";
    totalP1, totalP2 = process_data(connection_map, start_loc, mid1, mid2, end_loc);
    
    print("The total output is P1: ", totalP1, "P2: ", totalP2);
    stoptime = time.time()
    print("Total time:",stoptime-starttime,"seconds");



if __name__=="__main__":
    main()
