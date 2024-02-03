# CycleGAN - Monet
*Projekt na języki i biblioteki analizy danych*

## Opis

Projekt dotyczył stworzenia sieci generacyjnej, umożliwającej wygenerowanie obrazu w stylu Claude Moneta, z podanego na wejściu dowolnego zdjęcia.

Zestaw danych oraz wskazówki do stworzenia modelu zostały zaczerpnięte z [Kaggla](https://www.kaggle.com/code/amyjang/monet-cyclegan-tutorial/notebook).
Sam model od strony teoretycznej został stworzony z pomocą pracy naukowej [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593)

---

## Opis - trenowanie

Do wytrenowania własnej sieci wystarczy uruchomić w Jupyteer Notebook plik **CycleGAN.ipynb**.
Potrzebne biblioteki do wytrenowania sieci:

- tensorflow
- numpy
- pandas
- matplotlib
- keras (jako część tensorflow)

Aby zainstalować podane biblioteki najlepiej użyć narzędzia **Anaconda** i stworzyć w nim nowe środowisko, jak w tym [tutorialu](https://docs.anaconda.com/free/anaconda/applications/tensorflow/). Pakiet matplotlib należy doinstalować ręcznie używając **pip**

Wytrenowana sieć pojawi się w folderze głównym pod nazwą **cycleGAN**. 

Podczas trenowania należy się uzbroić w cierpliwość - trwa ono na lepszej klasie laptopie *(NVIDIA GeForce GTX 1660 Ti)* około 20 godzin.

---

## Opis - API
Do projektu zostało dołączone API, które umożliwia użycia sieci za pomocą przeglądarki. Samo API zostało napisane za pomocą micro frameworka **Flask**

### Proces instalacji
- Zainstaluj narzędzie [Docker](https://docs.docker.com/get-docker/)
- Przekopiuj do folderu **API** wytrenowaną sieć i nazwij ją cycleGAN (pomiń jeżeli sieć już tam się znajduje)
- W folderze **API** w konsoli wywołaj polecenie *docker compose up*

Pod adresem **127.0.0.1:5000**(Sic!) powinna funkcjonować strona, która będzie umożliwać używanie sieci.

**Uwaga** sieć akceptuje zdjęcia tylko z trzema kanałami (RGB). Jeżeli dostanie na wejście zdjęcia z na przykład kanałem alfa (4 kanały) to wtedy nie zadziała.

### ngrok
Api zawiera możliwość wystawienia tymczasowego hostingu w internecie używając aplikacji ngrok. Aby poprawnie skonfigurować hosting należy

- Założyć konto na stronie [ngrok](https://ngrok.com/)
- Uzyskaj swój [token autoryzacji](https://dashboard.ngrok.com/get-started/your-authtoken)
- Przekopij swój token do pliku **ngrork-example.yml** w miejsce **authtoken**
- Zmień nazwę **ngrork-example.yml** na **ngrork.yml**
- Uruchom jeszcze raz środowisku - *docker compose up*

Na [stronie ngrok](https://dashboard.ngrok.com/tunnels/agents) powinień się znaleźć adres, pod którym dostępne jest nasze API
