class Nucleobase:
    def __init__(self):

        def adenine(self, string):
            a_count = 0
            for i in string:
                if i == "A":
                    a_count += 1
                else:
                    continue
            return a_count
        
        def cytosine(self, string):
            c_count = 0
            for i in string:
                if i == "C":
                    c_count += 1
                else:
                    continue  
            return c_count 

        def guanine(self, string):
            g_count = 0
            for i in string:
                if i == "G":
                    a_count += 1
                else:
                    continue   
            return g_count      

        def thymine(self, string):
            t_count = 0
            for i in string:
                if i == "T":
                    t_count += 1
                else:
                    continue
            return t_count

dna_test = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

parse_test = Nucleobase()
print(parse_test.adenine(dna_test), parse_test.cytosine(dna_test), parse_test.guanine(dna_test), parse_test.thymine(dna_test))








