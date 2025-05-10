This github repository is dedicated for transformer model based project.
Here,
    ✅ pah-vit.ipynb is the notebook for classifying Pulmonary Atrial Hypertension (PAH) from the echocardiogram images. 
    ✅ asd-vit.ipynb is the notebook for classifying Atrial Septal Defect (ASD) from the echocardiogram images. 
        Here some associated code books are
               ✔️file_formater.py : for fomratting the images file name for passing through the transformer model
               ✔️Data_prep.ipynb : for extracting slice images from the .nii file from the CardiacNet dataset

    🚩Steps: CardiacNet dataset ---> label ---> best slices selection which can label A4C of heart ---> same slices from the .nii images ---> Test_train dataset ---> ViT model (with & without pretrained weight) ---> classification 

✅ smoking.ipynb for people who smoking classification from image 
✅ EEG SEED V for emotion classification using subject 1 session 1 

Other files are different implementations of the transformer model on various dataset.
