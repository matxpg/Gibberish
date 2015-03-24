import sys
import goslate #Gibberish- Translates to english using google translate!

class Gibberish:
    """v1
    I should be asleep right now, but, I made a program to convert what I just wrote into
    I soshohouloldod bobe asosloleepop rorigoghohtot nonowow... Or translate it to a different language
    and then gibberish it up. 
    As well as deconvert gibberish from any language google can translate.
    
    SAMPLE USAGE:
    SENTENCE = "This is a sentence."
     = Gibberish(SENTENCE)
    gib.Gibberish_translate('Swedish')
    gib.Gibberish()
    print SENTENCE +" became: " + gib.get_sentence()
    This is a sentence. became: Dodetottota aror enon momenoninongog.
    """
    
    def __str__(self):
        return unicode(self).encode('utf-8')

    def __init__(self, sentence):
        self.sentence = sentence
        self.consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    
        self.languages = {'afrikaans':'af','arabic':'ar','armenian':'hy','belarusian':'be','bulgarian':'bg',
                          'catalan':'ca','chinese (simplified)':'zh-cn','chinese (traditional)':'zh-tw',
                          'croatian':'hr','czech':'cs','danish':'da','dutch':'nl','english':'en','esperanto':'eo',
                          'estonian':'et','filipino':'tl','finnish':'fi','french':'fr','german':'de','greek':'el',
                          'hebrew':'iw','hindi':'hi','hungarian':'hu','icelandic':'is','indonesian':'id',
                          'italian':'it','japanese':'ja','korean':'ko','latvian':'lv','lithuanian':'lt',
                          'norwegian':'no','persian':'fa','polish':'pl','portuguese':'pt','romanian':'ro',
                          'russian':'ru','serbian':'sr','slovak':'sk','slovenian':'sl','spanish':'es',
                          'swahili':'sw','swedish':'sv','thai':'th','turkish':'tr','ukrainian':'uk',
                          'vietnamese':'vi'}
        
  
    def gibber(self):
        """Maps all consonants x -> xox
        """   
        for x in self.consonants:
            if (x in self.sentence):
        	    self.sentence = self.sentence.replace(x, x+'o'+unicode(x).lower())
    
    def degibber(self):
    	"""From left to right in a sentence, maps all three letter xox pairs to x
    	(x consonant)
    	"""
        for x in self.consonants:
            if (x in self.sentence):
                self.sentence=self.sentence.replace(x+'o'+unicode(x).lower(), x)    
 
    def get_sentence(self):
    	"""Gets the sentence it's working on
    	"""
        return self.sentence
    
    def translate(self, language=None):
    	"""Translate the sentence it is workig on to a different language
    	"""
        gs= goslate.Goslate()
        if(language is None):
            self.sentence = gs.translate(self.get_sentence(), self.languages['english'])
        else:
            self.sentence = gs.translate(self.get_sentence(), self.languages[language.lower()])


def main():
    N_ARGS = len(sys.argv)
    if (N_ARGS >= 4):
        command, sentence, language,  = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        sentence = None
        language = "English"

    if (sentence is None):
        sentence = "This is a test"
    
    gib = Gibberish(sentence)

    if ((command == '-d') or (command == 'degibber')):
    	gib.degibber()
        gib.translate(language)
    elif ((command == '-g') or (command == 'gibber')):
    	gib.translate(language)
    	gib.gibber()
    
    print gib.get_sentence()

main()
