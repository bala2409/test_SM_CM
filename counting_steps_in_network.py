
adj_list={1:[2,4],2:[1,3,4,8],3:[2,6,8,7],4:[1,5,2],5:[4,6],6:[3,9,5],7:[3,8,9,10],8:[2,3,7],9:[6,7,10],10:[7,9]}

def count_steps(current_vertex, destination, steps=0, calling=0):
    """
    Counts the number of steps between two nodes in an adjacent array
    :param current_vertex: Vertex to start looking from
    :param destination: Node we want to count the steps to
    :param steps: Number of steps taken so far (only used from this method, ignore when calling)
    :param calling: The node that called this function (only used from this method, ignore when calling)
    :return:
    """
    # Start at illegal value so we know it can be changed
    min_steps = -1
    # Check every vertex at the current index
    if current_vertex==destination:
        # print("No Loops allowed")
        return "No Self Loops Allowed"
    elif current_vertex>destination:
        return count_steps(destination,current_vertex)
    elif current_vertex<destination:
        for vertex in adj_list[current_vertex]:
            if destination in adj_list[current_vertex]:
                # We found the destination in the current array of vertexes
                return steps + 1
            elif vertex > calling:
                # Make sure the vertex we will go to is greater than wherever we want to go so we don't end up in a loop
                counted = count_steps(vertex, destination, steps + 1, current_vertex)
                if counted != -1 and (min_steps == -1 or counted < min_steps):
                    # If this is actually the least amount of steps we have found
                    min_steps = counted
        return min_steps

print(count_steps(10,1))
#this will create error in the output
print(count_steps(1,10))
print(count_steps(1,2))
