# Plagiarism-checker-Python

This repo consists of a source code of a python script to detect plagiarism in textual document using **cosine similarity**

[Patreon of original creator](https://www.patreon.com/kalebujordan)

## How is it done?

You might be wondering on how plagiarism detection on textual data is done, well it aint that complicated as you may think.

We all all know that computer are good at numbers, so in order to compute the simlilarity between on two text documents, the textual  raw data is transformed into vectors => arrays of numbers and then from that we are going to use a basic knowledge vector to compute the the similarity between them.

This repo consist of a basic example on how to do that.

## Where is the improvement?

- My fork checks and compares all files in subdirectories recursively (binary files excluded)
- It's colorful (red: > 80%, orange: <= 80 && >= 60, green < 60%)
- Simple visible percentage in output

## Getting started

To get started with the code on this repo, you need to either *clone* or *download* this repo into your machine just as shown below;

```bash
git clone https://github.com/DanielADK/Plagiarism-checker-Python
```

## Dependencies 

Before you begin playing with the source code you might need to install deps just as shown below;

```bash
pip3 install -r requirements.txt
```

## Running the App

To run this code you need to have your non-binary documents in your "files/" directory and then when you run the script, it will automatically loads all the documents with that extension and then compute the similarity between them just as shown below;

```bash
$-> cd Plagiarism-checker-Python
$ Plagiarism-checker-Python-> python3 app.py
Plagiarism checker
[41.47%] 'files/kevin.html' -> 'files/max.html
[37.63%] 'files/andrew.html' -> 'files/kevin.html
[32.48%] 'files/jesse.html' -> 'files/max.html
[31.58%] 'files/andrew.html' -> 'files/max.html
[30.72%] 'files/jesse.html' -> 'files/kevin.html
[26.73%] 'files/andrew.html' -> 'files/jesse.html

```

## A python library ?

Would you like to use Python library instead to help you compare strings and documents without spending time writing the vectorizers by your own then take a look at [Pysimilar](https://github.com/Kalebu/pysimilar).

## Explore it 

Explore it and twist it to your own use case, in case of any question feel free to reach me out directly *isaackeinstein(at)gmail.com*

## Issues 

Incase you have any difficulties or issues while trying to run the script
you can raise it on the issues. 

## Pull Requests

If you have something to add I welcome pull requests on improvement , you're helpful contribution will be merged as soon as possible

## Give it a Star

If you find this repo useful , give it a star so as many people can get to know it.

## Credits

All the credits to [kalebu](https://github.com/kalebu)

Forker: [DanielADK](https://github.com/DanielADK)
