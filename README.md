# Assignment Objectives

Project ini dibuat guna mengevaluasi konsep berikut:

- Mampu menggunakan Apache Airflow
- Mampu melakukan validasi data dengan menggunakan Great Expectations
- Mampu memahami konsep NoSQL secara keseluruhan.
- Mampu mempersiapkan data untuk digunakan sebelum masuk ke database NoSQL.
- Mampu mengolah dan memvisualisasikan data dengan menggunakan Kibana.

---

# Data Sources
Dataset diambil dari repository dibawah ini:

- [Kaggle datasets](https://www.kaggle.com/code/akshitmadan/complete-data-analysis-supermarket-dataset/input)

# Problems

Membuat report yang berisi Exploratory Data Analysis (EDA) dari dataset.
  
Dataset akan terlebih dahulu dilakukan Data Cleaning dan validasi data menggunakan Great Expectation. Semua proses dilakukan dengan pipeline yang dijalankan menggunakan Apache Airflow. Berikut ini adalah langkah-langkah yang dilakukan : 

1. Dataset ini diberi nama `data_raw.csv`.

2. Data dimasukkan ke dalam PostgreSQL local dan diberi nama table untuk menyimpan data tersebut dengan `table_m3`.

3. Setelah data berada didalam database, semua data diambil dari database dengan menggunakan Python dan lakukan beberapa Data Cleaning berikut ini dengan menggunakan Python :
   - Hapus data yang duplikat.
   - Normalisasi column dengan cara : 
     + Semua nama column menjadi lowercase. Contoh : `ID` → `id`, `EDUCATION` → `education`, `Age` → `age`.
     + Mengganti tipe data

4. Setelah dilakukan Data Cleaning, data clean ini disimpan ke dalam CSV file dengan nama `data_clean.csv`.

5. Python Notebook (data_GX.ipynb) dibuat untuk melakukan validasi data menggunakan Great Expectations. Adapun kriteria mengenai Expectation yang dipilih adalah :
   - 7 Expectations yang didalamnya ada Expectation untuk:
     + to be unique
     + to be between min_value and max_value
     + to be contain in column
     + to be in type list
     + to be match strftime format
     + to be in set


   - Ketujuh Expectation yang digunakan semuanya bernilai `success: true`.

6. Selain disimpan ke dalam file CSV seperti poin 4, data clean ini juga dimasukkan ke dalam Elastic Search dengan menggunakan Python.

7. Automasi dengan membuat DAG dengan kriteria :
   - DAG berisi 3 node/task dibawah ini :
     + `Fetch from Postgresql` : berisi script untuk mengambil data dari PostgreSQL.
     + `Data Cleaning` : berisi script untuk melakukan Data Cleaning dan penyimpanan ke CSV file.
     + `Post to Elasticsearch` : berisi script untuk me-load CSV yang berisi data yang sudah clean dan memasukkannya ke Elasticsearch.
   - Penjadwalan dilakukan setiap jam 06:30.
   - File DAG dengan nama `DAG.py`.

8. Membuat dashboard dengan Kibana terhadap data clean ini dengan ketentuan :
   - Exploratory Data Analysis dilakukan terkait :
     * Latar belakang adanya report
     * Tujuan yang hendak dicapai
     * Divisi/tim yang membutuhkan
     * dll
   - Terdapat 6 visualisasi terhadap data tersebut yang mendukung tercapainya objective dari proses EDA yang dilakukan. Adapun 6 visualisasi menggunakan plot seperti :
     * 1 penggunaan Bar Plot
     * 1 penggunaan Pie Chart
     * 1 penggunaan Vertical Bar Plot
     * 1 penggunaan Word Cloud
     * 1 penggunaan Table
     * 1 penggunaan Line Chart
     
    - 1 visualisasi berupa `Markdown` yang berisi :
     + Kesimpulan eksplorasi yang dilakukan.
     + Saran lanjutan atau insight bisnis terhadap eksplorasi yang dilakukan.
     + Kesimpulan yang dituliskan berisi rekomendasi mengenai objective yang telah ditentukan berdasarkan gabungan antara hasil eksplorasi yang dilakukan dan suatu referensi eksternal (seperti teori suatu domain, pernyataan seorang ahli, fakta kompetitor, dll) sehingga rekomendasi dapat tepat sasaran dan masuk akal untuk diberikan.
   - Total visualisasi : 6 visualisasi + 1 visualisasi Markdown mengenai kesimpulan = 7 visualiasi.
   
---
## Conceptual Problems

1. Jelaskan apa yang dimaksud dengan NoSQL menggunakan pemahaman yang kalian ketahui !

2. Jelaskan kapan harus menggunakan NoSQL dan Relational Database Management System !

3. Sebutkan contoh 2 tools/platform NoSQL selain ElasticSearch beserta keunggulan tools/platform tersebut !

4. Jelaskan apa yang Anda ketahui dari Airflow menggunakan pemahaman dan bahasa Anda sendiri !

5. Jelaskan apa yang Anda ketahui dari Great Expectations menggunakan pemahaman dan bahasa Anda sendiri !

6. Jelaskan apa yang Anda ketahui dari Batch Processing menggunakan pemahaman dan bahasa Anda sendiri (Definisi, Contoh Kasus Penggunaan, Tools, dll) !