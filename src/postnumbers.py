# Kopioi aikaisempi ratkaisusi tänne. Lisää tarvittaessa myös muut ratkaisusi tiedostot.
from typing import Optional
from http_request import get_postal_data


def get_postal_code(name: str) -> Optional[str]:
    data = get_postal_data()

    postal_codes = []

    if " " in name:
        name = name.replace(" ", "")

    if name in data.values():
        for code, city in data.items():
            if city.replace(" ", "") == name:
                postal_codes.append(code)
        if postal_codes:
            postal_codes.sort()
            list = ', '.join(postal_codes)
            return list
    else:
        return None


if __name__ == '__main__':

    name = input('Kirjoita postitoimipaikka: ').upper()

    data = get_postal_data()

    if " " in name:
        name = name.replace(" ", "")

    postal_codes = []

    if name in data.values():
        for code, city in data.items():
            if city.replace(" ", "") == name:
                postal_codes.append(code)
        if postal_codes:
            postal_codes.sort()
            list = ', '.join(postal_codes)
            print(f'Postinumerot: {list}')
        else:
            print('Tuntematon postitoimipaikka')
