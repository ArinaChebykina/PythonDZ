RNA_DNA_pairs = {'A':'T', 'U':'A', 'G':'C', 'C':'G'}
DNA_DNA_pairs = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
RNA = list(input())
DNA1=[]
DNA2=[]
for nuc in range(len(RNA)):
    NA = RNA_DNA_pairs.get(RNA[nuc])
    DNA1.append(NA)
    NA = DNA_DNA_pairs.get(DNA1[nuc])
    DNA2.append(NA)
DNA1=''.join(DNA1)
DNA2=''.join(DNA2)
print(DNA1)
print(DNA2)
    
