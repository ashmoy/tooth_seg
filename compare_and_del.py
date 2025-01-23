import os

def compare_and_delete(folder1, folder2):
    """
    Compare les noms des fichiers entre deux dossiers et supprime ceux qui n'ont
    pas de correspondant dans l'autre dossier.

    :param folder1: Chemin du premier dossier
    :param folder2: Chemin du second dossier
    """
    # Obtenir la liste des fichiers dans chaque dossier
    files_folder1 = set(os.listdir(folder1))
    files_folder2 = set(os.listdir(folder2))

    # Fichiers à supprimer dans chaque dossier
    files_to_delete_in_folder1 = files_folder1 - files_folder2
    files_to_delete_in_folder2 = files_folder2 - files_folder1

    # Supprimer les fichiers dans folder1 qui n'ont pas de correspondant dans folder2
    for file in files_to_delete_in_folder1:
        file_path = os.path.join(folder1, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Supprimé dans {folder1} : {file}")

    # Supprimer les fichiers dans folder2 qui n'ont pas de correspondant dans folder1
    for file in files_to_delete_in_folder2:
        file_path = os.path.join(folder2, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Supprimé dans {folder2} : {file}")

# Exemple d'utilisation
folder1 = "Scan_Ana"
folder2 = "labels_for_retrain_dental"

compare_and_delete(folder1, folder2)
