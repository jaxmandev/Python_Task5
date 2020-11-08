# create parent class
class Nucleobase:
    def __init__(self):

        # create method to count A occurences
        def adenine(self, string):
            a_count = 0
            for i in string:
                if i == "A":
                    a_count += 1
                else:
                    continue
            return a_count
        
        # create method to count C occurences
        def cytosine(self, string):
            c_count = 0
            for i in string:
                if i == "C":
                    c_count += 1
                else:
                    continue  
            return c_count 

        # create method to count G occurences
        def guanine(self, string):
            g_count = 0
            for i in string:
                if i == "G":
                    a_count += 1
                else:
                    continue   
            return g_count      

        # create method to count T occurences
        def thymine(self, string):
            t_count = 0
            for i in string:
                if i == "T":
                    t_count += 1
                else:
                    continue
            return t_count

# test data
dna_test = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# create an object or instance of the Nucleobase class
parse_test = Nucleobase()

# print the respective Nucleobase's counts
print(parse_test.adenine(dna_test), parse_test.cytosine(dna_test), parse_test.guanine(dna_test), parse_test.thymine(dna_test))








