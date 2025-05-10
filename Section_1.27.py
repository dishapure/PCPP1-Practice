class ItemNotFound(Exception):
    def __init__(self, item):
        self.item = item
        super().__init__(f"Item '{item}' not found in inventory.")

inventory = {"apple": 10, "banana": 5}
def get_stock(item):
    try:
        return inventory[item]
    except KeyError as ke:
        raise ItemNotFound(item) from ke

try:
    print(get_stock("orange"))
except ItemNotFound as e:
    print(f"Custom Exception: {e}")
    print(f"Original cause: {e.__cause__}")
