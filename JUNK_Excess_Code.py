# for ind1, seq in enumerate(seqs):
#     lens.append(len(seq))
#     max_len=min(lens)
# # print(max_len)
#     for i in range(1,max_len+1):
#         mot=seq[:i]
#         # print(mot)
#         for ind2, seq2 in enumerate(seqs):
#             # print(seq2)
#             if ind1==ind2 or len(mot)<2:
#                 pass
#             elif re.findall(mot,seq2):
#                 # print(f'found motif: {mot}')
#                 prelim_mots.add(mot)
#
#         mot=seq[i:]
#         # print(mot)
#         for ind2, seq2 in enumerate(seqs):
#             # print(seq2)
#             if ind1==ind2:
#                 pass
#             elif len(mot)<2:
#                 pass
#             elif re.findall(mot,seq2):
#                 # print(f'found motif: {mot}')
#                 prelim_mots.add(mot)
#
#         for k in range(0,max_len+1):
#             mot=seq[i:k]
#             for ind2, seq2 in enumerate(seqs):
#                 # print(seq2)
#                 if ind1==ind2:
#                     pass
#                 elif len(mot)<2:
#                     pass
#                 elif re.findall(mot,seq2):
#                     # print(f'found motif: {mot}')
#                     prelim_mots.add(mot)
