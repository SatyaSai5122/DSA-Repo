def add_edge_list(g, u, v):
    g[u].append(v)
    g[v].append(u)  # Delete this line if graph is directed

def add_edge_matrix(g, u, v):
    g[u][v] = 1
    g[v][u] = 1  # Delete this line for directed graph

def print_graph_list(g):
    print("ADJ LIST:")
    for i in range(len(g)):
        print(f"{i}: ", end="")
        for v in g[i]:
            print(v, end=" ")
        print()
    print()

def print_graph_matrix(g):
    print("ADJ MATRIX:")
    print("  ", end="")
    for i in range(len(g)):
        print(f" {i}", end="")
    print()

    for i in range(len(g)):
        print(f"{i}: ", end="")
        for j in range(len(g[i])):
            print(g[i][j], end=" ")
        print()
    print()

def main():
    n, e = map(int, input().split())

    # Adjacency list
    adj_list = [[] for _ in range(n)]

    # Adjacency matrix
    adj_matrix = [[0] * n for _ in range(n)]

    # Our nodes are from 0 to n-1
    for _ in range(e):
        u, v = map(int, input().split())
        add_edge_list(adj_list, u, v)
        add_edge_matrix(adj_matrix, u, v)

    print_graph_list(adj_list)
    print_graph_matrix(adj_matrix)

if __name__ == "__main__":
    main()
