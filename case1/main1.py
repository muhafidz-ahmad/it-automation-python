import time
from auth import auth
from gsheet_editor import update_gsheet
from get_data_from_web import get_data

def main():
    # --- Langkah-langkah untuk memakai program ini
    # Share file Google Sheet ke email Service Account di Google Cloud Project yang telah aktif Google Sheet API dan Google Drive API
    # Copy path keys Service Account pada variabel key_path di bawah
    key_path = 'it-automation-dicoding-gsheet.json'
    gc = auth(key_path)

    # Buka file Google Sheets
    sheet = gc.open('Kampus Merdeka Program')

    # Buka Worksheet
    worksheet = sheet.get_worksheet(0)

    # Web Scraping
    df = get_data('https://kampusmerdeka.kemdikbud.go.id/program/studi-independen/browse/')
    update_gsheet(worksheet, df)
    return

# Function Call
if __name__ == '__main__':
    start = time.time()
    main()
    runtime = time.time() - start
    menit = int(runtime / 60)
    detik = int(runtime % 60)
    print(f"Runtime: {menit} menit {detik} detik")