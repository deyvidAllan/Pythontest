na = float(input('Fala pintor ! qual é a altura da parede? '))
nl = float(input('Agora me diga qual a Largura da parede ? '))
ar = na * nl
lt = ar / 2

print('A area total a ser pintada é de: {:.2f} em metros, e para pinta-la será nescessário {:.3f} litros de tinta'.format(ar, lt))
