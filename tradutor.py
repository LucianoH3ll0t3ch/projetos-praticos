
from google import Translator
trans = Translator()
t = trans.translate(
    'hello how can i help you?'
)
print(f'source: {t.src}')
print(f'destination: {t.dest}')
print(f'{t.origin} -> {t.text}')