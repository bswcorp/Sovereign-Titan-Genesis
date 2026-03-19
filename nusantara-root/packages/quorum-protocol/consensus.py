class QuorumProtocol:
    def verify_node(self, signature, aksara_key):
        # Jika signature tidak cocok dengan kunci Aksara, intervensi aktif
        return signature.startswith(aksara_key[:4])
      
