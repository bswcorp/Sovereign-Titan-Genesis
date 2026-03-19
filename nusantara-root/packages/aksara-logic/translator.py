class AksaraLogic:
    def __init__(self):
        self.syllables = ["ha", "na", "ca", "ra", "ka", "da", "ta", "sa", "wa", "la"]
    
    def encode_to_aksara(self, data_hex):
        # Mengubah Hash Hex menjadi deretan suku kata Aksara
        decimal = int(data_hex[:10], 16)
        return "".join([self.syllables[int(d)] for d in str(decimal)])
