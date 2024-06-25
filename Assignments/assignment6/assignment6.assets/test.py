class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def buildHuffmanTree(char_freq):
    nodes = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    if not nodes:  # 如果节点列表为空，返回空树
        return None
    while len(nodes) > 1:
        nodes.sort(key=lambda x: (x.freq, x.char))
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = HuffmanNode(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        nodes.append(parent)
    return nodes[0]


def encode(root, code='', encoding_map={}):
    if root is None:
        return
    if root.char is not None:
        encoding_map[root.char] = code
    encode(root.left, code + '0', encoding_map)
    encode(root.right, code + '1', encoding_map)


def decode(root, encoded_str):
    decoded_str = ''
    current = root
    for bit in encoded_str:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.char is not None:
            decoded_str += current.char
            current = root
    return decoded_str


if __name__ == "__main__":
    # 读取字符集
    char_freq = {}
    line = input().strip()
    while not line.isdigit():
        char, freq = line.split()
        char_freq[char] = int(freq)
        line = input().strip()

    # 构建哈夫曼树和编码映射表
    tree = buildHuffmanTree(char_freq)
    if tree is not None:
        encode_map = {}
        encode(tree, '', encode_map)

        # 处理剩余输入，并输出结果
        n = int(line)
        for _ in range(n):
            line = input().strip()
            if line.isdigit():
                print(decode(tree, line))
            else:
                print(encode_map[line])

