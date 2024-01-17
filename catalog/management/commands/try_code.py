from django.core.management import BaseCommand
from django.utils.text import slugify



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('text', type=str, help="Текст для перевода в транслит")

    def handle(self, *arg, **options):
        rus_abc = ('абвгдеёжзийклмнопрстуфхцчшщьыъэюя')
        slug_abc = ('a', 'b', 'v', 'g', 'd', 'e', 'jo', 'zh', 'z', 'i',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f',
                    'h', 'c', 'ch', 'sh', 'sch', '', 'y', '', 'e', 'ju', 'ja')
        trance_table = {}
        for num in range(len(rus_abc)):
            letter = rus_abc[num]
            trance_table[ord(letter)] = slug_abc[num]

        result = options['text'].lower().translate(trance_table)

        return slugify(result)