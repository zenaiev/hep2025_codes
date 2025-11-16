## Матеріали курсу "Сучасні розрахункові коди" (2025 р., 1 семестр, бакалаври, 4 курс)

 <!--<details>-->
   <!--<summary> -->

#### [Посилання на zoom](https://cern.zoom.us/j/66654166304?pwd=yHmoaRNUrHEkrPTYIFN2kXAoJJsgIc.1) (паскод 156629)

#### [Записи занять](https://cernbox.cern.ch/s/ejcI6MijmGb2q4o)

  <!--</summary>-->
  Додакткові матеріали:  
  - 01.09.2025
     - [слайди](https://github.com/zenaiev/hep2025_codes/blob/main/slides/into/%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BD%D1%96%20%D0%BA%D0%BE%D0%B4%D0%B8%20%D0%B4%D0%BB%D1%8F%20%D1%84%D1%96%D0%B7%D0%B8%D0%BA%D0%B8%20%D0%B2%D0%B8%D1%81%D0%BE%D0%BA%D0%B8%D1%85%20%D0%B5%D0%BD%D0%B5%D1%80%D0%B3%D1%96%D0%B9.pdf)
  - 08.09.2025
     - [слайди1](https://github.com/zenaiev/hep2025_codes/blob/main/slides/pandas/pandas.pdf) [слайди2](https://github.com/zenaiev/hep2025_codes/blob/main/slides/combine/combine_annotated.pdf)
  - 15.09.2025
     - [слайди](https://github.com/zenaiev/hep2025_codes/blob/main/slides/invmass/invmass.pdf)
     - коди "hello world":
        - [hello.cpp](https://github.com/zenaiev/hep2025_codes/tree/main/invmass/hello.cpp)
        - [hello_main.cpp](https://github.com/zenaiev/hep2025_codes/tree/main/invmass/hello_main.cpp)
        - [hello.py](https://github.com/zenaiev/hep2025_codes/tree/main/invmass/hello.py)
     - [головний скрипт](https://github.com/zenaiev/hep2025_codes/tree/main/invmass/invmass.py)
  - 22.09.2025 (продовжували розбирати код для завдання фітування розподілу інваріантної маси, пройшли теорію розділення сигналу і фону та визначення перерізів)
     - [головний скрипт](https://github.com/zenaiev/hep2025_codes/tree/main/invmass/invmass.py)
     - [слайди](https://github.com/zenaiev/hep2025_codes/blob/main/slides/cuts_xsec/cuts_xsec.pdf)
  - 29.09.2025 (розділення сигналу і фону, визначення перерізів)
     - [головний скрипт](https://github.com/zenaiev/hep2025_codes/tree/main/invmass/invmass_adv.py)
     - [слайди](https://github.com/zenaiev/hep2025_codes/blob/main/slides/cuts_xsec/cuts_xsec.pdf)
     - домашнє завдання: у функції varycut() обчислити і намалювати перерізи народження D0 (зі статистичною похибкою) для різних значень обмежень на p_min. Переріз обчислити за спрощеною формулою як відношення кількості сигнальних подій до ефективності відбору подій (тобто світимість взяти за 1).
   - 06.10.2025
     - [слайди1](https://github.com/zenaiev/hep2025_codes/tree/main/slides/cms_od_ttbar/cms_od_ttbar.pdf) [слайди2](https://github.com/zenaiev/hep2025_codes/tree/main/slides/cms_od_ttbar/OZ_dataValidation_Top_2016.12.13.pdf)
     - [репозиторій з кодом](https://github.com/zenaiev/2011-ttbar) (branch 2024)
   - 20.10.2025
     - [слайди про діаграми Фейнмана](https://github.com/zenaiev/hep2025_codes/tree/main/slides/diagrams/diagrams.pdf)
     - [слайди](https://github.com/zenaiev/hep2025_codes/tree/main/slides/cms_od_ttbar/cms_od_ttbar.pdf) [слайди2](https://github.com/zenaiev/hep2025_codes/tree/main/slides/cms_od_ttbar/OZ_dataValidation_Top_2016.12.13.pdf)
     - [репозиторій з кодом](https://github.com/zenaiev/2011-ttbar) (branch 2024)
   - 27.10.2025
     - DUNE (нейтрино):
       - [посилання на документацію по DUNE](https://dune.github.io/duneanaobj/classcaf_1_1StandardRecord.html)
     - CMS Open Data (топ кварки):
       - [слайди](https://github.com/zenaiev/hep2025_codes/tree/main/slides/cms_od_ttbar/cms_od_ttbar.pdf) [слайди2](https://github.com/zenaiev/hep2025_codes/tree/main/slides/cms_od_ttbar/OZ_dataValidation_Top_2016.12.13.pdf)
       - [репозиторій з кодом](https://github.com/zenaiev/2011-ttbar) (branch 2024)
   - 03.11.2025
     - [слайди про діаграми Фейнмана і розпади частинок](https://github.com/zenaiev/hep2025_codes/tree/main/slides/diagrams/diagrams.pdf)
     - домашнє завдання: на парі була чорна коробка, якій ми показували картинки (8к), а потім ми питали у чорної коробки на інших (2к) подіях чи це сигнальна подія (розпад t-кварка), чи це фонова. Працювали з [цією папкою](https://drive.google.com/drive/folders/1BxqrlV8dDB-eLfOCll3WYpb2ALwemR0B?usp=share_link). На домашку задав погратись з параметрами чорної коробки. На старших курсах розкажуть що там всередині, а поки можна на [сайті](https://playground.tensorflow.org) погратись з параметрами чорної коробки. Повторити і надіслати [2 скріншоти](https://t.me/modern_computational_codes_2025/35) (в класифікації спіралька, в регресії шахова дошка) з власною оптимізованою архітектурою (мінімально слоїв, нейронів). Погратись з learning rate (крок спуску), регуляризацією (наскільки сильно бити нейромережу за помилку).
   - 10.11.2025
     - [слайди](https://github.com/zenaiev/hep2025_codes/tree/main/slides/cms_od_ttbar/cms_od_ttbar.pdf) [слайди2](https://github.com/zenaiev/hep2025_codes/tree/main/slides/cms_od_ttbar/OZ_dataValidation_Top_2016.12.13.pdf)
     - [репозиторій з кодом](https://github.com/zenaiev/2011-ttbar) (branch 2024)
   - 17.11.2025
     - [слайди по CMS Open Data](https://github.com/zenaiev/hep2025_codes/tree/main/slides/cms_od_ttbar/cms_od_ttbar.pdf) [слайди2](https://github.com/zenaiev/hep2025_codes/tree/main/slides/cms_od_ttbar/OZ_dataValidation_Top_2016.12.13.pdf)
     - [репозиторій з кодом CMS Open Data](https://github.com/zenaiev/2011-ttbar) (branch 2024)
     - [слайди про розгортання (unfolding)](https://github.com/zenaiev/hep2025_codes/tree/main/slides/unfolding/unfolding.pdf)
     - скрипти по розгортанню (unfolding) [Python](https://github.com/zenaiev/hep2025_codes/tree/main/unfold/unfold.py) [C++](https://github.com/zenaiev/hep2025_codes/tree/main/unfold/unfold.cpp)
   - 01.12.2025
     - [завдання на залік](https://github.com/zenaiev/hep2025_codes/tree/main/tasks/tasks.txt)
