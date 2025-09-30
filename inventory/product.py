import uuid


class Product:
    __slots__ = ("_title", "__price", "_sku")

    def __init__(self, title: str, price: float):
        self._title = title
        self.__price = price
        self._sku = self.generate_sku()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может отрицательной!")
        self.__price = value

    @property
    def sku(self):
        return self._sku

    # Фабричный метод
    @classmethod
    def create_from_dict(cls, data: dict):
        return cls(title=data["title"], price=data["price"])

    @staticmethod
    def generate_sku():
        return str(uuid.uuid4())[:8].upper()

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self._sku == other._sku

    def __hash__(self):
        return hash(self._sku)

    def __repr__(self):
        return f"Product(title={self._title!r}, price={self.__price}, sku={self._sku})"

    def __str__(self):
        return f"{self._title} - {self.__price}"
