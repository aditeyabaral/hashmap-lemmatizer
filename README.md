# HashMap-Lemmatizer
A simple lemmatizer made as a part of the Data Structures (UE18CS202) course at PES University. We used the concepts of graph networks combined with a HashMap to create the database of words along with their lemma. Our lemmatizer worked faster than WordNet's Lemmatizer on Python, and hence can be used on a higher scale to lemmatize large corpuses in marginal time.

# Dependencies
* WordForms.py: Scrapes content from an online database of verb forms and stores them in VerbForms.csv
* VerbForms.csv: Contains words along with their lemmas

# Execution
```
gcc HashMapLemma.c
./a.out
```
