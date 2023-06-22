class SimpleItemInfo:
    def __init__(self, sku, title) -> None:
        self.id = None
        self.sku = sku
        self.title = title

class SimpleLootboxItem:
    def __init__(self, sku=None, title=None, diff=None, id=None) -> None:
        self.sku = sku
        self.title = title
        self.diff = diff
        self.id = id
        self.reward_items = None

    def write_to_console(self, indent : str):
        print(f"{indent}Lootbox Item ID: {self.id}\n")
        if self.reward_items:
            print(f"{indent}Reward Items:\n")
            for item in self.reward_items:
                print(f"\t{indent}{item.id} : {item.sku} : {item.title}\n")