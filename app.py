import os
import math

from binaryornot.check import is_binary
from termcolor import colored
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

student_files = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser("files/")) for f in fn if not (is_binary(dp+"/"+f))]
student_notes = [open(_file, encoding='utf-8').read()
                 for _file in student_files]


def vectorize(Text): return TfidfVectorizer().fit_transform(Text).toarray()
def similarity(doc1, doc2): return cosine_similarity([doc1, doc2])

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def is_binary(f):
    return 'b' in f.mode

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))
plagiarism_results = set()


def check_plagiarism():
    global s_vectors
    for student_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            score = (student_pair[0], student_pair[1], sim_score)
            plagiarism_results.add(score)
    return plagiarism_results


print("Plagiarism checker")
for data in sorted(check_plagiarism(), key=lambda i: float(i[2]), reverse=True):
    val = round_up(data[2]*100, 3)
    if val > 80:
        print(colored("[" + str('{:.2%}'.format(data[2])) + "] '" + data[0] + "' -> '" + data[1], 'red'))
    elif (val < 80) & (val > 60):
        print(colored("[" + str('{:.2%}'.format(data[2])) + "] '" + data[0] + "' -> '" + data[1], 'yellow'))
    else:
        print(colored("[" + str('{:.2%}'.format(data[2])) + "] '" + data[0] + "' -> '" + data[1], 'green'))

