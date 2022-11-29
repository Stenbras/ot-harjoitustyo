# Noteeditor
Soveluksen avulla käyttäjien on mahdollista konvertoida audio tiedostot nuottit muotoina (esim jos audio tiedosto song.wav on joku piano laulu voit luoda song.wav ja muokka laulun nuottit). Voit myös rakentaa lulua valkoisen pohjasta.

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.
