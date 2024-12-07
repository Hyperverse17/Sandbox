
# pip install astropy
from astropy.coordinates import get_body, EarthLocation
from astropy.time import Time

print()
now = Time.now()
location = EarthLocation.of_site("greenwich")
planet_name = input("Ingresa el nombre del planeta: ").lower()
if planet_name != "":
    planet_position = get_body(planet_name,now,location)
    print(f"{planet_name.capitalize()}"
          f"Posición: RA = {planet_position.ra}, "
          f"Dec = {planet_position.dec}")
