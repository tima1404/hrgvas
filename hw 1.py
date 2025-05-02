name = input('Як тебе звати? ')
age = int(input('Скільки тобі років? '))
if age >= 18:
    admission = 'Вхід дозволено!'
else:
    admission = 'На жаль, вхід заборонено.'
print('Привіт,',name,', тобі',age,'років.',admission)