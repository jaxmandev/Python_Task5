# create parent class
class Nucleobase:
    def __init__(self, dna_to_count):
        self.dna_to_count = dna_to_count

        # create method to count A occurences
        def adenine(self, dna_to_count):
            a_count = 0
            for i in dna_to_count:
                if i == "A":
                    a_count += 1
                else:
                    continue
            return a_count
        
        # create method to count C occurences
        def cytosine(self, dna_to_count):
            c_count = 0
            for i in dna_to_count:
                if i == "C":
                    c_count += 1
                else:
                    continue  
            return c_count 

        # create method to count G occurences
        def guanine(self, dna_to_count):
            g_count = 0
            for i in dna_to_count:
                if i == "G":
                    a_count += 1
                else:
                    continue   
            return g_count      

        # create method to count T occurences
        def thymine(self, dna_to_count):
            t_count = 0
            for i in dna_to_count:
                if i == "T":
                    t_count += 1
                else:
                    continue
            return t_count

def main():
    # ask for an input to be checked
    dna_to_count = input("Please input a DNA sequence: ").upper()
    
    # create an object or instance of the Nucleobase class
    parse_test = Nucleobase(dna_to_count)
    
    # print the respective Nucleobase's counts
    print(parse_test.adenine(dna_to_count), parse_test.cytosine(dna_to_count), parse_test.guanine(dna_to_count), parse_test.thymine(dna_to_count))








