class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        node = root
        while node.value is None:
            if x[node.indx]:
                node = node.left
            else:
                node = node.right

        return node.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node is None:
            cls.root = obj
            return obj
        elif left:
            node.left = obj
            return obj
        else:
            node.right = obj
            return obj


class TreeObj:
    def __init__(self, indx, value=None):
        """
        :params indx: - проверяемый индекс (целое число);
        :params value: - значение с данными (строка);
        :params __left: - ссылка на следующий объект дерева по левой ветви (изначально None);
        :params __right: - ссылка на следующий объект дерева по правой ветви (изначально None).
        """
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right
