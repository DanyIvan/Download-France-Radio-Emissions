# python program to download france radio emissions

I used to work at a place where it was forbidden to stream radio emissions from the WiFi. However, I love to listen to france radio emissions while working. That is why i decided to  create a program to download my favorite emissions to listen to them offline.

# Example

I store my favorite emissions on a dictionary:

```python
favorite_emissions = {
        'chemins_philo': '"https://www.franceculture.fr/emissions/les-chemins-de-la-philosophie"',
        'allegretto': '"https://www.francemusique.fr/emissions/allegretto"',
        'van_bethoveen': '"https://www.francemusique.fr/emissions/le-van-beethoven"',
        'methode_scientifique': '"https://www.franceculture.fr/emissions/la-methode-scientifique"',
        'open_jazz' : '"https://www.francemusique.fr/emissions/open-jazz"'
        }
```

Then I download my favorite emissions with the function `download_list`, using the keys of my favorite_emissions dictionary.

```python
download_list(['allegretto',
                   'chemins_philo',
                   'methode_scientifique',
                   'van_bethoveen',
                   'open_jazz' ])
```

# Requirements

* requests=2.22.0