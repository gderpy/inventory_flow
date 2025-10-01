import re


class EmailField:
    """Дескриптор, проверяющий E-Mail при назначении"""

    EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

    def __set_name__(self, owner, name):
        self._private_name = f"_{name}"

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return getattr(instance, self._private_name, None)

    def __set__(self, instance, value):
        self._validate(value)
        setattr(instance, self._private_name, value)

    @classmethod
    def _validate(cls, email: str) -> None:
        if not isinstance(email, str):
            raise TypeError("E-Mail должен быть строкой.")
        if not cls.EMAIL_REGEX.match(email):
            raise ValueError("Некорректно указан E-Mail")


class Supplier:
    """Класс,описывающий поставщика"""

    email = EmailField()

    def __init__(self, name: str, email: str, contact_person: str) -> None:
        self.name = self._normalize_name(name)
        self.email = email
        self.contact_person = contact_person

    @staticmethod
    def _normalize_name(name: str) -> str:
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой.")
        clean_name = name.strip()
        if not clean_name:
            raise ValueError("Название не может быть пустым.")
        return clean_name

    @property
    def contact_person(self) -> str:
        return self.__contact_person

    @contact_person.setter
    def contact_person(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Контакт для связи должен быть строкой.")
        clean_value = value.strip()
        if not clean_value:
            raise ValueError("Контакт для связи не может быть пустым")
        self.__contact_person = clean_value

    def __repr__(self) -> str:
        return (
            f"Supplier(name={self.name!r}, email={self.email!r}, "
            f"contact_person={self.contact_person!r})"
        )
    