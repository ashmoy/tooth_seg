# BatchDentalSeg
3D Slicer extension for fully-automatic segmentation of CT and CBCT dental volumes in batch using Dentalsegmentator model (for adults scans)  or PediatricDentalsegmentator model (for children scans).

![image](https://github.com/user-attachments/assets/240928bd-6551-46db-8688-7b6b581f5d70)
After selecting the folder with the volumes to process and the model that fit better your scans, this module generates the following segmentations for each volumes: 
* Maxilla & Upper Skull
* Mandible
* Upper Teeth
* Lower Teeth
* Mandibular canal

## DentalSegmentator model

DentalSegmentator is based on nnU-Net framework. It has been trained on 470 dento-maxillo-facial CT and CBCT scans, and evaluated on a hold-out test dataset of 256 CT and CBCT scans from 7 institutions by Dot G, et al, here is their paper and nnUnet paper:

>Dot G, et al. DentalSegmentator: robust open source deep learning-based CT and CBCT image segmentation. Journal of Dentistry (2024) doi:[10.1016/j.jdent.2024.105130](https://doi.org/10.1016/j.jdent.2024.105130)

>Isensee F, et al. nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nat Methods. 2021;18(2):203-211. doi:[10.1038/s41592-020-01008-z](https://doi.org/10.1038/s41592-020-01008-z)

## PediatricDentalSegmentator model

As DentalSegmentator, PediatricDentalSegmentator is based on nnUnet too, It has been trained on 513 dento-maxillo-facial CBCT scans including scans withs primary teeths and evaluated on a hold-out test dataset of 56 CT and CBCT scans


## Using the extension

This extension is compatible with the latest 3D Slicer Stable Release (version 5.8.0, or later), downloadable [from the official website]( https://download.slicer.org/ ). 

The plugin can be installed in Slicer using
the [extension manager]( https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions).
It's a module frome the automated dental tools so it can be can be found using the search bar by typing "Atomated Dental Tools".

After the install process and restart of Slicer, the extension can be found in the module file explorer under `Automated Dental Tools>BatchDentalSegmentator`.
It can also be found by using the `find` module button and searching for the keyword `BatchDentalSegmentator`.

To use the extension, click on `Select Folder` to select the folder where your scans are.

![image](https://github.com/user-attachments/assets/72bb7c14-6ed7-4036-a2e5-e76633f03c44)

Then choose the model that you want to use (DentalSegmentator for adults scans) or PediatricDentalSegmentator (for children scans)

![image](https://github.com/user-attachments/assets/c4529265-3dcc-4deb-b835-4988630100e2)

Finally click on the `Apply` button to start the segmentations.

![image](https://github.com/user-attachments/assets/3c03bc13-cfc6-4b37-b743-13d30a8c1107)

If your device doesn't include CUDA, the processing may be very long and a dialog will ask for confirmation before
starting the segmentation process.

During execution, the processing can be canceled using the `Stop` button.
The progress will be reported in the console logs.

![image](https://github.com/user-attachments/assets/fff5a0a2-d29d-4368-b10c-e4dd3490b70f)


After the segmentation process has run, the segmentation will be loaded into the application.
The segmentation results can be modified using the `Segment Editor` tools.

![Screencast from 04-22-2025 11_01_23 AM](https://github.com/user-attachments/assets/df2ba70d-bd36-46f4-8ab2-a9dfabc68874)

The segmentation can be exported using the `Export segmentation` menu and selecting the export format to use.

The `Surface smoothing` slider allows to change the 3D view surface smoothing algorithm.

## Exemple of using 

![exemple_use3](https://github.com/user-attachments/assets/19ec5b61-9733-4749-99ca-a9ce748df811)


## Acknowledgments 

