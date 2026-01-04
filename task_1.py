import heapq

def min_cost_to_connect_cables(cables):
    if not cables or len(cables) <= 1:
        return 0

    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        min1 = heapq.heappop(cables)
        min2 = heapq.heappop(cables)
                
        current_connection_cost = min1 + min2
                
        total_cost += current_connection_cost
                
        heapq.heappush(cables, current_connection_cost)
        
        # для наочності 
        print(f"З'єднали {min1} та {min2}. Витрати операції: {current_connection_cost}. Кабелі в купі: {cables}")

    return total_cost

# тести
cable_lengths = [4, 3, 2, 6]
print(f"Початкові кабелі: {cable_lengths}")

result = min_cost_to_connect_cables(cable_lengths)
print(f"---")
print(f"Мінімальні загальні витрати: {result}")
