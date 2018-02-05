# MusicGenreClassifier
A Python program that utilizes the k-nearest neighbors algorithm (k-NN) in order to classify wav files into various music genres. This program was initially made for HackUCI 2018, so it is not very robust.

## Getting Started
This program requires a few libraries. It requires that Scipy is installed. We used Anaconda 2 during the development of this project. It also utilizes python_speech_features, which can be installed as such:

To install from pypi:: 
```
pip install python_speech_features
```
	
From this repository::
```
git clone https://github.com/jameslyons/python_speech_features
python setup.py develop
```
## Running the classifier
### Creating the training data
This program requires training data in the form of .wav files. These will be placed into a directory named Music. Within this directory, songs will be categorized by genre for the the program to read. These files will then be preprocessed and turned into data that the classifier can read. This data will be written in SongData.txt. A default SongData.txt with sample test data from a few genres is included.

It is also recommended that songs in which it is trained on are split into multiple .wav files of 15 second intervals. This seems to increase the accuracy of the learner.
You can turn off preprocessing by changing:
```
#classify.py
PREPROCESS = True #if True, it will preprocess the data
```
to
```
#classify.py
PREPROCESS = False #if True, it will preprocess the data
```
This doing this will shorten the runtime of the program, as the preprocess phase can take a long time on large data sets.

### Predicting Song Genres
Once the learner is given adequate training data, it can attempt to interpolate the genre of a song. To do this, place all .wav files in a directory titled "predictions". You can now run the program from classifier.py.

Once all of the input songs are classified, it will create a text file titled "predictions.txt" with the names of the files and their predicted genres.
