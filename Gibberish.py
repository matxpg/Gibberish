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
        
        
    def Gibberish(self):
        for x in self.consonants:
            if (x in self.sentence):
                self.sentence=self.sentence.replace(x, x+'o'+unicode(x).lower())    
    def deGibberish(self):
        for x in self.consonants:
            if (x in self.sentence):
                self.sentence=self.sentence.replace(x+'o'+unicode(x).lower(), x)    
 
    def get_sentence(self):
        return self.sentence
    
    def Gibberish_translate(self, language=None):
        gs= goslate.Goslate()
        if(language is None):
            self.sentence = gs.translate(self.get_sentence(), self.languages['english'])
        else:
            self.sentence = gs.translate(self.get_sentence(), self.languages[language.lower()])

def main():
    N_ARGS = len(sys.argv)
    if (N_ARGS >= 3):
        sentence, language = sys.argv[1], sys.argv[2]
    else:
        sentence = None
        language = "English"

    if (sentence is None):
        sentence = "This is a test"
    
    gib = Gibberish(sentence)

    print sentence

    print "became: \n"

    gib.Gibberish_translate(language)
    gib.Gibberish()
    print gib.get_sentence()

main()
