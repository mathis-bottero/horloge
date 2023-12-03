from time import sleep, strftime, localtime, mktime

alarm_time = None  # Initialise l'heure de l'alarme à None

def afficher_heure():
    current_time = strftime('%I:%M:%S %p')
    print("\r" + current_time, end="", flush=True)

    if alarm_time is not None and strftime('%I:%M:%S %p') == strftime('%I:%M:%S %p', localtime(alarm_time)):
        afficher_message_alarme()

    sleep(1)
    afficher_heure()

def regler_alarme(heure_alarme):
    global alarm_time
    alarm_time = mktime((2000, 1, 1, heure_alarme[0], heure_alarme[1], heure_alarme[2], 0, 0, -1))
    print(f'\nAlarme réglée à {strftime("%I:%M:%S %p", localtime(alarm_time))}')

regler_alarme((17, 22, 00))  # Réglez l'alarme pour 5:18:30 PM

def afficher_message_alarme():
    print("\nDing Dong ! C'est l'heure de l'alarme.")

def get_heure_alarme():
    user_input = input("Entrez l'heure de l'alarme (HH:MM:SS AM/PM): ")

    try:
        heure_alarme = localtime().tm_hour  # Obtenez l'heure actuelle au format 24 heures
        heure_alarme_str = user_input.split()[0]
        heure_alarme += int(heure_alarme_str.split(':')[0])
        if user_input.split()[1].lower() == 'pm':
            heure_alarme += 12

        minute_alarme = int(heure_alarme_str.split(':')[1])
        seconde_alarme = int(heure_alarme_str.split(':')[2])

        return heure_alarme, minute_alarme, seconde_alarme
    except (ValueError, IndexError):
        print("Format d'heure incorrect. Réglez à nouveau l'alarme.")
        return None

while True:
    afficher_heure()
    regler_alarme(get_heure_alarme())