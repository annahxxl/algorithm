from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    sec = 0
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    
    while bridge:
        sec += 1
        out = bridge.popleft()
        bridge_weight -= out
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                enter = truck_weights.popleft()
                bridge.append(enter)
                bridge_weight += enter
            else:
                bridge.append(0)
            
    return sec