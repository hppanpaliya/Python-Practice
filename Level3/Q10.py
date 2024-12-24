def count_unserviced_customers(N, S):
    computers_in_use = set()
    serviced = set()
    unserviced = set()
    
    for i, customer in enumerate(S):
        if customer in serviced:
            computers_in_use.remove(customer)
            continue
            
        if customer in unserviced:
            continue
            
        if len(computers_in_use) < N:
            computers_in_use.add(customer)
            serviced.add(customer)
        else:
            unserviced.add(customer)
            
    return len(unserviced)

if __name__ == '__main__':
    N = 3
    S = "GACCBDDBAGEE"
    assert count_unserviced_customers(N, S) == 1

    N = 1
    S = "ABCBAC"
    assert count_unserviced_customers(N, S) == 2
