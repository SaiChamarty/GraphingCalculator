import sys
import matplotlib.pyplot as plt
import numpy as np  
import re
import networkx as nx

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return abs(a - b)
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Division not possible!")
    
    def quadratic(self):
        # This method can be enhanced to parse a quadratic string if needed.
        function = input("Usage: Enter a quadratic in the form <a * X^2 + b * X + C>: ")
        # Replace '^2' with '*X' as a simple transformation (adjust as needed)
        function = function.replace("^2", "*X")
        x_values = []
        y_values = []
        for x in range(-10, 10):
            x_values.append(x)
            y = self.evalTerm(function, x)
            y_values.append(y)
        plt.plot(x_values, y_values)
        plt.title(f"Quadratic equation: {function}")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()
    
    def evalTerm(self, term, x_val):
        # Replace 'X' with the numeric value and evaluate the term.
        x_sub_term = term.replace("X", str(x_val))
        return eval(x_sub_term)
    
    def plot_weighted_graph(self):
        # Define the weighted graph as a dictionary
        weighted_graph = {
            'A': {'B': 2, 'C': 5},
            'B': {'C': 1, 'D': 2},
            'C': {'D': 3, 'E': 1},
            'D': {'E': 2, 'F': 3},
            'E': {'F': 2},
            'F': {}
        }
        # Create a directed graph using NetworkX
        G = nx.DiGraph()
        for node, edges in weighted_graph.items():
            for neighbor, weight in edges.items():
                G.add_edge(node, neighbor, weight=weight)
        
        # Compute positions for visualization using a spring layout
        pos = nx.spring_layout(G)
        
        # Draw the graph components
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
        nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
        
        plt.title("Weighted Graph")
        plt.axis('off')
        plt.show()


print("Usage: python calculator.py <operation> <a> <b>")
print("Available operations: add, subtract, multiply, divide")
option = input("[1]: Arithmetic [2]: Graph [3]: Matrix ")

if __name__ == "__main__":
    calculator = Calculator()

    if option == "1":
        # Arithmetic operations: use command line arguments
        while True:
            try:
                operation = sys.argv[1].lower()
                a = float(sys.argv[2])
                b = float(sys.argv[3])
    
                if operation == "add":
                    result = calculator.add(a, b)
                elif operation == "subtract":
                    result = calculator.subtract(a, b)
                elif operation == "multiply":
                    result = calculator.multiply(a, b)
                elif operation == "divide":
                    result = calculator.divide(a, b)
                else:
                    print("Invalid input; Usage: python calculator.py <operation> <a> <b>")
                    break
    
                print("Result:", result)
                break
            except (ValueError, IndexError):
                print("Invalid input; Usage: python calculator.py <operation> <a> <b>")
                break
    
    elif option == "2":
        # Graphing option: let the user choose which graph to plot.
        while True:
            try:
                print("Select Graph Type:")
                print("[1]: Quadratic Equation")
                print("[2]: Weighted Graph (Directed)")
                graph_option = input("Enter your choice (1 or 2): ")
                if graph_option == "1":
                    calculator.quadratic()
                    break
                elif graph_option == "2":
                    calculator.plot_weighted_graph()
                    break
                else:
                    print("Invalid graph option. Please choose 1 or 2.")
            except Exception as e:
                print("Error:", e)
                break
    
    elif option == "3":
        print("Matrix functionality is not implemented yet.")
    
    else:
        print("Invalid option. Please select 1, 2, or 3.")