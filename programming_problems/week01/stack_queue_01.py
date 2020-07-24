def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []  # trucks on bridge
    crossed = []  # truck crossed bridge
    total_trucks = len(truck_weights)  # total truck num
    bridge_weight = 0  # current weight on bridge

    finished = False  # loop flag
    while not finished:

        # truck on bridge
        if len(bridge) != 0:
            for truck in bridge:
                truck[1] -= 1  # decrease left bridge length
            if bridge[0][1] == 0:  # finished bridge
                t = bridge.pop(0)  # pop from bridge
                crossed.append(t)
                bridge_weight -= t[0]  # decrease current bridge weigth

        # truck left
        if len(truck_weights) != 0:
            if truck_weights[0] + bridge_weight <= weight:  # weight ok
                next = truck_weights.pop(0)
                bridge.append([next, bridge_length])  # append to bridge as list [weight, remaining bridge length]
                bridge_weight += next  # add current bridge weight

        answer += 1  # increase time
        if len(crossed) == total_trucks:  # all trucks crossed
            finished = True

    return answer

print(solution(2, 10, [7, 4, 5, 6]))
