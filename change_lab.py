import os
import nibabel as nib
import numpy as np
from tqdm import tqdm

# Dictionnaire de mappage des labels
label_mapping = {
    0: 0,  # Background
    54: 1,  # Maxilla -> Upper Skull
    53: 2,  # Mandible
    **dict.fromkeys(list(range(1, 17)) + list(range(33, 44)), 3),  # Upper Teeth (1-16, 33-43)
    **dict.fromkeys(list(range(17, 33)) + list(range(44, 53)), 4),  # Lower Teeth (17-32, 44-52)
    55: 5  # Mandibular canal
}

def remap_labels(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    # Liste des fichiers à traiter
    nii_files = [f for f in os.listdir(input_folder) if f.endswith(".nii.gz")]
    
    # Barre de progression
    with tqdm(total=len(nii_files), desc="Traitement des fichiers", unit="fichier") as pbar:
        for filename in nii_files:
            file_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            # Charger l'image NIfTI
            img = nib.load(file_path)
            data = img.get_fdata()
            
            # Remapper les labels
            remapped_data = np.zeros_like(data, dtype=np.int32)
            for original_label, new_label in label_mapping.items():
                remapped_data[data == original_label] = new_label
            
            # Créer une nouvelle image NIfTI
            new_img = nib.Nifti1Image(remapped_data, img.affine, img.header)
            
            # Sauvegarder l'image modifiée
            nib.save(new_img, output_path)
            pbar.update(1)  # Met à jour la barre de progression

    print(f"\nTraitement terminé. Fichiers modifiés sauvegardés dans {output_folder}.")

# Exemple d'utilisation
input_folder = "dentalseg"
output_folder = "labels_for_retrain_dental"
remap_labels(input_folder, output_folder)
