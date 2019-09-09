class Buffer:
    def __init__(self, size):
        """
        Args:
            size (int): Tamanho máximo do buffer
        """
        self.size = size

        # node_blocks (list): Lista de Buffer_Node's
        self.node_blocks = list()


    def sort(self):
        """
        Ordena o buffer a partir do valor do nodo, usando insertion sort 
        """
        for i in range(1, len(self.node_blocks)):
            key = self.node_blocks[i]

            j = i - 1
            while j >= 0 and key.value < self.node_blocks[j].value:
                self.node_blocks[j + 1] = self.node_blocks[j]
                j -= 1
            self.node_blocks[j + 1] = key


    def pop(self, index: int = -1):
        """
        Remove e retorna um nodo em um indice (último por padrão)

        Args:
            index (int): Índice onde será eliminado o item

        Returns:
            bool: Retorna o nodo eliminado da lista
        """
        return self.node_blocks.pop(index)


    def clear(self):
        """
        Remove todos os itens do buffer
        """
        self.node_blocks.clear()


    def writeFita(self, node, fita, end='\n'):
        """
        Escreve o valor de um nodo em uma fita

        Args:
            node (Buffer_Node): Um nodo de buffer
            fita: Arquivo txt onde será escrito
            end (str): String que terminará após a escrita do valor no arquivo
        """
        fita.write(f"{node.value}{end}")


    def writeAllInFita(self, fita, end='\n', sorted_buffer=True):
        """
        Escreve todos os itens do buffer em um arquivo txt, eliminando
        todos os itens do buffer

        Args:
            fita: Arquivo txt onde será escrito
            end (str): String que terminará após a escrita do valor no arquivo
            sorted_buffer (bool): Caso for verdadeiro, o buffer é ordenado antes
            da operação de escrita no arquivo
        """
        if sorted_buffer:
            self.sort()
        while not self.isEmpty():
            self.writeFita(self.pop(0), fita, end)


    def readNextInFita(self, node):
        """
        Lê de um nodo o próximo valor da fita onde ele pertence,
        adicionando um novo nodo ao Buffer

        Args: 
            node (Buffer_Node): Um nodo de buffer
        
        Returns:
            bool: Retorna falso caso não foi possivel ler o arquivo 
        """
        try:
            return self.addNode(node.readFitaValue(), node.fita)
        except ValueError:
            return False

    def readFita(self, fita):
        value = int(fita.readline().rstrip())
        self.addNode(value, fita)

    
    def addNode(self, value, fita):
        """
        Adiciona um novo nodo ao Buffer, respeitando o tamanho máximo dele

        Args:
            value (int): Valor da fita para adicionar no novo nodo
            fita: Arquivo txt onde o valor pertence

        Returns:
            bool: Retorna verdadeiro caso a operação de adição for bem sucedida
        """
        if not self.isFull():
            new_node = Buffer_Node(value, fita)
            self.node_blocks.append(new_node)
            return True
        else:
            print("Buffer is Full! Can't add more itens.")
            return False
    

    def isFull(self):
        """
        Returns:
            bool: Retorna verdadeiro caso o buffer estiver cheio
        """
        return len(self.node_blocks) == self.size


    def isEmpty(self):
        """
        Returns:
            bool: Retorna verdadeiro caso o buffer estiver vazio
        """
        return len(self.node_blocks) == 0

    def currentSize(self):
        """
        Returns:
            int: Retorna o tamanho atual do buffer
        """
        return len(self.node_blocks)

    
    def printBuffer(self):
        """
        Imprime o Buffer
        """
        print('-=' * 20)
        print("Buffer:")
        for i, node in enumerate(self.node_blocks):
            print(f'Node {i}:')
            print(node)
        print('-=' * 20)


class Buffer_Node:
    def __init__(self, value, fita):
        """
        Args:
            value (int): Valor do Buffer
            fita: Arquivo txt onde value pertence
        """
        self.value = value
        self.fita = fita


    def readNextFitaValue(self):
        """
        Lê o próximo elemento que está na fita do nodo

        Returns:
            int: Retorna o valor da fita caso a operação for bem sucedida
            None: Caso não foi possivel ler o valor da fita
        """
        try:
            return int(self.fita.readLine().rstrip())
        except:
            return None


    def __str__(self):
        return f"""\tValue: {self.value}\n\tFita: {self.fita.name}"""
