✅ download the SEED V dataset from the official website 

✅ download the subjeect1_session_1 eeg file in .cnt format

✅ then run dataprocessor.ipynb

✅ eeg signal ---> eeg down sample (200Hz) ---> eeg bandpass filtering (1-50 Hz) --> 15 trial find out ---> separate 62 channel 5 band data (62*5 eeg signal) ---> generate CWT scalogram image ---> train test split ---> classification using ViT

✅ for train test band-wise. for each trial for each band 80% training and 20% testing

✅ EEG-SEEDV-s1s1.ipynb for ViT 

✅ putting different single image to see the performance of classification task. 