Instagram Web Scraping 
By:
-Steven Putra Tanoto (03082180016)
-Mario Chandra (03082180013)
-Andika Adhinata (03082180004)

Program tersebut memiliki fitur untuk:
- Mengambil link post dari user instagram yang diinginkan
nama function : last_recent_post
- Mencari hashtags dan mentions dari suatu komentar instagram
nama function : find_hashtags and find_mentions
- Mengambil data-data dari postingan berupa waktu,likes,komentar terakhir dari suatu postingan instagram
nama function : post_link_detail
- Mendownload foto yang diposting ke instagram
nama function : download_ig_photo
- Membuat laporan csv hasil pendataan dari data-data postingan
nama function :generate_csv

Library yang perlu diinstall sebelum menggunakan program atau menjalankan main.py adalah:
- pandas
- selenium
- geckodriver

Cara Install pandas:
install from pip : "pip install pandas"
jika pip error boleh refer ke "https://stackoverflow.com/questions/42907331/how-to-install-pandas-from-pip-on-windows-cmd"

Cara Install Selenium :
Dengan pip : C:\Python34\Scripts\pip.exe install -U selenium
atau dengan file yang sudah saya berikan 
cd ke folder selenium-3.141.0 lalu ketik "python setup.py install"

Geckodriver sudah built in di folder, jadi akan run otomatis ketika main.py dijalankan

Browser yang harus digunakan : firefox diatas versi 60

Github : https://github.com/StevenTannn/teknikpemogramanuas

Hasil Tampilan :

Saat run main.py di environment mac os:
https://raw.githubusercontent.com/StevenTannn/images/master/run.png

Hasil Csv:
https://raw.githubusercontent.com/StevenTannn/images/master/csv.png

Hasil folder csv:
https://raw.githubusercontent.com/StevenTannn/images/master/foldercsv.png

Hasil folder images:
https://raw.githubusercontent.com/StevenTannn/images/master/folderimg.png
