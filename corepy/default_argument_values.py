def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("Swetha")
banner("Nirvaan", '*')
banner('Pradeep', border='$')
banner(border='@', message='Nirvaan')