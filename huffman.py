import heapq
from collections import Counter, namedtuple

# Define a Node structure to store each character and its frequency
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

# Build the Huffman Tree
def build_huffman_tree(frequencies):
    heap = [Node(char, freq, None, None) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, new_node)

    return heap[0] if heap else None

# Generate Huffman Codes
def generate_codes(node, prefix="", code_dict={}):
    if node:
        if node.char is not None:
            code_dict[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_dict)
        generate_codes(node.right, prefix + "1", code_dict)
    return code_dict

# Main function to perform Huffman Encoding
def huffman_encoding(data):
    if not data:
        return {}, ""
    
    frequencies = Counter(data)
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_codes(huffman_tree)

    encoded_data = "".join(huffman_codes[char] for char in data)
    return huffman_codes, encoded_data

# Example usage
data = "huffman encoding example"
codes, encoded_text = huffman_encoding(data)
print("Character codes:", codes)
print("Encoded text:", encoded_text)
