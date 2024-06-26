<h1>Python CSV</h1>

Menonton sekarangTutorial ini memiliki kursus video terkait yang dibuat oleh tim Real Python. Tonton bersama dengan tutorial tertulis untuk memperdalam pemahaman Anda: [**Membaca dan Menulis File CSV**](https://realpython.com/courses/reading-and-writing-csv-files/)

Jujur saja: Anda perlu memasukkan dan mengeluarkan informasi dari program Anda melalui lebih dari sekedar keyboard dan konsol. Bertukar informasi melalui file teks adalah cara umum untuk berbagi informasi antar program. Salah satu format paling populer untuk bertukar data adalah format CSV. Tapi bagaimana cara menggunakannya?

Mari kita perjelas satu hal: Anda tidak perlu (dan Anda tidak akan) membuat parser CSV Anda sendiri dari awal. Ada beberapa perpustakaan yang dapat Anda gunakan. [`csv`Pustaka](https://docs.python.org/3/library/csv.html) Python akan berfungsi untuk sebagian besar kasus. Jika pekerjaan Anda memerlukan banyak data atau analisis numerik, [`pandas`perpustakaan](http://pandas.pydata.org/) juga memiliki kemampuan penguraian CSV, yang akan menangani sisanya.

Dalam artikel ini, Anda akan mempelajari cara membaca, memproses, dan mengurai CSV dari file teks menggunakan Python. Anda akan melihat cara kerja file CSV, mempelajari semua `csv`pustaka penting yang ada di dalam Python, dan melihat cara kerja penguraian CSV menggunakan [`pandas`pustaka](https://realpython.com/pandas-python-explore-dataset/) tersebut .

Jadi mari kita mulai!

**Ikuti Kuis:**Uji pengetahuan Anda dengan kuis interaktif “Membaca dan Menulis File CSV dengan Python”. Anda akan menerima skor setelah selesai untuk membantu Anda melacak kemajuan pembelajaran Anda:

___

[

![Penguraian CSV Python](https://files.realpython.com/media/Python-Text-Parsing_Watermarked.5ac48b25acf2.jpg)



](https://realpython.com/quizzes/python-csv/)

## Apa itu File CSV?

File CSV (file Comma Separated Values) adalah jenis file teks biasa yang menggunakan penataan khusus untuk menyusun data tabular. Karena ini adalah file teks biasa, maka hanya dapat berisi data teks aktual—dengan kata lain, karakter [ASCII](https://en.wikipedia.org/wiki/ASCII) atau [Unicode yang dapat dicetak.](https://en.wikipedia.org/wiki/Unicode)

Struktur file CSV ditentukan berdasarkan namanya. Biasanya, file CSV menggunakan koma untuk memisahkan setiap nilai data tertentu. Berikut tampilan strukturnya:

Perhatikan bagaimana setiap bagian data dipisahkan dengan koma. Biasanya, baris pertama mengidentifikasi setiap bagian data—dengan kata lain, nama kolom data. Setiap baris berikutnya setelah itu adalah data aktual dan hanya dibatasi oleh batasan ukuran file.

Secara umum, karakter pemisah disebut delimiter, dan koma bukan satu-satunya yang digunakan. Delimiter populer lainnya termasuk karakter tab ( `\t`), titik dua ( `:`) dan titik koma ( `;`). Untuk mengurai file CSV dengan benar, kita harus mengetahui delimiter mana yang digunakan.

### Dari Mana File CSV Berasal?

File CSV biasanya dibuat oleh program yang menangani data dalam jumlah besar. Mereka adalah cara mudah untuk mengekspor data dari spreadsheet dan database serta mengimpor atau menggunakannya dalam program lain. Misalnya, Anda mungkin mengekspor hasil program penambangan data ke file CSV dan kemudian mengimpornya ke dalam spreadsheet untuk menganalisis data, menghasilkan grafik untuk presentasi, atau menyiapkan laporan untuk dipublikasikan.

File CSV sangat mudah digunakan secara terprogram. Bahasa apa pun yang mendukung input file teks dan manipulasi string (seperti Python) dapat bekerja dengan file CSV secara langsung.

## Mengurai File CSV Dengan Perpustakaan CSV Bawaan Python

Pustaka [`csv`menyediakan](https://docs.python.org/3/library/csv.html) fungsionalitas untuk membaca dan menulis ke file CSV. Dirancang untuk langsung digunakan dengan file CSV yang dihasilkan Excel, file ini mudah diadaptasi untuk bekerja dengan berbagai format CSV. Pustaka `csv`berisi objek dan kode lain untuk membaca, menulis, dan memproses data dari dan ke file CSV.

### Membaca File CSV Dengan`csv`

Membaca dari file CSV dilakukan menggunakan `reader`objek. File CSV dibuka sebagai file teks dengan fungsi bawaan Python `open()`, yang mengembalikan objek file. Ini kemudian diteruskan ke `reader`, yang melakukan pengangkatan berat.

Ini `employee_birthday.txt`filenya:

Berikut kode untuk membacanya:

Ini menghasilkan keluaran berikut:

Setiap baris yang dikembalikan oleh `reader`adalah daftar `String`elemen yang berisi data yang ditemukan dengan menghapus pembatas. Baris pertama yang dikembalikan berisi nama kolom, yang ditangani dengan cara khusus.

### Membaca File CSV Ke Kamus Dengan`csv`

Daripada berurusan dengan daftar elemen individual , Anda juga `String`dapat membaca data CSV langsung ke dalam kamus (secara teknis, [Kamus Terurut ).](https://realpython.com/python-ordereddict/)

Sekali lagi, file masukan kami `employee_birthday.txt`adalah sebagai berikut:

Here’s the code to read it in as a [dictionary](https://realpython.com/python-dicts/) this time:

This results in the same output as before:

Where did the dictionary keys come from? The first line of the CSV file is assumed to contain the keys to use to build the dictionary. If you don’t have these in your CSV file, you should specify your own keys by setting the `fieldnames` optional parameter to a list containing them.

### Optional Python CSV `reader` Parameters

The `reader` object can handle different styles of CSV files by specifying [additional parameters](https://docs.python.org/3/library/csv.html?highlight=csv#csv-fmt-params), some of which are shown below:

-   `delimiter` specifies the character used to separate each field. The default is the comma (`','`).
    
-   `quotechar` specifies the character used to surround fields that contain the delimiter character. The default is a double quote (`' " '`).
    
-   `escapechar` specifies the character used to escape the delimiter character, in case quotes aren’t used. The default is no escape character.
    

These parameters deserve some more explanation. Suppose you’re working with the following `employee_addresses.txt` file:

This CSV file contains three fields: `name`, `address`, and `date joined`, which are delimited by commas. The problem is that the data for the `address` field also contains a comma to signify the zip code.

There are three different ways to handle this situation:

-   **Use a different delimiter**  
    That way, the comma can safely be used in the data itself. You use the `delimiter` optional parameter to specify the new delimiter.
    
-   **Wrap the data in quotes**  
    The special nature of your chosen delimiter is ignored in quoted strings. Therefore, you can specify the character used for quoting with the `quotechar` optional parameter. As long as that character also doesn’t appear in the data, you’re fine.
    
-   **Escape the delimiter characters in the data**  
    Escape characters work just as they do in format strings, nullifying the interpretation of the character being escaped (in this case, the delimiter). If an escape character is used, it must be specified using the `escapechar` optional parameter.
    

### Writing CSV Files With `csv`

You can also write to a CSV file using a `writer` object and the `.write_row()` method:

The `quotechar` optional parameter tells the `writer` which character to use to quote fields when writing. Whether quoting is used or not, however, is determined by the `quoting` optional parameter:

-   If `quoting` is set to `csv.QUOTE_MINIMAL`, then `.writerow()` will quote fields only if they contain the `delimiter` or the `quotechar`. This is the default case.
-   If `quoting` is set to `csv.QUOTE_ALL`, then `.writerow()` will quote all fields.
-   If `quoting` is set to `csv.QUOTE_NONNUMERIC`, then `.writerow()` will quote all fields containing text data and convert all numeric fields to the `float` data type.
-   If `quoting` is set to `csv.QUOTE_NONE`, then `.writerow()` will escape delimiters instead of quoting them. In this case, you also must provide a value for the `escapechar` optional parameter.

Reading the file back in plain text shows that the file is created as follows:

### Writing CSV File From a Dictionary With `csv`

Since you can read our data into a dictionary, it’s only fair that you should be able to write it out from a dictionary as well:

Unlike `DictReader`, the `fieldnames` parameter is required when writing a dictionary. This makes sense, when you think about it: without a list of `fieldnames`, the `DictWriter` can’t know which keys to use to retrieve values from your dictionaries. It also uses the keys in `fieldnames` to write out the first row as column names.

The code above generates the following output file:

## Parsing CSV Files With the `pandas` Library

Of course, the Python CSV library isn’t the only game in town. [Reading CSV files](https://realpython.com/pandas-read-write-files/#read-a-csv-file) is possible in [`pandas`](http://pandas.pydata.org/index.html) as well. It is highly recommended if you have a lot of data to analyze.

`pandas` is an open-source Python library that provides high performance data analysis tools and easy to use data structures. `pandas` is available for all Python installations, but it is a key part of the [Anaconda](https://www.anaconda.com/) distribution and works extremely well in [Jupyter notebooks](https://jupyter.org/) to share data, code, analysis results, visualizations, and narrative text.

Installing `pandas` and its dependencies in `Anaconda` is easily done:

As is using [`pip`/`pipenv`](https://realpython.com/pipenv-guide/) for other Python installations:

We won’t delve into the specifics of how `pandas` works or how to use it. For an in-depth treatment on using `pandas` to read and analyze large data sets, check out [Shantnu Tiwari’s](https://realpython.com/team/stiwari/) superb article on [working with large Excel files in pandas](https://realpython.com/working-with-large-excel-files-in-pandas/).

### Reading CSV Files With `pandas`

To show some of the power of `pandas` CSV capabilities, I’ve created a slightly more complicated file to read, called `hrdata.csv`. It contains data on company employees:

Reading the CSV into a `pandas` [`DataFrame`](https://realpython.com/pandas-dataframe/) is quick and straightforward:

That’s it: three lines of code, and only one of them is doing the actual work. `pandas.read_csv()` opens, analyzes, and reads the CSV file provided, and stores the data in a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html). Printing the `DataFrame` results in the following output:

Here are a few points worth noting:

-   First, `pandas` recognized that the first line of the CSV contained column names, and used them automatically. I call this Goodness.
-   However, `pandas` is also using zero-based integer indices in the `DataFrame`. That’s because we didn’t tell it what our index should be.
-   Further, if you look at the data types of our columns , you’ll see `pandas` has properly converted the `Salary` and `Sick Days remaining` columns to numbers, but the `Hire Date` column is still a `String`. This is easily confirmed in interactive mode:
    

Let’s tackle these issues one at a time. To use a different column as the `DataFrame` index, add the `index_col` optional parameter:

Now the `Name` field is our `DataFrame` index:

Next, let’s fix the data type of the `Hire Date` field. You can force `pandas` to read data as a date with the `parse_dates` optional parameter, which is defined as a list of column names to treat as dates:

Notice the difference in the output:

The date is now formatted properly, which is easily confirmed in interactive mode:

If your CSV files doesn’t have column names in the first line, you can use the `names` optional parameter to provide a list of column names. You can also use this if you want to override the column names provided in the first line. In this case, you must also tell `pandas.read_csv()` to ignore existing column names using the `header=0` optional parameter:

Notice that, since the column names changed, the columns specified in the `index_col` and `parse_dates` optional parameters must also be changed. This now results in the following output:

### Writing CSV Files With `pandas`

Of course, if you can’t get your data out of `pandas` again, it doesn’t do you much good. Writing a `DataFrame` to a CSV file is just as easy as reading one in. Let’s write the data with the new column names to a new CSV file:

The only difference between this code and the reading code above is that the `print(df)` call was replaced with `df.to_csv()`, providing the file name. The new CSV file looks like this:

## Conclusion

If you understand the basics of reading CSV files, then you won’t ever be caught flat footed when you need to deal with importing data. Most CSV reading, processing, and writing tasks can be easily handled by the basic `csv` Python library. If you have a lot of data to read and process, the `pandas` library provides quick and easy CSV handling capabilities as well.

**Take the Quiz:** Test your knowledge with our interactive “Reading and Writing CSV Files in Python” quiz. You’ll receive a score upon completion to help you track your learning progress:

___

[

![Penguraian CSV Python](https://files.realpython.com/media/Python-Text-Parsing_Watermarked.5ac48b25acf2.jpg)



](https://realpython.com/quizzes/python-csv/)

Are there other ways to parse text files? Of course! Libraries like [ANTLR](http://www.antlr.org/), [PLY](http://www.dabeaz.com/ply/), and [PlyPlus](https://pypi.org/project/PlyPlus/) can all handle heavy-duty parsing, and if simple `String` manipulation won’t work, there are always [regular expressions](https://realpython.com/regex-python/).

But those are topics for other articles…

Menonton sekarangTutorial ini memiliki kursus video terkait yang dibuat oleh tim Real Python. Tonton bersama dengan tutorial tertulis untuk memperdalam pemahaman Anda: [**Membaca dan Menulis File CSV**](https://realpython.com/courses/reading-and-writing-csv-files/)

sumber : https://realpython.com/python-csv/