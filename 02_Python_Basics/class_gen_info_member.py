class Member: 
    def __init__(self,name: str, age: int, secret_identity: str, powers: list[str]):
        self.name = name
        self.age = age
        self.secret_identity = secret_identity
        self.powers = powers
    

    def __str__(self):
        return f"Members(name={self.name}, age={self.age}, secret_identity={self.secret_identity}, powers={self.powers})"



