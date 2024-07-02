from dataclasses import dataclass

@dataclass
class Gene:
    GeneID: str
    Function: str
    Essential: str
    Chromosome: int
