import pkg_resources
from symspellpy import SymSpell, Verbosity


#An average 5 letter word has about 3 million possible spelling errors within a maximum edit distance of 3
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename("symspellpy", "frequency_dictionary_en_82_765.txt")
bigram_path = pkg_resources.resource_filename("symspellpy", "frequency_bigramdictionary_en_243_342.txt")

# term_index is the column of the term and count_index is the
# column of the term frequency
def spell_corrector(input_term):
       sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
       sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)

       # lookup suggestions for multi-word input strings (supports compound
       # splitting & merging)
       #input_term = ('The yougn boy finaly understod the diffrence betwen paralell and perpendcular.')
       #input_term = ("whereis th elove hehad dated forImuch of thepast who couqdn'tread in sixtgrade and ins pired him")

       # max edit distance per lookup (per single word, not per whole input string)
       suggestions = sym_spell.lookup_compound(input_term, max_edit_distance=2)

       # display suggestion term, edit distance, and term frequency
       sent = []
       for suggestion in suggestions:
              sent.append(suggestion)

       predicted_sentence = str(sent[0])
       splitter = predicted_sentence[:-6]
       return splitter


#output = spell_corrector(input_term = 'The yougn boy finaly understod the diffrence betwen paralell and perpendcular.')
#print(output)