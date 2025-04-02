import argparse
import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, ranges, output_folder="output"):
    """
    Découpe un fichier PDF selon les plages de pages spécifiées.

    Args:
        input_pdf (str): Chemin vers le fichier PDF d'entrée
        ranges (list): Liste de plages de pages sous forme de tuples (début, fin)
                      Les numéros de page commencent à 1 (comme dans un lecteur PDF)
        output_folder (str): Nom du dossier de sortie (par défaut: "output")

    Returns:
        list: Liste des chemins des fichiers PDF créés
    """
    # Vérifier que le fichier existe
    if not os.path.exists(input_pdf):
        raise FileNotFoundError(f"Le fichier {input_pdf} n'existe pas")

    # Obtenir le nom de base du fichier sans l'extension
    base_name = os.path.splitext(os.path.basename(input_pdf))[0]

    # Créer le dossier output s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Dossier '{output_folder}' créé.")

    # Créer un sous-dossier spécifique au fichier d'entrée
    file_output_folder = os.path.join(output_folder, base_name)
    if not os.path.exists(file_output_folder):
        os.makedirs(file_output_folder)
        print(f"Dossier '{file_output_folder}' créé.")

    # Ouvrir le PDF source
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    output_files = []

    # Traiter chaque plage
    for i, page_range in enumerate(ranges):
        start, end = page_range

        # Vérifier que les numéros de page sont valides
        if start < 1 or end > total_pages or start > end:
            print(f"Avertissement: Plage {start}-{end} invalide. Le PDF contient {total_pages} pages.")
            continue

        # Créer un nouveau PDF
        writer = PdfWriter()

        # Ajouter les pages (en convertissant de l'index utilisateur (1-based) à l'index Python (0-based))
        for page_num in range(start - 1, end):
            writer.add_page(reader.pages[page_num])

        # Créer le nom du fichier de sortie
        output_filename = f"{base_name}_{start}-{end}.pdf"
        output_path = os.path.join(file_output_folder, output_filename)

        # Enregistrer le nouveau PDF
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        output_files.append(output_path)
        print(f"Créé: {output_path}")

    return output_files

def parse_range(range_str):
    """
    Convertit une chaîne de caractères représentant une plage en tuple (début, fin).

    Args:
        range_str (str): Chaîne au format "début-fin"

    Returns:
        tuple: (début, fin) avec des valeurs entières
    """
    try:
        if '-' in range_str:
            start, end = map(int, range_str.split('-'))
            return (start, end)
        else:
            # Si une seule page est spécifiée, la page de début et de fin sont identiques
            page = int(range_str)
            return (page, page)
    except ValueError:
        raise ValueError(f"Format de plage invalide: {range_str}. Utilisez 'début-fin' ou 'page'.")

def main():
    parser = argparse.ArgumentParser(description="Découpe un fichier PDF en plusieurs selon des plages de pages spécifiées.")
    parser.add_argument("input_pdf", help="Chemin vers le fichier PDF à découper")
    parser.add_argument("ranges", nargs='+', help="Plages de pages au format '1-5' ou '7-10' ou un numéro de page unique")
    parser.add_argument("--output", "-o", default="output", help="Dossier de sortie (par défaut: 'output')")

    args = parser.parse_args()

    # Convertir les chaînes de plages en tuples (début, fin)
    page_ranges = [parse_range(r) for r in args.ranges]

    # Découper le PDF
    try:
        output_files = split_pdf(args.input_pdf, page_ranges, args.output)
        print(f"Découpage terminé. {len(output_files)} fichiers créés.")
    except Exception as e:
        print(f"Erreur lors du découpage du PDF: {e}")

if __name__ == "__main__":
    main()