from deep_translator import GoogleTranslator
import os


langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)
langs_list = GoogleTranslator.get_supported_languages()

def see_lang():
	for i, lang in enumerate(langs_dict):
		print(i,'. ', lang)

def translate_it(targ, sentence):
	translated = GoogleTranslator(source='auto', target=targ).translate(sentence)
	print(translated)

def welcome(lang=''):
	return """
	WELCOME TO TRANSLATE APP WITH PYTHON.
	Made by Arwani
	Choosen Language = """+lang+"""


	Here The Command You Can Use (1-3):
		1. See All The Language Support 
		   And Set Target Language to Translate
		2. Translate My Sentence
	"""





if __name__=='__main__':
	target = ''
	selected_lang = ''
	cond = True
	while cond:
		os.system('clear')
		os.system('cls')


		print(welcome(selected_lang))

		task = int(input('insert the number you want: '))


		if task == 1:
			see_lang()
			selected_lang = langs_list[int(input('Insert number of language you want : '))]
			target = langs_dict[selected_lang]
			print('You Choose ', selected_lang, ' For The Target Language')
		elif task == 2:
			sentence = input('Write your sentence to translated : ')
			if target == '':
				translate_it(targ='en',sentence=sentence)
			else:
				translate_it(targ=target, sentence=sentence)

			input('--Enter to refresh--')
		else:
			cond = False

			


